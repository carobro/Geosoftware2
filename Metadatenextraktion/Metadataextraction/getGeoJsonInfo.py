import click, pygeoj, detailebenen, geojson, json
from osgeo import ogr
from scipy.spatial import ConvexHull

def getGeoJsonbbx(filepath, detail, folder):
    """returns the bounding Box GeoJson
    @param path Path to the file """
    points = 0
    print("geojson")
    if detail =='bbox':
        #nur ein testentwurf
        #funktioniert noch nicht. Was machen wir mit 3d Koordinaten?
        #falls wir die akzeptieren wollen: Dann so wie bei der feature ebene
        with open (filepath, "r") as myfile:
            data=myfile.read()

        dataset = json.loads(data)
        t=0
        min1=[]
        min2=[]
        max1=[]
        max2=[]
        for f in (dataset["features"]):
            t=t+1
            print(t)
            print(len(dataset["features"]))
            print("hi")
            c = f["geometry"]["coordinates"][0]
            c1 = [x[0] for x in c] # first coordinate
            print(c1)
            c2 = [x[1] for x in c]
            print(c2)
            print("box")
            #bbox = [[min(c1),min(c2)],[min(c1),max(c2)],[max(c1),max(c2)],[max(c1),min(c2)]]
            min1.append(min(c1))
            min2.append(min(c2))
            max1.append(max(c1))
            max2.append(max(c2))
            #click.echo(bbox)
        bbox=[[min(min1), min(min2)], [max(max1), max(max2)]]
        print("box")
        print(bbox)
        #return bbox

        #bis hierhin nur ein TEst gewesen!
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox
        #click.echo(geojbbx)
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the GeoJSON object:")
            click.echo(geojbbx)
            print("----------------------------------------------------------------")
            return (geojbbx)
        if folder=='whole':
            detailebenen.bboxSpeicher.append(geojbbx)
            click.echo(filepath)
            click.echo(geojbbx)
            #print(detailebenen.bboxSpeicher)
            return(geojbbx)
            
    if detail == 'feature':
        geojson = pygeoj.load(filepath)
        point = list()

        for feature in geojson:
            point.append(feature.geometry.coordinates)

        # calculation of the convex hull
        #funktioniert bisher nur bei jagdbezirke viersen...
        hull=ConvexHull(point[0][0])
        hull_points=hull.vertices
        convHull=[]
        for z in hull_points:
            hullcoord=[point[0][0][z][0], point[0][0][z][1]]
            convHull.append(hullcoord)
        print("convHull:")
        print(convHull)
        return point

if __name__ == '__main__':
    getGeoJsonbbx()