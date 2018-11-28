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
    sf = shapefile.Reader(filepath)
    output = sf.bbox
    click.echo(output)

def getGeoTiffbbx(filepath):

    """returns the bounding Box GeoTiff. (.tif)
    @param path Path to the file """
    metadata = gdal.Info(filepath)
    click.echo(metadata)

def getCSVbbx(filepath):
        click.echo("Dies ist ein Test")


def getGeoJsonbbx(filepath):
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox 
        click.echo(geojbbx)

def getNetCDFbbx(filepath):
        ds = xr.open_dataset(filepath)
        lats = ds.coords["lat"]
        lons = ds.coords["lon"]
        bbox = (min(lats), min(lons), max(lats), max(lons))
        click.echo(bbox)

        
def getGeopackagebbx(filepath):
        click.echo("GeoPagackeBlock")




if __name__ == '__main__':
    getMetadata()