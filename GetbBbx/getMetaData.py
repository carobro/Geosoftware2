from osgeo import gdal
import pandas as pd
import pygeoj
def firsttry(path):

"""returns the metadata of supported Datatypes. supported data: Shapefile (.shp), 
    GeoJson (.json/.geojson), GeoTIFF (.tif), netCDF (.nc), GeoPackage (.gpkg) CSV on the web
    @param path to the file """
    # connect path to file
     filepath = "%s\%s" % (path, name)p
      
    switcher = { """ filepath immer in (" ") eingeben """
        1: gdalinfo(filepath),              """GeoTiff""" 
        2: pd.read_csv(filepath),           """CSV"""
        3: (test).bbox                      """GeoJson; bounding box of entire file: test=pygeoj.load(filepath)""""
        4: shapefile.Reader(filepath)       """Shapefile"
        5:
        6:
    }
    print switcher.get(path, click.echo("type %s not supported" % filepath))

 """ if (1+1=2):
  try:
      gdalinfo(filepath)
      ogrinfo(filepath)
else: 
     click.echo("type %s not supported" % filepath)
        return None"""

"""
Main Methode anpassen
# Main method
if __name__ == '__main__':
    getMetaData()
    """
