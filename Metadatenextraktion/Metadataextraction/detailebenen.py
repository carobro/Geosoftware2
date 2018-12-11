import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, openFolder
#import getIsoInfo
#import ogr2ogr
#ogr2ogr.BASEPATH = "/home/caro/Vorlagen/Geosoftware2/Metadatenextraktion"


bboxSpeicher = []

""" Vorteil uneres Codes: Es wird nicht auf die Endung (.shp etc.) geachtet,
sondern auf den Inhalt"""
@click.command()
@click.option('--path',required=True, help='Path to the data.')
@click.option('--bbox', 'detail', flag_value='bbox',
              default=True)
@click.option('--feature', 'detail', flag_value='feature')
@click.option('--single', 'folder', flag_value='single', default=True)
@click.option('--whole', 'folder', flag_value='whole')



def getMetadata(path, detail, folder):
    
    
    print(bboxSpeicher)
    filepath = path
    # Program that extracts the boudingbox of files.

    try:
        getShapefileInfo.getShapefilebbx(filepath, detail, folder)
    except Exception as e:
        try:
            getGeoJsonInfo.getGeoJsonbbx(filepath, detail, folder)
        except Exception as e:
            try:
                getNetCDFInfo.getNetCDFbbx(filepath, detail, folder)
            except Exception as e:
                try:
                    getCSVInfo.getCSVbbx(filepath, detail, folder)
                except Exception as e:
                    try:
                        getGeoPackageInfo.getGeopackagebbx(filepath, detail, folder)
                    except Exception as e:
                        try:
                            getGeoTiffInfo.getGeoTiffbbx(filepath, detail, folder)
                        except Exception as e:
                            #try:
                            #getIsoInfo.getIsobbx(filepath, detail)
                            #except Exception as e:
                            try:
                                openFolder.openFolder(filepath, detail, folder)
                            except Exception as e:
                                click.echo ("invalid file format!")


if __name__ == '__main__':
    getMetadata()
