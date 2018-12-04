import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os

""" Vorteil uneres Codes: Es wird nicht auf die Endung (.shp etc.) geachtet,
sondern auf den Inhalt"""
@click.command()
@click.option('--path',required=True, help='Path to the data.')
@click.option('--bbox', 'detail', flag_value='bbox',
              default=True)
@click.option('--feature', 'detail', flag_value='feature')

def getMetadata(path, detail):
    filepath = path
    # Program that extracts the boudingbox of files.

    try:
        getShapefilebbx(filepath, detail)
    except Exception as e:
        try:
            getGeoJsonbbx(filepath, detail)
        except Exception as e:
            try:
                getNetCDFbbx(filepath, detail)
            except Exception as e:
                try:
                    getCSVbbx(filepath, detail)
                except Exception as e:
                    try:
                        getGeoTiffbbx(filepath, detail)
                    except Exception as e:
                        try:
                            getGeopackagebbx(filepath, detail)
                        except Exception as e:
                            try:
                                openFolder(filepath, detail)
                            except Exception as e:
                                click.echo ("invalid file format!")


def openFolder(filepath, detail):
    folderpath= filepath
    click.echo("drin")
    docs=os.listdir(folderpath)
    for x in docs:
        docPath= folderpath +"/"+ x
        print docPath
        #getMetadata(docPath, detail2)
        try:
            getShapefilebbx(docPath, detail)
        except Exception as e:
            try: 
                getGeoJsonbbx(docPath, detail)
            except Exception as e:
                try:
                    getNetCDFbbx(docPath, detail)
                except Exception as e:
                    try:
                        getCSVbbx(docPath, detail)
                    except Exception as e:
                        try:
                            getGeopackagebbx(docPath, detail)
                        except Exception as e:
                            try:
                                getGeoTiffbbx(docPath, detail)
                            except Exception as e:
                                try:
                                    openFolder(docPath, detail)
                                except Exception as e:
                                    click.echo ("invalid file format!")



def getShapefilebbx(filepath, detail):
    """returns the bounding Box Shapefile.
    @param path Path to the file """
    click.echo(detail)
    if detail =='bbox':
        sf = shapefile.Reader(filepath)
        output = sf.bbox
        click.echo(output)
    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')

def getGeoTiffbbx(filepath, detail):
    if detail =='bbox':
        ds = gdal.Info(filepath)
        click.echo(ds)
    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')

def getCSVbbx(filepath, detail):
    """returns the bounding Box CSV
    @see https://www.programiz.com/python-programming/reading-csv-files
    @param path Path to the file """
    if detail =='bbox':
        path = open(filepath)
        reader = csv.reader(path)
        content = next(reader)[0].replace(";", ",").split(",")

        #inhalt richtig in lng und lat speichern
        for x in content:
            if x == "longitude":
                lons = "longitude"
            if x == "Longitude":
                lons = "Longitude"
            if x == "lon":
                lons = "lon"
            if x == "lng":
                lons = "lng"
            if x == "latitude":
                lats = "latitude"
            if x == "Latitude":
                lats = "Latitude"
            if x == "lat":
                lats = "lat"
        print(content)

    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')

def getGeoJsonbbx(filepath, detail):
    """returns the bounding Box GeoJson
    @param path Path to the file """
    if detail =='bbox':
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox
        click.echo(geojbbx)

    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')

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
        # Bounding Box Ausgabe in Schön
        print("Min Latitude: ")
        print(minlat)
        print("Min Longitude: ")
        print(minlon)
        print("Max Latitude: ")
        print(maxlat)
        print("Max Longitude: ")
        print(maxlon)

        # Speicherung als bbox noch nicht so schön, da Ausgabe als vier Arrays mit einem Wert
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

def getGeopackagebbx(filepath, detail):
    """returns the bounding Box Geopackage
    @param path Path to the file
    @see https://docs.python.org/2/library/sqlite3.html"""
    if detail =='bbox':
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT min(min_x), min(min_y), max(max_x), max(max_y), srs_id
                     FROM gpkg_contents """)
        row = c.fetchall()
        print(row)
    if detail == 'feature':
            click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')

if __name__ == '__main__':
    getMetadata()
