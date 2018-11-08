# Entfernungsberechnung mit der Annahme die Erde sei eine Kugel
Möglich wäre auch eine Entfernungsberechnung mit der Annahme, dass die Erde ein Rotationsellispoid sei. Dafür eignet sich die [PROJ 4 Library](https://proj4.org/).
Allerdings ist diese Methode dann bei bspw. der Entfernung Berlin - Lissabon nur 500 Meter (0,02%) besser. Ich behaupte, dass wir bei unserem 
Projekt nicht diese Genauigkeitsansprüche haben und wir somit davon ausgehen können, dass die Erde eine Kugel ist.

lat1, lat2 bezeichnen im folgenden den mittleren Breitengrad(max lat+min lat)/2) der beiden Bounding Boxes, welche verglichen werden:  
lon1, lon2 bezeichnen im folgenden den mittleren Längengrad(max lon+min lon)/2) der beiden Bounding Boxes, welche verglichen werden:


### erste verbesserte Methode:
Nur zum Verständnis, wir würden dann die unten beschriebene exakte Entfernungsberechnung verwenden.  
  `distance = sqrt(dx * dx + dy * dy)`  
  mit distance: Entfernung in km  
  `dx = 113.3 * cos(lat) * (lon1 - lon2)`  
  `lat = (lat1 + lat2) / 2 * 0.01745`  
  `dy = 111.3 * (lat1 - lat2)`  
  lat1, lat2, lon1, lon2: Breite, Länge in Grad  
Warum 0.01745?
-> Umrechnung von Grad in Radiant `1° = pi/180 rad ~=0.01745`



## Exakte Entfernungsberechnung für die Kugeloberfläche
Anwendung von Seitenkosinussatz:
  `cos(g) = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1)`  
  mit g: Gesucheter Großkreisbogen  
  lat1, lat2, lon1, lon2: Breite, Länge  
  `dist = 6378.388 * acos(cos(g))`  
  mit dist: Entfernung in km`
***
[Quelle](https://www.kompf.de/gps/distcalc.html)
