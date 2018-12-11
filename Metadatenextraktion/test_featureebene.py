import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr

import featureebene
import detailebenen

# Tests fuer die convex-hull methode
def test_answer():
    assert featureebene.convexhull(getalleCoordinaten1) == [lat1, lon1, lat2, lon2]

def test_answer1():
    assert featureebene.convexhull(getalleCoordinaten2) == [lat1, lon1, lat2, lon2]

def test_answer2():
    assert featureebene.convexhull(getalleCoordinaten3) == [lat1, lon1, lat2, lon2]


# zur jeweiligen Datei
path = 'https://uni-muenster.sciebo.de/s/QFj5pzm7AzxAh1f'
def test_answer3():
    assert detailebenen.getShapefilebbx(path, 'feature') == 0

def test_answer4():    
    assert detailebenen.getCSVbbx(path, 'feature') == 0

def test_answer5():    
    assert detailebenen.getGeopackagebbx(path, 'feature') == 0

def test_answer6():    
    assert detailebenen.getGeoJsonbbx(path, 'feature') == 0

def test_answer7():    
    assert detailebenen.getIsobbx(path, 'feature') == 0

def test_answer8():    
    assert detailebenen.getGeoTiffbbx(path, 'feature') == 0

def test_answer9():    
    assert detailebenen.getNetCDFbbx(path, 'feature') == 0