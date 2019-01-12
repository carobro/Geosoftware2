import click, json, sqlite3, csv, pygeoj, detailebenen as de
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import sqlite3
from pyproj import Proj, transform
from scipy.spatial import ConvexHull


def getGeopackagebbx(filepath, detail, folder):
    """returns the bounding Box Geopackage
    @param path Path to the file
    @see https://docs.python.org/2/library/sqlite3.html"""
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    c.execute("""SELECT min(min_y), min(min_x), max(max_y), max(max_x), srs_id
                     FROM gpkg_contents""")
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
        lat1t,lng1t = de.transformToWGS84(lat1,lng1,myCRS)
        lat2t,lng2t = de.transformToWGS84(lat2,lng2,myCRS)
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
            detailebenen.bboxArray.append(bbox)
            
            return (bbox)
    if detail == 'convexHull':
        click.echo("convexHull geop")
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT min_x,min_y
                     FROM gpkg_contents""")
        print("3")
        points = c.fetchall()
        print(points)
        print(points[0][0])
        print(points[0][1])
        #print(points[0][2])
        print(points[1])
        print(points[2])
        for z in points:
            print(z)
            lat=points[z][0]
            lng=points[z][1]
        # Assuming that the CRS won't change
        inputProj='epsg:'
        inputProj+=str(myCRS)
        print(inputProj)
        inProj = Proj(init=inputProj)
        outProj = Proj(init='epsg:4326')
        lat,lng = transform(inProj,outProj,lat,lng)
        print("4")
        print(points)
        hull=ConvexHull(points[0])
        print("5")
        hull_points=hull.vertices
        convHull=[]

        print("11111111111111")
        for y in hull_points:
            point=[points[y][0], points[y][1]]
            convHull.append(point)
        print("----------------------------------------------------------------")
        click.echo("Filepath:")
        click.echo(filepath)
        click.echo("Convex hull of the GeoPackage object:")
        print(point)
        print("----------------------------------------------------------------")
        #return points
    if detail=='time':
        # We open the file with the sqlite function and search for
        # words like time, timestamp or date and collect them
        # to calculate the temporal extend
        click.echo("GeoPackage")
        #click.echo("DRIN")
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT time or timestamp or date
                        FROM gpkg_contents""")
        try:
            #print c.fetchone()
            row = c.fetchall()
            if folder=='single':
                print("The time value is:")
                print(row)
            if folder=='whole':
                timeextend=[min(timelist), max(timelist)]
                detailebenen.timeextendArray.append(timeextend)
                print("timeextendArray:")
                print(detailebenen.timeextendArray)
            return row
        except Exception as e:
            click.echo(e)
            click.echo ("There is no time-value or invalid file")
            return None

if __name__ == '__main__':
    getGeopackagebbx()
