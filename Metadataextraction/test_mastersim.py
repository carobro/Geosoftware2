import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os

import extractTool, mastersim, similar
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
"""
These tests check if the calucated similar score from two files is
equal to our hand-calculted score
"""

def test_master1():
    filepath1 = __location__+'/testdata/Abgrabungen_Kreis_Kleve.geojson'
    filepath2 = __location__+'/testdata/Abgrabungen_Kreis_Kleve.geojson'
    assert mastersim.master(filepath1, filepath2) == 1

'''
def test_master2():
    filepath1 = 
    filepath2 = 
    assert mastersim.master(filepath1, filepath2) == 

def test_master3():
    filepath1 = 
    filepath2 = 
    assert mastersim.master(filepath1, filepath2) == 

def test_master4():
    filepath1 = 
    filepath2 = 
    assert mastersim.master(filepath1, filepath2) == 

def test_master5():
    filepath1 = 
    filepath2 = 
    assert mastersim.master(filepath1, filepath2) == 

def test_master6():
    filepath1 = 
    filepath2 = 
    assert mastersim.master(filepath1, filepath2) == 

def test_master7():
    filepath1 = 
    filepath2 = 
    assert mastersim.master(filepath1, filepath2) == 

def test_master8():
    filepath1 = 
    filepath2 = 
    assert mastersim.master(filepath1, filepath2) == 

def test_master9():
    filepath1 = 
    filepath2 = 
    assert mastersim.master(filepath1, filepath2) == 

def test_master10():
    filepath1 = 
    filepath2 = 
    assert mastersim.master(filepath1, filepath2) == 
'''