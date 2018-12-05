import click, shapefile

def getShapefilebbx(filepath, detail):
    """returns the bounding Box Shapefile.
    @param path Path to the file """
    if detail =='bbox':
        sf = shapefile.Reader(filepath)
        output = sf.bbox
        click.echo(output)
    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')

if __name__ == '__main__':
    getShapefilebbx()