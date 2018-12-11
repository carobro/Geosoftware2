import click, pygeoj, detailebenen



def getGeoJsonbbx(filepath, detail, folder):
    """returns the bounding Box GeoJson
    @param path Path to the file """
    print(detail)
    print(folder)
    if detail =='bbox':
        geojson = pygeoj.load(filepath)
        geojbbx = (geojson).bbox
        click.echo(geojbbx)
        return geojbbx
        if folder=='single':
            click.echo(geojbbx)
        if folder=='whole':
            detailebenen.bboxSpeicher.append(geojbbx)
            print("halo")
            print(detailebenen.bboxSpeicher)
    if detail == 'feature':
        geojson = pygeoj.load(filepath)
        #TO-DO feature.geometry.coordinates in variable speichern
        points = 0
        for feature in geojson:
            click.echo(feature.geometry.coordinates)
    #convex_hull(points)
    return points

if __name__ == '__main__':
    getGeoJsonbbx()