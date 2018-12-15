import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import ogr2ogr

def getIsobbx(filepath, detail, folder):
    print("ISO!!!")
    """@see http://manpages.ubuntu.com/manpages/trusty/man1/ogr2ogr.1.html"""
    if detail =='bbox':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        #print("ee")
        iso = pygeoj.load(filepath="out.json")
        isobbx = (iso).bbox
        click.echo(isobbx)
        return isobbx


    if detail == 'feature':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        #TO-DO feature.geometry.coordinates in variable speichern
        points = 0
        print("in ISO")
        for feature in iso:
            click.echo(feature.geometry.coordinates)
        #convex_hull(points)
        return points


if __name__ == '__main__':
    getIsobbx()