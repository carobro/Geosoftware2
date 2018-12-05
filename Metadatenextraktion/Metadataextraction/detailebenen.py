import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo
#import ogr2ogr
#ogr2ogr.BASEPATH = "/home/caro/Vorlagen/Geosoftware2/Metadatenextraktion"

""" Vorteil uneres Codes: Es wird nicht auf die Endung (.shp etc.) geachtet,
sondern auf den Inhalt"""
@click.command()
@click.option('--path',required=True, help='Path to the data.')
@click.option('--bbox', 'detail', flag_value='bbox',
              default=True)
@click.option('--feature', 'detail', flag_value='feature')

def getMetadata(path, detail):
    filepath = path
    # Program that extracts the boudingbox of files.

    try:
        getShapefileInfo.getShapefilebbx(filepath, detail)
    except Exception as e:
        try:
            getGeoJsonInfo.getGeoJsonbbx(filepath, detail)
        except Exception as e:
            try:
                getNetCDFInfo.getNetCDFbbx(filepath, detail)
            except Exception as e:
                try:
                    getCSVbbx(filepath, detail)
                except Exception as e:
                    try:
                        getGeoTiffInfo.getGeoTiffbbx(filepath, detail)
                    except Exception as e:
                        try:
                            getGeoPackageInfo.getGeopackagebbx(filepath, detail)
                        except Exception as e:
                            try:
                                getIsoInfo.getIsobbx(filepath, detail)
                            except Exception as e:
                                try:
                                    openFolder(filepath, detail)
                                except Exception as e:
                                    click.echo ("invalid file format!")


def openFolder(filepath, detail):
    folderpath= filepath
    click.echo("drin")
    docs=os.listdir(folderpath)
    for x in docs:
        docPath= folderpath +"/"+ x
        print docPath
        #getMetadata(docPath, detail2)
        try:
            getShapefilebbx(docPath, detail)
        except Exception as e:
            try:
                getGeoJsonbbx(docPath, detail)
            except Exception as e:
                try:
                    getNetCDFbbx(docPath, detail)
                except Exception as e:
                    try:
                        getCSVbbx(docPath, detail)
                    except Exception as e:
                        try:
                            getGeoPackageInfo.getGeopackagebbx(docPath, detail)
                        except Exception as e:
                            try:
                                getGeoTiffbbx(docPath, detail)
                            except Exception as e:
                                try:
                                    getIsobbx(filepath, detail)
                                except Exception as e:
                                    try:
                                        openFolder(docPath, detail)
                                    except Exception as e:
                                        click.echo ("invalid file format!")





if __name__ == '__main__':
    getMetadata()
