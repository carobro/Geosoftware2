from pyproj import Proj, transform # used for the CRS transformation
import click    # used for output messages
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getIsoInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, openFolder   # used for the specific extraction functions

"""
Auxiliary function to bypass problems with the CLI tool when executed from anywhere else

:param path: path to the directory of the files or to the file itself
:param detail: specifies the level of detail of the geospatial extent (bbox or convex hull)
:param time: boolean variable, if it is true the user gets the temporal extent instead of the spatial extent
:returns: spatial extent as a bbox in the format [minlon, minlat, maxlon, maxlat]
"""
@click.command()
@click.option('--path',required=True,prompt='insert filepath!', help='please insert the path to the data here.')
@click.option('--time', is_flag=True, help='returns the time extend of one object')
@click.option('--detail', type=click.Choice(['bbox', 'convexHull']), default='bbox', help='select which information you want to get')

def click_function(path, detail, time):
    getMetadata(path, detail, time)

"""
Function for extracting the metadata (bounding box)
An advantage of our code is that the file extension is not important for the metadataextraction but the content of the file

:param path: path to the directory of the files or to the file itself
:param detail: specifies the level of detail of the geospatial extent (bbox or convex hull)
:param time: boolean variable, if it is true the user gets the temporal extent instead of the spatial extent
:returns: spatial extent as a bbox in the format [minlon, minlat, maxlon, maxlat]
"""
def getMetadata(path, detail, time):
   
    filepath = path
    result = None
   
    if(len(filepath)==0):
        click.echo("Filepath is empty! Please insert a correct filepath")
        return None
    try:
        result=getShapefileInfo.getShapefilebbx(filepath, detail, time)
    except Exception as e:
        try:
            result=getGeoJsonInfo.getGeoJsonbbx(filepath, detail, time)
        except Exception as e:
            try:
                result=getNetCDFInfo.getNetCDFbbx(filepath, detail, time)
            except Exception as e:
                try:
                    result=getCSVInfo.getCSVbbx(filepath, detail, time)
                except TypeError as e:
                    try:
                        result=getGeoPackageInfo.getGeopackagebbx(filepath, detail, time)
                    except Exception as e:
                        try:
                            result=getGeoTiffInfo.getGeoTiffbbx(filepath, detail, time)
                        except Exception as e:
                            try:
                                result=getIsoInfo.getIsobbx(filepath, detail, time)
                            except Exception as e:
                                try:
                                    result=openFolder.openFolder(filepath, detail, time)
                                except Exception as e:
                                    click.echo(e)
    click.echo("Final extraction:")
    click.echo(result)
    return result

"""
Function for transforming the coordinate reference system to WGS84 using PyProj (https://github.com/jswhit/pyproj)

:param lat: value for latitude
:param lng: value for longitude
:sourceCRS: epsg identifier for the source coordinate reference system
:returns: the transformed values for latitude and longitude 
"""
def transformToWGS84(lat, lng, sourceCRS):
    try:
        # formatting the input CRS
        inputProj='epsg:'
        inputProj+=str(sourceCRS)
        inProj = Proj(init=inputProj)
        # epsg:4326 is WGS84
        outProj = Proj(init='epsg:4326')
        latT, lngT = transform(inProj,outProj,lat,lng)
        return(latT,lngT)
    except Exception as e:
        click.echo(e)

"""
Function to print the bounding box in a pretty format.

:param path: path to the file
:param bbox: bounding box
:param data_format: data format
"""
def print_pretty_bbox(path, bbox, data_format):
    print("----------------------------------------------------------------")
    click.echo("Filepath:")
    click.echo(path)
    click.echo("Boundingbox of the "+data_format+" object:")
    click.echo(bbox)
    print("----------------------------------------------------------------")

"""
Function to print the convex hull in a pretty format.

:param path: path to the file
:param convex_hull: convex hull
:param data_format: data format
"""
def print_pretty_hull(path, convex_hull, data_format):
    print("----------------------------------------------------------------")
    click.echo("Filepath:")
    click.echo(path)
    click.echo("Convex Hull of the "+data_format+" file: ")
    click.echo(convex_hull)
    print("----------------------------------------------------------------")

"""
Function to print the time in a pretty format.

:param path: path to the file
:param bbox: bounding box
:param data_format: data format
"""
def print_pretty_time(path, time, data_format):
    print("----------------------------------------------------------------")
    click.echo("Timeextend of the "+data_format+" file:")
    click.echo(time)
    print("----------------------------------------------------------------")

if __name__ == '__main__':
    click_function()
