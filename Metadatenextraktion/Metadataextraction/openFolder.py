import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, detailebenen

def openFolder(filepath, detail, folder):
    folderpath= filepath
    click.echo("drin")
    docs=os.listdir(folderpath)
    for x in docs:
        docPath= folderpath +"/"+ x
        print docPath
        #getMetadata(docPath, detail2)
        try:
            getShapefileInfo.getShapefilebbx(docPath, detail, folder)
        except Exception as e:
            try:
                getGeoJsonInfo.getGeoJsonbbx(docPath, detail, folder)
            except Exception as e:
                try:
                    getNetCDFInfo.getNetCDFbbx(docPath, detail, folder)
                except Exception as e:
                    try:
                        getCSVInfo.getCSVbbx(docPath, detail, folder)
                    except Exception as e:
                        try:
                            getGeoTiffInfo.getGeoTiffbbx(docPath, detail, folder)
                        except Exception as e:
                            try:
                                getGeoPackageInfo.getGeopackagebbx(docPath, detail, folder)
                            except Exception as e:
                                try:
                                    getIsoInfo.getIsobbx(docPath, detail)
                                except Exception as e:
                                    try:
                                        openFolder(docPath, detail, folder)
                                    except Exception as e:
                                        click.echo ("invalid file format in folder!")


    if folder=='whole':
        bboxes=detailebenen.bboxSpeicher
        print("2")
        print(bboxes)
        min1=100000000
        min2=100000000
        max1=0
        max2=0
        lat1List=[lat1 for lat1, lng1, lat2, lng2 in bboxes]
        print(lat1List)
        for x in lat1List:
            if x<min1:
                min1=x


        lng1List=[lng1 for lat1, lng1, lat2, lng2 in bboxes]
        #print(lng1List)
        for x in lng1List:
            if x<min2:
                min2=x

        lat2List=[lat2 for lat1, lng1, lat2, lng2 in bboxes]
        #print(lat2List)
        for x in lat2List:
            if x>max1:
                max1=x


        lng2List=[lng2 for lat1, lng1, lat2, lng2 in bboxes]
        #print(lng2List)
        for x in lng2List:
            if x>max2:
                max2=x

        folderbbox=[min1, min2, max1, max2]
        print("halo2")
        print(folderbbox)


if __name__ == '__main__':
    openFolder()