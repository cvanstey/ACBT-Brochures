# Atlantic City Board of Trade Brochures Project

## Overview
This project digitizes and analyzes historic African American tourism brochures produced by the Atlantic City Board of Trade in Atlantic City, NJ, during the 1930s–1940s. The brochures highlight Black-owned businesses, cultural institutions, and leisure sites in a segregated Atlantic City.

Using Python and open-source libraries, the project extracts text and images from scanned brochures, parses structured data like names, addresses, and phone numbers, and geocodes locations to create interactive maps and visualizations. The work bridges data science, archival research, and digital humanities to make these fragile historical materials accessible and analyzable.

## Features
- High-resolution image extraction from scanned PDFs and PNGs  
- OCR text extraction using PyMuPDF and pytesseract  
- Parsing of names, titles, addresses, and phone numbers with regex and heuristics  
- Splitting scanned brochure pages into individual sections  
- Geocoding addresses for mapping with Folium and GIS tools  
- Integration of historical research and cultural context

## Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/acbt-brochures.git
