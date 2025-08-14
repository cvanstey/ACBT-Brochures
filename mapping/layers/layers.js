ol.proj.proj4.register(proj4);

var lyr_OpenStreetMap_0 = new ol.layer.Tile({
    title: 'OpenStreetMap',
    type: 'base',
    opacity: 1.0,
    source: new ol.source.XYZ({
        attributions: ' ',
        url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
    })
});

var lyr_AC1899_1 = new ol.layer.Image({
    opacity: 1,
    title: 'AC1899<br />',
    source: new ol.source.ImageStatic({
        url: "./layers/AC1899_1.png",
        attributions: ' ',
        projection: 'EPSG:3857',
        alwaysInRange: true,
        imageExtent: [-8301664.187728, 4762837.255947, -8282080.918499, 4778863.598559]
    })
});

var lyr_AC1940_2 = new ol.layer.Image({
    opacity: 1,
    title: 'AC1940<br />',
    source: new ol.source.ImageStatic({
        url: "./layers/AC1940_2.png",
        attributions: ' ',
        projection: 'EPSG:3857',
        alwaysInRange: true,
        imageExtent: [-8310385.980900, 4755223.881200, -8278686.106300, 4789251.295200]
    })
});

// Ensure you define a style for vector layers (example for parsed_brochure_geocoded_3)
var style_parsed_brochure_geocoded_3 = new ol.style.Style({
    fill: new ol.style.Fill({
        color: 'rgba(255, 255, 255, 0.6)'
    }),
    stroke: new ol.style.Stroke({
        color: '#000',
        width: 2
    })
});

var format_parsed_brochure_geocoded_3 = new ol.format.GeoJSON();
var features_parsed_brochure_geocoded_3 = format_parsed_brochure_geocoded_3.readFeatures(json_parsed_brochure_geocoded_3, {
    dataProjection: 'EPSG:4326',
    featureProjection: 'EPSG:3857'
});

var jsonSource_parsed_brochure_geocoded_3 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_parsed_brochure_geocoded_3.addFeatures(features_parsed_brochure_geocoded_3);

var lyr_parsed_brochure_geocoded_3 = new ol.layer.Vector({
    declutter: false,
    source: jsonSource_parsed_brochure_geocoded_3,
    style: style_parsed_brochure_geocoded_3,
    title: 'parsed_brochure_geocoded<br />' +
        '<img src="styles/legend/parsed_brochure_geocoded_3_0.png" /> Academics<br />' +
        // Add more legend items as needed
});

var layersList = [lyr_OpenStreetMap_0, lyr_AC1899_1, lyr_AC1940_2, lyr_parsed_brochure_geocoded_3];

var map = new ol.Map({
    target: 'map',
    layers: layersList,
    view: new ol.View({
        center: [-8290000, 4775000], // Adjust the center point
        zoom: 12
    })
});

lyr_OpenStreetMap_0.setVisible(true);
lyr_AC1899_1.setVisible(true);
lyr_AC1940_2.setVisible(true);
lyr_parsed_brochure_geocoded_3.setVisible(true);
