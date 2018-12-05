import click, pygeoj
from osgeo import gdal, ogr, osr
#import ogr2ogr
#ogr2ogr.BASEPATH = "/home/caro/Vorlagen/Geosoftware2/Metadatenextraktion"

def getCSVbbx(filepath, detail):
    """returns the bounding Box CSV
    @see https://www.programiz.com/python-programming/reading-csv-files
    @param path Path to the file """
    if detail == 'feature':
        click.echo('hier kommt eine Ausgabe der Boundingbox eines einzelnen features hin.')
    if detail =='bbox':
        path = open(filepath)
        reader = csv.reader(path)
        contentfirst = next(reader)[0].replace(";", ",")
        content = contentfirst.split(",")
        print(content)

        #inhalt richtig in lng und lat speichern
        try:
            for x in content:
                if x == 'longitude':
                    lons = 'longitude'
                if x == "Longitude":
                    lons = "Longitude"
                if x == "lon":
                    lons = "lon"
                if x == "lng":
                    lons = "lng"
                if x == 'latitude':
                    lats = 'latitude'
                if x == "Latitude":
                    lats = "Latitude"
                if x == "lat":
                    lats = "lat"
            print(content)
            if(lats == None or lons == None):
                click.echo("There are no valid coordinates")
            
            print(content)

            for x in content:
                print ("hallo")
                if x != lons or x != lats:
                    try:
                        data = pd.read_csv(filepath, content=0)
                        getcoords(data)

                    except:     
                        data = pd.read_csv(filepath, content=0, sep=';')
                        getcoords(data)

        except Exception as e:
            click.echo ("No latitude,longitude")
            return None


def getcoords(data):
        lats = data[lng].tolist()
        lons = data[lat].tolist()
                
        bbox = [min(lons), min(lats), max(lons), max(lats)]
        click.echo(bbox)
        return bbox
        
if __name__ == '__main__':
    getCSVbbx()