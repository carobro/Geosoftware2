# Entfernungsberechnung
**Annahme: die Erde sei eine Kugel**
Möglich wäre auch eine Entfernungsberechnung mit der Annahme, dass die Erde ein Rotationsellispoid sei. Dafür eignet sich die [PROJ 4 Library](https://proj4.org/).
Allerdings ist diese Methode dann bei bspw. der Entfernung Berlin - Lissabon nur 500 Meter (0,02%) besser. 
> Ich behaupte, dass wir bei unserem 
> Projekt nicht diese Genauigkeitsansprüche haben und wir somit davon ausgehen können, dass die Erde eine Kugel ist.

lat1, lat2 bezeichnen im folgenden den mittleren Breitengrad(max lat+min lat)/2) der beiden Bounding Boxes, welche verglichen werden:  
lon1, lon2 bezeichnen im folgenden den mittleren Längengrad(max lon+min lon)/2) der beiden Bounding Boxes, welche verglichen werden:
bbox1, bbox2 bezeichnen im folgenden die Bounding Boxes, bestehend aus: min lon, min lat, max lon, max lat
min lat, max lat are decimal numbers between -90.0 and 90.0.
min lon, max lon are decimal numbers between -180.0 and 180.0.

### Exakte Entfernungsberechnung für die Kugeloberfläche
Anwendung von Seitenkosinussatz:
  `cos(g) = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1)`  
  mit g: Gesucheter Großkreisbogen  
  lat1, lat2, lon1, lon2: Breite, Länge in Grad
  `dist = 6378.388 * acos(cos(g))`  
  mit dist: Entfernung in km
***
[Quelle](https://www.kompf.de/gps/distcalc.html)

### Flächenberechnung
`(max lat - min lat)*111.3 = y`  
`(max lon - min lon)*111.3 * cos(max lat+min lat)/2) = x`  
`A=x*y`
mit A: Fläche in km²

## Ähnlichkeitsberechnung Version 1
sim(bbox1,bbox2)=distance/(A(bbox1)+A(bbox2))

**Beispiele:**
###### Deutschland - Polen  
bbox(DE)=5.866315,47.270111,15.041932,55.099159
bbox(POL)=14.122971,49.002048,24.145782,55.033695

`lat1 = (55.099159 + 47.270111)/2  
lat1 = 51.184635  
lat2 = (49.002048 + 55.033695)/2  
lat2 = 52.0178715  

lon1 = (5.866315 + 15.041932)/2  
lon1 = 10.4541235  
lon2 = (14.122971 + 24.145782)/2  
lon2 = 19.1343765`  

*Entfernung:*  
`cos(g) = 0.9954758561  

dist = 111.324 * acos(cos(g)) = 606.9570157`  

*Fläche:*
Deutschland:  
`(55.099159 - 47.270111)*111.3 = 871.3730424  
(15.041932 - 5.866315)*111.3*cos(51.184635) = 640.130156  
A(DE) = 871.3730424\*640.130156 = 557792.1616`  
      
Polen: 
`(55.033695 - 49.002048)*111.3 = 671.3223111  
(24.145782 - 14.122971)*111.3*cos(52,0178715) = 686.5200773  
A(POL)=671.3223111*686.5200773 = 460876.2449`  

*Ähnlichkeitsberechnung:*  
`sim = 606.9570157/(557792.1616+460876.2449) = 0.00059583374791  
sim = 606.9570157²/(557792.1616+460876.2449) = 0.3616454742`  

###### Deutschland - Mexiko  
bbox(MEX)= -118.6,14.39,-86.49,32.72  

`lat2 = (14.39 + 32.72)/2  
lat2 = 23.55  
 
lon2 = (-118.6 + (-86.49))/2  
lon2 = -102.545`  

*Entfernung:*  
`cos(g) = -0.0343531528  
dist = 111.3 * acos(cos(g)) = 10236.11386`  

*Fläche:*  
Mexiko:  
`(32.72-14.39)*111.3 = 1020.0645  
(-86.49-(-118.6))*111.3*cos(23.55) = 3276.183874  
A(MEX) = 1020.0645*3276.183874 = 3341918.865`  
 
`sim = 10236.11386/(557792.1616+3341918.865) = 0.0026248391  
sim = 10236.11386²/(557792.1616+3341918.865) = 26.86815157`  

###### Deutschland - Münster  
`bbox(MS) = 7.473785,51.840145,7.774364,52.060024  
lat2 = 51.9500845  
lon2 = 7.6240745`  
 
*Entfernung:*  
`cos(g) = 0.9994395804  
dist = 213.5518683`  

*Fläche:*  
Münster:  
`x = 24.4725327  
y = 20.61957  
A(MS) = 504.6131119  

sim = 213.5518683/(557792.1616+504.6131119) = 0.0003825060039  
sim = 213.5518683²/(557792.1616+504.6131119) = 0.0816848718`  

###### Münster - Greven  
`bbox(Greven) = 7.5234,52.0326,7.7556,52.152  
lat2 = 52.0923  
lon2 = 7.6395`  

*Entfernung:*  
`cos(g) = 0.9999969058  
dist = 15.86379531`  

*Fläche:*  
Greven:  
`x = 13.28922  
y = 15.87824119  
A(Greven) = 211.0094404  

sim = 15.86379531/(504.6131119+211.0094404) =0.0221880112  
sim = 15.86379531²/(504.6131119+211.0094404) =0.352306593`  

## Ähnlichkeitsberechnung Version 2  
_wird von uns präferiert und verwendet_
Aufteilung Ähnlichkeit Distanz und Ähnlichkeit Fläche:    
Ähnlichkeit Distanz:   
`simdis=dist/20000` wobei simdis maximal 1 beträgt  
> 0km -> 100% ähnlich  
> 20000km -> 0% ähnlich  
> 20000km ist ungefähr die Hälfte des Äquatorumfangs  
Ähnlichkeit Fläche:  
`simA=|A(bbox1)-A(bbox2)|/1 000 000` wobei simA maximal 1 beträgt  
> 0km² Diffeerenz -> 100% ähnlich  
> 1 000 000km² -> 0% ähnlich  

`sim = (2*simdis+simA)/3`  

Sim(Münster - Greven)  
15.86379531/20000 = 0.0007931  
504 - 211 = 293  
293/1000000 = 0.000293  
(2\*0.0007931+0.000293)/3= **0,0006**  

Sim(Deutschland - Münster)  
213.5518683/20000 = 0.0106776  
557287,5484881/1 000 000 = 0.5573  
(2\*0.0106776+0.5573)/3 = **0,1929**  

Sim(Deutschland - Mexiko)  
10236.11386/20000 =0,5118  
2784126,7034/1000000 = 2,7 > 1  
(2\*0,5118+1)/3 = **0,6745**

Sim(Deutschland - Polen)   
606.9570157/20000 = 0,0303  
96915,9167/1 000 000 = 0,0969  
(2\*0,0303+0,0969)/3 = **0,0525**  

***
[Quelle der Bounding Boxes](http://boundingbox.klokantech.com/)
