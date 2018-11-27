from osgeo import gdal

def firsttry(path):

"""returns the metadata of supported Datatypes. supported data: Shapefile (.shp), 
    GeoJson (.json/.geojson), GeoTIFF (.tif), netCDF (.nc), GeoPackage (.gpkg) CSV on the web
    @param path to the file """
    # connect path to file
     filepath = "%s\%s" % (path, name)
      
    switcher = {
        1: gdalinfo(filepath),
        2: ogrinfo(filepath)
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