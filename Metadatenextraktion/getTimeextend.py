import click, shapefile, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import ogr2ogr
import csv
import os
import sys
import json
import sqlite3


@click.command()
@click.option('--path', prompt='Datapath', help='Path to the data.')
@click.option('--time', 'detail', flag_value='time', default=True)

def getTimeextend(path, detail):
    filepath = path
    # Program that extracts the time-extend of files.

    try:
        getShapefiletime(filepath, detail)
    except Exception as e:
        try:
            getGeoJsontime(filepath, detail)
        except Exception as e:
            try:
                getCSVtime(filepath, detail)
            except Exception as e:
                try:
                    getNetCDFtime(filepath, detail)
                except Exception as e:
                    try:
                        getGeopackagetime(filepath, detail)
                    except Exception as e:
                        try: 
                            getGeoTifftime(filepath, detail)    
                        except Exception as e:
                            try: 
                                getGeoTifftime(filepath, detail)    
                            except Exception as e:
                                try: 
                                    getGeoTifftime(filepath, detail)    
                                except Exception as e:
                                    click.echo ("invalid file format or no time-values included!")

def getShapefiletime(filepath, detail):
    click.echo(detail)
    if detail =='time':
        sf = shapefile.Reader(filepath)
        click.echo("There is no time-value or invalid file")

def getGeoTifftime(filepath, detail):
    if detail =='time':
        ds =  gdal.Open(filepath)
        print(ds)
        print("test2")
        try:
            print(gdal.Info(ds))
            click.echo("no time-value found yet")
            return None
        except Exception as e:
            click.echo ("There is no time-value or invalid file")
            return None

def getCSVtime(filepath, detail):
    if detail =='time':
        # Using Pandas: http://pandas.pydata.org/pandas-docs/stable/io.html
        df = pd.read_csv(filepath, delimiter=';',engine='python')
        listtime = ["time", "timestamp", "date", "Time"]
        print("testhallo")
        if not intersect(listtime,df.columns.values):
            print("No fitting header for time-values")
            # TODO: fehlerbehandlung  
            try:
                print("test2")
                for t in listtime:
                    if(x not in df.columns.values):
                        click.echo("This file does not include time-values")
                    else:
                        time=df[t]
                        timeextend =[min(time), max(time)]
                        click.echo(timeextend)
                        return timeextend
            except Exception as e:
                click.echo ("There is no time-value or invalid file")
                return None   

def getGeoJsontime(filepath, detail):
        ds = open(filepath)
        geojson = json.load(ds)
        print(" ")
        print("The time value of this file is:")
        try:
            click.echo(geojson["features"][0]["date"])
        except Exception as e:
            try:
                click.echo(geojson["features"][0]["time"])
            except Exception as e:
                try:
                    click.echo(geojson["features"][0]["properties"]["date"])
                except Exception as e:
                    try:
                        click.echo(geojson["features"][0]["properties"]["time"])
                    except Exception as e:
                        click.echo("there is no time-value")
                

def getNetCDFtime(filepath, detail):
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
            print("the temporalextend is:")
            print(anfang)
            print(ende)
            return anfang, ende
        except Exception as e:
            click.echo ("There is no time-value or invalid file")
            return None
    
def getGeopackagetime(filepath, detail):
    if detail =='time':
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        try:
            c.execute("""SELECT time or timestamp or date
                        FROM gpkg_contents""")
            print c.fetchone()
            row = c.fetchall()
            print("The time value is:")
            print(row)
            return row
        except Exception as e:
            click.echo ("There is no time-value or invalid file")
            return None
        

def getIsoTime(filepath, detail):
    if detail =='time':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        ds = open(filepath="out.json")
        geojson = json.load(ds)
        print(" ")
        print("The time value of this file is:")
        try:
            click.echo(geojson["features"][0]["date"])
        except Exception as e:
            try:
                click.echo(geojson["features"][0]["time"])
            except Exception as e:
                try:
                    click.echo(geojson["features"][0]["properties"]["date"])
                except Exception as e:
                    try:
                        click.echo(geojson["features"][0]["properties"]["time"])
                    except Exception as e:
                        click.echo("there is no time-value")

if __name__ == '__main__':
    getTimeextend()