import ogr2ogr

def getGMLBoundingBox(name, path):

filepath = "%s\%s" % (path, name)
""" https://docs.python.org/2/library/os.path.html """
f_extension = os.path.splitext(filepath)

if f_extension == ".gml" or f_extension == ".xml" or f_extension == ".kml":
  try:
""" We need to convert the .gml file to a Geojson file"""
"""https://gis.stackexchange.com/questions/39080/using-ogr2ogr-to-convert-gml-to-shapefile-in-python"""
   ogr2ogr.main(["","-f", "GeoJSON", "output.json", filepath])
  
  """Hier fehlt was """

else 
    click.echo("Invalid File")