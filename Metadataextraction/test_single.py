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
# --detail=bbox --folder=single
###############################

def test_answerA():
    filepath=__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp'
    assert extractTool.getMetadata(filepath, 'bbox', 'single', False) == [[None], [None], [None]]

def test_answerB():  
    filepath= __location__+'/testdata/Baumfaellungen_Duesseldorf.csv'
    assert extractTool.getMetadata(filepath, 'bbox', 'single', False) == [[None], [None], [None]]

def test_answerC():
    filepath = __location__+'/testdata/Queensland_Children_geopackage/census2016_cca_qld_short.gpkg'    
    assert extractTool.getMetadata(filepath, 'bbox', 'single', False) == [[-43.7405, 96.8169, -9.14218, 167.998], [None], [None]]

def test_answerD():
    filepath=__location__+'/testdata/Abgrabungen_Kreis_Kleve.geojson'
    assert extractTool.getMetadata(filepath, 'bbox', 'single', False) == [[6.04705316429154, 51.3721631194526, 6.4894453535296, 51.8440745554806], [None], [None]]

def test_answerE():
    filepath=__location__+'/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif'
    assert extractTool.getMetadata(filepath, 'bbox', 'single', False) == [[5.9153007564753155, 50.31025197410836, 9.468398712484145, 52.5307755328733], [None], [None]]

def test_answerF():    
    filepath=__location__+'/testdata/clc_1000_PT.gml'
    assert extractTool.getMetadata(filepath, 'bbox', 'single', False) == [[-17.54207241592243, 32.396692819320194, -6.95938792923511, 39.30113527461412], [None], [None]]

def test_answerxx():    
    filepath=__location__+"/testdata/mypolygon_px6.gml"
    assert extractTool.getMetadata(filepath, 'bbox', 'single', False) == [[79.39064024773653, 11.627857397680971, 79.44763182487713, 11.697121798928404], [None], [None]]

def test_answerG():    
    filepath= __location__+'/testdata/ECMWF_ERA-40_subset1.nc'
    assert extractTool.getMetadata(filepath, 'bbox', 'single', False) == [[-90.0, 0.0, 90.0, 357.5], [None], [None]]

#####################################
# --detail=convexHull --folder=single
# ################################### 
def test_answerO():
    filepath=__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp'
    assert extractTool.getMetadata(filepath, 'convexHull', 'single', False) == [[None], [None], [None]] 

def test_answerP():  
    filepath=  __location__+'/testdata/Behindertenparkplaetze_Duesseldorf.csv'
    assert extractTool.getMetadata(filepath, 'convexHull', 'single', False) == [[None], [None], [None]]

def test_answerQ():
    filepath = __location__+'/testdata/Queensland_Children_geopackage/census2016_cca_qld_short.gpkg'    
    assert extractTool.getMetadata(filepath, 'convexHull', 'single', False) == [[None], [None], [None]]

def test_answerR():
    filepath=__location__+'/testdata/muenster_ring_zeit.geojson'
    assert extractTool.getMetadata(filepath, 'convexHull', 'single', False) == [[None], [[7.6016807556152335, 51.96537036973145], [7.602796554565429, 51.953258408047034], [7.608118057250977, 51.94881477206191], [7.643308639526367, 51.953258408047034], [7.647256851196289, 51.95807185013927], [7.6471710205078125,51.96330786509095], [7.645540237426757, 51.96780294552556], [7.645368576049805, 51.96817310852836], [7.636871337890624, 51.97240332571046], [7.62125015258789, 51.974624029877454], [7.606401443481445, 51.97361943924433]], [None]]

def test_answerS():
    filepath=__location__+'/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif'
    assert extractTool.getMetadata(filepath, 'convexHull', 'single', False) == [[None], [None], [None]]

def test_answerAE():    
    filepath=__location__+'/testdata/clc_1000_PT.gml'
    assert extractTool.getMetadata(filepath, 'convexHull', 'single', False) == [[None], [None], [None]]

def test_answerUE():    
    filepath= __location__+'/testdata/ECMWF_ERA-40_subset.nc'
    assert extractTool.getMetadata(filepath, 'convexHull', 'single', False) == [[None], [None], [None]]
