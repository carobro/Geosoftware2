from osgeo import gdal

def getMetaData(path):

"""returns the metadata of supported Datatypes. supported data: Shapefile (.shp), 
    GeoJson (.json/.geojson), GeoTIFF (.tif), netCDF (.nc), GeoPackage (.gpkg) CSV on the web
    @param path to the file """
    # connect path to file
     filepath = "%s\%s" % (path, name)
  
 """ if (1+1=2):
  try:
      gdalinfo(filepath)
      ogrinfo(filepath)"""
      
def firsttry(argument):
    switcher = {
        1: gdalinfo(filepath),
        2: ogrinfo(filepath)
    }
    print switcher.get(argument, click.echo("type %s not supported" % filepath))

else: 
     click.echo("type %s not supported" % filepath)
        return None

"""
Main Methode anpassen
# Main method
if __name__ == '__main__':
    getMetaData()
    """