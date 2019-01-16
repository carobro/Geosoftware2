## Ablaufsshema API

Teil 1

User greift auf Upload-Seite zu 
- laedt auf Uploads eine neue Datei hoch 
- Trigger fuer die Speicherung der Datei (im cache oder) lokal im Vezeichnis 
- Extraktion der Metadaten auf Basis dieser File (CLI-Tool Befehl mit hinterlegtem Pfad) 
- Hinzufuegen der Felder fuer bbox und timeextent in der json-metadata (/api/records/[ID]) /oder neuer Endpunkt? 
- Speicherung der Daten

Teil 2

User greift auf record-Seite zu 
- Abgleich der Metadaten jeglicher gespeicherter records mit dem aktuell auf der Seite (similarity calculation) 
- Erstellung der Aehnlichkeitskeitswerte und Speicherung als sortierte Liste 
- Endpoint (/api/similar/) gibt die 5 (20) ersten Eintraege zurueck 
- Darstellung dieser Eintraege auf der zenodo record-page 

## to do

Schritt 1 Metadatenextraktion
- [x] Punkt im code finden, wo Daten hochgeladen werden
- [x] Punkt im code finden, wo Metadaten erstellt werden
- [x] Speicherort der Daten finden
- [ ] CLI-Tool als pypi installer importieren und fuer die zenodo distribution bereitstellen 
- [ ] die metadata-extraction implementieren



## Ort wo die Daten lokal gespeichert werde
`~/Envs/zenodo/var/instance/data`   
   
&larr; Das wird der path zu unseren Dateien mit der wir die Metadateextraktion ausführen wollen
   
## Dateien die wir (warscheinlich verändern müssen)   
`~/zenodo/zenodo/modules/deposit/ext.py` &larr; (Zeile 62)   
before_record_index.connect(extractor_receiver, sender=app, weak=False) 


`/zenodo/zenodo/modules/deposit/indexer.py` &larr; (Zeile 101)   
   
def extractor_receiver(sender, json=None, record=None, index=None,
                     **dummy_kwargs):
"""    
    :param sender: Sender of the signal.   
    :param json: JSON to be passed for the elastic search.   
    :type json: `invenio_records.api.Deposit`   
    :param record: Indexed deposit record.   
    :type record: `invenio_records.api.Deposit`   
    :param index: Elasticsearch index name.   
    :type index: str
    """   
print("API-Test")

&larr; Hier könnte unser extractTool aufgerufen werden, welche und die zeitliche und räumliche Ausdehnung gibt.