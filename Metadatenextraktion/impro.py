import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import detailebenen


a = detailebenen.getShapefilebbx('/home/paulsenmann/Documents/gs2/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp', 'bbx')
[295896.274870878, 5694747.64703736, 325999.79578122497, 5747140.98659967]

b = detailebenen.getCSVbbx('/home/paulsenmann/Documents/gs2/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'bbx')
No fitting header for latitudes or longitudes

c = detailebenen.getGeopackagebbx('/home/paulsenmann/Documents/gs2/testdata/Geopackage_Queensland_geopackage/census2016_cca_qld_short.gpkg', 'bbx')
[295896.274870878, 5694747.64703736, 325999.79578122497, 5747140.98659967]

d = detailebenen.getGeoJsonbbx('/home/paulsenmann/Documents/gs2/testdata/schutzhuetten_aachen.json', 'bbx')
[292063.81225905, 5618144.09259115, 302531.3161606, 5631223.82854667]

e = detailebenen.getGeoTiffbbx('/home/paulsenmann/Documents/gs2/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif', 'bbx')
[5.9153007564753155, 50.31025197410836, 9.468398712484145, 52.5307755328733]

f = detailebenen.getIsobbx('/home/paulsenmann/Documents/gs2/testdata/', 'bbx')
No fitting header for latitudes or longitudes

g = detailebenen.getNetCDFbbx('/home/paulsenmann/Documents/gs2/testdata/tos_01_2001-2002.nc', 'bbx')
[-79.5, 1.0, 89.5, 359.0]
