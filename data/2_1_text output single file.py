import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import re
import cv2
import numpy as np


#this give a single text file - line are mostly intact as are dollar and cent signs.
#this does not extract images
#Loads each page of the PDF using PyMuPDF (fitz).
#Renders each page as a 300 DPI image — good for OCR clarity.
#Converts the image to grayscale, binarizes, and denoises using OpenCV.
#Runs Tesseract OCR on the cleaned image.
#Cleans up the OCR text:
#Removes hyphenated line breaks (Sec-\nretary → Secretary)
#Joins lines into paragraphs
#Normalizes spacing
#Fixes camelCase-like issues (pubYou → pub You)
#Appends each cleaned page’s text to a Python list.
#Writes a single .txt file with all cleaned text, separated by page headers like:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pdf_path = r"C:\Users\Public\Documents\archive\ACBT Project\brochures\H130.BoardofTrade001_1936.pdf"

def clean_ocr_text(text):
    # Remove hyphenation at line breaks (e.g. "Sec-\nretaries" -> "Secretaries")
    text = re.sub(r'-\s*\n\s*', '', text)
    # Replace single newlines inside paragraphs with space
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # Normalize multiple spaces/tabs to single space
    text = re.sub(r'[ \t]+', ' ', text)
    # Insert space between a lowercase letter followed by uppercase letter (e.g. 'pubYou' -> 'pub You')
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    # Strip leading/trailing whitespace
    return text.strip()

doc = fitz.open(pdf_path)
all_texts = []

for page_num in range(len(doc)):
    page = doc[page_num]
    print(f"Processing page {page_num + 1}...")

    # Render page to image at 300 dpi for better OCR accuracy
    pix = page.get_pixmap(dpi=300)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Convert PIL Image to OpenCV format
    img_cv = np.array(img)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

    # Grayscale
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    # Threshold (binarize)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Noise removal (optional)
    clean = cv2.medianBlur(thresh, 3)

    # Convert back to PIL Image for pytesseract
    clean_img = Image.fromarray(clean)

    # OCR the cleaned image to raw text
    raw_text = pytesseract.image_to_string(clean_img, lang='eng')

    # Clean the OCR text
    clean_text = clean_ocr_text(raw_text)

    print(f"\n----- CLEANED OCR TEXT PREVIEW (Page {page_num + 1}) -----\n")
    print(clean_text)
    print("\n------------------------------------\n")

    all_texts.append({
        "Page": page_num + 1,
        "Clean OCR Text": clean_text
    })

# Save all cleaned OCR text to a single .txt file with page breaks
with open("ocr_cleaned_text.txt", "w", encoding="utf-8") as f:
    for page_data in all_texts:
        f.write(f"--- Page {page_data['Page']} ---\n")
        f.write(page_data["Clean OCR Text"])
        f.write("\n\n")

print("Done! Cleaned OCR text saved to ocr_cleaned_text.txt")
