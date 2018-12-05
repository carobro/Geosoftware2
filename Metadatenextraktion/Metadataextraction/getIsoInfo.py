import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import ogr2ogr
ogr2ogr.BASEPATH = "/home/cornelia/Dokumente/geosoft/Geosoftware2/Geosoftware2/Metadatenextraktion"

def getIsobbx(filepath, detail):
    """@see http://manpages.ubuntu.com/manpages/trusty/man1/ogr2ogr.1.html"""
    if detail =='bbox':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        isobbx = (iso).bbox
        click.echo(isobbx)

    if detail == 'feature':
           click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')



if __name__ == '__main__':
    getIsobbx()