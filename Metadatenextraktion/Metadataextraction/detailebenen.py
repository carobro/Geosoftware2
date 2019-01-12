#import click, json, sqlite3, csv, pygeoj
#from osgeo import gdal, ogr, osr
#import pandas as pd
#import numpy as np
#import xarray as xr
#import os
import click
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getIsoInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, openFolder

"""global variable to save the bbox values of single files it is used for the boundingbox extraction of a whole folder"""
bboxArray = []
timeextendArray=[]

""" Advantage of our code is that the file extension is not important for the metadataextraction but the content of the file"""

@click.command(name='1')
@click.option('--path',required=True, help='please insert the path to the data here.')
#@click.option('--single', 'folder', flag_value='single', default=True, help='returns all the boundingboxes from objects of a folder')
#@click.option('--whole', 'folder', flag_value='whole', help='returns one overall boundingbox from all objects of a folder')
@click.option('--detail', type=click.Choice(['bbox', 'convexHull', 'time']), default='bbox', help='select which information you want to get')
@click.option('--folder', type=click.Choice(['single', 'whole']), default='single', help='select if you want to get the Metadata from the whole folder or for each seperate file.')

def getMetadata(path, detail, folder):
    #print(bboxArray)
    filepath = path
    # Program that extracts the boudingbox of files.

    try:
        #click.echo("detailShape")
        getShapefileInfo.getShapefilebbx(filepath, detail, folder)
    except Exception as e:
        try:
            print("This is no valid Shapefile.")
            #click.echo("detailjson")
            getGeoJsonInfo.getGeoJsonbbx(filepath, detail, folder)
        except Exception as e:
            #print (e)
            #return 0
            try:
                #click.echo("netcd")
                getNetCDFInfo.getNetCDFbbx(filepath, detail, folder)
            except Exception as e:
                try:
                    #print("cdf fehler")
                    #print(e)
                    #print("aussencsv")
                    #print("2")
                    getCSVInfo.getCSVbbx(filepath, detail, folder)
                except Exception as e:
                    try:
                        #print(e)
                        #print("aussengeop")
                        #click.echo("2")
                        getGeoPackageInfo.getGeopackagebbx(filepath, detail, folder)
                    except Exception as e:
                        try:
                            #click.echo("geop fehler:")
                            click.echo(e)
                            getGeoTiffInfo.getGeoTiffbbx(filepath, detail, folder)
                        except Exception as e:
                            try:
                                #click.echo("hhihihih")
                                getIsoInfo.getIsobbx(filepath, detail, folder)
                            except Exception as e:
                                print(e)
                                try:
                                    openFolder.openFolder(filepath, detail, folder)
                                except Exception as e:
                                    click.echo(e)
                                    #click.echo("2")
                                    click.echo ("invalid file format!!!!!")
                                    return 0
if __name__ == '__main__':
    getMetadata()
