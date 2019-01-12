import click, pygeoj, detailebenen, json
from osgeo import ogr
from scipy.spatial import ConvexHull
#from geojson import Feature, Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon, GeometryCollection
import geojson as gj

def getGeoJsonbbx(filepath, detail, folder):
    """returns the bounding Box GeoJson
    @param path Path to the file """
    geojson = pygeoj.load(filepath)
    #new=gj.dumps(data, sort_keys=True)
    #print(new)

    if detail =='bbox':
        click.echo("hallo")
        geojson = pygeoj.load(filepath)
        click.echo("hu")
        #click.echo(str(geojson))
        geojbbx = (geojson).bbox
        #click.echo(geojbbx)
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the GeoJSON object:")
            click.echo(geojbbx)
            print("----------------------------------------------------------------")
            #return (geojbbx)
        if folder=='whole':
            detailebenen.bboxArray.append(geojbbx)
            click.echo(filepath)
            click.echo(geojbbx)
            print(detailebenen.bboxArray)
            print("ghgh")
            return(geojbbx)
            
    if detail == 'convexHull':
        print("geojsonfeature")
        geojson = pygeoj.load(filepath)
        point = list()
        print("pointlist")
        print(point)

        for feature in geojson:
            #print(point)
            print("coords")
            print(feature.geometry.coordinates)
            point.append(feature.geometry.coordinates)
            print("da")
            
        print(point)
        #calculation of the convex hull
        #funktioniert bisher nur bei jagdbezirke viersen...
        print("test")
        hull=ConvexHull(point)
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
            #print("ghgh")

    # After opening the file check if the file seems to have the right format
    # Then we search for words like date, creationDate or time at two different levels
    #print("GeoJsonTIMES")
    if detail =='time':
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
                                            return None 

        if folder=='single':   
            print("The time value of this file is:")     
            timemax = min(timelist)
            timemin = max(timelist)
            if timemax==timemin:
                click.echo(min(timelist))
            else:
                click.echo(min(timelist))
                click.echo(max(timelist))
            return timemax, timemin
        if folder=='whole':
            timeextend=[min(timelist), max(timelist)]
            detailebenen.timeextendArray.append(timeextend)
            print("timeextendArray:")
            print(detailebenen.timeextendArray)


if __name__ == '__main__':
    getGeoJsonbbx(filepath, detail, folder)