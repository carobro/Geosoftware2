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
        isocrs = (iso).crs
        mycrs= isocrs["properties"]["name"]
        mycrsString=mycrs.encode('ascii','ignore')
        # Extracting the epsg id
        CRSID= mycrsString.split('::')
        lat1t,lng1t=detailebenen.transformToWGS84(isobbx[0],isobbx[1],CRSID[1])
        lat2t,lng2t=detailebenen.transformToWGS84(isobbx[2],isobbx[3],CRSID[1])
        mybbx=[lat1t,lng1t,lat2t,lng2t]

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
