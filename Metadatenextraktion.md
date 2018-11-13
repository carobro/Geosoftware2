# M E T A D A T E N E X T R A K T I O N

[Apache Tika](https://tika.apache.org/1.19.1/gettingstarted.html) sollte einen großen Teil der Formate abdecken, bei GeoJSON, GeoPackage und CSV sind wir uns nicht sicher.

Aber diese könnten durch [GDAL](https://www.gdal.org/) übernommen werden.

Da Apache Tika native in Java geschrieben wurde, sollte man überlegen auf [diese](https://github.com/chrismattmann/tika-python) Python-Übersetzung zurückzugreifen.    

Installation (with pip)
-----------------------
1. `pip install tika`

Installation (without pip)
--------------------------
1. `python setup.py build`  
2. `python setup.py install`  




