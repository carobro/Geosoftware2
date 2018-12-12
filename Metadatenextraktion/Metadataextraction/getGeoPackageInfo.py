import click, json, sqlite3, csv, pygeoj, detailebenen
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import sqlite3

def getGeopackagebbx(filepath, detail, folder):
    """returns the bounding Box Geopackage
    @param path Path to the file
    @see https://docs.python.org/2/library/sqlite3.html"""
    if detail =='bbox':
        print(filepath)
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT min(min_x), min(min_y), max(min_x), max(min_x)
                     FROM gpkg_contents""")
        row = c.fetchall()
        print(row)
    if detail == 'feature':
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT min_x,min_y
                     FROM gpkg_contents""")
        points = c.fetchall()
        print(points)
        #convex_hull(points)
        return points
        
if __name__ == '__main__':
    getGeopackagebbx()
