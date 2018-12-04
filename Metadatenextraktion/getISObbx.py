import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import ogr2ogr
ogr2ogr.BASEPATH = "/home/caro/Vorlagen/Geosoftware2/Metadatenextraktion"

@click.command()
@click.option('--path',required=True, help='Path to the data.')
@click.option('--bbox', 'detail', flag_value='bbox',
              default=True)
@click.option('--feature', 'detail', flag_value='feature')

def getMetadata(path, detail):
    filepath = path
    # Program that extracts the boudingbox of files.
    try:
        getIsobbx(filepath, detail)
    except Exception as e:
        click.echo ("invalid file format!")

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
    getMetadata()
