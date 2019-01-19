import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os
import sqlite3

import extractTool
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

print(__location__+'/testdata/')

# convex hull
def test_featureShape():
    assert getShapefileInfo.getShapefilebbx(__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp', 'feature', 'single', False) == 0

def test_featureCSV():    
    assert getCSVInfo.getCSVbbx(__location__+'/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'feature', 'single', False) == "nich fertig"

def test_featureGeoPackage():    
    assert getGeoPackageInfo.getGeopackagebbx(__location__+'/testdata/Geopackage_Queensland_geopackage/census2016_cca_qld_short.gpkg', 'feature', 'single', False) == [(96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169,-43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (112.921, -43.7405), (96.8169, -43.7405),(96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405)]

def test_featureGeoJson():    
    assert getGeoJsonInfo.getGeoJsonbbx(__location__+'/testdata/schutzhuetten_aachen.json', 'feature', 'single', False) == [302039.51397745, 5626416.78906231]

def test_featureGeoTiff():    
    assert getGeoTiffInfo.getGeoTiffbbx(__location__+'/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif', 'feature', 'single', False) == None

def test_featureIso():    
     assert getIsoInfo.getIsobbx(__location__+'/testdata/3D_LoD1_33390_5664.gml', 'feature', 'single', False) == None

def test_featureNetCDF():    
    assert getNetCDFInfo.getNetCDFbbx(__location__+'/testdata/ECMWF_ERA-40_subset.nc', 'feature', 'single', False) == [[None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]]
