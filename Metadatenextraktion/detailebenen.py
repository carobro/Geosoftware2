import click, shapefile, json, sqlite3, csv, pygeoj, geojson
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import numpy as np
import ogr2ogr

""" Vorteil unseres Codes: Es wird nicht auf die Endung (.shp etc.) geachtet,
sondern auf den Inhalt"""
@click.command()
@click.option('--path',required=True, help='Path to the data.')
@click.option('--bbox', 'detail', flag_value='bbox',
              default=True)
@click.option('--feature', 'detail', flag_value='feature')

def getMetadata(path, detail):
    filepath = path
    # Program that extracts the boudingbox of files.

    try:
        getShapefilebbx(filepath, detail)
    except Exception as e:
        try:
            getGeoJsonbbx(filepath, detail)
        except Exception as e:
            try:
                getNetCDFbbx(filepath, detail)
            except Exception as e:
                try:
                    getCSVbbx(filepath, detail)
                except Exception as e:
                    try:
                        getGeopackagebbx(filepath, detail)
                    except Exception as e:
                        try:
                            getGeoTiffbbx(filepath, detail)
                        except Exception as e:
                            try:
                                getIsobbx(filepath, detail)
                            except Exception as e:
                                try:
                                    openFolder(filepath, detail)
                                except Exception as e:
                                    click.echo ("invalid file format!")


def openFolder(filepath, detail):
    folderpath= filepath
    click.echo("drin")
    docs=os.listdir(folderpath)
    for x in docs:
        docPath= folderpath +"/"+ x
        print docPath
        #getMetadata(docPath, detail2)
        try:
            getShapefilebbx(docPath, detail)
        except Exception as e:
            try:
                getGeoJsonbbx(docPath, detail)
            except Exception as e:
                try:
                    getNetCDFbbx(docPath, detail)
                except Exception as e:
                    try:
                        getCSVbbx(docPath, detail)
                    except Exception as e:
                        try:
                            getGeopackagebbx(docPath, detail)
                        except Exception as e:
                            try:
                                getGeoTiffbbx(docPath, detail)
                            except Exception as e:
                                try:
                                    getIsobbx(docpath, detail)
                                except Exception as e:
                                    try:
                                        openFolder(docPath, detail)
                                    except Exception as e:
                                        click.echo ("invalid file format!")


def getShapefilebbx(filepath, detail):
    """returns the bounding Box Shapefile.
    @param path Path to the file """
    click.echo(detail)
    if detail =='bbox':
        sf = shapefile.Reader(filepath)
        output = sf.bbox
        click.echo(output)
    if detail == 'feature':
        sf = shapefile.Reader(filepath)
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')
        return 0

def getGeoTiffbbx(filepath, detail):
    """@see https://stackoverflow.com/questions/2922532/obtain-latitude-and-longitude-from-a-geotiff-file"""
    if detail =='bbox':

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
        return (bbox)

    if detail == 'feature':
        ds = gdal.Open(filepath)
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')
        
        return 0

def getCSVbbx(filepath, detail):
    """returns the bounding Box CSV
    @see https://www.programiz.com/python-programming/reading-csv-files
    @param path Path to the file """
    if detail == 'feature':
        df = pd.read_csv(filepath, delimiter=',',engine='python')
        listlat = ["Koordinate_Hochwert","lat","Latitude","latitude"]
        listlon = ["Koordinate_Rechtswert","lon","Longitude","longitude","lng"]
        if not intersect(listlat,df.columns.values):
            click.echo("No fitting header for latitudes")
            # TODO: fehlerbehandlung  
        for x in listlat:
            if(x not in df.columns.values):
                print("No valid coordinates")
                return None
            lats=df[x]
            for y in listlon:
                lons=df[y]
                print("All Points")
                points=[lons, lats]
                click.echo(points)
                #conhex_hull(points)
                return points
        return 0

    if detail =='bbox':
        # Using Pandas: http://pandas.pydata.org/pandas-docs/stable/io.html
        df = pd.read_csv(filepath, delimiter=';',engine='python')
        listlat = ["Koordinate_Hochwert","lat","Latitude","latitude"]
        listlon = ["Koordinate_Rechtswert","lon","Longitude","longitude","lng"]
        if not intersect(listlat,df.columns.values):
            click.echo("No fitting header for latitudes")
            # TODO: fehlerbehandlung  
        for x in listlat:
            if(x not in df.columns.values):
                print("Hello")
            lats=df[x]
            for y in listlon:
                lons=df[y]
                print("Bounding Box: ")
                bbox=[min(lons),min(lats),max(lons),max(lats)]
                click.echo(bbox)
                return bbox
        
