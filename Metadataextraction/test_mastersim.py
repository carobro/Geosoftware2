import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os

import extractTool, mastersim, similar
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
print(__location__+'/testdata/')
"""
These tests check if the calucated similar score from two files is
equal to our hand-calculted score
"""

# def test_master1():
#     filepath1 = (__location__+'/testdata/Abgrabungen_Kreis_Kleve.shp')
#     filepath2 = (__location__+'/testdata/Abgrabungen_Kreis_Kleve.shp')
#     assert mastersim.master(filepath1, filepath2) == 1

def test_master2():
    filepath1 = __location__+'/testdata/Abgrabungen_Kreis_Kleve.geojson' 
    filepath2 = __location__+'/testdata/Abgrabungen_Kreis_Kleve.geojson' 
    assert mastersim.master(filepath1, filepath2) == 1

def test_master3():
    filepath1 = __location__+'/testdata/wf_100m_klas.tif'
    filepath2 = __location__+'/testdata/wf_100m_klas.tif'
    assert mastersim.master(filepath1, filepath2) == 1

# def test_master4():
#     filepath1 = _location_+'/testdata/Behindertenparkplaetze_Duesseldorf.csv'
#     filepath2 = _location_+'/testdata/Behindertenparkplaetze_Duesseldorf.csv'
#     assert mastersim.master(filepath1, filepath2) == 1

# def test_master5():
#     filepath1 = _location_+'/testdata/ECMWF_ERA-40_subset.nc'
#     filepath2 = _location_+'/testdata/ECMWF_ERA-40_subset.nc'
#     assert mastersim.master(filepath1, filepath2) == 1

# def test_master6():
#     filepath1 = _location_+'/testdata/Queensland_Children_geopackage/census2016_cca_qld_short.gpkg'
#     filepath2 = _location_+'/testdata/Queensland_Children_geopackage/census2016_cca_qld_short.gpkg'
#     assert mastersim.master(filepath1, filepath2) == 1

# def test_master7():
#     filepath1 = _location_+'/testdata/3D_LoD1_33390_5664.gml'
#     filepath2 = _location_+'/testdata/3D_LoD1_33390_5664.gml'
#     assert mastersim.master(filepath1, filepath2) == 1

# def test_master8():
#     filepath1 = _location_+'/testdata/3D_LoD1_33390_5664.gml'
#     filepath2 = _location_+'/testdata/Queensland_Children_geopackage/census2016_cca_qld_short.gpkg'
#     assert mastersim.master(filepath1, filepath2) == 0

# def test_master9():
#     filepath1 = _location_+'/testdata/ECMWF_ERA-40_subset.nc'
#     filepath2 = _location_+'/testdata/Queensland_Children_geopackage/census2016_cca_qld_short.gpkg'
#     assert mastersim.master(filepath1, filepath2) == 0

# def test_master10():
#     filepath1 = __location__+' /testdata/Abgrabungen_Kreis_Kleve.geojson' 
#     filepath2 = __location__+'/testdata/Abgrabungen_Kreis_Kleve.shp'
#     assert mastersim.master(filepath1, filepath2) == 0

# def test_master11():
#     filepath1 = __location__+' /testdata/Abgrabungen_Kreis_Kleve.geojson' 
#     filepath2 = _location_+'/testdata/Behindertenparkplaetze_Duesseldorf.csv'
#     assert mastersim.master(filepath1, filepath2) == 0

# def test_master12():
#     filepath1 = _location_+'/testdata/Behindertenparkplaetze_Duesseldorf.csv'
#     filepath2 = __location__+'/testdata/Abgrabungen_Kreis_Kleve.shp'
#     assert mastersim.master(filepath1, filepath2) == 0

# def test_master13():
#     filepath1 =_location_+'testdata/wf_100m_klas.tif'
#     filepath2 = __location__+'/testdata/Abgrabungen_Kreis_Kleve.shp'
#     assert mastersim.master(filepath1, filepath2) == 0

# def test_master14():
#     filepath1 = __location__+' /testdata/Abgrabungen_Kreis_Kleve.geojson' 
#     filepath2 = _location_+'testdata/wf_100m_klas.tif'
#     assert mastersim.master(filepath1, filepath2) == 0

# def test_master15():
#     filepath1 = _location_+'/testdata/3D_LoD1_33390_5664.gml'
#     filepath2 = __location__+'/testdata/Abgrabungen_Kreis_Kleve.shp'
#     assert mastersim.master(filepath1, filepath2) == 0