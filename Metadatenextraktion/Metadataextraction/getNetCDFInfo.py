import click, json, sqlite3, csv, pygeoj, detailebenen
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os

def getNetCDFbbx(filepath, detail, folder):
    """returns the bounding Box NetCDF
    @param path Path to the file """
    print("netcdf")
    ds = xr.open_dataset(filepath)
    if detail =='bbox':
        print("bbox")
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


        bbox = [minlatFloat,minlonFloat,maxlatFloat,maxlonFloat]
        #click.echo(bbox)

        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the NetCDF Object:")
            click.echo(bbox)
            print("----------------------------------------------------------------")
            #print("test")
            #return bbox
        if folder=='whole':
            #fuer Boundingbox des Ordners
            detailebenen.bboxArray.append(bbox)
            click.echo(filepath)
            print(bbox)
            #return bbox
    if detail == 'convexHull':
        #ds = xr.open_dataset(filepath)
        #try:
            #lats = ds.coords["lat"]
            #lons = ds.coords["lon"]

        #except Exception as e:
            #lats = ds.coords["latitude"]
            #lons = ds.coords["longitude"]
            #convex_hull(points)
            #GeoTiff is a rastadata, so:
        
        click.echo('Sorry there is no second level of detail for NetCDF files')
        #return None

        
    # @author Jannis Froehlking
    # After opening the file we are looking for 
    # time values and calculate the temporal extend 
    # with min and max functions
    click.echo("NetCDF")
    """returns the Time from NetCDF file
    @param path Path to the file """
    if detail =='time':
        ds = xr.open_dataset(filepath)
        try:
            mytime = ds.coords["time"]
            # print(ds.values)
            starttime = min(mytime)
            endtime = max(mytime)
            # Zeitliche Ausdehnung
            anfang = starttime.values
            ende = endtime.values
            print("the temporal extend of the NetCDF object is:")
            print(anfang)
            print(ende)
            return anfang, ende
        except Exception as e:
            click.echo ("There is no time-value or invalid file")
            return None
    ds.close()
    #print("fertig")

if __name__ == '__main__':
    getNetCDFbbx()