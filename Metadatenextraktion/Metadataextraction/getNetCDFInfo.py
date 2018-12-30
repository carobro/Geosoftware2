import click, json, sqlite3, csv, pygeoj, detailebenen
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os

def getNetCDFbbx(filepath, detail, folder):
    """returns the bounding Box NetCDF
    @param path Path to the file """
    #print("netcdf")
    if detail =='bbox':
        ds = xr.open_dataset(filepath)
        try:
            lats = ds.coords["lat"]
            lons = ds.coords["lon"]

        except Exception as e:
            lats = ds.coords["latitude"]
            lons = ds.coords["longitude"]
        #print(ds.values)
        minlat=min(lats).values
        minlatFloat=float(minlat)
        minlon=min(lons).values
        minlonFloat=float(minlon)
        maxlat=max(lats).values
        maxlatFloat=float(maxlat)
        maxlon=max(lons).values
        maxlonFloat=float(maxlon)
        # Bounding Box Ausgabe in Schoen
        #print("Min Latitude: ")
        #print(minlat)
        #print("Min Longitude: ")
        #print(minlon)
        #print("Max Latitude: ")
        #print(maxlat)
        #print("Max Longitude: ")
        #print(maxlon)


        bbox = [minlatFloat,minlonFloat,maxlatFloat,maxlonFloat]
        #click.echo(bbox)

        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Boundingbox of the NetCDF Object:")
            click.echo(bbox)
            print("----------------------------------------------------------------")
            return bbox
        if folder=='whole':
            #fuer Boundingbox des Ordners
            detailebenen.bboxSpeicher.append(bbox)
            #print(detailebenen.bboxSpeicher)
            return bbox
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