# GDAL- Metadatenextraktion


GDAL ist ein Package und enthält nicht nur gdal selbst, sondern auch ogr.

Mit dem Befehl ogrinfo lassen sich Informationen über räumliche Vektordaten erheben.
- GeoJSON
- Shapefile
- CSV (on the web)
- GeoPackage
- netCDF

Mit dem Befehl gdalinfo können Informationen über räumliche Rasterdaten erheben.
- GeoTIFF

## Allgemeines Vorgehen

### Allgemeines Vorgehen bei [gdal](https://www.gdal.org/gdalinfo.html):

$ gdalinfo + Pfad zu Datei + optional:beliebiger Befehl, siehe [gdal Dokumentation](https://www.gdal.org/gdalinfo.html)


### Allgemeines Vorgehen bei [ogr](https://www.gdal.org/ogrinfo.html):

$ ogrinfo + Pfad zu Datei → gibt alle Layer der Datei aus
$ ogrinfo + Pfad zu Datei + Name eines Layers + beliebiger Befehl, siehe [ogr Dokumentation](https://www.gdal.org/ogrinfo.html) 

Ein guter Befehl um die Metadaten von Dokumenten zu erhalten ist „-so“


## Beispiele: 
### GeoJSON

`$ ogrinfo '/home/cornelia/Schreibtisch/Testdaten-Die Gruppe 1/geoJSON-die Gruppe 1/Abgrabungen_Kreis_Kleve.geojson'`

INFO: Open of `/home/cornelia/Schreibtisch/Testdaten-Die Gruppe 1/geoJSON-die Gruppe 1/Abgrabungen_Kreis_Kleve.geojson'
      using driver `GeoJSON' successful.
1: ABGRABUNGEN

`$ ogrinfo '/home/cornelia/Schreibtisch/Testdaten-Die Gruppe 1/geoJSON-die Gruppe 1/Abgrabungen_Kreis_Kleve.geojson' ABGRABUNGEN -so`

INFO: Open of `/home/cornelia/Schreibtisch/Testdaten-Die Gruppe 1/geoJSON-die Gruppe 1/Abgrabungen_Kreis_Kleve.geojson'
      using driver `GeoJSON' successful.

Layer name: ABGRABUNGEN
Geometry: Unknown (any)
Feature Count: 71
Extent: (6.047053, 51.372163) - (6.489445, 51.844075)
Layer SRS WKT:
GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.0174532925199433,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]
GDO_GID: Integer (0.0)
TOOLTIP: String (0.0)
BEMERKUNG: String (0.0)
OBJEKTNUMMER: String (0.0)
FIRMA: String (0.0)
GEMEINDE: String (0.0)
BEZEICHNUNG: String (0.0)
RECHTSGRUNDLAGE: String (0.0)
FLAECHE_HA: Real (0.0)
ROHSTOFF: String (0.0)
STATUS: String (0.0)
VERFUELLUNG: String (0.0)
ZUSTAND: String (0.0)
BEGINN_ABGRABUNG: String (0.0)
STAND_DER_DATEN: String (0.0)
MATERIAL_VERFUELLUNG: String (0.0)
TEILFLAECHE: String (0.0)
JAHRGANG: String (0.0)
LINK_DOKUMENT: String (0.0)
BILD: String (0.0)
FREIGABE_INTERNET: String (0.0)
ABGABE_BEZREG: String (0.0)


### GeoPackage:
`$ ogrinfo '/home/cornelia/Schreibtisch/Testdaten-Die Gruppe 1/Geopackage-die Gruppe 1/Geopackage_Queensland_Children/census2016_cca_qld_short.gpkg'`

INFO: Open of `/home/cornelia/Schreibtisch/Testdaten-Die Gruppe 1/Geopackage-die Gruppe 1/Geopackage_Queensland_Children/census2016_cca_qld_short.gpkg'
      using driver `GPKG' successful.
1: census2016_cca_qld_ced_short (3D Measured Unknown (any))
2: census2016_cca_qld_gccsa_short (3D Measured Unknown (any))
3: census2016_cca_qld_lga_short (3D Measured Unknown (any))
4: census2016_cca_qld_poa_short (3D Measured Unknown (any))
5: census2016_cca_qld_ra_short (3D Measured Unknown (any))
6: census2016_cca_qld_sa1_short (3D Measured Unknown (any))
7: census2016_cca_qld_sa2_short (3D Measured Unknown (any))
8: census2016_cca_qld_sa3_short (3D Measured Unknown (any))
9: census2016_cca_qld_sa4_short (3D Measured Unknown (any))
10: census2016_cca_qld_sed_short (3D Measured Unknown (any))
11: census2016_cca_qld_sos_short (3D Measured Unknown (any))
12: census2016_cca_qld_sosr_short (3D Measured Unknown (any))
13: census2016_cca_qld_ssc_short (3D Measured Unknown (any))
14: census2016_cca_qld_ste_short (3D Measured Unknown (any))
15: census2016_cca_qld_sua_short (3D Measured Unknown (any))
16: census2016_cca_qld_ucl_short (3D Measured Unknown (any))

`$ ogrinfo '/home/cornelia/Schreibtisch/Testdaten-Die Gruppe 1/Geopackage-die Gruppe 1/Geopackage_Queensland_Children/census2016_cca_qld_short.gpkg' census2016_cca_qld_ced_short -so`

INFO: Open of `/home/cornelia/Schreibtisch/Testdaten-Die Gruppe 1/Geopackage-die Gruppe 1/Geopackage_Queensland_Children/census2016_cca_qld_short.gpkg'
      using driver `GPKG' successful.

Layer name: census2016_cca_qld_ced_short
Geometry: 3D Measured Unknown (any)
Feature Count: 32
Extent: (96.816900, -43.740500) - (167.998000, -9.142180)
Layer SRS WKT:
GEOGCS["GDA94",
    DATUM["Geocentric_Datum_of_Australia_1994",
        SPHEROID["GRS 1980",6378137,298.257222101,
            AUTHORITY["EPSG","7019"]],
        TOWGS84[0,0,0,0,0,0,0],
        AUTHORITY["EPSG","6283"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.0174532925199433,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4283"]]
FID Column = primaryindex
Geometry Column = geom
ced_code_2016: String (0.0)
C0_4F_EO_M_EO: Integer64 (0.0)
C0_4F_EO_M_O_EVWW: Integer64 (0.0)
C0_4F_EO_M_O_ENWNA: Integer64 (0.0)
C0_4F_EO_M_O_PENS: Integer64 (0.0)
C0_4F_EO_M_O_E_T: Integer64 (0.0)
C0_4F_EO_M_LPENS: Integer64 (0.0)
C0_4F_EO_M_T: Integer64 (0.0)
C0_4F_O_EVWW_M_EO: Integer64 (0.0)
C0_4F_O_EVWW_M_O_EVWW: Integer64 (0.0)
C0_4F_O_EVWW_M_O_ENWNA: Integer64 (0.0)
C0_4F_O_EVWW_M_O_PENS: Integer64 (0.0)
C0_4F_O_EVWW_M_O_E_T: Integer64 (0.0)
C0_4F_O_EVWW_M_LPENS: Integer64 (0.0)
C0_4F_O_EVWW_M_T: Integer64 (0.0)
C0_4F_O_ENWNA_M_EO: Integer64 (0.0)
C0_4F_O_ENWNA_M_O_EVWW: Integer64 (0.0)
C0_4F_O_ENWNA_M_O_ENWNA: Integer64 (0.0)
C0_4F_O_ENWNA_M_O_PENS: Integer64 (0.0)
C0_4F_O_ENWNA_M_O_E_T: Integer64 (0.0)
C0_4F_O_ENWNA_M_LPENS: Integer64 (0.0)
C0_4F_O_ENWNA_M_T: Integer64 (0.0)
C0_4F_O_PENS_M_EO: Integer64 (0.0)
C0_4F_O_PENS_M_O_EVWW: Integer64 (0.0)
C0_4F_O_PENS_M_O_ENWNA: Integer64 (0.0)
C0_4F_O_PENS_M_O_PENS: Integer64 (0.0)
C0_4F_O_PENS_M_O_E_T: Integer64 (0.0)
C0_4F_O_PENS_M_LPENS: Integer64 (0.0)
C0_4F_O_PENS_M_T: Integer64 (0.0)
C0_4F_O_E_T_M_EO: Integer64 (0.0)
C0_4F_O_E_T_M_O_EVWW: Integer64 (0.0)
uvm.



### GeoTIFF
`$ gdalinfo '/home/cornelia/Schreibtisch/Tesdaten-Die Gruppe 1/tif-die Gruppe 1/digitale_Verwaltungsgrenzen_tiff/dvg2bld_geo_nw.tif'`

Driver: GTiff/GeoTIFF
Files: /home/cornelia/Schreibtisch/Testdaten-Die Gruppe 1/tif-die Gruppe 1/digitale_Verwaltungsgrenzen_tiff/dvg2bld_geo_nw.tif
Size is 16250, 16500
Coordinate System is:
PROJCS["ETRS89 / UTM zone 32N",
    GEOGCS["ETRS89",
        DATUM["European_Terrestrial_Reference_System_1989",
            SPHEROID["GRS 1980",6378137,298.2572221008872,
                AUTHORITY["EPSG","7019"]],
            AUTHORITY["EPSG","6258"]],
        PRIMEM["Greenwich",0],
        UNIT["degree",0.0174532925199433],
        AUTHORITY["EPSG","4258"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",9],
    PARAMETER["scale_factor",0.9996],
    PARAMETER["false_easting",500000],
    PARAMETER["false_northing",0],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    AUTHORITY["EPSG","25832"]]
Origin = (249999.999997620063368,5859999.999999721534550)
Pixel Size = (20.000000000146908,-20.000000001067576)
Metadata:
  AREA_OR_POINT=Area
Image Structure Metadata:
  COMPRESSION=LZW
  INTERLEAVE=BAND
Corner Coordinates:
Upper Left  (  250000.000, 5860000.000) (  5d17'18.64"E, 52d49'53.95"N)
Lower Left  (  250000.000, 5530000.000) (  5d31'14.34"E, 49d52'12.52"N)
Upper Right (  575000.000, 5860000.000) ( 10d 6'52.59"E, 52d53' 4.07"N)
Lower Right (  575000.000, 5530000.000) ( 10d 2'41.04"E, 49d55' 3.61"N)
Center      (  412500.000, 5695000.000) (  7d44'31.80"E, 51d23'58.10"N)
Band 1 Block=16250x65 Type=Byte, ColorInterp=Palette
  NoData Value=255
  Image Structure Metadata:
    NBITS=1
  Color Table (RGB with 2 entries)
    0: 0,0,0,255
    1: 255,255,255,255


`$ gdalinfo '/home/cornelia/Schreibtisch/Tesdaten-Die Gruppe 1/tif-die Gruppe 1/digitale_Verwaltungsgrenzen_tiff/dvg2bld_geo_nw.tif' -json`

{
  "description":"\/home\/cornelia\/Schreibtisch\/Testdaten-Die Gruppe 1\/tif-die Gruppe 1\/digitale_Verwaltungsgrenzen_tiff\/dvg2bld_geo_nw.tif",
  "driverShortName":"GTiff",
  "driverLongName":"GeoTIFF",
  "files":[
    "\/home\/cornelia\/Schreibtisch\/Testdaten-Die Gruppe 1\/tif-die Gruppe 1\/digitale_Verwaltungsgrenzen_tiff\/dvg2bld_geo_nw.tif"
  ],
  "size":[
    16250,
    16500
  ],
  "coordinateSystem":{
    "wkt":"PROJCS[\"ETRS89 \/ UTM zone 32N\",\n    GEOGCS[\"ETRS89\",\n        DATUM[\"European_Terrestrial_Reference_System_1989\",\n            SPHEROID[\"GRS 1980\",6378137,298.2572221008872,\n                AUTHORITY[\"EPSG\",\"7019\"]],\n            AUTHORITY[\"EPSG\",\"6258\"]],\n        PRIMEM[\"Greenwich\",0],\n        UNIT[\"degree\",0.0174532925199433],\n        AUTHORITY[\"EPSG\",\"4258\"]],\n    PROJECTION[\"Transverse_Mercator\"],\n    PARAMETER[\"latitude_of_origin\",0],\n    PARAMETER[\"central_meridian\",9],\n    PARAMETER[\"scale_factor\",0.9996],\n    PARAMETER[\"false_easting\",500000],\n    PARAMETER[\"false_northing\",0],\n    UNIT[\"metre\",1,\n        AUTHORITY[\"EPSG\",\"9001\"]],\n    AUTHORITY[\"EPSG\",\"25832\"]]"
  },
  "geoTransform":[
    249999.9999976200633682,
    20.0000000001469083,
    0.0,
    5859999.9999997215345502,
    0.0,
    -20.0000000010675762
  ],
  "metadata":{
    "":{
      "AREA_OR_POINT":"Area"
    },
    "IMAGE_STRUCTURE":{
      "COMPRESSION":"LZW",
      "INTERLEAVE":"BAND"
    }
  },
  "cornerCoordinates":{
    "upperLeft":[
      250000.0,
      5860000.0
    ],
    "lowerLeft":[
      250000.0,
      5530000.0
    ],
    "lowerRight":[
      575000.0,
      5530000.0
    ],
    "upperRight":[
      575000.0,
      5860000.0
    ],
    "center":[
      412500.0,
      5695000.0
    ]
  },
  "wgs84Extent":{
    "type":"Polygon",
    "coordinates":[
      [
        [
          5.2885106,
          52.8316541
        ],
        [
          5.5206489,
          49.8701444
        ],
        [
          10.0447325,
          49.9176687
        ],
        [
          10.114608,
          52.8844642
        ],
        [
          5.2885106,
          52.8316541
        ]
      ]
    ]
  },
  "bands":[
    {
      "band":1,
      "block":[
        16250,
        65
      ],
      "type":"Byte",
      "colorInterpretation":"Palette",
      "noDataValue":255.0,
      "metadata":{
        "IMAGE_STRUCTURE":{
          "NBITS":"1"
        }
      },
      "colorTable":{
        "palette":"RGB",
        "count":2,
        "entries":[
          [
            0,
            0,
            0,
            255
          ],
          [
            255,
            255,
            255,
            255
          ]
        ]
      }
    }
  ]
