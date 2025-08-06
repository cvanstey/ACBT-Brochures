import fitz  # PyMuPDF
import pytesseract
import os
import re
import numpy as np
import cv2
from PIL import Image, ImageOps, ImageFilter


#we like this one - don't delete. It creates text files that are used in text to csv.py.
#Reads a scanned brochure PDF
#Splits each page into left/right column images
#Applies image preprocessing (contrast, sharpening, resizing)
#Uses Tesseract OCR to extract text
#Cleans and normalizes text (removing artifacts, fixing hyphens, etc.)
#Uses heuristics to group lines into entries
#Outputs one .txt file per column (e.g., page_1a.txt, page_1b.txt) with grouped entries
#This is structured OCR — not just raw text — which is exactly what’s needed for reliable downstream parsing.

# Configure tesseract path here if needed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pdf_path = r"C:\Users\crook\OneDrive\Documents\archive\ACBT Project\brochures\H130.BoardofTrade003_1940.pdf"
output_dir = r"C:\Users\Public\Documents\archive\ACBT Project\ocr_split_pages1"
os.makedirs(output_dir, exist_ok=True)

import numpy as np
from PIL import Image, ImageOps, ImageFilter

def preprocess_image(img):
    # Convert to grayscale
    gray = img.convert("L")

    # Resize (scale up by 1.5–2x)
    width, height = gray.size
    scale_factor = 2  # Try 1.5 if 2 is too sharp
    gray = gray.resize((int(width * scale_factor), int(height * scale_factor)), Image.LANCZOS)

    # Enhance contrast gently
    enhanced = ImageOps.autocontrast(gray)

    # Mild sharpening
    sharpened = enhanced.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))

    # Return the processed image
    return sharpened


    # Optional: Sharpen the result slightly using PIL filter
    sharpened = Image.fromarray(thresh).filter(ImageFilter.SHARPEN)

    return sharpened

def clean_raw_text_preserve_lines(text):
    # Fix ligatures, remove odd chars but keep lines
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("¬", "-").replace("|", "")
    # Remove hyphenation at line breaks (e.g. "Sec-\nretaries" -> "Secretaries")
    text = re.sub(r'-\s*\n\s*', '', text)
    # Replace single newlines inside paragraphs with space
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # Normalize multiple spaces/tabs to single space
    text = re.sub(r'[ \t]+', ' ', text)
    # Insert space between a lowercase letter followed by uppercase letter (e.g. 'pubYou' -> 'pub You')
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    # Strip leading/trailing whitespace
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        line = re.sub(r'\s+', ' ', line)  # Normalize spaces inside line
        # Fix initials capitalization
        line = re.sub(r'\b(Ww|Jr|Sr)\b', lambda m: m.group(1).capitalize() + '.', line)
        # Remove extra spaces between uppercase letters (like F R A N K -> FRANK)
        line = re.sub(r'(?<=\b[A-Z])[ ]{1,2}(?=[A-Z])', '', line)
        if line:
            cleaned_lines.append(line)
    return cleaned_lines

def is_noise_line(line):
    # True if line is mostly dots, repeated letters, or gibberish
    if re.fullmatch(r'[\.\s-]+', line):
        return True  # line of mostly dots/dashes/spaces
    # Check for repeated letter patterns, e.g., 'veteeteeteeseetees'
    if re.fullmatch(r'([a-zA-Z])\1{3,}', line):
        return True
    # Check if the line has a high ratio of repeated letters (e.g., more than 70%)
    letters = re.findall(r'[a-zA-Z]', line)
    if letters:
        from collections import Counter
        c = Counter(letters)
        most_common_letter, count = c.most_common(1)[0]
        if count / len(letters) > 0.7:
            return True
    return False

def is_entry_start(line):
    # Heuristic patterns to detect start of new entry
    name_pattern = re.compile(
        r'^(?:[A-Z][a-z]+(?:\s[A-Z]\.)?(?:\s(Jr|Sr|III|IV))?|'  # Capitalized names
        r'[A-Z]{2,}\s[A-Z]{2,})$'  # OR ALL CAPS names
    )
    phone_pattern = re.compile(r'(Phone|DIAL|Dial|Telephone|Phone-|Tel\.?|[0-9]{1,2}-[0-9]{3,4})', re.IGNORECASE)
    address_pattern = re.compile(
        r'\d{1,4}\s+(?:N\.|S\.|E\.|W\.|NORTH|SOUTH|EAST|WEST)?\.?\s*'
        r'(?:Indiana|Arctic|New Jersey|Atlantic|Boardwalk|Avenue|Ave|Street|St|Road|Rd|Blvd|Lane|Ln|Drive|Dr|Place|Pl|Court|Ct|Terrace|Ter|Boulevard|Bvd)\b',
        re.IGNORECASE
    )
    title_keywords = [
        'Expert', 'Editor', 'Proprietor', 'Jeweler', 'Prop.', 'Manager', 'Salesman',
        'President', 'Secretary', 'Executive Secretary', 'Atty', 'Commissioner',
        'Watchmaker', 'Phone', 'Tel', 'All Work'
    ]

    if (name_pattern.match(line)
        or phone_pattern.search(line)
        or address_pattern.search(line)
        or any(keyword.lower() in line.lower() for keyword in title_keywords)):
        return True
    return False


def group_entries(lines):
    entries = []
    current_entry = []

    for line in lines:
        if is_entry_start(line) and current_entry:
            # Start new entry, save previous
            entries.append(' '.join(current_entry).strip())
            current_entry = []
        current_entry.append(line)

    if current_entry:
        entries.append(' '.join(current_entry).strip())

    return entries

def main():
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=300)
        img_path = os.path.join(output_dir, f"page_{page_num+1}.png")
        pix.save(img_path)

        img = Image.open(img_path)
        width, height = img.size

        left_img = img.crop((0, 0, width // 2, height))
        right_img = img.crop((width // 2, 0, width, height))

        for side, side_img in zip(('a', 'b'), (left_img, right_img)):
            processed_img = preprocess_image(side_img)
            raw_text = pytesseract.image_to_string(processed_img, lang='eng')

            lines = clean_raw_text_preserve_lines(raw_text)
            grouped = group_entries(lines)

            out_text = '\n\n'.join(grouped)
            out_path = os.path.join(output_dir, f"page_{page_num+1}{side}.txt")
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(out_text)

            print(f"✅ Processed page {page_num+1}{side}")

    print("🎉 OCR extraction and grouping complete!")

if __name__ == "__main__":
    main()
