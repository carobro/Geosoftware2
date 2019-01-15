import click, json, sqlite3, csv, pygeoj, detailebenen as de
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import sqlite3
from pyproj import Proj, transform
from scipy.spatial import ConvexHull

#Boolean variable that shows if the crs of the bbox is in wgs84
wgs_84=False

def getGeopackagebbx(filepath, detail, folder):
    """returns the bounding Box Geopackage
    @param path Path to the file
    @see https://docs.python.org/2/library/sqlite3.html"""
    print ("geop")
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    c.execute("""SELECT min(min_y), min(min_x), max(max_y), max(max_x), srs_id
                     FROM gpkg_contents""")
    print ("geopackage")
    
    #print(filepath)
    print("1")
    conn = sqlite3.connect(filepath)
    print("2")
    c = conn.cursor()
    # @see: https://www.geopackage.org/spec121/index.html#_contents_2
    c.execute("""SELECT min(min_y), min(min_x), max(max_y), max(max_x), srs_id
                    FROM gpkg_contents""")
    row = c.fetchall()
    print("test")
    try:
        lat1=row[0][0]
        print("hu")
        lng1=row[0][1]
        print(lat1)
        print(lng1)
        lat2=row[0][2]
        lng2=row[0][3]
        print("ha")
        myCRS=row[0][4]
        if not(lat1 and lat2):
            print("keine koord")
    except (not(lat1 and lat2)):
        raise Exception ("There are no coordinate values in this file.")
    print("hi")
        # Especially the KML data files have this id, which is wgs84
        # No need to transform
    if detail =='bbox':
        if ((myCRS=="CRS84" or myCRS == 4326) and (lat1 and lng1)):
            print("first if")
            wgs_84=True
            bbox=[lat1,lng1,lat2,lng2]
        elif(myCRS):
            print("second if")
            wgs_84=True
            print("vor")
            lat1t,lng1t = de.transformToWGS84(lat1,lng1,myCRS)
            print("transformation success")
            lat2t,lng2t = de.transformToWGS84(lat2,lng2,myCRS)
            bbox=[lat1t,lng1t,lat2t,lng2t]
        else:
            print("There is no crs provided.")
            bbox=[lat1,lng1,lat2,lng2]

        #print(myCRS)
        #print("3")
        #lat1t,lng1t = de.transformToWGS84(lat1,lng1,myCRS)
        #print("transformation success")
        #lat2t,lng2t = de.transformToWGS84(lat2,lng2,myCRS)
        #bbox=[lat1t,lng1t,lat2t,lng2t]
        #print("bbox")

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
            de.bboxArray.append(bbox)
            
            return (bbox)
    if detail == 'convexHull':
        click.echo("convexHull geop")
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT min_x,min_y
                     FROM gpkg_contents""")
        print("3")
        points = c.fetchall()
        new_point_list=[]
        for z in points:
            print(points)
            print("5")
            #print(z)
            lat=z[0]
            lng=z[1]
            # Assuming that the CRS won't change
            inputProj='epsg:'
            inputProj+=str(myCRS)
            inProj = Proj(init=inputProj)
            outProj = Proj(init='epsg:4326')
            lat,lng = transform(inProj,outProj,lat,lng)
            new_point=[lat,lng]
            new_point_list.append(new_point)
        #print(points)
        print("TESTTEST")
        #TODO
        #an dieser Stelle tritt ein Fehler auf!
        hull=ConvexHull(new_point_list)
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
        click.echo("DRIN")
        conn = sqlite3.connect(filepath)
        click.echo("hallo")
        c = conn.cursor()
        #TODO 
        #Fehler"so such column time" -> fragt immer nur den ersten ab : trotz allem: keine Testdaten mit time
        c.execute("""SELECT time or timestamp or date
                        FROM gpkg_contents""")
        try:
            #print c.fetchone()
            row = c.fetchall()
            print(row)
            print("row")
            if folder=='single':
                print("The time value is:")
                print(row)
            if folder=='whole':
                timeextend=[min(timelist), max(timelist)]
                de.timeextendArray.append(timeextend)
                print("timeextendArray:")
                print(de.timeextendArray)
            return row
        except Exception as e:
            click.echo(e)
            click.echo ("There is no time-value or invalid file")
            return None

if __name__ == '__main__':
    getGeopackagebbx()
