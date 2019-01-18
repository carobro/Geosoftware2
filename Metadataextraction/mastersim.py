import math
import extractTool
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder
import similar
import click
import os

"""Calls up all important fuctions and returns 
the final similarity score from two files
:param filepath1: filepath from a file
:param filepath2: filepath from a file
"""
def master(filepath1, filepath2):
    print(filepath1)
    print(filepath2)
    first = extractTool.getMetadata(filepath1, 'bbox', 'single', True)
    second = extractTool.getMetadata(filepath2, 'bbox', 'single', True)
    print("Hier bin ich")
    '''danach muessen wir uns nur die Werte rausupicken die wir haben wollen'''
    print('-----------------')
    print first
    print('------------------')
    #bbox1 = firstBbox[0][1]
    #bbox2 = secondBbox[0][1]
    #@Caro: Hier verkettest du einen String mit einer liste. Das geht anscheinend nicht.
    #Falls du die Ausgabe unbedingt haben moechtest, dann kannst du das ja nochmal googlen.
    #Aber eigentlich ist die ja nicht so wichtig...
    #print("BoundingBox from"+ filepath1 + ":" + bbox1)
    #print("BoundingBox from"+ filepath2 + ":" + bbox2)
    sim = similar.calcuateScore(first, second)
    score = similar.whatDataType(filepath1, filepath2, sim)

    print(score)
    return score