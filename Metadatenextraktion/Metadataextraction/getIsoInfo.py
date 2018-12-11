import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
#import ogr2ogr
#ogr2ogr.BASEPATH = "/home/cornelia/Dokumente/geosoft/Geosoftware2/Geosoftware2/Metadatenextraktion"

def getIsobbx(filepath, detail):
    """@see http://manpages.ubuntu.com/manpages/trusty/man1/ogr2ogr.1.html"""
    if detail =='bbox':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        isobbx = (iso).bbox
        click.echo(isobbx)
        return isobbx


    if detail == 'feature':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        #TO-DO feature.geometry.coordinates in variable speichern
        points = 0
        for feature in iso:
            click.echo(feature.geometry.coordinates)
        #convex_hull(points)
        return points


if __name__ == '__main__':
    getIsobbx()