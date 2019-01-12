import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getIsoInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, detailebenen
from scipy.spatial import ConvexHull

def openFolder(filepath, detail, folder):
    folderpath= filepath
    click.echo("folderfolderfolder")
    docs=os.listdir(folderpath)
    for x in docs:
        docPath= folderpath +"/"+ x
        #print docPath
        #getMetadata(docPath, detail2)
        try:
            click.echo("folderShape")
            getShapefileInfo.getShapefilebbx(docPath, detail, folder)
        except Exception as e:
            try:
                click.echo("folderGeoJSON")
                getGeoJsonInfo.getGeoJsonbbx(docPath, detail, folder)
            except Exception as e:
                try:
                    click.echo(e)
                    click.echo("folderNetCDF")
                    getNetCDFInfo.getNetCDFbbx(docPath, detail, folder)
                except Exception as e:
                    try:
                        click.echo("folderCSV")
                        getCSVInfo.getCSVbbx(docPath, detail, folder)
                    except Exception as e:
                        try:
                            click.echo("folderGeoTIFF")
                            getGeoTiffInfo.getGeoTiffbbx(docPath, detail, folder)
                        except Exception as e:
                            try:
                                click.echo("folderGeoPackage")
                                getGeoPackageInfo.getGeopackagebbx(docPath, detail, folder)
                            except Exception as e:
                                try:
                                    click.echo("folderISO")
                                    getIsoInfo.getIsobbx(docPath, detail, folder)
                                except Exception as e:
                                    try:
                                        click.echo("folderfolder")
                                        openFolder(docPath, detail, folder)
                                    except Exception as e:
                                        click.echo("fodlerInvalid")
                                        click.echo ("invalid file format in folder!")
    if folder=='whole':
        if detail=='bbox':
            print("if")
            bboxes=detailebenen.bboxArray
            print("222222222")
            print(bboxes)
            min1=100000000
            min2=100000000
            max1=0
            max2=0
            lat1List=[lat1 for lat1, lng1, lat2, lng2 in bboxes]
            #print(lat1List)
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
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("boundingbox of the whole folder:")
            print(folderbbox)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if detail=='convexHull':
            points=detailebenen.bboxArray
            hull=ConvexHull(points)
            hull_points=hull.vertices
            convHull=[]
            for y in hull_points:
                point=[points[y][0], points[y][1]]
                convHull.append(point)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            click.echo("convex hull of the folder:")    
            click.echo(convHull)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if detail=='time':
            print("zeitordnerausgabe fehlt noch")

        
        
        return 0


if __name__ == '__main__':
    openFolder()