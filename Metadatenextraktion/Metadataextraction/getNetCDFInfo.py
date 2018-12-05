import click, json, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os

def getNetCDFbbx(filepath, detail):
    """returns the bounding Box NetCDF
    @param path Path to the file """
    if detail =='bbox':
        ds = xr.open_dataset(filepath)
        try:
            lats = ds.coords["lat"]
            lons = ds.coords["lon"]

        except Exception as e:
            lats = ds.coords["latitude"]
            lons = ds.coords["longitude"]
        mytime = ds.coords["time"]
        # print(ds.values)
        minlat=min(lats).values
        minlon=min(lons).values
        maxlat=max(lats).values
        maxlon=max(lons).values
        starttime=min(mytime)
        endtime=max(mytime)
        # Bounding Box Ausgabe in Schoen
        print("Min Latitude: ")
        print(minlat)
        print("Min Longitude: ")
        print(minlon)
        print("Max Latitude: ")
        print(maxlat)
        print("Max Longitude: ")
        print(maxlon)

        # Speicherung als bbox noch nicht so schoen, da Ausgabe als vier Arrays mit einem Wert
        bbox = [minlat,minlon,maxlat,maxlon]
        click.echo(bbox)
        print("-------------------------------------------------")

        # Zeitliche Ausdehnung
        print("Timestamp: ")
        print(starttime.values)
        print(endtime.values)
        print("__________________________________________________")

    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')


if __name__ == '__main__':
    getNetCDFbbx()