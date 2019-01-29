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

######################################
# --detail=bbox --folder=single --time
######################################
def test_answerU():  
    filepath=  __location__+'/testdata/cities_NL.csv'
    assert extractTool.getMetadata(filepath, 'bbox' , True) == [[4.3175, 51.434444000000006, 6.574722, 53.217222], [None], ['2018-09-30 00:00:00', '2018-09-30 00:00:00']]


def test_answerT():
    filepath=__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp'
    assert extractTool.getMetadata(filepath, 'bbox' , True) == [[None], [None], [None]]


def test_answerUU():  
    filepath=  __location__+'/testdata/Baumfaellungen_Duesseldorf.csv'
    assert extractTool.getMetadata(filepath, 'bbox' , True) == [[None],[None],[None]]

def test_answerV():
    filepath = __location__+'/testdata/Queensland_Children_geopackage/census2016_cca_qld_short.gpkg'    
    assert extractTool.getMetadata(filepath, 'bbox' , True) == [[96.8169, -43.7405, 167.998, -9.14218], [None], [None]]

def test_answerW():
    filepath=__location__+'/testdata/muenster_ring_zeit.geojson'
    assert extractTool.getMetadata(filepath, 'bbox' , True) == [[7.6016807556152335, 51.94881477206191, 7.647256851196289, 51.974624029877454], [None], ['2018-11-14 00:00:00', '2018-11-14 00:00:00']]

def test_answerY():    
    filepath=__location__+'/testdata/clc_1000_PT.gml'
    assert extractTool.getMetadata(filepath, 'bbox' , True) == [[-17.54207241592243, 32.396692819320194, -6.95938792923511, 39.30113527461412], [None], [None]]

def test_answerX():
    filepath=__location__+'/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif'
    assert extractTool.getMetadata(filepath, 'bbox' , True) == [[5.9153007564753155, 50.31025197410836, 9.468398712484145, 52.5307755328733], [None], [None]]


def test_answerZ():    
    filepath= __location__+'/testdata/ECMWF_ERA-40_subset1.nc'
    assert extractTool.getMetadata(filepath, 'bbox' , True) == [[-90.0, 0.0, 90.0, 357.5], [None], ['2002-07-01 12:00:00', '2002-07-31 18:00:00']]


# def test_answerT():
#     filepath=__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp'
#     assert extractTool.getMetadata(filepath, 'bbox' , True) == [[None], [None], [None]]
