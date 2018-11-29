import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr

""" Vorteil uneres Codes: Es wird nicht auf die Endung (.shp etc.) geachtet, 
sondern auf den Inhalt"""
@click.command()
@click.option('--path', prompt='Datapath', help='Path to the data.')

def getMetadata(path):
    filepath = path
    # Program that extracts the boudingbox of files.

    try:
        getShapefilebbx(filepath)
    except Exception as e:
        try: 
            getGeoJsonbbx(filepath)
        except Exception as e:
            try:
                getNetCDFbbx(filepath)
            except Exception as e:
                try:
                    getCSVbbx(filepath)
                except Exception as e:
                    try:
                        getGeoTiffbbx(filepath)
                    except Exception as e:
                        try:
                            getGeopackagebbx(filepath)
                        except Exception as e:
                            click.echo ("invalid file format!")


def getShapefilebbx(filepath):
    """returns the bounding Box Shapefile.
    @param path Path to the file """
    sf = shapefile.Reader(filepath)
    output = sf.bbox
    click.echo(output)

def getGeoTiffbbx(filepath):
    ds = gdal.Info(filepath)
    click.echo(ds)

def getCSVbbx(filepath):
    """returns the bounding Box CSV
    @see https://www.programiz.com/python-programming/reading-csv-files
    @param path Path to the file """
    
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

def getGeoJsonbbx(filepath):
    """returns the bounding Box GeoJson
    @param path Path to the file """
    geojson = pygeoj.load(filepath)
    geojbbx = (geojson).bbox 
    click.echo(geojbbx)

def getNetCDFbbx(filepath):
    """returns the bounding Box NetCDF
    @param path Path to the file """
    ds = xr.open_dataset(filepath)
    lats = ds.coords["lat"]
    lons = ds.coords["lon"]
    bbox = (min(lats), min(lons), max(lats), max(lons))
    click.echo(bbox)

def getGeopackagebbx(filepath):
    """returns the bounding Box Geopackage
    @param path Path to the file 
    @see https://docs.python.org/2/library/sqlite3.html"""
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    c.execute("""SELECT min(min_x), min(min_y), max(max_x), max(max_y), srs_id
                 FROM gpkg_contents """)
    row = c.fetchall()
    print(row)

if __name__ == '__main__':
    getMetadata()