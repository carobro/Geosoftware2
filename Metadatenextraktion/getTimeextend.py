import click, shapefile
import csv
from osgeo import gdal
import pandas as pd
import pygeoj
import numpy as np
import xarray as xr

@click.command()
@click.option('--path', prompt='Datapath', help='Path to the data.')

def getTimeextend(path):
    filepath = path
    # https://docs.python.org/2/library/os.path.html
    # Program that extracts the time-extend of files.

    try:
        getShapefiletime(filepath)
    except Exception as e:
        try: 
            getGeoTifftime(filepath)
        except Exception as e:
            try:
                getCSVtime(filepath)
            except Exception as e:
                try:
                    getGeoJsontime(filepath)
                except Exception as e:
                    try:
                        getNetCDFtime(filepath)
                    except Exception as e:
                        try:
                            getGeopackagetime(filepath)
                        except Exception as e:
                            click.echo ("invalid file format!")

def getShapefiletime(filepath):


def getGeoTifftime(filepath):
    ds =  gdal.Open(filepath)
    print(gdal.Info(ds))

def getCSVtime(filepath):
    path = open(filepath)
    reader = csv.reader(path)
    content = next(reader)[0].replace(";", ",").split(",")

    for x in content:
        if x == "time":
           time = "time"
        if x == "Time":
           time = "Time"
        if x == "date":
            time = "date"
        if x == "timestamp":
           time = "timestamp"

def getGeoJsontime(filepath):
    geojson = pygeoj.load(filepath)


def getNetCDFtime(filepath):
    ds = xr.open_dataset(filepath)

        
def getGeopackagetime(filepath):
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    c.execute("""SELECT ???
                 FROM ??? """)
    row = c.fetchall()
    print(row)

if __name__ == '__main__':
    getTimeextend()