import click, json, sqlite3, csv, pygeoj, detailebenen
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import sqlite3
from pyproj import Proj, transform


def getGeopackagebbx(filepath, detail, folder):
    """returns the bounding Box Geopackage
    @param path Path to the file
    @see https://docs.python.org/2/library/sqlite3.html"""
    print ("geopackage")
    if detail =='bbox':
        #print(filepath)
        #print("1")
        conn = sqlite3.connect(filepath)
        #print("2")
        c = conn.cursor()
        # @see: https://www.geopackage.org/spec121/index.html#_contents_2
        c.execute("""SELECT min(min_y), min(min_x), max(max_y), max(max_x), srs_id
                     FROM gpkg_contents""")
        row = c.fetchall()
        lat1=row[0][0]
        lng1=row[0][1]
        lat2=row[0][2]
        lng2=row[0][3]
        myCRS=row[0][4]
        bbox=[lat1,lng1,lat2,lng2]
        print("Unmodified BBOX: ")
        print(bbox)
        # Assuming that the CRS won't change
        inputProj='epsg:'
        inputProj+=str(myCRS)
        print(inputProj)
        inProj = Proj(init=inputProj)
        outProj = Proj(init='epsg:4326')
        lat1t,lng1t = transform(inProj,outProj,lat1,lng1)
        lat2t,lng2t = transform(inProj,outProj,lat2,lng2)
        print("Modified BBOX: ")
        bbox=[lat1t,lng1t,lat2t,lng2t]

        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the GeoPackage object:")
            print(bbox)
            print("----------------------------------------------------------------")
            return (bbox)
        if folder=='whole':
            click.echo(filepath)
            print(bbox)
            detailebenen.bboxSpeicher.append(bbox)
            #print(detailebenen.bboxSpeicher)
            return (bbox)
    if detail == 'feature':
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT min_x,min_y
                     FROM gpkg_contents""")
        points = c.fetchall()
        print("----------------------------------------------------------------")
        click.echo("Filepath:")
        click.echo(filepath)
        click.echo("All features of the GeoPackage object:")
        print(points)
        print("----------------------------------------------------------------")
        return points

if __name__ == '__main__':
    getGeopackagebbx()
