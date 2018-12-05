import click, pygeoj



def getGeoJsonbbx(filepath, detail):
    """returns the bounding Box GeoJson
    @param path Path to the file """
    if detail =='bbox':
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox
        click.echo(geojbbx)

    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')


if __name__ == '__main__':
    getGeoJsonbbx()