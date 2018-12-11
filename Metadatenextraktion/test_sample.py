import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import impro

"""
Bounding Box Extraction
"""

def test_answer():
<<<<<<< HEAD
    print a
    assert detailebenen.getShapefilebbx('/home/paulsenmann/Documents/gs2/testdata/shapefile/Abgrabungen_Kreis_Kleve/Abgrabungen_Kreis_Kleve_Shape.shp', 'bbx') == a
=======
    assert detailebenen.getShapefilebbx('/home/paulsenmann/Documents/gs2/testdata/shapefile/Abgrabungen_Kreis_Kleve/Abgrabungen_Kreis_Kleve_Shape.shp', 'bbx') == "295896.274870878, 5694747.64703736, 325999.79578122497, 5747140.98659967"
>>>>>>> 1c520e847ffa90ba08737befd3af233d37045ec3

def test_answer1():
    print b    
    assert detailebenen.getCSVbbx('/home/paulsenmann/Documents/gs2/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'bbx') == b

def test_answer2():
    print c    
    assert detailebenen.getGeopackagebbx('/home/paulsenmann/Documents/gs2/testdata/Geopackage_Queensland_Children/census2016_cca_qld_short.gpkg', 'bbx') == c

def test_answer3():
    print d
    assert detailebenen.getGeoJsonbbx('/home/paulsenmann/Documents/gs2/testdata/schutzhuetten_aachen.json', 'bbx') == d

def test_answer4():
    print e
    assert detailebenen.getGeoTiffbbx('/home/paulsenmann/Documents/gs2/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif', 'bbx') == e

def test_answer6():
    print g
    assert detailebenen.getNetCDFbbx('/home/paulsenmann/Documents/gs2/testdata/tos_01_2001-2002.nc', 'bbx') == g

"""
Time Frame Extraction
"""

