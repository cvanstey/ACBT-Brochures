# 🗺️ MAPS

## Overview

The maps in this project serve as a visual interface for exploring Northside businesses, portraits, and community spaces featured in Atlantic City Board of Trade brochures (1936–1945). While the brochures easily stand alone as their own objects of study, layering their historical data onto the city’s geography gives way to spatial patterns of entrepreneurship, leisure, resistance during segregation, disparity of New Deal initiatives, and a country recovering from a historic financial collapse as it transitions into a second world war.

---

## 🔍 Cartography

- **Business Listings**: Locations of hotels, restaurants, beauty parlors, nightclubs, tailors, and more.
- **Portraits**: Cropped images of individuals and groups linked to brochure locations.
- **Letters & Endorsements**: Visualized when tied to civic or organizational addresses.
- **Grouped Images**: For entries with no address, related content is clustered into contextual markers (e.g., “Boardwalk Images”).

---

## 🗺️ Basemap

- **Historical Base Layer**: 1940 GeoTIFF map of Atlantic City sourced from archival scans and georeferenced using QGIS and Rasterio.
- **Modern Context Layer**: Optional modern map layer for comparative exploration.

---

## 🧩 Map Layers & Filters

- **Toggleable Industry Layers**: Users can show/hide industries (e.g., lodging, services, food, entertainment).
- **Year Filters**: View entries by brochure year to analyze change over time.
- **Image Markers**: Icons open pop-ups containing brochure images, captions, and OCR snippets.
- **Unknown Address Layer**: Entries without specific location are grouped in “gallery” markers with explanations.

---

## 🧭 Navigation Features

- **Clustered Markers**: Densely located businesses auto-cluster at low zoom levels.
- **Pop-Up Cards**: Each location opens with images, text, and source year.
- **Searchable**: By business name, person, or street address.
- **Legends & Labels**: Custom legends provide context for icons and color codes.

---

## ⚙️ Technologies Used

- **Folium**: Python-based interactive maps rendered with Leaflet.js.
- **GeoJSON**: Structured geographic data exported from CSV and shapefiles.
- **Rasterio**: Used to georeference and overlay historical maps.
- **OpenCV + Tesseract**: Image crops and OCR for generating map-linked content.

---

## 📐 Accuracy Notes

- **Geocoding**: Historical addresses matched using directories and Sanborn maps; modern coordinates are approximated where addresses no longer exist.
- **Errors**: Due to OCR artifacts or unclear layout, some locations are estimated or marked “approximate.”
- **Map Boundaries**: Focused on historically Black neighborhoods, particularly the Northside and Kentucky Avenue corridor.


You can open the map in a new tab here:  
[Open the full map](./maps/index.html){:target="_blank"}

---

<!-- Embed the map using an iframe -->
<iframe src="./maps/index.html" width="100%" height="600" style="border:none;"></iframe>


## 🔗 Coming Soon

Interactive map link + GitHub deployment  
Exportable layers as:  
- `business_locations.geojson`  
- `basemap_overlay.tif`  
- `map_readme.md` (schema and coordinate reference)

---

> The map serves as a navigational tool—it but it has a way of narrating place, memory, and positioning itself as a method to interpret theory.  
> *Use it to explore what was built, preserved, and remembered in the margins of Atlantic City's tourism economy.*
