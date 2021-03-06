import click, pygeoj, extractTool, json
import dateparser
from osgeo import ogr
from scipy.spatial import ConvexHull
import geojson as gj


point = list()

#in diese methode muss ein feature.geometry.coordinates wert eingefuegt werden.
def extract_coordinates(geoj):
    if (len(geoj)==2) and (type(geoj[0])==int or type(geoj[0])==float):
        new_point=[geoj[0], geoj[1]]
        point.append(geoj)
        return new_point
    else:
        for z in geoj:
            extract_coordinates(z)
    


def getGeoJsonbbx(filepath, detail, folder, time):
    """returns the bounding Box GeoJson
    @param path Path to the file 

    As mentioned in the geojson specification the standard crs is wgs84.
    https://tools.ietf.org/html/rfc7946#section-4"""
    #TODO
    #pygeoj only works with two-dimensional coordinates
    geojson = pygeoj.load(filepath)

    if detail =='bbox':
        click.echo("geojson bbox")
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the GeoJSON object:")
            click.echo(geojbbx)
            print("----------------------------------------------------------------")
            extractTool.ret_value.append(geojbbx)
        if folder=='whole':
            print("geojson bbox whole")
            extractTool.bboxArray.append(geojbbx)
            click.echo(filepath)
            click.echo(geojbbx)
            print(extractTool.bboxArray)
        #return(geojbbx)

    else:
        extractTool.ret_value.append([None])  

    if detail == 'convexHull':
        print("geojson convexHull")
        geojson = pygeoj.load(filepath)
        #point = list()

        
        for feature in geojson:
            try:
                r= feature.geometry.coordinates
                extract_coordinates(r)
            except Exception:
                #TODO
                #hier besser raise exception?!
                print("There is a feature without coordinates in the geojson.")
            
        #calculation of the convex hull
        hull=ConvexHull(point)
        hull_points=hull.vertices
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
            extractTool.ret_value.append(convHull)
        if folder=='whole':
            print("----------------------------------------------------------------")
            extractTool.bboxArray=extractTool.bboxArray+convHull
            click.echo("convex hull whole")
            click.echo(convHull)
            print(extractTool.bboxArray)
    else:
        extractTool.ret_value.append([None])  

    # After opening the file check if the file seems to have the right format
    # Then we search for words like date, creationDate or time at two different levels
    #print("GeoJsonTIMES")
    if (time):
        ds = open(filepath)
        geojson = json.load(ds)
        timelist = list()
        if geojson["type"] == "FeatureCollection":
            first = geojson["features"]
            for time in geojson: 
                try:
                    #click.echo(first[0]["Date"])
                    time = first[0]["Date"]
                    timelist.append(time)
                except Exception as e:
                    try:
                        #click.echo(first[0]["creationDate"])
                        time = time[0]["creationDate"]
                        timelist.append(time)
                    except Exception as e:
                        try:
                            #click.echo(first[0]["date"])
                            time = first[0]["date"]
                            timelist.append(time)
                        except Exception as e:
                            try:
                                #click.echo(first[0]["time"])
                                time = first[0]["time"]
                                timelist.append(time)
                            except Exception as e:
                                try:
                                    #click.echo(first[0]["properties"]["date"])
                                    time = first[0]["properties"]["date"]
                                    timelist.append(time)
                                except Exception as e:
                                    try:
                                        #click.echo(first[0]["properties"]["time"])
                                        time = first[0]["properties"]["time"]
                                        timelist.append(time)
                                    except Exception as e:
                                        try:
                                            #click.echo(first[0]["geometry"][0]["properties"]["STAND_DER_DATEN"])
                                            time = first[0]["geometry"][0]["properties"]["STAND_DER_DATEN"]
                                            timelist.append(time)
                                        except Exception as e:
                                            click.echo("there is no time-value")
                                            extractTool.ret_value.append([None])
                                            if folder=='single': 
                                                print(extractTool.ret_value)
                                                return extractTool.ret_value
                                            if folder=='whole':
                                                return None

        timemax = str(max(timelist))
        timemin = str(min(timelist))
        timemax_formatted=dateparser.parse(timemax)
        timemin_formatted=dateparser.parse(timemin)

        if folder=='single':   
            print("The time value of this file is:")     
            if timemax==timemin:
                #timeextend=[timemax_formatted, timemin_formatted]
                #extractTool.ret_value.append(timeextend)
                print(timemin_formatted)
            else:
                click.echo(timemin_formatted)
                click.echo(timemax_formatted)
            extractTool.ret_value.append([timemax_formatted, timemin_formatted]) 

        if folder=='whole':
            timeextend=[timemin_formatted, timemax_formatted]
            extractTool.timeextendArray.append(timeextend)
            print("timeextendArray:")
            print(extractTool.timeextendArray)
    else:
        extractTool.ret_value.append([None]) 
    if folder=='single':
        print(extractTool.ret_value)        
        return extractTool.ret_value


if __name__ == '__main__':
    getGeoJsonbbx(filepath, detail, folder)