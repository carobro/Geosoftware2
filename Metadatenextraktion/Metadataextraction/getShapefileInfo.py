import click
import shapefile
import detailebenen
from scipy.spatial import ConvexHull

def getShapefilebbx(filepath, detail, folder):
    """Extracts metadata from shapefiles.

    :param filepath: Path to the file
    :param detail: bbox, convexHull or time
    :param folder: whole or single
    :return: selected detail of the shapefile
    """

    #if the file is a valid shapefile it will be opened with this function.
    #otherwise an exception will be thrown.
    sf = shapefile.Reader(filepath)

    if detail =='bbox':
        output = sf.bbox
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the Shapefile:")
            click.echo(output)
            print("----------------------------------------------------------------")
            return output
        if folder=='whole':
            #adds the boundingbox of the shapefile to the bboxArray
            detailebenen.bboxArray.append(output)
        return output
            
    #calculation of the convex hull of the shapefile
    if detail == 'convexHull':
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
        if folder =='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("The convex hull of the Shapefile is:")    
            click.echo(convHull)
            print("----------------------------------------------------------------")
        if folder=='whole':
            detailebenen.bboxArray=detailebenen.bboxArray+convHull
            click.echo(detailebenen.bboxArray)
        return convHull

    #returns information about not existing timevalues for shapefiles.
    if detail=='time':
        echo="There is no timevalue for Shapefiles"
        click.echo(echo)
        return echo
if __name__ == '__main__':
    getShapefilebbx()
