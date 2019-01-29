import click        # used to print something , shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os
import dateparser   # used to parse the dates

import extractTool # used for the the transformation and prints  # used for the the transformation and prints
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
###############################
# --detail=bbox --folder=whole
###############################
def test_whole_A():
    filepath=__location__+'/testdata/mischung_bbox1'
    assert extractTool.getMetadata(filepath, 'bbox' , False) == [[5.9153007564753155, -43.7405, 167.998, 52.5307755328733], [None], [None]]

def test_whole_B():  
    filepath=__location__+"/testdata/mischung_bbox2"  
    assert extractTool.getMetadata(filepath, 'bbox' , False) == [[5.520648869321924, 49.87014441103477, 10.114607987362609, 52.88446415203189], [None], [None]]

def test_whole_C():    
    filepath=__location__+'/testdata/geotifftest'
    assert extractTool.getMetadata(filepath, 'bbox' , False) == [[5.520648869321924, 49.87014441103477, 10.114607987362609, 52.88446415203189], [None], [None]]

def test_whole_D():  
    filepath=__location__+"/testdata/geopackagetest"  
    assert extractTool.getMetadata(filepath, 'bbox' , False) == [[96.8169, -43.7405, 167.998, -9.14218], [None], [None]]

def test_whole_E():
    filepath=__location__+"/testdata/csvordnertest"
    assert extractTool.getMetadata(filepath, 'bbox' , False) == [[4.3175, 47.988889, 9.731219, 53.217222], [None], [None]]

def test_whole_F():
    filepath=__location__+"/testdata/innergeoj"
    assert extractTool.getMetadata(filepath, 'bbox', False) == [[6.60864, 51.2380774, 6.71483, 51.31549], [None], [None]]


#####################################
# --detail=bbox --folder=whole --time
#####################################

def test_wholeD():
    filepath=__location__+"/testdata/timegeo/timegeo"
    assert extractTool.getMetadata(filepath, 'bbox' , True) == [[6.220493316650391, 50.52150360276628, 7.647256851196289, 51.974624029877454], [None], ['2018-11-14 00:00:00', '2018-11-14 00:00:00']]

def test_wholeE():    
    filepath=__location__+"/testdata/time_mischung"
    assert extractTool.getMetadata(filepath, 'bbox', True) == [[-90.0, 0.0, 90.0, 357.5], [None], ['2002-07-01 12:00:00', '2018-11-14 00:00:00']]

def test_wholeF():    
    filepath=__location__+"/testdata/timegeo/timegeo"
    assert extractTool.getMetadata(filepath, 'bbox', True) == [[6.220493316650391, 50.52150360276628, 7.647256851196289, 51.974624029877454], [None], ['2018-11-14 00:00:00', '2018-11-14 00:00:00']]

def test_wholeG():    
    filepath=__location__+"/testdata/leer"
    assert extractTool.getMetadata(filepath, 'bbox', True) == None


#####################################
# --detail=convexHull --folder=whole 
#####################################

def test_whole_AC():
    filepath=__location__+'/testdata/mischung_bbox1'
    assert extractTool.getMetadata(filepath, 'convexHull', False) == [[None], [None], [None]]

def test_whole_BC():  
    filepath=__location__+"/testdata/mischung_bbox2"  
    assert extractTool.getMetadata(filepath, 'convexHull', False) == [[None], [None], [None]]

def test_whole_CC():    
    filepath=__location__+'/testdata/geotifftest'
    assert extractTool.getMetadata(filepath, 'convexHull', False) == [[None], [None], [None]]

def test_whole_DC():  
    filepath=__location__+"/testdata/geopackagetest"  
    assert extractTool.getMetadata(filepath, 'convexHull', False) == [[None], [None], [None]]

def test_whole_EC():
    filepath=__location__+"/testdata/csvordnertest"
    assert extractTool.getMetadata(filepath, 'convexHull', False) == [[None], [None], [None]]

def test_whole_FC():
    filepath=__location__+"/testdata/innergeoj"
    assert extractTool.getMetadata(filepath, 'convexHull', False) == [[None], [None], [None]]


###########################################
# --detail=convexHull --folder=whole --time 
###########################################

def test_wholeDC():
    filepath=__location__+"/testdata/timegeo/timegeo"
    assert extractTool.getMetadata(filepath, 'convexHull', True) == [[None], [None], ['2018-11-14 00:00:00', '2018-11-14 00:00:00']]

def test_wholeEC():    
    filepath=__location__+"/testdata/time_mischung"
    assert extractTool.getMetadata(filepath, 'convexHull', True) == [[None], [None], ['2002-07-01 12:00:00', '2018-11-14 00:00:00']]

def test_wholeFC():    
    filepath=__location__+"/testdata/timegeo/timegeo"
    assert extractTool.getMetadata(filepath, 'convexHull', True) == [[None], [None], ['2018-11-14 00:00:00', '2018-11-14 00:00:00']]

def test_wholeGC():    
    filepath=__location__+"/testdata/leer"
    assert extractTool.getMetadata(filepath, 'convexHull', True) == None


###########################################
# --detail=bbox folder in folder 
###########################################

def test_wholeFF():    
    filepath=__location__+"/testdata/folder"
    assert extractTool.getMetadata(filepath, 'bbox', False) == [[6.59663465544554, 51.2380774, 6.71483, 51.486636388722296], [None], [None]]
