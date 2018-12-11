import click, shapefile, sqlite3, csv, pygeoj
from osgeo import gdal, ogr, osr
import pandas as pd
import numpy as np
import xarray as xr
import ogr2ogr

@click.command()
@click.option('--path', prompt='Datapath', help='Path to the data.')
@click.option('--time', 'detail', flag_value='time', default=True)

def getTimeextend(path, detail):
    filepath = path
    # Program that extracts the time-extend of files.

    try:
        getShapefiletime(filepath, detail)
    except Exception as e:
        try:
            getCSVtime(filepath, detail)
        except Exception as e:
            try:
                getGeoJsontime(filepath, detail)
            except Exception as e:
                try:
                    getNetCDFtime(filepath, detail)
                except Exception as e:
                    try:
                        getGeopackagetime(filepath, detail)
                    except Exception as e:
                        try: 
                            getGeoTifftime(filepath, detail)    
                        except Exception as e:
                            click.echo ("invalid file format or no time-values included!")

def getShapefiletime(filepath, detail):
    click.echo(detail)
    if detail =='time':
        sf = shapefile.Reader(filepath)
        output = sf.time
        click.echo(output)

def getGeoTifftime(filepath, detail):
    if detail =='time':
        ds =  gdal.Open(filepath)
        print(gdal.Info(ds))
        click.echo("Sorry there is no time-value")
        return None

def getCSVtime(filepath, detail):
    if detail =='time':
        # Using Pandas: http://pandas.pydata.org/pandas-docs/stable/io.html
        df = pd.read_csv(filepath, delimiter=';',engine='python')
        listtime = ["time", "timestamp", "date", "Time"]
        print("test")
        if not intersect(listtime,df.columns.values):
            print("No fitting header for time-values")
            # TODO: fehlerbehandlung  

        print("test2")
        for t in listtime:
            if(x not in df.columns.values):
                click.echo("This file does not include time-values")
            else:
                time=df[t]
                timeextend =[min(time), max(time)]
                click.echo(timeextend)
                return timeextend

    """
    except Exception as e:
        click.echo ("There is no time-value or invalid file")
        return None
        """
        
def getGeoJsontime(filepath, detail):
    if detail =='time':
        geojson = pygeoj.load(filepath)
        print(geojson.common_attributes)
        print("hallo")
        data = json_decode(filepath)
        click.ech(data)
        try:
            click.echo(data['time'])
        except Exception as e:
            try:
                click.echo(data['timestamp'])
            except Exception as e:
                try:
                    click.echo(data['Time'])
                except Exception as e:
                    try:
                        click.echo(data['time'])
                    except Exception as e:
                        click.echo("error")
        click.echo("Sorry there is no time-value")

def getNetCDFtime(filepath, detail):
    """returns the Time from NetCDF file
    @param path Path to the file """
    if detail =='time':
        ds = xr.open_dataset(filepath)
        mytime = ds.coords["time"]
        # print(ds.values)
        starttime = min(mytime)
        endtime = max(mytime)
        # Zeitliche Ausdehnung
        anfang = starttime.values
        ende = endtime.values
        print(anfang)
        print(ende)
        return anfang, ende
    
def getGeopackagetime(filepath, detail):
    if detail =='time':
        conn = sqlite3.connect(filepath)
        print(conn)
        c = conn.cursor()
        # try: weil last_change unlogisch ist. Alternative finden!
        c.execute("""SELECT last_change
                    FROM gpkg_contents""")
        print c.fetchone()
        row = c.fetchall()
        print(row)

def getIsoTime(filepath, detail):
    if detail =='time':
        ogr2ogr.main(["","-f", "GeoJSON", "out.json", filepath])
        iso = pygeoj.load(filepath="out.json")

if __name__ == '__main__':
    getTimeextend()