# Geosoftware II - WiSe 2018/19
### Enhancing discovery of geospatial datasets in data repositories

:arrow_forward: Die Gruppe :one:
# Zenodo - Installation:   
Zur Zenodo-Installation bitte folgende Anleitung befolgen:   
https://github.com/zenodo/zenodo/blob/master/INSTALL.rst   
(Wer sich nerven sparen will, sollte es nicht unter Windows versuchen.
 Unter Linux deutlich schneller und einfacher :wink: )

# CLI-Tool
## Installationsbeschreibung
Diese Installtion wurde bisher nur mit Linux getestet, sollte aber auch unter Windows funktionieren.   
pip für pip install wird vorausgesetzt.
Um unser CLI-Tool auszuführen muss im Projektordner die folgende Datei ausgeführt werden:
   
`pip install -r requirements.txt --user`
   
In dieser Datei sind alle benötigten Plugins gelistet, die wir in unserem Tool nutzen.

Außerdem müssen noch folgende Befehle ausgeführt werden:
`apt-get install python-gdal`
`apt-get install gdal-bin`

`pip install pytest`

Dann kann in einer beliebigen, gängigen Konsole in den Ordner des Tools navigiert werden und
dort folgender Befehl ausgeführt werden 

`python detailebenen.py --path="Der Path zur Datei"`

hinten dran können dann noch speizifikationen hinzugefügt werden:

`--bbox` &larr; für die Bounding Box der Datei ( ist auch als default eingestellt)   
`--feature` &larr; um alle Koordinaten der Datei zu erhalten   
`--single` &larr; um nur die Koordinaten einer Datei zu erhalten (auch default)
`--whole` &larr; in Kombination mit --bbox oder --feature um das jeweilige aus einem desamten Verzeichnis zu lesen
`--time` &larr; um die Zeit einer Datei zu erhalten

# Ähnlichkeitsberechnung

Unser Code zur Ähnlichkeitsberechnung ist in der `similar.py` Datei zu finden.
Die dazu gehörenden Tests befinden sich in der `test_similar.py` Datei.

# Tests

Unsere Tests können einfach mit dem Befehl

`pytest` ausgeführt werden

# Probleme ?
Falls Probleme oder Fragen bei der Installation entstehen, erstellt doch direkt ein Issue damit wir euch helfen und Fehler korrigiern können :blush:
