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