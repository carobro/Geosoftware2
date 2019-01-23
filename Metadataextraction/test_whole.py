import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os
import dateparser

import extractTool
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder

###############################
# --detail=bbox --folder=whole
###############################
def test_wholeA():
    filepath='https://uni-muenster.sciebo.de/s/QFj5pzm7AzxAh1f?path=%2FfunktionierendeTestdaten_gruppe1%2Fmischung'
    filepath1="/home/minicaro/Downloads/mischung"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == None

def test_wholeB():    
    filepath='https://uni-muenster.sciebo.de/s/QFj5pzm7AzxAh1f?path=%2FfunktionierendeTestdaten_gruppe1%2Fgeotiff'
    filepath1="/home/minicaro/Downloads/geotiff"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == None

def test_wholeC():  
    filepath="https://uni-muenster.sciebo.de/s/QFj5pzm7AzxAh1f?path=%2FfunktionierendeTestdaten_gruppe1%2Fgeopackage"  
    filepath1="/home/minicaro/Downloads/geopackage"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == None

#####################################
# --detail=bbox --folder=whole --time
#####################################
def test_wholeD():
    filepath="https://uni-muenster.sciebo.de/s/QFj5pzm7AzxAh1f?path=%2FfunktionierendeTestdaten_gruppe1%2Fzeitdaten%2Ftimegeo"
    filepath1="/home/minicaro/Downloads/timegeo"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == None

def test_wholeE():    
    filepath= "https://uni-muenster.sciebo.de/s/QFj5pzm7AzxAh1f?path=%2FfunktionierendeTestdaten_gruppe1%2Fzeitdaten%2Ftime%20mischung"
    filepath1="/home/minicaro/Downloads/time_mischung"
    assert extractTool.getMetadata(filepath, 'bbox', 'whole', False) == None

