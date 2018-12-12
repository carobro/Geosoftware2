import click,json, sqlite3, pygeoj, csv
from osgeo import gdal, ogr, osr
import pandas as pd
import detailebenen

#import ogr2ogr
#ogr2ogr.BASEPATH = "/home/caro/Vorlagen/Geosoftware2/Metadatenextraktion"

def getCSVbbx(filepath, detail, folder):
    """returns the bounding Box CSV
    @see https://www.programiz.com/python-programming/reading-csv-files
    @param path Path to the file """
    if detail == 'feature':
        df = pd.read_csv(filepath, delimiter=';',engine='python')
        listlat = ["Koordinate_Hochwert","lat","Latitude","latitude"]
        listlon = ["Koordinate_Rechtswert","lon","Longitude","longitude","lng"]
        if not intersect(listlat,df.columns.values) or not intersect(listlon,df.columns.values):
            #click.echo("No fitting header for latitudes or longitudes")
            output="No fitting header for latitudes or longitudes"
            print(output)
            return output 

        for x in listlat:
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
        if not intersect(listlat,df.columns.values)or not intersect(listlon,df.columns.values):
            #click.echo("No fitting header for latitudes or longitudes")
            output="No fitting header for latitudes or longitudes"
            print(output)
            return output 
        if folder=='single':
            for x in listlat:
                lats=df[x]
                for y in listlon:
                    lons=df[y]
                    print("Bounding Box: ")
                    bbox=[min(lons),min(lats),max(lons),max(lats)]
                    click.echo(bbox)
                    return bbox
        if folder=='whole':
            for x in listlat:
                lats=df[x]
                for y in listlon:
                    lons=df[y]
                    print("Bounding Box: ")
                    bbox=[min(lons),min(lats),max(lons),max(lats)]
                    click.echo(bbox)
                    detailebenen.bboxSpeicher.append(bbox)
                    print(detailebenen.bboxSpeicher)
                    return (bbox)

        
# Hilfsfunktion fuer csv fehlerbehandlung
def intersect(a, b):
     return list(set(a) & set(b))

