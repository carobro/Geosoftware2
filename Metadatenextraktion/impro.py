import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import detailebenen


a = detailebenen.getShapefilebbx('/home/paulsenmann/Documents/gs2/testdata/shapefile/Abgrabungen_Kreis_Kleve/Abgrabungen_Kreis_Kleve_Shape.shp', 'bbx')
global b
b = detailebenen.getCSVbbx('/home/paulsenmann/Documents/gs2/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'bbx')
global c
c = detailebenen.getGeopackagebbx('/home/paulsenmann/Documents/gs2/testdata/Geopackage_Queensland_Children/census2016_cca_qld_short.gpkg', 'bbx')
global d
d = detailebenen.getGeoJsonbbx('/home/paulsenmann/Documents/gs2/testdata/schutzhuetten_aachen.json', 'bbx')
global e
e = detailebenen.getGeoTiffbbx('/home/paulsenmann/Documents/gs2/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif', 'bbx')
global g
g = detailebenen.getNetCDFbbx('/home/paulsenmann/Documents/gs2/testdata/tos_01_2001-2002.nc', 'bbx')

print a
print b
print c
print d
print e
print g
