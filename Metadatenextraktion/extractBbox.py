import click, shapefile
from osgeo import gdal
import pandas as pd
import pygeoj
import numpy as np
import xarray as xr

@click.command()
@click.option('--path', prompt='Datapath', help='Path to the data.')

def getMetadata(path):
    filepath = path
    # https://docs.python.org/2/library/os.path.html
    # Program that extracts the boudingbox of files.
"""Jede Try Funktion versucht den Path auszulesen, falls dies nicht
möglich ist, springt er weiter """
    try:
        getShapefilebbx(filepath)
    except Exception as e:
        try: 
            getGeoTiffbbx(filepath)
        except Exception as e:
            try:
                getCSVbbx(filepath)
            except Exception as e:
                try:
                    getGeoJsonbbx(filepath)
                except Exception as e:
                    try:
                        getNetCDFbbx(filepath)
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
    """returns the bounding Box GeoTiff. (.tif)
    @param path Path to the file """
    metadata = gdal.Info(filepath)
    click.echo(metadata)

def getCSVbbx(filepath):
    """returns the bounding Box CSV
    @param path Path to the file """
    pd.read_csv(filepath)


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
    @param path Path to the file """
        click.echo("GeoPagackeBlock")



"""main method"""
if __name__ == '__main__':
    getMetadata()