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
    CRSinfo = True
    df = pd.read_csv(filepath, delimiter=';',engine='python')
    listlat = ["Koordinate_Hochwert","lat","Latitude","latitude"]
    listlon = ["Koordinate_Rechtswert","lon","Longitude","longitude","lng"]
    listCRS = ["CRS","crs","Koordinatensystem","EPSG","Coordinate reference system", "coordinate system"]
    if not intersect(listCRS,df.columns.values):
        CRSinfo= False
        print("No fitting header for a reference system")

    if not intersect(listlat,df.columns.values) or not intersect(listlon,df.columns.values):
        #click.echo("No fitting header for latitudes or longitudes")
        output="No fitting header for latitudes or longitudes"
        print(output)
        #return output

    if detail == 'feature':
        for x in listlat:
            lats=df[x]
            for y in listlon:
                lons=df[y]
                print("All Points")
                points=[lons, lats]
                click.echo(points)
                #conhex_hull(points)
                #return points
        #return 0

    if detail =='bbox':
        # Using Pandas: http://pandas.pydata.org/pandas-docs/stable/io.html
        if folder=='single':
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
            print(bbox)
        if folder=='whole':
            for x in listlat:
                lats=df[x]
                for y in listlon:
                    lons=df[y]
                    #print("Bounding Box: ")
                    bbox=[min(lons),min(lats),max(lons),max(lats)]

                    #click.echo(bbox)
                    click.echo(filepath)
                    click.echo(bbox)
                    detailebenen.bboxSpeicher.append(bbox)
                    #print(detailebenen.bboxSpeicher)
                    #return (bbox)
# Hilfsfunktion fuer csv fehlerbehandlung
def intersect(a, b):
     return list(set(a) & set(b))
