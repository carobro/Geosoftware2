# author: Jannis

import numpy as np
import pandas as pd
import xarray as xr

# path to the file
filepath = '/home/jannis/Schreibtisch/Geosoft-II-2018_Testdaten/netCDF-die Gruppe 1/test_echam_spectral.nc'
ds = xr.open_dataset(filepath)
lats = ds.coords["lat"]
lons = ds.coords["lon"]
bbox = (min(lats), min(lons), max(lats), max(lons))
print("Bounding Box: ")
print(bbox)
