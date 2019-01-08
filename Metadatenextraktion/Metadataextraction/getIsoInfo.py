import click, json, sqlite3, csv, pygeoj, detailebenen
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import os
import ogr2ogr
#new for this module
import tempfile

def getIsobbx(filepath, detail, folder):
    gdal.UseExceptions()
    click.echo("iso")
    """@see http://manpages.ubuntu.com/manpages/trusty/man1/ogr2ogr.1.html"""
    if detail =='bbox':
        #HIER NOCH TEMPORAERE FILES ERSTELLEN
        #with tempfile.TemporaryFile() as folder:
            #click.echo("folder")
            #click.echo(folder)
        #d=folder
        fp=tempfile.TemporaryFile()
        #pa=tempfile.gettempdir()
        #ogr2ogr.main(["","-f", "GeoJSON", fp, filepath])
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        #ogr2ogr.main(["","-f","GeoJSON", folder])

        iso = pygeoj.load(filepath="out.json")
        isobbx = (iso).bbox
        if folder=='single':
            print("----------------------------------------------------------------")
            click.echo("filepath:")
            click.echo(filepath)
            click.echo("Boundingbox of the ISO object:")
            click.echo(isobbx)
            print("----------------------------------------------------------------")
            os.remove("out.json")
            #return isobbx
        if folder=='whole':
            detailebenen.bboxSpeicher.append(isobbx)
            click.echo(filepath)
            click.echo(isobbx)
            #return (isobbx)


    if detail == 'feature':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")
        #TO-DO feature.geometry.coordinates in variable speichern
        points = 0
        point = list()
        for feature in iso:
            point.append(feature.geometry.coordinates)
        #convex_hull(points)
        print point
        os.remove("out.json")
        return point

if __name__ == '__main__':
    getIsobbx()