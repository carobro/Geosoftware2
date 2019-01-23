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
def test_wholeA():
    filepath=__location__+'/testdata/mischung_bbox1'
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[-43.7405, 50.31025197410836, 9.468398712484145, 167.998], [None], [None]]

def test_wholeD():  
    filepath=__location__+"/testdata/mischung_bbox2"  
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[5.520648869321924, 49.87014441103477, 10.114607987362609, 52.88446415203189], [None], [None]]

def test_wholeB():    
    filepath=__location__+'/testdata/geotifftest'
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[5.520648869321924, 49.87014441103477, 10.114607987362609, 52.88446415203189], [None], [None]]

def test_wholeC():  
    filepath=__location__+"/testdata/geopackagetest"  
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[-43.7405, 96.8169, -9.14218, 167.998], [None], [None]]

def test_wholeD():
    filepath=__location__+"/testdata/csvordnertest"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == [[47.988889, 4.3175, 53.217222, 9.731219], [None], [None]]

"""
#####################################
# --detail=bbox --folder=whole --time
#####################################
def test_wholeD():
    filepath="https://uni-muenster.sciebo.de/s/QFj5pzm7AzxAh1f?path=%2FfunktionierendeTestdaten_gruppe1%2Fzeitdaten%2Ftimegeo"
    filepath1="/home/minicaro/Downloads/timegeo/timegeo"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == None[[47.988889, 4.3175, 53.217222, 9.731219], [None], [None]]

def test_wholeE():    
    filepath= "https://uni-muenster.sciebo.de/s/QFj5pzm7AzxAh1f?path=%2FfunktionierendeTestdaten_gruppe1%2Fzeitdaten%2Ftime%20mischung"
    filepath1="/home/minicaro/Downloads/time_mischung"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == None

"""