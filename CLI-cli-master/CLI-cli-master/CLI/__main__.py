from osgeo import gdal
import pandas as pd

def getMetaData(path):

    # connect path to file
    filepath = "%s\%s" % (path, name)
      
    switcher = {
        1: gdalinfo(filepath),             
        2: pd.read_csv(filepath),         

    }
    print switcher.get(path, click.echo("type %s not supported" % filepath))

if __name__ == '__main__':
    getMetaData()
