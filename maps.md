# 🗺️ MAPS

## Overview

The maps in this project serve as a visual interface for exploring Northside businesses, portraits, and community spaces featured in Atlantic City Board of Trade brochures (1936–1945). While the brochures easily stand alone as their own objects of study, layering their historical data onto the city’s geography gives way to spatial patterns of entrepreneurship, leisure, resistance during segregation, disparity of New Deal initiatives, and a country recovering from a historic financial collapse as it transitions into a second world war.

---

You can open the map in a new tab here:  
[Open the full map](./maps/index.html){:target="_blank"}

---

<!-- Embed the map using an iframe -->
<iframe src="./maps/index.html" width="100%" height="600" style="border:none;"></iframe>

---

## 🔍 Cartography

- **Business Listings**: Locations of hotels, restaurants, beauty parlors, nightclubs, tailors, and more.
- **Portraits**: Cropped images of individuals and groups linked to brochure locations.
- **Letters & Endorsements**: Visualized when tied to civic or organizational addresses.
- **Grouped Images**: For entries with no address, related content is clustered into contextual markers (e.g., “Boardwalk Images”).

---

## 🗺️ Basemap

- **Historical Base Layer**: 11940 map of Atlantic City, created from archival scans and georeferenced in QGIS as a GeoTIFF, then exported to PNG tiles for OpenLayers display via qgis2web.
- **Historical Overlay**: 1899 map of Atlantic City, reconstructed from multiple partial archival scans with assistance from an archivist. The scans were stitched together in Photoshop, georeferenced in QGIS, and exported to PNG tiles for OpenLayers display via qgis2web.
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

**QGIS**: Georeferenced historical maps (1940 GeoTIFF and stitched 1899 map) and prepared data for web export.
**qgis2web + OpenLayers**: Converted georeferenced rasters and vector data into interactive, browser-based maps with layer controls.
**GeoJSON**: Structured geographic data exported from CSV and shapefiles for use in web maps.
**Rasterio**: Programmatically handled GeoTIFFs and spatial metadata during preprocessing.
**OpenCV + Tesseract**: Detected and cropped image regions, and performed OCR to generate map-linked historical content.

---

## 📐 Accuracy Notes

- **Geocoding**: Historical addresses matched using directories and Sanborn maps; modern coordinates are approximated where addresses no longer exist.
- **Errors**: Due to OCR artifacts or unclear layout, some locations are estimated or marked “approximate.”
- **Map Boundaries**: Focused on historically Black neighborhoods, particularly the Northside and Kentucky Avenue corridor.


## 🔗 Coming Soon

Interactive map link + GitHub deployment  
Exportable layers as:  
- `business_locations.geojson`  
- `basemap_overlay.tif`  
- `map_readme.md` (schema and coordinate reference)

---

> This project serves as a navigational tool— as a way of narrating place, memory.
> *Use it to explore what was built, preserved, and remembered within the spaces Atlantic City's tourism economy.*
