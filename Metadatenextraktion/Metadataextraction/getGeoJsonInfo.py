import click, pygeoj, detailebenen



def getGeoJsonbbx(filepath, detail, folder):
    """returns the bounding Box GeoJson
    @param path Path to the file """
    print(detail)
    print(folder)
    if detail =='bbox':
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox
        if folder=='single':
            click.echo(geojbbx)
        if folder=='whole':
            detailebenen.bboxSpeicher.append(geojbbx)
            print("halo")
            print(detailebenen.bboxSpeicher)
    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')


if __name__ == '__main__':
    getGeoJsonbbx()