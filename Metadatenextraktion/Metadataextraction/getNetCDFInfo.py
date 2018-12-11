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
        # print(ds.values)
        minlat=min(lats).values
        minlon=min(lons).values
        maxlat=max(lats).values
        maxlon=max(lons).values
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

    if detail == 'feature':
        ds = xr.open_dataset(filepath)
        try:
            lats = ds.coords["lat"]
            lons = ds.coords["lon"]

        except Exception as e:
            lats = ds.coords["latitude"]
            lons = ds.coords["longitude"]
        print("Latitude:")
        print(lats.values)
        print("Longitude:")
        print(lons.values)
        #convex_hull(points)
        return 0

if __name__ == '__main__':
    getNetCDFbbx()