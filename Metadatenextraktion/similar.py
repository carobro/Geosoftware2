import math

# Beispielkoordinaten
bbox1 = [5.8663155, 47.270111, 15.041932 , 55.099159]
bbox2 = [7.5234, 52.0326, 7.7556, 52.152]

def aehnlickeit (bbox1,bbox2):
    """
    if bbox1[0]==bbox2[0] and bbox1[1]==bbox2[1] and bbox1[2]==bbox2[2] and bbox1[3]==bbox2[3]:
    """    
    if isinstance(bbox1[0], float) and isinstance(bbox1[1], float) and isinstance(bbox1[2], float) and isinstance(bbox1[3], float):
        if isinstance(bbox2[0], float) and isinstance(bbox2[1], float) and isinstance(bbox2[2], float) and isinstance(bbox2[3], float):

            if distanz(bbox1,bbox2) < 20000:
                simdis = distanz(bbox1,bbox2)/20000
            else:
                simdis = 1
            if abs(flaeche(bbox1) - flaeche(bbox2)) < 1000000:
                simA = (abs(flaeche(bbox1) - flaeche(bbox2)))/1000000
            else:
                simA = 1
            sim = (2 * simdis + simA)/3
            print(sim)
            return sim
        
    else:
        return None

def mittlererBreitengrad (list):
    lat = (list[3]+list[1])/2
    return lat

def mittlererLaengengrad (list):
    lon = (list[2]+list[0])/2
    return lon

def breite (list):
    x = (list[2]-list[0])*111.3 * (math.cos(mittlererBreitengrad(list)*math.pi/180))
    return x

def laenge (list):
    y =(list[3]-list[1])*111.3
    return y

def flaeche (list):
    A = breite(list) * laenge(list)
    return A

def seitenkosinussatz(bbox1,bbox2):
    cos = math.sin((mittlererBreitengrad(bbox1) * math.pi/180))*math.sin((mittlererBreitengrad(bbox2)*math.pi/180)) + math.cos((mittlererBreitengrad(bbox1)*math.pi/180)) * math.cos((mittlererBreitengrad(bbox2)*math.pi/180)) * math.cos((mittlererLaengengrad(bbox1)*math.pi/180)-(mittlererLaengengrad(bbox2)*math.pi/180))
    return cos

def distanz(bbox1,bbox2):
    dist = math.acos(seitenkosinussatz(bbox1,bbox2)) * 6378.388
    return dist

if __name__ == '__main__':
    aehnlickeit(bbox1, bbox2)
