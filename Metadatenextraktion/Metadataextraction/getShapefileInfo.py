import click, shapefile, detailebenen

def getShapefilebbx(filepath, detail, folder):
    """returns the bounding Box Shapefile.
    @param path Path to the file """
    sf = shapefile.Reader(filepath)
    #just for debugging
    #print("shapefile")

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
            #adds the boundingbox of the shapefile to the bboxSpeicher array
            detailebenen.bboxSpeicher.append(output)

            #just for debugging -> delete in the end!
            click.echo(filepath)
            click.echo(output)
            return output
    if detail == 'feature':
        #sf = shapefile.Reader(filepath)
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')
        return 0

if __name__ == '__main__':
    getShapefilebbx()
