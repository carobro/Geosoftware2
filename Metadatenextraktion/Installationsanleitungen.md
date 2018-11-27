# Installationsanleitungen - Kurzfassung

## Für CSV - Extraktion
`$ pip install pandas`
`$ python`
`>>> import pandas as pd`
`>>> pd.read_csv(filepath)`

## Für Shapefile - Extraktion

`$ pip install pyshp`
`$ python`
`>>> import shapefile`
`>>> shapefile.Reader("filepath")`

## Für GeoJson - Extraktion
`$ pip install PyGeoj`
`$python`
`>>> import pygeoj`
`data = pygeoj.load(filepath)`
`(data).bbox`  

## Für GeoTiff - Extraktion
`install from https://github.com/nextgis/pygdal`
`$ python`
`>>> from osgeo import gdal`
`>>> gdalinfo(filepath)`