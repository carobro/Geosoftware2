import click,json, sqlite3, pygeoj, csv
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import detailebenen
from scipy.spatial import ConvexHull

#import ogr2ogr
#ogr2ogr.BASEPATH = "/home/caro/Vorlagen/Geosoftware2/Metadatenextraktion"

def getCSVbbx(filepath, detail, folder):
    """returns the bounding Box CSV
    @see https://www.programiz.com/python-programming/reading-csv-files
    @param path Path to the file """
    click.echo("csv")
    CRSinfo = True
    df = pd.read_csv(filepath, delimiter=';',engine='python')
    listlat = ["Koordinate_Hochwert","lat","Latitude","latitude"]
    listlon = ["Koordinate_Rechtswert","lon","Longitude","longitude","lng"]
    listCRS = ["CRS","crs","Koordinatensystem","EPSG","Coordinate reference system", "coordinate system"]
    #tests if there is a column named Coordinatesystem or similar
    if not intersect(listCRS,df.columns.values):
        CRSinfo= False
        print("No fitting header for a reference system")

    if not intersect(listlat,df.columns.values) or not intersect(listlon,df.columns.values):
        output="No fitting header for latitudes or longitudes"
        print(output)
        #return output

    #returns the convex hull of the coordinates from the CSV object.
    if detail == 'feature':
        mylat=intersect(listlat,df.columns.values)
        mylon=intersect(listlon,df.columns.values)
        lats=df[mylat[0]]
        lons=df[mylon[0]]
        coords=np.column_stack((lats, lons))
        #definition and calculation of the convex hull
        hull=ConvexHull(coords)
        hull_points=hull.vertices
        convHull=[]
        for z in hull_points:
            point=[coords[z][0], coords[z][1]]
            convHull.append(point)
        if(CRSinfo):
            mycrsID=intersect(listCRS,df.columns.values)
            myCRS=df[mycrsID[0]]
            inputProj='epsg:'
            inputProj+=str(myCRS[0])
            print(inputProj)
            inProj = Proj(init=inputProj)
            outProj = Proj(init='epsg:4326')
            for z in coords:
                z[0],z[1] = transform(inProj,outProj,z[0],z[1])
        click.echo("convex Hull: ")
        click.echo(convHull)
        click.echo("csv")

    if detail =='bbox':
        # Using Pandas: http://pandas.pydata.org/pandas-docs/stable/io.html
        #if folder=='single':
        mylat=intersect(listlat,df.columns.values)
        mylon=intersect(listlon,df.columns.values)
        lats=df[mylat[0]]
        lons=df[mylon[0]]
        bbox=[min(lats),min(lons),max(lats),max(lons)]
        # CRS transformation if there is information about crs
        if(CRSinfo):
            mycrsID=intersect(listCRS,df.columns.values)
            myCRS=df[mycrsID[0]]
            inputProj='epsg:'
            inputProj+=str(myCRS[0])
            print(inputProj)
            inProj = Proj(init=inputProj)
            outProj = Proj(init='epsg:4326')
            lat1t,lng1t = transform(inProj,outProj,bbox[0],bbox[1])
            lat2t,lng2t = transform(inProj,outProj,bbox[2],bbox[3])
            bbox=[lat1t,lng1t,lat2t,lng2t]

        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the CSV object:")
            click.echo(bbox)
            print("----------------------------------------------------------------")
        if folder=='whole':
            #click.echo(bbox)
            click.echo(filepath)
            click.echo(bbox)
            detailebenen.bboxSpeicher.append(bbox)
            #print(detailebenen.bboxSpeicher)
            #return (bbox)
# Hilfsfunktion fuer csv fehlerbehandlung
def intersect(a, b):
     return list(set(a) & set(b))