# Hilfsfunktion fuer csv fehlerbehandlung
def intersect(a, b):
     return list(set(a) & set(b))

def getGeoJsonbbx(fiimport click, shapefile, sqlite3, csv
from osgeo import gdal, ogr, osr
import os
import pandas as pd
import numpy as np
import xarray as xr
import ogr2ogr
import json


@click.command()
@click.option('--path', prompt='Datapath', help='Path to the data.')
@click.option('--time', 'detail', flag_value='time', default=True)

def getTimeextend(path, detail):
    filepath = path
    # Program that extracts the time-extend of files.
    try:
        getShapefiletime(filepath, detail)
    except Exception as e:
        """
        try:
            getCSVtime(filepath, detail)
        except Exception as e:
            """
        try:
            getNetCDFtime(filepath, detail)
        except Exception as e:
            try:
                getGeopackagetime(filepath, detail)
            except Exception as e:
                try: 
                    getGeoTifftime(filepath, detail)    
                except Exception as e:
                    try:
                        getGeoJsontime(filepath, detail)
                    except Exception as e:
                        try: 
                            getIsoTime(filepath, detail)    
                        except Exception as e:
                            click.echo ("invalid file format or no time-values included!")

def getShapefiletime(filepath, detail):
    click.echo("Shapefile")
    click.echo(detail)
    if detail =='time':
        sf = shapefile.Reader(filepath)
        click.echo("There is no time-value or invalid file")
        return None

def getGeoTifftime(filepath, detail):
    click.echo("GeoTiff")
    if detail =='time':
        ds = gdal.Open(filepath)
        gdal.Info(ds)
        click.echo("no time-value found yet")
        return None

def getCSVtime(filepath, detail):
    click.echo("CSV")
    if detail =='time':
        # Using Pandas: http://pandas.pydata.org/pandas-docs/stable/io.html
        df = pd.read_csv(filepath, delimiter=';',engine='python')
        listtime = ["time", "timestamp", "date", "Time"]
        print("testhallo")
        if not intersect(listtime,df.columns.values):
            print("No fitting header for time-values")
            # TODO: fehlerbehandlung  
            try:
                print("test2")
                for t in listtime:
                    if(x not in df.columns.values):
                        click.echo("This file does not include time-values")
                    else:
                        time=df[t]
                        timeextend =[min(time), max(time)]
                        click.echo(timeextend)
                        return timeextend
            except Exception as e:
                click.echo ("There is no time-value or invalid file")
                return None   

def getGeoJsontime(filepath, detail):
    print("GeoJson")
    if detail =='time':
        ds = open(filepath)
        geojson = json.load(ds)
        print(" ")
        print("The time value of this file is:")
        if geojson["type"] == "FeatureCollection":
            first = geojson["features"]
            try:
                click.echo(first[0]["Date"])
                time = first[0]["Date"]
                return time
            except Exception as e:
                try:
                    click.echo(first[0]["creationDate"])
                    time = time[0]["creationDate"]
                    return time
                except Exception as e:
                    try:
                        click.echo(first[0]["date"])
                        time = first[0]["date"]
                        return time
                    except Exception as e:
                        try:
                            click.echo(first[0]["time"])
                            time = first[0]["time"]
                            return time
                        except Exception as e:
                            try:
                                click.echo(first[0]["properties"]["date"])
                                time = geojson["features"][0]["properties"]["date"]
                                return time
                            except Exception as e:
                                try:
                                    click.echo(first[0]["properties"]["time"])
                                    time = first[0]["properties"]["time"]
                                    return time
                                except Exception as e:
                                    click.echo("there is no time-value")
                                    return None
                
def getNetCDFtime(filepath, detail):
    click.echo("NetCDF")
    """returns the Time from NetCDF file
    @param path Path to the file """
    if detail =='time':
        ds = xr.open_dataset(filepath)
        try:
            mytime = ds.coords["time"]
            # print(ds.values)
            starttime = min(mytime)
            endtime = max(mytime)
            # Zeitliche Ausdehnung
            anfang = starttime.values
            ende = endtime.values
            print("the temporalextend is:")
            print(anfang)
            print(ende)
            return anfang, ende
        except Exception as e:
            click.echo ("There is no time-value or invalid file")
            return None
    
def getGeopackagetime(filepath, detail):
    click.echo("GeoPackage")
    if detail =='time':
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT time or timestamp or date
                        FROM gpkg_contents""")
        try:
            print c.fetchone()
            row = c.fetchall()
            print("The time value is:")
            print(row)
            return row
        except Exception as e:
            click.echo ("There is no time-value or invalid file")
            return None
        

def getIsoTime(filepath, detail):
    click.echo("Iso")
    if detail =='time':
        ogr2ogr.main(["","-f", "GeoJSON", "time.json", filepath])
        iso = open("time.json")
        geojson = json.load(iso)
        # @see https://www.w3schools.com/python/python_file_remove.asp
        os.remove("time.json")
        print(" ")
        print("The time value of this file is:")
        if geojson["type"] == "FeatureCollection":
            first = geojson["features"]  
            time = []
            for i in range(0,5):            
                try:
                    click.echo(first[i]["Date"])
                    time = first[i]["Date"]
                    return time
                except Exception as e:
                    try:
                        click.echo(first[i]["properties"]["creationDate"])
                        time = time[i]["properties"]["creationDate"]
                        return time
                    except Exception as e:
                        try:
                            click.echo(first[i]["date"])
                            time = first[i]["date"]
                            return time
                        except Exception as e:
                            try:
                                click.echo(first[i]["time"])
                                time = first[i]["time"]
                                return time
                            except Exception as e:
                                try:
                                    click.echo(first[i]["properties"]["date"])
                                    time = first[i]["properties"]["date"]
                                    return time
                                except Exception as e:
                                    try:
                                        click.echo(first[i]["properties"]["time"])
                                        time = first[i]["properties"]["time"]
                                        return time
                                    except Exception as e:
                                        try:
                                            click.echo(first[i]["properties"]["Date"])
                                            time = first[i]["properties"]["Date"]
                                            return time
                                        except Exception as e:
                                            click.echo("there is no time-value")
                                            return None   
            print(time)
            return time

if __name__ == '__main__':
    getTimeextend()lepath, detail):
    """returns the bounding Box GeoJson
    @param path Path to the file """
    if detail =='bbox':
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox
        click.echo(geojbbx)
        return geojbbx

    if detail == 'feature':
        geojson = pygeoj.load(filepath)
        #TO-DO feature.geometry.coordinates in variable speichern
        points = 0
        for feature in geojson:
            points = np.array(feature.geometry.coordinates)
            click.echo(points)
    #convex_hull(points)
    return points

def getNetCDFbbx(filepath, detail):
    """returns the bounding Box NetCDF
    @param path Path to the file """
    if detail =='bbox':
        ds = xr.open_dataset(filepath)
        try:
            lats = ds.coords["lat"]
            lons = ds.coords["lon"]

        except Exception as e:
            lats = ds.coords["latitude"]
            lons = ds.coords["longitude"]
        # print(ds.values)
        minlat=min(lats).values
        minlon=min(lons).values
        maxlat=max(lats).values
        maxlon=max(lons).values
        # Bounding Box Ausgabe in Schoen
        print("Min Latitude: ")
        print(type(minlat))
        print("Min Longitude: ")
        print(type(minlon))
        print("Max Latitude: ")
        print(maxlat)
        print("Max Longitude: ")
        print(maxlon)

        # Speicherung als bbox noch nicht so schoen, da Ausgabe als vier Arrays mit einem Wert
        bbox = [(minlat,minlon,maxlat,maxlon)]
        click.echo(bbox)

    if detail == 'feature':
        ds = xr.open_dataset(filepath)
        try:
            lats = ds.coords["lat"]
            lons = ds.coords["lon"]

        except Exception as e:
            lats = ds.coords["latitude"]
            lons = ds.coords["longitude"]
        print("Latitude:")
        print(lats.values)
        print("Longitude:")
        print(lons.values)
        #convex_hull(points)
        return 0

def getGeopackagebbx(filepath, detail):
    """returns the bounding Box Geopackage
    @param path Path to the file
    @see https://docs.python.org/2/library/sqlite3.html"""
    if detail =='bbox':
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT min(min_x), min(min_y), max(min_x), max(min_x)
                     FROM gpkg_contents""")
        row = c.fetchall()
        print(row)
    if detail == 'feature':
        conn = sqlite3.connect(filepath)
        c = conn.cursor()
        c.execute("""SELECT min_x,min_y
                     FROM gpkg_contents""")
        points = c.fetchall()
        print(points)
        #convex_hull(points)
        return points

def getIsobbx(filepath, detail):
    """@see http://manpages.ubuntu.com/manpages/trusty/man1/ogr2ogr.1.html"""
    if detail =='bbox':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        isobbx = (iso).bbox
        click.echo(isobbx)
        return isobbx

    if detail == 'feature':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        #TO-DO feature.geometry.coordinates in variable speichern
        points = 0
        for feature in iso:
            click.echo(feature.geometry.coordinates)
        #convex_hull(points)
        return points

if __name__ == '__main__':
    getMetadata()
