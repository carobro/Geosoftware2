import math

# Beispielkoordinaten
bbox1 = [7.473785, 51.840145, 7.774364, 52.060024]
bbox2 = [7.5234, 52.0326, 7.7556, 52.152]

def aehnlickeit (bbox1,bbox2):
    if distanz(bbox1,bbox2) < 20000:
        simdis = distanz(bbox1,bbox2)/20000
    else:
        simdis = 1
    if abs(flaeche(bbox1) - flaeche(bbox2)) < 1000000:
        simA = (abs(flaeche(bbox1) - flaeche(bbox2)))/1000000
    else:
        simA = 1
    sim = (2 * simdis + simA)/3
    return sim
    print(sim)

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
