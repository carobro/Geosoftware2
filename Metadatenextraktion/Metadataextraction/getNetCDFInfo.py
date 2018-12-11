import click, json, sqlite3, csv, pygeoj, detailebenen
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os

def getNetCDFbbx(filepath, detail, folder):
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

        bbox = [minlat,minlon,maxlat,maxlon]

        if folder=='single':
            # Speicherung als bbox noch nicht so schoen, da Ausgabe als vier Arrays mit einem Wert
            print(minlat)
            click.echo(bbox)
            print("-------------------------------------------------")

        if folder=='whole':
            print("ausdehnung")
            #fuer Boundingbox des Ordners
            detailebenen.bboxSpeicher.append(bbox)
            
            print(detailebenen.bboxSpeicher)
        
        # Zeitliche Ausdehnung
        print("Timestamp: ")
        print(starttime.values)
        print(endtime.values)
        print("__________________________________________________")

    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')


if __name__ == '__main__':
    getNetCDFbbx()