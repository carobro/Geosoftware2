import click, shapefile, json, sqlite3, csv, pygeoj, pytest, math, os
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os

import extractTool
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

print(__location__+'/testdata/')

# Bounding Box from file
def test_answerA():
    assert getShapefileInfo.getShapefilebbx(__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp', 'bbox', 'single', True) == [[None], [None], [None]]

def test_answerB():    
    assert getCSVInfo.getCSVbbx(__location__+'/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'bbox', 'single', True) == None

def test_answerC():    
    assert getGeoPackageInfo.getGeopackagebbx(__location__+'/testdata/Geopackage_Queensland_geopackage/census2016_cca_qld_short.gpkg', 'bbox', 'single', True) == [[-43.7405, 96.8169, -9.14218, 167.998], [None], [None]]

def test_answerD():    
    assert getGeoJsonInfo.getGeoJsonbbx(__location__+'/testdata/schutzhuetten_aachen.json', 'bbox', 'single', True) == [[None], [None], [None], [292063.81225905, 5618144.09259115, 302531.3161606, 5631223.82854667], [None], [None]]

def test_answerE():    
    assert getGeoTiffInfo.getGeoTiffbbx(__location__+'/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif', 'bbox', 'single', False) ==[[None], [None], [None], [292063.81225905, 5618144.09259115, 302531.3161606, 5631223.82854667], [None], [None], [5.9153007564753155, 50.31025197410836, 9.468398712484145, 52.5307755328733], [None], [None]] 

def test_answerF():    
    assert getIsoInfo.getIsobbx(__location__+'/testdata/3D_LoD1_33390_5664.gml', 'bbox', 'single', True) == [[None]]

def test_answerG():    
    assert getNetCDFInfo.getNetCDFbbx(__location__+'/testdata/tos_O1_2001-2002.nc', 'bbox', 'single', False) == "Fehler"

# Boundig Box folder -> es fehler nach Ordner
def test_bboxWholeShapefile():
     assert getShapefileInfo.getShapefilebbx(__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp', 'bbox', 'whole', False) == None

def test_bboxWholeGeoJson():
     assert getGeoJsonInfo.getGeoJsonbbx(__location__+'/testdata/schutzhuetten_aachen.json', 'bbox', 'whole', False) == None

def test_bboxWholeNetCDF():
     assert getNetCDFInfo.getNetCDFbbx(__location__+'/testdata/ECMWF_ERA-40_subset.nc', 'bbox', 'whole', False) == None

def test_bboxWholeCSV():
     assert getCSVInfo.getCSVbbx(__location__+'/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'bbox', 'whole', False) == "nich fertig"

def test_bboxWhole0Geopackage():
     assert getGeoPackageInfo.getGeopackagebbx(__location__+'/testdata/Geopackage_Queensland_geopackage/census2016_cca_qld_short.gpkg', 'bbox', 'whole', False) == None

def test_bboxWholeGeoTiff():
      assert getGeoTiffInfo.getGeoTiffbbx(__location__+'/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif', 'bbox', 'whole', False) == None

def test_bboxWholeIso():
      assert getIsoInfo.getIsobbx(__location__+'/testdata/3D_LoD1_33390_5664.gml', 'bbox', 'whole', False) == None