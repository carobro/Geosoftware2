import click, detailebenen
from osgeo import gdal, ogr, osr

def getGeoTiffbbx(filepath, detail, folder):
    gdal.UseExceptions()
    ds = gdal.Open(filepath)
    print("geotiff")
    """@see https://stackoverflow.com/questions/2922532/obtain-latitude-and-longitude-from-a-geotiff-file"""

    if detail =='bbox':
        """CRS Transformation"""
        #get the existing coordinate system
        old_cs= osr.SpatialReference()
        old_cs.ImportFromWkt(ds.GetProjectionRef())

        # create the new coordinate system
        wgs84_wkt = """
        GEOGCS["WGS 84",
            DATUM["WGS_1984",
                SPHEROID["WGS 84",6378137,298.257223563,
                    AUTHORITY["EPSG","7030"]],
                AUTHORITY["EPSG","6326"]],
            PRIMEM["Greenwich",0,
                AUTHORITY["EPSG","8901"]],
            UNIT["degree",0.01745329251994328,
                AUTHORITY["EPSG","9122"]],
            AUTHORITY["EPSG","4326"]]"""
        new_cs = osr.SpatialReference()
        new_cs .ImportFromWkt(wgs84_wkt)

        # create a transform object to convert between coordinate systems
        transform = osr.CoordinateTransformation(old_cs,new_cs)

        #get the point to transform, pixel (0,0) in this case
        width = ds.RasterXSize
        height = ds.RasterYSize
        gt = ds.GetGeoTransform()

        minx = gt[0]
        miny = gt[3] + width*gt[4] + height*gt[5]
        maxx = gt[0] + width*gt[1] + height*gt[2]
        maxy = gt[3]
        #get the coordinates in lat long
        latlongmin = transform.TransformPoint(minx,miny)
        latlongmax = transform.TransformPoint(maxx,maxy)
        bbox = [latlongmin[0], latlongmin[1], latlongmax[0], latlongmax[1]]
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("Filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the GeoTiff:")
            click.echo(bbox)
            print("----------------------------------------------------------------")
            return (bbox)
        if folder=='whole':
            detailebenen.bboxArray.append(bbox)
            click.echo(filepath)
            print(bbox)
            return (bbox)

    """second level of detail is not reasonable for geotiffs because they are rasterdata."""
    if detail == 'convexHull':
        click.echo('Sorry there is no second level of detail for geotiffs')
        #ds = gdal.Info(filepath)
        #return None
        #if ds!=null:
            #click.echo('Sorry there is no second level of detail for geotiffs')
        #else: 
            #return None

    if detail=='time':
        gdal.UseExceptions()
        click.echo("GeoTiff")
        if detail =='time':
            ds = gdal.Open(filepath)
            gdal.Info(ds)
            click.echo("there is no time value for GeoTIFF files")
            return None

if __name__ == '__main__':
    getGeoTiffbbx()