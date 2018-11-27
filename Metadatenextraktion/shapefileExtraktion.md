# Metadatenextraktion Shapefiles

[github Repository](https://github.com/GeospatialPython/pyshp#reading-shapefiles-using-the-context-manager)

## pyshp installieren:

`$ pip install pyshp`

## Befehle zum Starten des Tools (aus der Kommandozeile heraus)

`$ python`

`>>> import shapefile`

`>>> sf = shapefile.Reader("Pfad zum Dokument")`


## Metadatenextraktion

`>>> sf.shapeType`
-> gibt die Art der Form als Zahl an

    NULL = 0
    POINT = 1
    POLYLINE = 3
    POLYGON = 5
    MULTIPOINT = 8
    POINTZ = 11
    POLYLINEZ = 13
    POLYGONZ = 15
    MULTIPOINTZ = 18
    POINTM = 21
    POLYLINEM = 23
    POLYGONM = 25
    MULTIPOINTM = 28
    MULTIPATCH = 31

`>>> sf.box`
-> gibt die Boundingbox des Shapefiles an

WEITERE FUNKTIONEN GIBT ES [HIER](https://github.com/GeospatialPython/pyshp#reading-shapefiles-using-the-context-manager)
