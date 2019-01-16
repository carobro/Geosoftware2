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

# <span style="color:blue">Blueprints</span> und wo sie zu finden sind (nicht)

Ein kleiner Fortschrittsbericht zu meinem Treiben in der Zenodo-API.

## ToDo-Liste:
- [x] zenodo aufsetzen
- [x] Daniels Anleitung befolgen
- [x] zenodo mit Testdaten fuellen
- [ ] API-Enpunkt fuer Similarity hinzufuegen
  - [x] Derzeitige Endpunkte anschauen
  - [x] flask service aufsetzen
  - [x] blueprint erstellen
  - [x] in den entrypoints in setup.py und config.py vermerken
  - [x] views.py erweitern, sodass Endpunkt ueber die localhost-Seite aufgerufen werden kann
  - [ ] Endpunkt mit den similarity-berechnungen u. dem CLI tool verknuepfen

So sieht ein Datensatz in der API-Speicherung(erreichbar unter http://localhost:5000/api/records/##) aus.
Von besonderem Interesse sind die Eintraege "key" und "links":
```
"key": "sresa1b_ncar_ccsm3-example.nc", 
"links": {
"self": "http://localhost:5000/api/files/80629a87-a92f-4948-83cd-3ed905a91941/sresa1b_ncar_ccsm3-example.nc"
```
diese enthalten die benoetigten Informationen des Dateinamens, der ausgelesen werden soll und dem Link zur Datei im System.

```
{
  "conceptdoi": "10.5072/zenodo.17", 
  "conceptrecid": "17", 
  "created": "2019-01-08T18:13:07.906896+00:00", 
  "doi": "10.5072/zenodo.18", 
  "files": [
    {
      "bucket": "80629a87-a92f-4948-83cd-3ed905a91941", 
      "checksum": "md5:acf429090caac75ee85e6ed38e8685aa", 
      "key": "sresa1b_ncar_ccsm3-example.nc", 
      "links": {
        "self": "http://localhost:5000/api/files/80629a87-a92f-4948-83cd-3ed905a91941/sresa1b_ncar_ccsm3-example.nc"
      }, 
      "size": 2767916, 
      "type": "nc"
    }
  ], 
  "id": 18, 
  "links": {
    "badge": "http://localhost:5000/badge/doi/10.5072/zenodo.18.svg", 
    "bucket": "http://localhost:5000/api/files/80629a87-a92f-4948-83cd-3ed905a91941", 
    "conceptbadge": "http://localhost:5000/badge/doi/10.5072/zenodo.17.svg", 
    "conceptdoi": "https://doi.org/10.5072/zenodo.17", 
    "doi": "https://doi.org/10.5072/zenodo.18", 
    "html": "http://localhost:5000/record/18", 
    "latest": "http://localhost:5000/api/records/18", 
    "latest_html": "http://localhost:5000/record/18", 
    "self": "http://localhost:5000/api/records/18"
  }, 
  "metadata": {
    "access_right": "open", 
    "access_right_category": "success", 
    "creators": [
      {
        "name": "alllelel"
      }
    ], 
    "description": "<p>moin7</p>", 
    "doi": "10.5072/zenodo.18", 
    "license": {
      "id": "CC-BY-4.0"
    }, 
    "publication_date": "2019-01-08", 
    "related_identifiers": [
      {
        "identifier": "10.5072/zenodo.17", 
        "relation": "isVersionOf", 
        "scheme": "doi"
      }
    ], 
    "relations": {
      "version": [
        {
          "count": 1, 
          "index": 0, 
          "is_last": true, 
          "last_child": {
            "pid_type": "recid", 
            "pid_value": "18"
          }, 
          "parent": {
            "pid_type": "recid", 
            "pid_value": "17"
          }
        }
      ]
    }, 
    "resource_type": {
      "subtype": "article", 
      "title": "Journal article", 
      "type": "publication"
    }, 
    "title": "NetCDF-Testdata"
  }, 
  "owners": [
    2
  ], 
  "revision": 1, 
  "stats": {}, 
  "updated": "2019-01-08T18:13:07.983202+00:00"
}
```

_Ein Blueprint hat in etwa diese Struktur:_

```
blueprint = Blueprint(
```
die Methode wird von flask importiert (http://flask.pocoo.org/docs/1.0/tutorial/views/)
```
    'zenodo_deposit',
```
der Name des Blueprints
```
    __name__,
```
zeigt auf den Ort der Definition
```
    url_prefix='',
```
Das wird an jede URL gehaengt, in diesem Fall ein Hauch von nichts
```
    template_folder='templates',
    static_folder='static',
)
```

Dieser Teil gibt die Route vor, die der Blueprint geht
```
@blueprint.route(
    '/record/<pid(recid,record_class='
    '"zenodo.modules.records.api:ZenodoRecord"):pid_value>',
    methods=['POST']
)
```
Hier wird etwa eine Datei unter localhost:5000/record/<pid_value> aufgerufen
```
@login_required
@pass_record('update')
def edit(pid=None, record=None, depid=None, deposit=None):
    """Edit a record."""
    # If the record doesn't have a DOI, its deposit shouldn't be editable.
    if 'doi' not in record:
        abort(404)

    return redirect(url_for(
        'invenio_deposit_ui.{0}'.format(depid.pid_type),
        pid_value=depid.pid_value
    ))
```
Und im folgenden geupdated.

Das ist in etwa die Struktur, die wir benoetigen - ein Endpunkt fuer die Kalkulationsergebnisse, wenn dann die Uebereinstimmung von zwei Datensaetzen errechnet wird, updatet das Blueprint den Endpunkt mit dem Ergebnis und man ruft mit einem weiteren dieses Ergebnis ab. Diesmal ['GET'] anstatt ['POST'].


Konsolen-Ausgabe eines Dateiuploads mit Speicherung als record in zenodo

```
127.0.0.1 - - [13/Jan/2019 17:01:05] "PUT /api/deposit/depositions/20 HTTP/1.1" 200 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /record/20 HTTP/1.1" 200 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /static/img/openaire-horizontal-old.png HTTP/1.1" 200 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /badge/DOI/10.5072/zenodo.20.svg HTTP/1.1" 200 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /record/20/preview/eric.png HTTP/1.1" 200 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /_debug_toolbar/static/css/toolbar.css?0.5577483203139662 HTTP/1.1" 200 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /_debug_toolbar/static/css/toolbar.css?0.3240897717185367 HTTP/1.1" 200 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /static/templates/invenio_csl/citeproc.html HTTP/1.1" 304 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /static/node_modules/invenio-csl-js/dist/templates/error.html HTTP/1.1" 304 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /static/node_modules/invenio-csl-js/dist/templates/loading.html HTTP/1.1" 304 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /static/node_modules/invenio-csl-js/dist/templates/typeahead.html HTTP/1.1" 304 -
127.0.0.1 - - [13/Jan/2019 17:01:12] "GET /api/iiif/v2/caa7d04d-3e6d-4e54-8425-d99e1802e665:da66ca39-ed63-484b-b884-98935bf28976:eric.png/full/750,/0/default.png HTTP/1.1" 200 -
```