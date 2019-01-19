import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os

import extractTool
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

#--detail=bboxSingle
def test_answerA():
    assert extractTool.click_function(__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp', 'bbox', 'single', True) == [295896.274870878, 5694747.64703736, 325999.79578122497, 5747140.98659967]

def test_answerB():    
    assert extractTool.click_function(__location__+'/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'bbox', 'single', True) == None

def test_answerC():    
    assert extractTool.click_function(__location__+'/testdata/Geopackage_Queensland_geopackage/census2016_cca_qld_short.gpkg', 'bbox', 'single', True) == [295896.274870878, 5694747.64703736, 325999.79578122497, 5747140.98659967]

def test_answerD():    
    assert extractTool.click_function(__location__+'/testdata/schutzhuetten_aachen.json', 'bbox', 'single', True) == [292063.81225905, 5618144.09259115, 302531.3161606, 5631223.82854667]

def test_answerE():    
    assert extractTool.click_function(__location__+'/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif', 'bbox', 'single', False) == [5.9153007564753155, 50.31025197410836, 9.468398712484145, 52.5307755328733]

def test_answerF():    
    assert extractTool.click_function(__location__+'/testdata/3D_LoD1_33390_5664.gml', 'bbx', 'single', True) == [5.9153007564753155, 50.31025197410836, 9.468398712484145, 52.5307755328733]

def test_answerG():    
    assert extractTool.click_function(__location__+'/testdata/tos_O1_2001-2002.nc', 'bbox', 'single', False) == None

def test_answerH():
    assert extractTool.click_function(__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp', 'bbox', 'whole', True) == None

def test_answerI():    
    assert extractTool.click_function(__location__+'/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'bbox', 'whole', True) == None

def test_answerJ():    
    assert extractTool.click_function(__location__+'/testdata/Geopackage_Queensland_geopackage/census2016_cca_qld_short.gpkg', 'bbox', 'whole', True) == None

def test_answerK():    
    assert extractTool.click_function(__location__+'/testdata/schutzhuetten_aachen.json', 'bbox', 'whole', True) == None

def test_answerL():    
    assert extractTool.click_function(__location__+'/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif', 'bbox', 'whole', False) == None

def test_answerM():    
    assert extractTool.click_function(__location__+'/testdata/3D_LoD1_33390_5664.gml', 'bbx', 'whole', True) == None

def test_answerN():    
    assert extractTool.click_function(__location__+'/testdata/tos_O1_2001-2002.nc', 'bbox', 'whole', False) == None
