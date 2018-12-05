import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr

import detailebenen

def test_answer():
    assert detailebenen.getShapefilebbx('/home/paulsenmann/Documents/gs2/testdata/shapefile/Abgrabungen_Kreis_Kleve/Abgrabungen_Kreis_Kleve_Shape.shp', 'bbx') == 'bbx'

def test_answer1():    
    assert detailebenen.getCSVbbx('/home/paulsenmann/Documents/gs2/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'bbx') == 42

def test_answer2():    
    assert detailebenen.getGeopackagebbx('/home/paulsenmann/Documents/gs2/testdata/Geopackage_Queensland_Children/census2016_cca_qld_short.gpkg', 'bbx') == 42