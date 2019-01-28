import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os
import dateparser

import extractTool
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
###############################
# --detail=bbox --folder=whole
###############################
def test_whole_A():
    filepath=__location__+'/testdata/mischung_bbox1'
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[-43.7405, 50.31025197410836, 9.468398712484145, 167.998], [None], [None]]

def test_whole_B():  
    filepath=__location__+"/testdata/mischung_bbox2"  
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[5.520648869321924, 49.87014441103477, 10.114607987362609, 52.88446415203189], [None], [None]]

def test_whole_C():    
    filepath=__location__+'/testdata/geotifftest'
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[5.520648869321924, 49.87014441103477, 10.114607987362609, 52.88446415203189], [None], [None]]

def test_whole_D():  
    filepath=__location__+"/testdata/geopackagetest"  
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[-43.7405, 96.8169, -9.14218, 167.998], [None], [None]]

def test_whole_E():
    filepath=__location__+"/testdata/csvordnertest"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[47.988889, 4.3175, 53.217222, 9.731219], [None], [None]]


#####################################
# --detail=bbox --folder=whole --time
#####################################

def test_wholeD():
    filepath=__location__+"/testdata/timegeo/timegeo"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', True) == [[6.220493316650391, 50.52150360276628, 7.647256851196289, 51.974624029877454], [None], ['2018-11-14 00:00:00', '2018-11-14 00:00:00']]

def test_wholeE():    
    filepath=__location__+"/testdata/time_mischung"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', True) == [[-90.0, 0.0, 90.0, 357.5], [None], ['2002-07-01 12:00:00', '2018-11-14 00:00:00']]
