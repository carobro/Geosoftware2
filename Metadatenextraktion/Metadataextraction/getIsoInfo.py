import click, json, sqlite3, csv, pygeoj, detailebenen
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import ogr2ogr
#new for this module
import tempfile
from scipy.spatial import ConvexHull
import geojson

#https://gis.stackexchange.com/questions/130963/write-geojson-into-a-geojson-file-with-python

def write_json(self, features):
   # feature is a shapely geometry type
   geom_in_geojson = geojson.Feature(geometry=features, properties={})
   tmp_file = tempfile.mkstemp(suffix='.geojson')
   with open(tmp_file[1], 'w') as outfile:
      geojson.dump(geom_in_geojson, outfile)
   return tmp_file[1]

def getIsobbx(filepath, detail, folder):
    gdal.UseExceptions()
    click.echo("iso")
    """@see http://manpages.ubuntu.com/manpages/trusty/man1/ogr2ogr.1.html"""
    if detail =='bbox':
        #HIER NOCH TEMPORAERE FILES ERSTELLEN
        #with tempfile.TemporaryFile() as folder:
            #click.echo("folder")
            #click.echo(folder)
        #d=folder
        fp=tempfile.TemporaryFile()
        #pa=tempfile.gettempdir()
        #ogr2ogr.main(["","-f", "GeoJSON", fp, filepath])
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        #ogr2ogr.main(["","-f","GeoJSON", folder])

        iso = pygeoj.load(filepath="out.json")
        isobbx = (iso).bbox
        # Identification of CRS and transformation
        # In some test data the epsg id was stored in an unicode object like this one'urn:ogc:def:crs:EPSG::4258'
        try:
            isocrs = (iso).crs
            mycrs= isocrs["properties"]["name"]
            print(mycrs)
            mycrsString=mycrs.encode('ascii','ignore')
            # Extracting the epsg id
            mySplit= mycrsString.split(':')
            CRSID=mySplit[len(mySplit)-1]
            # Especially the KML data files have this id, which is wgs84
            # No need to transform
            if (CRSID=="CRS84" or CRSID == 4326):
                mybbx=[isobbx[0],isobbx[1],isobbx[2],isobbx[3]]
            else:
                lat1t,lng1t=detailebenen.transformToWGS84(isobbx[0],isobbx[1],CRSID)
                lat2t,lng2t=detailebenen.transformToWGS84(isobbx[2],isobbx[3],CRSID)
                mybbx=[lat1t,lng1t,lat2t,lng2t]
        except:
            print("While splitting the string an error occurred")

        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the ISO object:")
            click.echo(mybbx)
            print("----------------------------------------------------------------")
            os.remove("out.json")
            #return isobbx
        if folder=='whole':
            detailebenen.bboxArray.append(isobbx)
            click.echo(filepath)
            click.echo(mybbx)
            #return (isobbx)


    if detail == 'convexHull':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        #TO-DO feature.geometry.coordinates in variable speichern
        points = 0
        point = list()
        for feature in iso:
            print("looop")
            print(len(feature.geometry.coordinates))
            point.append(feature.geometry.coordinates)
            print(point)
        print(point)
        #calculation of the convex hull
        #funktioniert bisher nur bei jagdbezirke viersen...
        #print("test")
        hull=ConvexHull(point)
        print("after hull")
        print(hull)
        hull_points=hull.vertices
        print(hull_points)
        print(point[0])
        convHull=[]
        for z in hull_points:
            hullcoord=[point[z][0], point[z][1]]
            convHull.append(hullcoord)
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Convex hull of the GeoJSON object:")
            click.echo(convHull)
            print("----------------------------------------------------------------")
        if folder=='whole':
            print("----------------------------------------------------------------")
            print("----------------------------------------------------------------")
            detailebenen.bboxArray.append(convHull)
            click.echo("convex hull whole")
            click.echo(convHull)
            print(detailebenen.bboxArray)
        #convex_hull(points)
        #print point
        os.remove("out.json")
        return point

    # We transform the gml file to a geojson file, then search for
    # words like "date", "timestamp", "time" and collect them
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
                                            click.echo("there is no time-value ISO")
                                            return None   
            print(time)
            return time



if __name__ == '__main__':
    getIsobbx()
