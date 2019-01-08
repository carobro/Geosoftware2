import click, json, sqlite3, csv, pygeoj, detailebenen
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import ogr2ogr

def getIsobbx(filepath, detail, folder):
    gdal.UseExceptions()
    """@see http://manpages.ubuntu.com/manpages/trusty/man1/ogr2ogr.1.html"""
    if detail =='bbox':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        isobbx = (iso).bbox
        # Identification of CRS and transformation
        # In some test data the epsg id was stored in an unicode object like this one'urn:ogc:def:crs:EPSG::4258'
        try:
            isocrs = (iso).crs
            mycrs= isocrs["properties"]["name"]
            print(mycrs)
            mycrsString=mycrs.encode('ascii','ignore')
            # Extracting the epsg id
            mySplit= mycrsString.split(':')
            CRSID=mySplit[len(mySplit)-1]
            # Especially the KML data files have this id, which is wgs84
            # No need to transform
            if (CRSID=="CRS84" or CRSID == 4326):
                mybbx=[isobbx[0],isobbx[1],isobbx[2],isobbx[3]]
            else:
                lat1t,lng1t=detailebenen.transformToWGS84(isobbx[0],isobbx[1],CRSID)
                lat2t,lng2t=detailebenen.transformToWGS84(isobbx[2],isobbx[3],CRSID)
                mybbx=[lat1t,lng1t,lat2t,lng2t]
        except:
            print("While splitting the string an error occurred")

        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the ISO object:")
            click.echo(mybbx)
            print("----------------------------------------------------------------")
            #return isobbx
        if folder=='whole':
            detailebenen.bboxSpeicher.append(mybbx)
            click.echo(filepath)
            click.echo(mybbx)
            #return (isobbx)


    if detail == 'feature':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        #TO-DO feature.geometry.coordinates in variable speichern
        points = 0
        #print("in ISO")
        for feature in iso:
            click.echo(feature.geometry.coordinates)
        #convex_hull(points)
        return points


if __name__ == '__main__':
    getIsobbx()
