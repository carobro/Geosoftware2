import click, shapefile, detailebenen
from scipy.spatial import ConvexHull

def getShapefilebbx(filepath, detail, folder):
    """returns the bounding Box Shapefile.
    @param path Path to the file """
    sf = shapefile.Reader(filepath)
    #just for debugging
    #print("shapefile")

    if detail =='bbox':
        
        output = sf.bbox
        #length=len(sf)
        #shapes=sf.shapes()
        #points=shapes[8].points
        #click.echo(points)
        #click.echo(length)

        click.echo(sf.shape(8))
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the Shapefile:")
            click.echo(output)
            print("----------------------------------------------------------------")
            return output
        if folder=='whole':
            #adds the boundingbox of the shapefile to the bboxSpeicher array
            detailebenen.bboxSpeicher.append(output)

            #just for debugging -> delete in the end!
            click.echo(filepath)
            click.echo(output)
            return output
            
    #calculation of the convex hull of the shapefile
    if detail == 'feature':
        shapes=sf.shapes()
        allPts=[]
        for z in shapes:
            points=z.points
            allPts=allPts+points
        hull=ConvexHull(allPts)
        hull_points=hull.vertices
        convHull=[]
        for y in hull_points:
            point=[allPts[y][0], allPts[y][1]]
            convHull.append(point)
        click.echo("convex hull:")    
        click.echo(convHull)
        return 0

if __name__ == '__main__':
    getShapefilebbx()
