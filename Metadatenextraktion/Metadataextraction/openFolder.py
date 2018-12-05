import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo

def openFolder(filepath, detail):
    folderpath= filepath
    click.echo("drin")
    docs=os.listdir(folderpath)
    for x in docs:
        docPath= folderpath +"/"+ x
        print docPath
        #getMetadata(docPath, detail2)
        try:
            getShapefileInfo.getShapefilebbx(docPath, detail)
        except Exception as e:
            try:
                getGeoJsonInfo.getGeoJsonbbx(docPath, detail)
            except Exception as e:
                try:
                    getNetCDFInfo.getNetCDFbbx(docPath, detail)
                except Exception as e:
                    try:
                        getCSVInfo.getCSVbbx(docPath, detail)
                    except Exception as e:
                        try:
                            getGeoTiffInfo.getGeoTiffbbx(docPath, detail)
                        except Exception as e:
                            try:
                                getGeoPackageInfo.getGeopackagebbx(docPath, detail)
                            except Exception as e:
                                try:
                                    getIsoInfo.getIsobbx(docPath, detail)
                                except Exception as e:
                                    try:
                                        openFolder(docPath, detail)
                                    except Exception as e:
                                        click.echo ("invalid file format in folder!")


if __name__ == '__main__':
    openFolder()