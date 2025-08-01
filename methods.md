### 🧪 Methods

This project combines computational methods with archival critique to recover and reinterpret mid-20th-century African American tourism materials—specifically brochures produced by the Atlantic City Board of Trade from the 1930s to 1950s. These fragile and visually complex documents were never meant to be data, but they offer a powerful window into the spatial and cultural history of segregation-era leisure and labor.

### 1. Document Processing & OCR

Each brochure was scanned as high-resolution images, then processed using Python and open-source tools:

- **Image Preprocessing**: Pages are split and enhanced using PIL and OpenCV to isolate columns, crop images, and improve legibility.
- **Optical Character Recognition**: Tesseract OCR extracts textual content. Custom regex rules group names, titles, addresses, and phone numbers, reconstructing business entries from noisy data.
- **Image Region Detection**: Graphic elements such as ads and portraits are identified and saved as individual image files with metadata (e.g., source page, dimensions).

### 2. Data Structuring

The extracted data is normalized into a structured format for CSV export and mapping:

- **Fields include**: Business name, proprietor(s), address, phone number, brochure year, industry type, image references, and OCR confidence scores.
- **Named Entity Linking** is manually supported to identify repeated individuals or businesses across years.

### 3. Geospatial Mapping

To map historical addresses:

- **Geocoding** is done via manual lookup, historical maps, and approximate placement when exact locations are unknown.
- A **1940 georeferenced basemap** is used in QGIS and Folium to provide historical spatial context.
- Businesses without geolocation are grouped in image galleries for visual browsing.

### 4. Critical Archival Practice

This is not a neutral data pipeline. The materials are situated in a deeply racialized past, and the methods acknowledge that:

- **Visual analysis** attends to gazes, smiles, and posture in portraits—questioning who is meant to be seen, and how.
- **Textual silences**—missing names, ambiguous addresses—are treated as meaningful, not errors.
- **Metadata ethics** are observed: no biometric tagging, no AI-generated inferences about faces or intentions.
- **Archival theory** from Black studies and memory work informs decisions about what to extract, annotate, and display.

### 5. Limitations & Future Work

- OCR errors persist in heavily degraded scans.
- Not all addresses can be reliably geocoded.
- Image classification and industry tagging are in progress and may evolve with community input.

This methodological approach foregrounds **imperfection, improvisation, and interpretation**—treating archival recovery as both a technical and ethical act.

---
