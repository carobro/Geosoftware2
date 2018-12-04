# author: Jannis

import numpy as np
import pandas as pd
import xarray as xr

# path to the file
filepaths = ['/home/jannis/Schreibtisch/Geosoft-II-2018_Testdaten/netCDF-die Gruppe 1/cami_0000-09-01_64x128_L26_c030918.nc',
'/home/jannis/Schreibtisch/Geosoft-II-2018_Testdaten/netCDF-die Gruppe 1/ECMWF_ERA-40_subset.nc',
'/home/jannis/Schreibtisch/Geosoft-II-2018_Testdaten/netCDF-die Gruppe 1/sresa1b_ncar_ccsm3-example(1).nc',
'/home/jannis/Schreibtisch/Geosoft-II-2018_Testdaten/netCDF-die Gruppe 1/test_echam_spectral.nc',
'/home/jannis/Schreibtisch/Geosoft-II-2018_Testdaten/netCDF-die Gruppe 1/tos_O1_2001-2002.nc']

for x in filepaths:
    ending=x.split("/")
    ds = xr.open_dataset(x)
    print(ending[len(ending)-1])
    try:
        lats = ds.coords["lat"]
        lons = ds.coords["lon"]

    except Exception as e:
        lats = ds.coords["latitude"]
        lons = ds.coords["longitude"]
    mytime = ds.coords["time"]
    # print(ds.values)
    minlat=min(lats).values
    minlon=min(lons).values
    maxlat=max(lats).values
    maxlon=max(lons).values
    starttime=min(mytime)
    endtime=max(mytime)
    # Bounding Box:
    """print("Min Latitude: ")
    print(minlat)
    print("Min Longitude: ")
    print(minlon)
    print("Max Latitude: ")
    print(maxlat)
    print("Max Longitude: ")
    print(maxlon)
    """
    bbox=[minlat,minlon,maxlat,maxlon]
    print(bbox)

    print("-------------------------------------------------")

    # Zeitliche Ausdehnung
    print("Timestamp: ")
    print(starttime.values)
    print(endtime.values)
    print("__________________________________________________")
