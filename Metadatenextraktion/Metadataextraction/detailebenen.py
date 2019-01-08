import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
from pyproj import Proj, transform
import pandas as pd
import numpy as np
import xarray as xr
import os
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getIsoInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, openFolder, getTimeextend
#import getIsoInfo
#import ogr2ogr
#ogr2ogr.BASEPATH = "/home/caro/Vorlagen/Geosoftware2/Metadatenextraktion"

bboxSpeicher = []


""" Vorteil uneres Codes: Es wird nicht auf die Endung (.shp etc.) geachtet,
sondern auf den Inhalt"""
@click.command()
@click.option('--path',required=True, help='please insert the path to the data here.')
@click.option('--bbox', 'detail', flag_value='bbox',
              default=True, help='returns the extent of an object as a boundingbox')
@click.option('--feature', 'detail', flag_value='feature', help='returns a more detailed representation of the extent of one object.')
@click.option('--single', 'folder', flag_value='single', default=True, help='returns all the boundingboxes from objects of a folder')
@click.option('--whole', 'folder', flag_value='whole', help='returns one overall boundingbox from all objects of a folder')
@click.option('--time', 'detail', flag_value='time', help='returns the time extend of one object')

def timeOrBbox(path, detail, folder):
    if detail=='time':
        getTimeextend.getTimeextend(path, detail)
    else:
        getMetadata(path,detail,folder)

def getMetadata(path, detail, folder):
    print(bboxSpeicher)
    filepath = path
    # Program that extracts the boudingbox of files.

    try:
        #click.echo("2")
        getShapefileInfo.getShapefilebbx(filepath, detail, folder)
    except Exception as e:
        try:
            #click.echo("2")
            getGeoJsonInfo.getGeoJsonbbx(filepath, detail, folder)
        except Exception as e:
            print (e)
            #return 0
            try:
                #click.echo("2")
                getNetCDFInfo.getNetCDFbbx(filepath, detail, folder)
            except Exception as e:
                try:
                    #click.echo("2")
                    getCSVInfo.getCSVbbx(filepath, detail, folder)
                except Exception as e:
                    try:
                        #click.echo("2")
                        getGeoPackageInfo.getGeopackagebbx(filepath, detail, folder)
                    except Exception as e:
                        try:
                            #click.echo("21")
                            getGeoTiffInfo.getGeoTiffbbx(filepath, detail, folder)
                        except Exception as e:
                            try:
                                #click.echo("22")
                                getIsoInfo.getIsobbx(filepath, detail, folder)
                            except Exception as e:
                                print(e)
                                try:
                                    #click.echo("2")
                                    openFolder.openFolder(filepath, detail, folder)
                                except Exception as e:

                                    #click.echo("2")
                                    click.echo ("invalid file format!")
                                    return 0

"""
@desc: Method for transform the coordinate reference system to WGS84 using the PyProj (https://github.com/jswhit/pyproj)
@param: latitude, longitude and the source ref system
"""
def transformToWGS84(lat, lng, sourceCRS):
    # formatting the input CRS
    inputProj='epsg:'
    inputProj+=str(sourceCRS)
    inProj = Proj(init=inputProj)
    # epsg:4326 is WGS84
    outProj = Proj(init='epsg:4326')
    latT, lngT = transform(inProj,outProj,lat,lng)
    return(latT,lngT)

if __name__ == '__main__':
    timeOrBbox()
