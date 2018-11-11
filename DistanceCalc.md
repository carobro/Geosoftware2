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

## Exakte Entfernungsberechnung für die Kugeloberfläche
Anwendung von Seitenkosinussatz:
  `cos(g) = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1)`  
  mit g: Gesucheter Großkreisbogen  
  lat1, lat2, lon1, lon2: Breite, Länge in Grad
  `dist = 6378.388 * acos(cos(g))`  
  mit dist: Entfernung in km
***
[Quelle](https://www.kompf.de/gps/distcalc.html)

# Flächenberechnung
`(max lat - min lat)*111.3 = y`
`(max lon - min lon)*111.3 * cos(max lat+min lat)/2) = x`
`A=x*y`
mit A: Fläche in km²

# Ähnlichkeitsberechnung
sim(bbox1,bbox2)=distance/(A(bbox1)+A(bbox2))


**Beispiele:**
Deutschland - Polen  
bbox(DE)=5.866315,47.270111,15.041932,55.099159
bbox(POL)=14.122971,49.002048,24.145782,,55.033695
