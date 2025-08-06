# 🗂️ DATA

## Overview

This project extracts, structures, and visualizes data from six African American tourism brochures produced by the Atlantic City Board of Trade (1936–1945). These materials are digitized artifacts of Black leisure and business during segregation—and the data drawn from them reflects not only what's visible, but also what’s missing or contested.

---

> "Owing to the rapid progress of the present civilized world along all lines, and more particularly along commercial lines, and since our group has kept pace with this upward progress both in the Professional and Business fields, we, the citizens of the Northside of Atlantic City, New Jersey, deem it fitting and proper to form an Organization through and by which, we hope to be able to meet the Commercial needs of the inhabitants of our community, and stimulate among them greater interest for cooperation and efficiency in their chosen Professions or Businesses and along all Commercial lines."
> C.J Newsome
> 

---

- **Years Covered**: 1936, 1939, 1941, 1942, 1944, 1945  
- **Origin**: Physical brochures held in the Atlantic City Free Public Library
- **Scanned Formats**: High-resolution PNGs and PDFs, each page representing two 4.5" × 9" brochure columns.

---

## 📊 Data Types Collected

| Field Name           | Description                                                         |
|----------------------|---------------------------------------------------------------------|
| `Brochure`           | Year or ID of the source document                                   |
| `Page`               | Brochure page number                                                |
| `Section`            | Left/right column or subsection                                     |
| `Name`, `Title`      | Individual names and honorifics (e.g., Prop., Proprietor)           |
| `Business`           | Business name                                           |
| `Address`, `City`, `State` | Parsed from OCR; often inferred from nearby text            |
| `Phone`              | Phone number (if present)                                           |
| `Industry`           | Labeled by human and/or inferred from business type                 |
| `Image`, `Image2`    | Associated cropped image files from original page                   |
| `Latitude`, `Longitude` | Manually or semi-automatically geocoded                         |
| `Details`            | Notes on services, slogans, or other distinguishing info            |
| `Section Type`       | Labeled as: advertisement, profile, letter, listing, image, etc.                |

---

## 🧠 Data Extraction & Cleaning

- **OCR**: Processed using Tesseract, with custom image preprocessing for enhanced accuracy.
- **Regex Parsing**: Heuristics segment multi-line entries and detect structured patterns (name/title/address/phone).
- **Manual Review**: Every entry was reviewed and corrected, with additional metadata added where relevant.
- **Duplicate Detection**: Names and businesses appearing across multiple years are linked for longitudinal analysis.

---

## 🗺️ Geospatial Data

- Addresses geocoded using QGIS, historical city directories, and 1940s fire insurance maps.
- Where addresses are incomplete or missing, entries are tagged as **approximate** or grouped in contextual image galleries (e.g., “Boardwalk businesses”).
- A 1940 historical basemap provides visual grounding in the city’s past layout.

---

## ⚖️ Data Ethics

- No facial recognition, identity inference, or algorithmic scoring applied.
- OCR errors are preserved in full-text files to maintain historical integrity.
- All uncertain or missing values are marked explicitly (e.g., `unknown`, `unreadable`, `inferred`).
- Image crops are stored with full source attribution, including page and year metadata.

---

## 📥 Downloads

Available soon via GitHub or project archive:

- `business_entries.csv` – Structured text data with named fields
- `image_metadata.csv` – Metadata for all cropped images, with source info
- `ocr_full_text.zip` – Full-page OCR output from all brochures
- `map_markers.geojson` – GeoJSON file for mapping businesses
- `README.md` – Schema and documentation for all dataset fields

> These datasets are provided for **historical, educational, and research purposes only**.  
> Please cite as:  
> *“Data derived from Atlantic City Board of Trade brochures (1936–1945), Atlantic City Board of Trade.”*

