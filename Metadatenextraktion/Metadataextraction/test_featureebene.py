import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os

import detailebenen
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

print(__location__+'/testdata/')

def test_featureShape():
    assert getShapefileInfo.getShapefilebbx(__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp', 'feature', 'single') == 0

def test_featureCSV():    
    assert getCSVInfo.getCSVbbx(__location__+'/testdata/Behindertenparkplaetze_Duesseldorf.csv', 'feature', 'single') == b

def test_featureGeoPackage():    
    assert getGeoPackageInfo.getGeopackagebbx(__location__+'/testdata/Geopackage_Queensland_geopackage/census2016_cca_qld_short.gpkg', 'feature', 'single') == [(96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169,-43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (112.921, -43.7405), (96.8169, -43.7405),(96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405), (96.8169, -43.7405)]

def test_featureGeoJson():    
    assert getGeoJsonInfo.getGeoJsonbbx(__location__+'/testdata/schutzhuetten_aachen.json', 'feature', 'single') == [[296952.85186914, 5624067.07285793], [295913.66024875, 5624880.6537705], [295319.12138993, 5623861.12308584], [301987.96613832, 5618723.70111273], [302067.71444814, 5619693.82603416], [295295.33077593, 5624535.3383897], [302039.51397745, 5626416.78906231], [302531.3161606, 5626839.79436834], [301151.43818774, 5631223.82854667], [300110.34453109, 5618144.09259115], [292537.45935834, 5623556.4350225], [293218.82603216, 5624555.09775785], [293940.83749215, 5624058.1092388], [292063.81225905, 5626164.30672035]]

def test_featureGeoTiff():    
    assert getGeoTiffInfo.getGeoTiffbbx(__location__+'/testdata/MittlWindgeschw-100m_GeoTIFF/wf_100m_klas.tif', 'feature', 'single') == None

def test_featureIso():    
     assert getIsoInfo.getIsobbx(__location__+'/testdata/3D_LoD1_33390_5664.gml', 'feature', 'single') == f

def test_featureNetCDF():    
    assert getNetCDFInfo.getNetCDFbbx(__location__+'/testdata/ECMWF_ERA-40_subset', 'feature', 'single') == "Latitude: [ 90.   87.5  85.   82.5  80.   77.5  75.   72.5  70.   67.5  65.   62.5  60.   57.5  55.   52.5  50.   47.5  45.   42.5  40.   37.5  35.   32.5  30.   27.5  25.   22.5  20.   17.5  15.   12.5  10.    7.5   5.    2.5   0.   -2.5  -5.   -7.5 -10.  -12.5 -15.  -17.5 -20.  -22.5 -25.  -27.5 -30.  -32.5 -35.  -37.5 -40.  -42.5 -45.  -47.5 -50.  -52.5 -55.  -57.5 -60.  -62.5 -65.  -67.5 -70.  -72.5 -75.  -77.5 -80.  -82.5 -85.  -87.5 -90. ] Longitude:[  0.    2.5   5.    7.5  10.   12.5  15.   17.5  20.   22.5  25.   27.5  30.   32.5  35.   37.5  40.   42.5  45.   47.5  50.   52.5  55.   57.5  60.   62.5  65.   67.5  70.   72.5  75.   77.5  80.   82.5  85.   87.5  90.   92.5  95.   97.5 100.  102.5 105.  107.5 110.  112.5 115.  117.5 120.  122.5 125.  127.5 130.  132.5 135.  137.5 140.  142.5 145.  147.5 150.  152.5 155.  157.5 160.  162.5 165.  167.5 170.  172.5 175.  177.5 180.  182.5 185.  187.5 190.  192.5 195.  197.5 200.  202.5 205.  207.5 210.  212.5 215.  217.5 220.  222.5 225.  227.5 230.  232.5 235.  237.5 240.  242.5 245.  247.5 250.  252.5 255.  257.5 260.  262.5 265.  267.5 270.  272.5 275.  277.5 280.  282.5 285.  287.5 290.  292.5 295.  297.5 300.  302.5 305.  307.5 310.  312.5 315.  317.5 320.  322.5 325.  327.5 330.  332.5 335.  337.5 340.  342.5 345.  347.5 350.  352.5 355.  357.5]"
