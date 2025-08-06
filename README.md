# Atlantic City Board of Trade Brochures Project

## Overview
This project digitizes and analyzes historic African American tourism brochures produced by the Atlantic City Board of Trade during the 1930s–1940s. These brochures highlight businesses, cultural institutions, and leisure sites located primarily in what was known as the Northside of Atlantic City, NJ.

While most of the featured businesses are Black-owned, a small percentage of Asian and Jewish businesses also appear, having purchased advertising space. Not all advertised locations are in Atlantic City—some are in Pleasantville, Ocean City, Absecon, Philadelphia, or even Florida.

These materials challenge assumptions and invite deeper exploration. Rather than summarize all findings here, we encourage you to:

Tour the project
Explore the dataset
Suggest refinements
Apply your critical data skills

Be part of a collaborative effort to center overlooked histories through open science and digital tools.

## Features
📄 OCR-based text extraction from scanned brochures (PDF and PNG)

Features
🖼️ Image enhancement, cropping, and enlargement
Improves scanned brochure visuals for better OCR accuracy and archival use.
🧠 Parsing of names, titles, addresses, and phone numbers
Uses regular expressions and custom heuristics to structure OCR output.
✂️ Splitting scanned pages into logical sections
Automatically separates brochure scans into readable, analyzable chunks.
🌐 Geocoding locations with Folium, GIS tools, and QGIS
Transforms street addresses into mappable coordinates for visualization.
🗺️ Interactive historical mapping
Visualizes geocoded data and brochure content over historical basemaps.
🧾 Integration of historical research and cultural context
Combines data science with archival inquiry and interpretive analysis.
☁️ Google Drive for high-resolution image hosting
Serves brochure images directly to maps and web-based tools.
💻 Built using Python, PyMuPDF, pytesseract, and GitHub Pages
Fully open-source and reproducible, designed for public scholarship.
✍️ Coding syntax and editing support from ChatGPT
Assisted in developing clean, readable, and efficient project documentation and scripts.

## Installation
1. Clone the repository:
```bash
Copy
Edit
git clone https://github.com/yourusername/acbt-brochures.git
cd acbt-brochures
```
2. Install dependencies (Python 3.9+ recommended):
```bash
Copy
Edit
pip install -r requirements.txt
```
3. (Optional) Set up Tesseract OCR:
Install Tesseract
Ensure it’s in your system PATH, or specify the path in your script:
```bash
python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # or your path
```
4. Run the processing script:
```bash
Copy
Edit
python process_brochures.py
```

## Getting Started
You can explore:

- data/ – Structured CSV output of parsed brochure data
- maps/ – Interactive map visualizations

See the docs/ folder or GitHub Pages site for project demos and visualizations.

## Contributing
Pull requests, suggestions, and historical context are welcome. This is a public humanities project built on transparency, collaboration, and curiosity.

## Citation
If using this project in research or teaching, please cite as:

Anstey, Cynthia. Atlantic City Board of Trade Brochures Project. GitHub, 2025. [https://github.com/cvanstey/ACBT-Brochures]
