ol.proj.proj4.register(proj4);
//ol.proj.get("EPSG:3857").setExtent([-8289318.504110, 4772322.690662, -8282175.948732, 4776529.605598]);
var wms_layers = [];


        var lyr_OpenStreetMap_0 = new ol.layer.Tile({
            'title': 'OpenStreetMap',
            'type':'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
            attributions: ' ',
                url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
            })
        });
var format_parsed_brochure_geocoded_1 = new ol.format.GeoJSON();
var features_parsed_brochure_geocoded_1 = format_parsed_brochure_geocoded_1.readFeatures(json_parsed_brochure_geocoded_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_parsed_brochure_geocoded_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_parsed_brochure_geocoded_1.addFeatures(features_parsed_brochure_geocoded_1);
var lyr_parsed_brochure_geocoded_1 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_parsed_brochure_geocoded_1, 
                style: style_parsed_brochure_geocoded_1,
                popuplayertitle: 'parsed_brochure_geocoded',
                interactive: true,
    title: 'parsed_brochure_geocoded<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_0.png" /> Academics<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_1.png" /> Accommodation<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_2.png" /> Aviation<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_3.png" /> Award<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_4.png" /> Charitable and Christian Organizations<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_5.png" /> Clubs and Associations<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_6.png" /> Convention<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_7.png" /> Education<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_8.png" /> Entertainment<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_9.png" /> Food<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_10.png" /> Government<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_11.png" /> Image<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_12.png" /> Journalism<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_13.png" /> Laboratories<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_14.png" /> Music<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_15.png" /> Retail<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_16.png" /> Services<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_17.png" /> Sports<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_18.png" /> Tobacco<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_19.png" /> Tourism<br />\
    <img src="styles/legend/parsed_brochure_geocoded_1_20.png" /> <br />' });
var lyr_AC1899_2 = new ol.layer.Image({
        opacity: 1,
        
    title: 'AC1899<br />' ,
        
        
        source: new ol.source.ImageStatic({
            url: "./layers/AC1899_2.png",
            attributions: ' ',
            projection: 'EPSG:3857',
            alwaysInRange: true,
            imageExtent: [-8301664.187728, 4762837.255947, -8282080.918499, 4778863.598559]
        })
    });
var lyr_AC1940_3 = new ol.layer.Image({
        opacity: 1,
        
    title: 'AC1940<br />' ,
        
        
        source: new ol.source.ImageStatic({
            url: "./layers/AC1940_3.png",
            attributions: ' ',
            projection: 'EPSG:3857',
            alwaysInRange: true,
            imageExtent: [-8310385.980900, 4755223.881200, -8278686.106300, 4789251.295200]
        })
    });

lyr_OpenStreetMap_0.setVisible(true);lyr_parsed_brochure_geocoded_1.setVisible(true);lyr_AC1899_2.setVisible(true);lyr_AC1940_3.setVisible(true);
var layersList = [lyr_OpenStreetMap_0,lyr_parsed_brochure_geocoded_1,lyr_AC1899_2,lyr_AC1940_3];
lyr_parsed_brochure_geocoded_1.set('fieldAliases', {'Brochure': 'Brochure', 'Lens': 'Lens', 'Details': 'Details', 'Image_Path': 'Image_Path', 'Image_URL': 'Image_URL', 'Year': 'Year', 'Page': 'Page', 'Section': 'Section', 'Name': 'Name', 'Title': 'Title', 'Name2': 'Name2', 'Title2': 'Title2', 'Business': 'Business', 'Type': 'Type', 'Denomination': 'Denomination', 'Department': 'Department', 'Industry': 'Industry', 'Section Type': 'Section Type', 'Image Content': 'Image Content', 'Address': 'Address', 'City': 'City', 'State': 'State', 'Phone': 'Phone', 'Image Content.1': 'Image Content.1', 'ImageAlt_Text': 'ImageAlt_Text', 'Notes': 'Notes', 'latitude': 'latitude', 'longitude': 'longitude', });
lyr_parsed_brochure_geocoded_1.set('fieldImages', {'Brochure': 'TextEdit', 'Lens': 'TextEdit', 'Details': 'TextEdit', 'Image_Path': 'TextEdit', 'Image_URL': 'TextEdit', 'Year': 'Range', 'Page': 'Range', 'Section': 'Range', 'Name': 'TextEdit', 'Title': 'TextEdit', 'Name2': 'TextEdit', 'Title2': 'TextEdit', 'Business': 'TextEdit', 'Type': '', 'Denomination': 'TextEdit', 'Department': 'TextEdit', 'Industry': 'TextEdit', 'Section Type': 'TextEdit', 'Image Content': 'TextEdit', 'Address': 'TextEdit', 'City': 'TextEdit', 'State': 'TextEdit', 'Phone': 'TextEdit', 'Image Content.1': 'TextEdit', 'ImageAlt_Text': 'TextEdit', 'Notes': 'TextEdit', 'latitude': 'TextEdit', 'longitude': 'TextEdit', });
lyr_parsed_brochure_geocoded_1.set('fieldLabels', {'Brochure': 'no label', 'Lens': 'no label', 'Details': 'no label', 'Image_Path': 'no label', 'Image_URL': 'no label', 'Year': 'inline label - always visible', 'Page': 'no label', 'Section': 'no label', 'Name': 'no label', 'Title': 'no label', 'Name2': 'no label', 'Title2': 'no label', 'Business': 'no label', 'Type': 'no label', 'Denomination': 'no label', 'Department': 'no label', 'Industry': 'inline label - always visible', 'Section Type': 'no label', 'Image Content': 'no label', 'Address': 'no label', 'City': 'no label', 'State': 'no label', 'Phone': 'no label', 'Image Content.1': 'no label', 'ImageAlt_Text': 'no label', 'Notes': 'no label', 'latitude': 'no label', 'longitude': 'no label', });
lyr_parsed_brochure_geocoded_1.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});