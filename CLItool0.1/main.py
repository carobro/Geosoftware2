import argparse
parser = argparse.ArgumentParser()

parser.add_argument("exmd", help="Extracts the metadata of a with the -t operand specified file an displays it in the console")
parser.add_argument("-i", "--interval", help="only extract the temporal extent")
parser.add_argument("-s", "--spatial", help="only extract the spatial extent")
parser.add_argument("-is", help="only extract the temporal & spatial extent")
parser.add_argument("-t","--type", choices=['gpkg', 'nc', 'cdf', 'geojson', 'shp', 'csv', 'geotiff', 'tif'],
                    help="choose the filetype from which the metadata should be extracted")
args = parser.parse_args()

if args.type == 'gpkg':
    print "this is GeoPackage"
elif args.type == 'nc':
    print "this is NetCDF"
elif args.type == 'nc':
    print "this is NetCDF"
elif args.type == 'cdf':
    print "this is NetCDF"
elif args.type == 'geojson':
    print "this is GeoJSON"
elif args.type == 'shp':
    print "this is Shapefile"
elif args.type == 'csv':
    print "this is CSV"
elif args.type == 'geotiff':
    print "this is GeoTIFF"
elif args.type == 'tif':
    print "this is GeoTIFF"     
else:
    print "file format not supported. -h shows all possibilities."