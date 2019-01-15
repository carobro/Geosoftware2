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
import geojson as gj

#https://gis.stackexchange.com/questions/130963/write-geojson-into-a-geojson-file-with-python

point=list()
#in diese methode muss ein feature.geometry.coordinates wert eingefuegt werden.
def extract_coordinates(geoj):
    if (len(geoj)==2) and (type(geoj[0])==int or type(geoj[0])==float):
        new_point=[geoj[0], geoj[1]]
        point.append(geoj)
        return new_point
    else:
        for z in geoj:
            extract_coordinates(z)


#without this function getIsobbx would open a folder and extract metadata the wrong way.
def is_folder_check(filepath):
    is_folder=False
    try:
        os.listdir(filepath)
        is_folder=True
    except Exception:
        pass
    return is_folder

def getIsobbx(filepath, detail, folder):
    gdal.UseExceptions()
    click.echo("iso")
    value=is_folder_check(filepath)

    if (is_folder_check(filepath)):
        raise Exception ("This is a folder! ------> first opening it")
    
    ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
    print("nochda")
    """@see http://manpages.ubuntu.com/manpages/trusty/man1/ogr2ogr.1.html"""
    if detail =='bbox':
        print("hi")
        #HIER NOCH TEMPORAERE FILES ERSTELLEN
        #fp=tempfile.TemporaryFile()
        #content=open(filepath, 'r')
        #iso_content=content.read()
        #print(iso_content)
        #tmp_file = tempfile.TemporaryFile(suffix='.geojson', prefix='help')
        #print("tmo")
        #print(tmp_file)
        #print("1")
        #tmp_file.write(iso_content)
        #print("2")
        #tmp_file.seek(0)
        #print(tmp_file.read())
        #print("3")
        #inhalt=tmp_file.read()
        #print("Inhalt:")
        #print(inhalt)

       
        #print("hu")
        #ogr2ogr.main(["","-f", "GeoJSON","out.json", filepath])
        #print("huhu")
        #ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        #ogr2ogr.main(["","-f", "GeoJSON", tmp_file, filepath])
        try:
            iso = pygeoj.load(filepath="out.json")
        except Exception as e:
            #print(e)
            raise Exception("Sorry! The ISO file is too big.")
        print("nach ist")
        isobbx = (iso).bbox
        print("w")
        # Identification of CRS and transformation
        # In some test data the epsg id was stored in an unicode object like this one'urn:ogc:def:crs:EPSG::4258'
        try:
            isocrs = (iso).crs
            mycrs= isocrs["properties"]["name"]
            print("mycrs")
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
            print("----------------------------------------------------------------")
            click.echo("filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the ISO object:")
            click.echo(mybbx)
            print("----------------------------------------------------------------")
            detailebenen.bboxArray.append(mybbx)
            click.echo(filepath)
            click.echo(mybbx)
            print("ho")
            #return (isobbx)


    if detail == 'convexHull':
        print("conv iso")
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        #TO-DO feature.geometry.coordinates in variable speichern
        #points = 0
        for feature in iso:
            try:
                f=feature.geometry.coordinates
                extract_coordinates(f)
            except Exception:
                #TODO
                #hier besser raise exception?!
                print("There is a feature without coordinates in the iso file")
            #point.append(feature.geometry.coordinates)
            #print(point)
        #print(point)
        #calculation of the convex hull
        print("hull")
        hull=ConvexHull(point)
        hull_points=hull.vertices
        print(hull_points)
        convHull=[]
        print("afterhull")
        for z in hull_points:
            hullcoord=[point[z][0], point[z][1]]
            convHull.append(hullcoord)
            print("in hull_points_loop")
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Convex hull of the ISO object:")
            click.echo(convHull)
            print("----------------------------------------------------------------")
        if folder=='whole':
            print("----------------------------------------------------------------")
            detailebenen.bboxArray=detailebenen.bboxArray+convHull
            #detailebenen.bboxArray.append(convHull)
            click.echo("convex hull whole")
            click.echo(convHull)
            print("bboxArray")
            print(detailebenen.bboxArray)
            print("----------------------------------------------------------------")
        os.remove("out.json")
        #iso.close()
        return point

    # We transform the gml file to a geojson file, then search for
    # words like "date", "timestamp", "time" and collect them
    if detail =='time':
        try:
            ogr2ogr.main(["","-f", "GeoJSON", "time.json", filepath])
        except Exception as a:
            print (a)
        iso = open("time.json")
        print("DRINNEN")
        geojson = json.load(iso)
        print("nach load")
        # @see https://www.w3schools.com/python/python_file_remove.asp
        os.remove("time.json")
        print("nach remove")
        if geojson["type"] == "FeatureCollection":
            #print(geojson["features"][0][])
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
                                            try:
                                                click.echo(first[i]["timeStamp"])
                                                time = first[i]["timeStamp"]
                                                return time
                                            except Exception as e:
                                                #this exception is important for folder time extraction of cvs files...DONT DELETE IT!
                                                raise Exception ("There is no time-value ISO")
                                                click.echo("there is no time-value ISO")
                                                return None   
            
            print("The time value of this ISO file is:")
            print(time)
            return time



if __name__ == '__main__':
    getIsobbx()
