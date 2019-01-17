import math
import extractTool
import similar
import click
import os

"""Calls up all important fuctions and returns 
the final similarity score from two files
:param filepath1: filepath from a file
:param filepath2: filepath from a file
"""
def master(filepath1, filepath2):
    bbox1 = extractTool.getMetadata(filepath1, "bbox", "single", "time")
    bbox2 = extractTool.getMetadata(filepath2, "bbox", "single", "time")
    '''danach müssen wir uns nur die Werte rasupicken die wir haben wollen
    bbox1 = bbox1[0]
    bbox2 = bbox2[0]
    '''
    sim = similar.calcuateScore(bbox1, bbox2)
    score = similar.whatDataType(filepath1, filepath2, sim)

    print(score)
    return score