ol.proj.proj4.register(proj4);
//ol.proj.get("EPSG:3857").setExtent([-8286506.807664, 4773408.649451, -8284466.310679, 4774182.684129]);
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
var lyr_AC1899_1 = new ol.layer.Image({
        opacity: 1,
        
    title: 'AC1899<br />' ,
        
        
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
        
    title: 'AC1940<br />' ,
        
        
        source: new ol.source.ImageStatic({
            url: "./layers/AC1940_2.png",
            attributions: ' ',
            projection: 'EPSG:3857',
            alwaysInRange: true,
            imageExtent: [-8310385.980900, 4755223.881200, -8278686.106300, 4789251.295200]
        })
    });
var format_parsed_brochure_geocoded_3 = new ol.format.GeoJSON();
var features_parsed_brochure_geocoded_3 = format_parsed_brochure_geocoded_3.readFeatures(json_parsed_brochure_geocoded_3, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_parsed_brochure_geocoded_3 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_parsed_brochure_geocoded_3.addFeatures(features_parsed_brochure_geocoded_3);
var lyr_parsed_brochure_geocoded_3 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_parsed_brochure_geocoded_3, 
                style: style_parsed_brochure_geocoded_3,
                popuplayertitle: 'parsed_brochure_geocoded',
                interactive: true,
    title: 'parsed_brochure_geocoded<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_0.png" /> Academics<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_1.png" /> Accommodation<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_2.png" /> Aviation<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_3.png" /> Beauty Culture<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_4.png" /> Beverages<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_5.png" /> Charitable and Christian Organizations<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_6.png" /> Clothing/Attire/Linen/Canvas<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_7.png" /> Clubs and Associations<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_8.png" /> Dairies<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_9.png" /> Eatery<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_10.png" /> Education<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_11.png" /> Entertainment<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_12.png" /> Finance<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_13.png" /> Government<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_14.png" /> Government_city<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_15.png" /> Government_county<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_16.png" /> Government_state<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_17.png" /> Health<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_18.png" /> Heating<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_19.png" /> Honor Award<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_20.png" /> Housing<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_21.png" /> Ice<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_22.png" /> Image<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_23.png" /> Journalism<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_24.png" /> Laboratories<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_25.png" /> Law and Order<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_26.png" /> Manufacturing<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_27.png" /> National<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_28.png" /> Project and Club Managers<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_29.png" /> Real Estate<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_30.png" /> Retail<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_31.png" /> Services<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_32.png" /> Sports<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_33.png" /> Tobacco<br />\
    <img src="styles/legend/parsed_brochure_geocoded_3_34.png" /> Tourism<br />' });

lyr_OpenStreetMap_0.setVisible(true);lyr_AC1899_1.setVisible(true);lyr_AC1940_2.setVisible(true);lyr_parsed_brochure_geocoded_3.setVisible(true);
var layersList = [lyr_OpenStreetMap_0,lyr_AC1899_1,lyr_AC1940_2,lyr_parsed_brochure_geocoded_3];
lyr_parsed_brochure_geocoded_3.set('fieldAliases', {'Source': 'Source', 'Lens': 'Lens', 'Lens_annotation': 'Lens_annotation', 'Details': 'Details', 'Git_image_path': 'Git_image_path', 'Image_Path': 'Image_Path', 'Google_Image_URL': 'Google_Image_URL', 'Year': 'Year', 'Page': 'Page', 'Section': 'Section', 'Name': 'Name', 'Title': 'Title', 'Name2': 'Name2', 'Title2': 'Title2', 'Name3': 'Name3', 'Title3': 'Title3', 'Business': 'Business', 'Type': 'Type', 'Denomination': 'Denomination', 'Department': 'Department', 'Industry': 'Industry', 'Section Type': 'Section Type', 'Image Content': 'Image Content', 'Address': 'Address', 'City': 'City', 'State': 'State', 'Phone': 'Phone', 'Image Content.1': 'Image Content.1', 'ImageAlt_Text': 'ImageAlt_Text', 'Notes': 'Notes', 'latitude': 'latitude', 'longitude': 'longitude', });
lyr_parsed_brochure_geocoded_3.set('fieldImages', {'Source': 'TextEdit', 'Lens': 'TextEdit', 'Lens_annotation': 'TextEdit', 'Details': 'TextEdit', 'Git_image_path': 'TextEdit', 'Image_Path': 'TextEdit', 'Google_Image_URL': 'TextEdit', 'Year': 'Range', 'Page': 'Range', 'Section': 'Range', 'Name': 'TextEdit', 'Title': 'TextEdit', 'Name2': 'TextEdit', 'Title2': 'TextEdit', 'Name3': 'TextEdit', 'Title3': 'TextEdit', 'Business': 'TextEdit', 'Type': 'TextEdit', 'Denomination': 'TextEdit', 'Department': 'TextEdit', 'Industry': 'TextEdit', 'Section Type': 'TextEdit', 'Image Content': 'TextEdit', 'Address': 'TextEdit', 'City': 'TextEdit', 'State': 'TextEdit', 'Phone': 'TextEdit', 'Image Content.1': 'TextEdit', 'ImageAlt_Text': 'TextEdit', 'Notes': 'TextEdit', 'latitude': 'TextEdit', 'longitude': 'TextEdit', });
lyr_parsed_brochure_geocoded_3.set('fieldLabels', {'Source': 'no label', 'Lens': 'no label', 'Lens_annotation': 'no label', 'Details': 'no label', 'Git_image_path': 'no label', 'Image_Path': 'no label', 'Google_Image_URL': 'no label', 'Year': 'no label', 'Page': 'no label', 'Section': 'no label', 'Name': 'no label', 'Title': 'no label', 'Name2': 'no label', 'Title2': 'no label', 'Name3': 'no label', 'Title3': 'no label', 'Business': 'no label', 'Type': 'no label', 'Denomination': 'no label', 'Department': 'no label', 'Industry': 'no label', 'Section Type': 'no label', 'Image Content': 'no label', 'Address': 'no label', 'City': 'no label', 'State': 'no label', 'Phone': 'no label', 'Image Content.1': 'no label', 'ImageAlt_Text': 'no label', 'Notes': 'no label', 'latitude': 'no label', 'longitude': 'no label', });
lyr_parsed_brochure_geocoded_3.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});
