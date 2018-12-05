import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os

def getGeopackagebbx(filepath, detail):
    """returns the bounding Box Geopackage
    @param path Path to the file
    @see https://docs.python.org/2/library/sqlite3.html"""
    if detail =='bbox':
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT min(min_x), min(min_y), max(max_x), max(max_y)
                     FROM gpkg_contents """)
        row = c.fetchall()
        print(row)
    if detail == 'feature':
            click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')


if __name__ == '__main__':
    getGeopackagebbx()
