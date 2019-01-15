## Ort wo die Daten lokal gespeichert werde
`~/Envs/zenodo/var/instance/data`   
   
&larr; Das wird der path zu unseren Dateien mit der wir die Metadateextraktion ausführen wollen
   
## Dateien die wir (warscheinlich verändern müssen)   
`~/zenodo/zenodo/modules/deposit/ext.py`      
   
&larr; (Zeile 62)   
before_record_index.connect(extractor_receiver, sender=app, weak=False) 


`/zenodo/zenodo/modules/deposit/indexer.py`
   
&larr; (Zeile 101)   
   
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

