import click, shapefile, json, sqlite3, csv, pygeoj, geojson, os, ogr2ogr
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import numpy as np

##############NOCH NICHT FERTIG################

def getTyp(path):
    filepath = path
    try:
        shapefile.Reader(filepath)
        input = "raster"
        return input
    except Exception as e:
        try:
            gdal.Open(filepath)
            input = "raster"
            return input
        except Exception as e:
            try:
                pd.read_csv(filepath, delimiter=';',engine='python')
                input = "raster"
                return input
            except Exception as e:
                try:
                    pygeoj.load(filepath)
                    input = "raster"
                    return input
                except Exception as e:
                    try:
                        xr.open_dataset(filepath)
                        input = "raster"
                        return input
                    except Exception as e:
                        try:
                            conn = sqlite3.connect(filepath)
                            conn.cursor()
                            input = "raster"
                            return input
                        except Exception as e:
                            try:
                                ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
                                pygeoj.load(filepath="out.json")
                                input = "raster"
                                return input
                            except Exception as e:
                                click.echo ("invalid file format!")
                                return None
                                
if __name__ == '__main__':
    getTyp()
