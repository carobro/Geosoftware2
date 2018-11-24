import xarray as xr
from osgeo import gdal
"""https://gis.stackexchange.com/questions/270165/gdal-to-acquire-netcdf-like-metadata-structure-in-python"""

def getNetCDFBoundingBox(name, path):

filepath = "%s\%s" % (path, name)
""" https://docs.python.org/2/library/os.path.html """
f_extension = os.path.splitext(filepath)

if f_extension ==".nc"

"Hier fehlt der Teil"

try: 
 ds = xr.open_dataset(filepath)

 else click.echo("Invalid File")
 return None