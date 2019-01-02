import click, shapefile, detailebenen

def getShapefilebbx(filepath, detail, folder):
    """returns the bounding Box Shapefile.
    @param path Path to the file """
    #print(detailebenen.bboxSpeicher)
    if detail =='bbox':
        sf = shapefile.Reader(filepath)
        output = sf.bbox
        #click.echo(output)
        if folder=='single':
            click.echo(output)
        if folder=='whole':
            click.echo(output)
            detailebenen.bboxSpeicher.append(output)
            print(detailebenen.bboxSpeicher)
    if detail == 'feature':
        sf = shapefile.Reader(filepath)
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')
        return 0

if __name__ == '__main__':
    getShapefilebbx()
