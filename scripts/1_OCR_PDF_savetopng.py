import os
import re
import fitz  # PyMuPDF
import pytesseract
import pandas as pd
from PIL import Image
import io
from tqdm import tqdm
import cv2
import numpy as np

#Processes
Loads a PDF from disk using PyMuPDF
Converts each page to an image (.png)
Runs Tesseract OCR on each page
Cleans common OCR text encoding errors
Saves the cleaned text to .txt files
#Use this if you need:
Saves images and text to a target output folder
# structured data for mapping, analysis, or tagging.
#extract embedded or layout-based images.
#full archival or public history pipeline.
#it might take time. let it process for high-quality results.

#if you prefer to extract each image from each page, use 3_multiple_files.py which is a batch processing script.  

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pdf_path = r"C:\ACBT Project\brochures\H130.BoardofTrade002_1939.pdf"
output_base = r"C:\Users\Public\Documents\archive\ACBT Project\images\1939"

def extract_year_from_filename(filename):
    match = re.search(r'\d{4}', filename)
    return match.group(0) if match else "Unknown"

phone_re = re.compile(r"(?:Phone|Telephone)?\s*\(?\d{1,4}\)?[-–]?\d{2,4}", re.IGNORECASE)
address_re = re.compile(
    r"(?:COR\.?\s+)?(?:\d{1,5}(?:[-–]\d{1,5})?\s+)?(?:[NSEW]\.? )?(?:[A-Z][a-z]+\s+)+(Avenue|Ave\.?|Street|St\.?|Road|Rd\.?|Blvd\.?|Lane|Drive|Dr\.?|Court|Ct\.?|Plaza|Pl\.?|Avenues)",
    re.IGNORECASE)
title_re = r"(?:HON\.?|MR\.?|MRS\.?|MS\.?|DR\.?|REV\.?|PROF\.?|PROP\.?)"
name_body_re = r"[A-Z][a-zA-Z.\-']+(?:\s+[A-Z][a-zA-Z.\-']+)*"
name_re = re.compile(rf"(?:{title_re}\s+)?{name_body_re}", re.IGNORECASE)

def normalize_text(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    blocks, current = [], ""
    for line in lines:
        if len(line) < 40 and current:
            current += " " + line
        else:
            if current:
                blocks.append(current)
            current = line
    if current:
        blocks.append(current)
    return blocks

def clean_ocr_text(text):
    replacements = {
        'â€œ': '“',
        'â€': '”',
        'â€™': '’',
        'â€“': '–',
        'â€”': '—',
        'Â': '',
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text

config = '--psm 3'

def extract_image_regions(cv_img, page_num, image_output_dir):
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    thresh = cv2.adaptiveThreshold(gray, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY_INV, 15, 10)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_counter = 0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 100 and h > 100:
            cropped = cv_img[y:y+h, x:x+w]
            save_path = os.path.join(image_output_dir, f"page{page_num+1}_img{image_counter}.png")
            cv2.imwrite(save_path, cropped)
            image_counter += 1
    return image_counter

if not os.path.isfile(pdf_path):
    print(f"❌ File not found: {pdf_path}")
else:
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"❌ Failed to open {pdf_path}: {e}")
        doc = None

    if doc:
        filename = os.path.basename(pdf_path)
        base_id = os.path.splitext(filename)[0].replace(" ", "_")
        year = extract_year_from_filename(filename)

        all_text = []
        structured_data = []
        line_data = []

        image_output_dir = os.path.join(output_base, f"{year}_extracted_images")
        os.makedirs(image_output_dir, exist_ok=True)

        for page_num in tqdm(range(len(doc)), desc=f"📚 Processing {filename}"):
            page = doc.load_page(page_num)

            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = os.path.join(image_output_dir, f"page{page_num + 1}_img{img_index}.{image_ext}")
                with open(image_filename, "wb") as img_out:
                    img_out.write(image_bytes)

            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), colorspace=fitz.csGRAY)

            # ✅ Moved inside loop after pix is defined
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            num_found = extract_image_regions(cv_img, page_num, image_output_dir)
            print(f"🖼️ Page {page_num + 1}: {num_found} images extracted")

            gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY, 11, 2)
            denoised = cv2.fastNlMeansDenoising(thresh, h=30)
            ocr_img = Image.fromarray(denoised)

            edges = cv2.Canny(gray, threshold1=30, threshold2=150)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            dilated = cv2.dilate(edges, kernel, iterations=2)
            contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            image_counter = 0
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                area = w * h
                if area > 5000:
                    sub_img = cv_img[y:y + h, x:x + w]
                    save_path = os.path.join(image_output_dir, f"page{page_num + 1}_img{image_counter}.png")
                    cv2.imwrite(save_path, sub_img)
                    image_counter += 1

            text = pytesseract.image_to_string(ocr_img, lang='eng', config=config)
            text = clean_ocr_text(text)
            blocks = normalize_text(text)

            all_text.append({
                "Brochure": filename,
                "Year": year,
                "Page": page_num + 1,
                "Text": text
            })

            structured_data.append({
                "Brochure": filename,
                "Year": year,
                "Page": page_num + 1,
                "Names": "; ".join(name_re.findall(text)),
                "Addresses": "; ".join(address_re.findall(text)),
                "Phones": "; ".join(phone_re.findall(text))
            })

            for block in blocks:
                line_data.append({
                    "Brochure": filename,
                    "Year": year,
                    "Page": page_num + 1,
                    "Line": block,
                    "Names": "; ".join(name_re.findall(block)),
                    "Addresses": "; ".join(address_re.findall(block)),
                    "Phones": "; ".join(phone_re.findall(block))
                })

        os.makedirs(output_base, exist_ok=True)

        with open(os.path.join(output_base, f"{base_id}_TEXT.txt"), "w", encoding="utf-8") as f:
            for entry in all_text:
                f.write(f"Brochure: {entry['Brochure']}\nYear: {entry['Year']}\nPage: {entry['Page']}\nText:\n{entry['Text']}\n{'-' * 40}\n")

        with open(os.path.join(output_base, f"{base_id}_tuples.txt"), "w", encoding="utf-8") as f:
            for entry in structured_data:
                f.write(f"Brochure: {entry['Brochure']}\nYear: {entry['Year']}\nPage {entry['Page']}\nNames: {entry['Names']}\nAddresses: {entry['Addresses']}\nPhones: {entry['Phones']}\n\n")

        print(f"✅ Done: {filename} with {len(doc)} pages.")
