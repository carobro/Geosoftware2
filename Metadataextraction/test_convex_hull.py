"""File for testing the convex hull"""
import os
import getGeoJsonInfo

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

#def test_featureShape():
#    assert getShapefileInfo.getShapefilebbx(__location__+'/testdata/Abgrabungen_Kreis_Kleve_shapefile/Abgrabungen_Kreis_Kleve_Shape.shp', 'feature', 'single', False) == 0
print(__location__)
testbbx = getGeoJsonInfo.getGeoJsonbbx('/home/jannis/Schreibtisch/aasee.geojson','convexHull', 'single', False)
print("________________________________________________")
print(getGeoJsonInfo.point)

def test_Logic():
    assert 1 !=0
