# Georeferencing & Overlaying Historical Maps in QGIS

**Atlantic City 1899 Map · OSM · CSV Data Integration**  
*Last updated: August 2025* · *QGIS version 3.34+*

---

## 📍 Project Overview

This README documents the process used to align an 1899 historic map of Atlantic City with modern basemaps and overlay structured location data from a CSV file. The workflow includes georeferencing, CRS alignment, and CSV point import.

It covers:
- Georeferencing historical imagery
- Setting the correct Coordinate Reference Systems (CRSs)
- Importing latitude-longitude CSV points
- Tracing and drawing polygon boundaries (e.g., housing tracts)

---

## 🧭 Coordinate Systems

| Layer Type                | CRS          | Notes                                      |
|---------------------------|--------------|--------------------------------------------|
| OpenStreetMap (basemap)  | EPSG:3857    | Web Mercator; default for XYZ tiles        |
| 1940 Historic Map.tif     | EPSG:3857    | Georeferenced raster from Mapping Inequality |
| 1899 Historical Map Image | No CRS       | Georeferenced manually via GCPs to EPSG:3857 |
| CSV Lat/Lon Points        | EPSG:4326    | Imported in geographic coordinates; QGIS reprojects to EPSG:3857 |

---

## 📂 Project Files Structure

project-folder/
├── data/
│ ├── 1940_map.tif
│ ├── 1899_original.png
│ ├── georef_1899.tif
│ └── georef_1899.points
├── csv/
│ └── points.csv
├── qgis/
│ └── project.qgz
└── README.md

yaml
Copy
Edit

---

## 🗺 Initial Setup

1. Start a new project: `Project > New`, name and save it.
2. Add base layer:  
   Use the **Browser Panel** → find **XYZ Tiles** → right-click → *New Connection* → name it (e.g. “OSM”) and use:  
   `https://tile.openstreetmap.org/{z}/{x}/{y}.png`
3. Drag the new tile layer into your Layers panel. Set the **project CRS** to **EPSG:3857**.

---

## 🧩 Georeferencing the 1899 Map

1. Open: `Raster > Georeferencer`
2. Load your unreferenced 1899 PNG.
3. Add **GCPs (Ground Control Points)**:
   - Use consistent, well-spaced landmarks or intersections.
   - Click on the image, then use **“From Map Canvas”** to select real-world positions.
4. Use at least **8–12** GCPs, well-distributed.
5. In **Transformation Settings**:
   - Transformation: *Thin Plate Spline* or *Polynomial 2*
   - Resampling: *Cubic*
   - Target CRS: EPSG:3857
   - Output file: e.g. `georef_1899.tif`
   - Uncheck “Draw GCP points” (for clean output)
   - Check “Load in QGIS when done”
6. Click **Start Georeferencing**
7. When prompted, save the `.points` file if future refinement is needed.

---

## 🧹 Hiding GCPs & Cleanup

- Close the Georeferencer window when done.  
- If asked to save points and you're finished, choose **No**.  
- Deselect GCPs in the table if they remain visible but faded.

---

## 📦 Importing CSV Lat/Long Data

1. `Layer > Add Layer > Add Delimited Text Layer…`
2. Load your CSV
3. Define:
   - X field = longitude
   - Y field = latitude
   - CRS = **EPSG:4326 – WGS 84**
4. QGIS will reproject to the project CRS (EPSG:3857)

**Optional Reprojection:**
- Right-click layer → `Export > Save Features As…`
- Format: GeoPackage (.gpkg) or Shapefile
- CRS: EPSG:3857

---

## 🛠 Drawing Polygons (e.g. Housing Tracts)

1. `Layer > Create Layer > New Shapefile Layer…`
   - Type: Polygon
   - CRS: EPSG:3857
   - Add fields: `name`, `notes`, etc.
2. Save (e.g. `housing_tracts.shp`)
3. Toggle editing mode
4. Use **Add Polygon Feature** tool:
   - Left-click = vertex
   - Right-click = finish
   - Add attribute data
5. Toggle editing off and save.

---

## ✅ Tips & Troubleshooting

- **Points not aligned?** Ensure CSV imported with EPSG:4326.
- **Layer disappears?** Use "Zoom to Layer" and check CRS settings.
- **Better alignment?** Use intersections or permanent structures for GCPs.
- **Try different transformations** (e.g. Thin Plate Spline vs Polynomial 2)

---

## 🌐 Add OpenStreetMap in QGIS

1. `View > Panels > Browser Panel`
2. Right-click `XYZ Tiles > New Connection`
3. Name: "OpenStreetMap"
4. URL: `https://tile.openstreetmap.org/{z}/{x}/{y}.png`

---

## 🗺️ Handling Large Historical Maps

Some historical maps may be very large GeoTIFFs (~150 MP). For web deployment:

| Use Case                       | Recommendation               |
|-------------------------------|------------------------------|
| Local QGIS work               | Full resolution              |
| Web use (Leaflet/QGIS2Web)   | Downscale or tile            |
| GitHub Pages overlay          | Resize + tile or compress    |
| Print/export                  | Keep full resolution         |

---

## 🧭 Check if a .TIF is Georeferenced

1. Load into QGIS: `Layer > Add Raster Layer`
2. Right-click > `Properties > Information`
3. Look for:
   - CRS (e.g., EPSG:3857)
   - World extents (not pixel-only)
   - GDAL metadata for GeoTIFF

---

## 📝 Final Notes

- Use `EPSG:3857` for all basemaps and output rasters
- Use `EPSG:4326` when importing raw lat/lon CSVs
- Avoid manually setting CRS — reproject instead
- Always save `.points` if georeferencing might need tweaking

---

## ✅ Final Outcome

After ~2 hours of refinement:
- 1899 map now aligns spatially with OSM and the 1940 map
- All vector and raster layers match under EPSG:3857
- CSV points imported using EPSG:4326 appear correctly
- Polygon layers trace housing tracts using modern features

Great for historical research, public housing studies, or urban mapping projects.
