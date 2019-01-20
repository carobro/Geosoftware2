import math
import extractTool
import click
# import typ 

# Beispielkoordinaten
# bbox1 = [5.8663155, 47.270111, 15.041932 , 55.099159]
# bbox2 = [7.5234, 52.0326, 7.7556, 52.152]

# def mastersim(filepath):
    # bbox1 = detailebenen(filepath) blabla Hier muessen die Bboxen berechet werden
    # bbox2 = detailebee(filepath) blabla also detailebenen Aufrufen
    # sim = aehnlickeit(bbox1, bbox2)
    # Hier muss typ.py
    # input1 = typ.getTyp(filepath)
    # input2 = typ.getTyp(filepath)
    # whatDataType(input1, input2, sim)

"""
Function to apply data type similarity on the similarity score

:param input1: filepath from a file
:param input2: filepath from a file
:param sim: spatial similarity score of two bounding boxes including the similarity of the data type
"""
def whatDataType(input1, input2, sim):
    if input1 == "raster" and input2 == "raster":
        click.echo("These files are rasterdata")
        return sim
    if input1 == "vector" and input2 == "vector":
        click.echo("These files are vectordata")
        return sim
    if input1 == "raster" and input2 == "vector" or input1 == "vector" and input2 == "raster":
        click.echo("These files are not the same datatype")
        sim = sim*5/4
        if sim > 1:
            sim = 1
        return sim

"""
Function to calculate the similarity score based on the spatial similarity
for a more detailed explanation look at: https://github.com/carobro/Geosoftware2/blob/master/Informationen_Allgemein/SimilarityCalculation.md#%C3%A4hnlichkeitsberechnung-version-2

:param bbox1: Bounding Box from a file
:param bbox2: Bounding Box from a file
:returns: similarity score from the two Bounding Boxes
"""
def aehnlickeit (bbox1,bbox2):
    
    if isinstance(bbox1[0], float) and isinstance(bbox1[1], float) and isinstance(bbox1[2], float) and isinstance(bbox1[3], float):
        if isinstance(bbox2[0], float) and isinstance(bbox2[1], float) and isinstance(bbox2[2], float) and isinstance(bbox2[3], float):

            if distance(bbox1,bbox2) < 20000:
                simdis = distance(bbox1,bbox2)/20000
            else:
                simdis = 1
            if abs(area(bbox1) - area(bbox2)) < 1000000:
                simA = (abs(area(bbox1) - area(bbox2)))/1000000
            else:
                simA = 1
            sim = (2 * simdis + simA)/3
            print(sim)
            return sim
        
    else:
        return None

"""
Function to calculate the mean latitude

:param bbox: bounding box of a file with the format: ['minlon', 'minlat', 'maxlon', 'maxlat']
:returns: the mean Latitude
"""
def meanLatitude (bbox):
    lat = (bbox[3]+bbox[1])/2
    return lat

"""
Function to calculate the mean longitude

:param bbox: bounding box of a file with the format: ['minlon', 'minlat', 'maxlon', 'maxlat']
:returns: the mean Longitude
"""
def meanLongitude (bbox):
    lon = (bbox[2]+bbox[0])/2
    return lon

"""
Function to calculate the width of the bounding box

:param bbox: bounding box of a file with the format: ['minlon', 'minlat', 'maxlon', 'maxlat']
:returns: the mean width of the bounding box (in km)
"""
def width (bbox):
    x = (bbox[2]-bbox[0])*111.3 * (math.cos(meanLatitude(bbox)*math.pi/180))
    return x

"""
Function to calculate the length of the bounding box

:param bbox: bounding box of a file with the format: ['minlon', 'minlat', 'maxlon', 'maxlat']
:returns: the length of the bounding box (in km)
"""
def length (bbox):
    y =(bbox[3]-bbox[1])*111.3
    return y

"""
Function to calculate the area of the bounding box

:param bbox: bounding box of a file with the format: ['minlon', 'minlat', 'maxlon', 'maxlat']
:returns: the area (in km²)
"""
def area (bbox):
    A = width(bbox) * length(bbox)
    return A

"""
auxiliary calculation https://en.wikipedia.org/wiki/Law_of_cosines

:param bbox1: Bounding Box from a file
:param bbox2: Bounding Box from a file
:returns: the cosinus
"""
def lawOfCosines(bbox1,bbox2):
    cos = math.sin((meanLatitude(bbox1) * math.pi/180))*math.sin((meanLatitude(bbox2)*math.pi/180)) + math.cos((meanLatitude(bbox1)*math.pi/180)) * math.cos((meanLatitude(bbox2)*math.pi/180)) * math.cos((meanLongitude(bbox1)*math.pi/180)-(meanLongitude(bbox2)*math.pi/180))
    return cos

"""
function to calculate the distace between two Bounding Boxes

:param bbox1: Bounding Box from a file
:param bbox2: Bounding Box from a file
:returns: the distance
"""
def distance(bbox1,bbox2):
    dist = math.acos(lawOfCosines(bbox1,bbox2)) * 6378.388
    return dist

if __name__ == '__main__':
    aehnlickeit(bbox1, bbox2)
