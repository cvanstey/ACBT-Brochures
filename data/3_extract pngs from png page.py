import cv2
import os
from PIL import Image

#This script is a semi-automated image cropper with user review, ideal for extracting photo-like regions (ads, portraits, signs) from scanned brochure pages.
Reads .png images from a folder (e.g., split brochure pages)
Converts to grayscale, thresholds, dilates to find contours
Finds bounding boxes and pads them for cropping
Shows each crop to the user, who can:
Press y to save
Press n to skip
Press m to manually crop using a GUI box
Press q to quit
Saves cropped images with DPI metadata for print/export

def resize_for_display(image, max_width=800, max_height=600):
    h, w = image.shape[:2]
    scale = min(max_width / w, max_height / h, 1.0)
    if scale < 1.0:
        new_w = int(w * scale)
        new_h = int(h * scale)
        resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
        return resized, scale
    else:
        return image.copy(), 1.0

from PIL import Image

def save_with_dpi(cv2_img, path, dpi=(300, 300)):
    # Convert BGR (OpenCV) to RGB (PIL)
    rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb)
    pil_img.save(path, dpi=dpi)

# === CONFIGURATION ===
input_folder = r'C:\Users\crook\OneDrive\Documents\archive\ACBT Project\PDF to PNG 300 DPI\ocr_cleaned_split_pages_1944'  # change this to your folder
output_folder = os.path.join(input_folder, 'cropped_images_1944')
padding = 15  # number of pixels to expand in all directions

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.png'):
        filepath = os.path.join(input_folder, filename)
        image = cv2.imread(filepath)
        img_h, img_w = image.shape[:2]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Your existing thresholding & dilation code here
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY_INV, 35, 15)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 20))
        dilated = cv2.dilate(thresh, kernel, iterations=1)

        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        base_name = os.path.splitext(filename)[0]

        for i, cnt in enumerate(contours):
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 80 and h > 80:
                # Asymmetric padding
                pad_left = int(w * 0.05)
                pad_right = int(w * 0.05)
                pad_top = int(h * 0.15)
                pad_bottom = int(h * 0.15)

                x1 = max(x - pad_left, 0)
                y1 = max(y - pad_top, 0)
                x2 = min(x + w + pad_right, img_w)
                y2 = min(y + h + pad_bottom, img_h)

                # Draw bounding box on a copy for display
                display_img = image.copy()
                cv2.rectangle(display_img, (x1, y1), (x2, y2), (0, 255, 0), 3)

                # Resize image for display to fit window
                display_resized, _ = resize_for_display(display_img, max_width=800, max_height=600)

                # Show the image with bounding box
                cv2.imshow('Review Crop - Press y to accept, n to skip, q to quit', display_resized)

                key = cv2.waitKey(0) & 0xFF
                if key == ord('y'):
                    # Save the crop
                    cropped = image[y1:y2, x1:x2]
                    output_path = os.path.join(output_folder, f"{base_name}_crop_{i}.png")
                    save_with_dpi(cropped, output_path, dpi=(300, 300))
                    print(f"Saved crop {i} from {filename}")

                elif key == ord('q'):
                    print("Quitting...")
                    cv2.destroyAllWindows()
                    exit()
                elif key == ord('m'):
                    resized_image, scale = resize_for_display(image, max_width=800, max_height=600)

                    # Safe manual crop on resized image
                    roi = cv2.selectROI("Manual Crop (resized)", resized_image, showCrosshair=True, fromCenter=False)
                    cv2.destroyWindow("Manual Crop (resized)")

                    x_r, y_r, w_r, h_r = map(int, roi)
                    if w_r > 0 and h_r > 0:
                        # Map back to full-size coordinates
                        x_orig = int(x_r / scale)
                        y_orig = int(y_r / scale)
                        w_orig = int(w_r / scale)
                        h_orig = int(h_r / scale)

                        # Final clamp
                        x_orig = max(0, min(x_orig, image.shape[1] - 1))
                        y_orig = max(0, min(y_orig, image.shape[0] - 1))
                        w_orig = min(w_orig, image.shape[1] - x_orig)
                        h_orig = min(h_orig, image.shape[0] - y_orig)

                        # Crop
                        cropped_manual = image[y_orig:y_orig + h_orig, x_orig:x_orig + w_orig]
                        manual_output_path = os.path.join(output_folder, f"{base_name}_manual_crop_{i}.png")
                        save_with_dpi(cropped_manual, manual_output_path, dpi=(300, 300))
                        print(f"Saved manual crop {i} from {filename}")
                    else:
                        print(f"Manual crop cancelled or empty for {filename}")


            else:
                    print(f"Skipped crop {i} from {filename}")

cv2.destroyAllWindows()
print("Done processing all images.")
