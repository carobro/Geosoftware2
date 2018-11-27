"""https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module"""
import csv
from collections import defaultdict
import sys, argparse, csv

def getCSVBoundingBox(name, path):

filepath = "%s\%s" % (path, name)
""" https://docs.python.org/2/library/os.path.html """
f_extension = os.path.splitext(filepath)

if f_extension == ".csv" or f_extension == ".txt":
    try:
        """Hier fehlt was"""

else 
 click.echo("Invalid File")
 return None