# Geosoftware II - WiSe 2018/19
### Enhancing discovery of geospatial datasets in data repositories

:arrow_forward: Die Gruppe 1

## Installationsbeschreibung

Um unser CLI-Tool auszuführen muss die folgende Datei ausgeführt werden:
   
`python ./yaml_install_Datein.py`
   
In dieser Datei sind alle benötigten Plugins gelistet, die wir in unserem Tool nutzen
Dann kann in einer beliebigen, gängigen Konsole in den Ordner des Tools navigiert werden und
dort folgender Befehl ausgeführt werden 

`python detailebenen.py --path=("Der Path zur Datei")`

hinten dran können dann noch speizifikationen hinzugefügt werden:

`--bbox` -> für die Bounding Box der Datei ( ist auch als default eingestellt)   
`--feature` -> um alle Koordinaten der Datei zu erhalten   
`--single` -> um nur die Koordinaten einer Datei zu erhalten (auch default)
`--whole` -> in Kombination mit --bbox oder --feature um das jeweilige aus einem desamten Verzeichnis zu lesen