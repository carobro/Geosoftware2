import click, shapefile
from osgeo import gdal
import pandas as pd
import pygeo
import numpy as np
import xarray as xr

@click.command()
@click.option('--path', prompt='Datapath', help='Path to the data.')
 """Program that extracts the boudingbox of files."""

def getMetadata(path):

filepath = "%s\%s" % (path)
""" https://docs.python.org/2/library/os.path.html """
f_extension = os.path.splitext(filepath)
  
        switcher = {
                1: f_extension == ".tif" or f_extension == ".tiff": getGeoTiffbbx(filepath),                          """GeoTiff""" 
                2: f_extension == ".csv" or f_extension == ".txt":    getCSVbbx(filepath),                            """CSV"""
                3: f_extension == ".json" or f_extension == ".geojson":   getGeoJsonbbx(filepath),                    """GeoJson""""
                4: f_extension == ".shp" or f_extension == ".dbf" or f_extension == ".shx": getShapefilebbx(filepath) """Shapefile"""
                5: f_extension == ".nc": getNetCDFbbx(filepath)                                                       """NetCDF"""
                6: f_extension == ".gpkg": getGeopackagebbx(filepath)                                                 """Geopackage"""
            }
        print switcher.get(path, click.echo("type %s not supported" % filepath))

"""if-Fälle müssen noch ergänzt werden, falls die Endung richtig ist, aber die Datei von innen trotzdem falsch ist"""

def getShapefilebbx(filepath):

  sf = shapefile.Reader(filepath)
    output = sf.bbox
    
    click.echo(output)

else
     click.echo("Invalid File")
     return None

def getGeoTiffbbx(filepath):

        """returns the bounding Box GeoTiff. (.tif)
        @param path Path to the file """
        # get the existing coordinate system
        ds = gdal.Open(filepath)
        old_cs= osr.SpatialReference()
        old_cs.ImportFromWkt(ds.GetProjectionRef())

        # create the new coordinate system
        wgs84_wkt = """
        GEOGCS["WGS 84",
            DATUM["WGS_1984",
                SPHEROID["WGS 84",6378137,298.257223563,
                    AUTHORITY["EPSG","7030"]],
                AUTHORITY["EPSG","6326"]],
            PRIMEM["Greenwich",0,
                AUTHORITY["EPSG","8901"]],
            UNIT["degree",0.01745329251994328,
                AUTHORITY["EPSG","9122"]],
            AUTHORITY["EPSG","4326"]]"""
        new_cs = osr.SpatialReference()
        new_cs .ImportFromWkt(wgs84_wkt)

        # create a transform object to convert between coordinate systems
        transform = osr.CoordinateTransformation(old_cs,new_cs) 

        #get the point to transform, pixel (0,0) in this case
        width = ds.RasterXSize
        height = ds.RasterYSize
        gt = ds.GetGeoTransform()
        minx = gt[0]
        miny = gt[3] + width*gt[4] + height*gt[5]
        maxx = gt[0] + width*gt[1] + height*gt[2]
        maxy = gt[3] 

        #get the coordinates in lat long
        latlongmin = transform.TransformPoint(minx,miny)
        latlongmax = transform.TransformPoint(maxx,maxy)
        bbox = [latlongmin[0], latlongmin[1], latlongmax[0], latlongmax[1]]
        click.echo(bbox)
        return bbox

    else
        click.echo("Invalid File")
        return None


def getCSVbbx(filepath):
    
    
    else
     click.echo("Invalid File")
     return None

def getGeoJsonbbx(filepath):
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox 
        click.echo(geojbbx)
        return geojbbx

    else
        click.echo("Invalid File")
        return None

def getNetCDFbbx(filepath):

        # path to the file
        ds = xr.open_dataset(filepath)
        lats = ds.coords["lat"]
        lons = ds.coords["lon"]
        bbox = (min(lats), min(lons), max(lats), max(lons))
        print("Bounding Box: ")
        print(bbox)

    else
        click.echo("Invalid File")
        return None
        
def getGeopackagebbx(filepath):

    else
     click.echo("Invalid File")
     return None




if __name__ == '__main__':
    getMetadata()