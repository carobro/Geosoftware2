# Enhancing discovery of geospatial datasets in data repositories

Carolin B. ([c\_bron02@wwu.de](mailto:c_bron02@wwu.de)),

 Cornelia (c\_zyga01@wwu.de),

Hilal ([h\_kara06@wwu.de](mailto:h_kara06@wwu.de)),

 Jannis ([j\_froe09@wwu.de](mailto:j_froe09@wwu.de)),

 Yannick (y\_paul02@wwu.de)

Münster, den 30. November 2018

1. Zielbestimmung

Unser Ziel ist es, Zenodo um eine Funktion weiterzuentwickeln, die es dem Besucher ermöglicht, ähnliche Datensätze als Empfehlungen anzuzeigen, während er sich einen Datensatz anschaut. Hier lehnen wir uns an einem Empfehlungssystem, wie beispielsweise Amazon an. Besonderes Augenmerk fällt auf die Implementation der Metadatenextraktion verschiedener Geodaten-Typen. Im Folgenden werden die Funktionalitäten näher erläutert.

**Das Programm**

- --Bei Betrachten eines Datensatzes werden weitere Datensätze empfohlen
- --Empfehlungen von Datensätzen basieren auf der räumlichen Ähnlichkeit der Daten

- **--** Die Datensätze werden in einer Datenbank gespeichert

**Die Benutzer**

- --Der Besucher der Internetseite ([https://www.zenodo.org/](https://www.zenodo.org/)) (= Benutzer) soll Metadaten einsehen können
- --Der Besucher der Internetseite soll auf die Empfehlungen klicken können/ mit ihnen interagieren und auf eine Seite weitergeleitet, auf der Informationen zu dem entsprechenden Datensatz angezeigt werden.

**Sonstiges**

- --Sprache: Englisch

2.  Produkteinsatz

**Anwendungsbereich**

- --Wissenschaftliches Repositorium

**Zielgruppen**

- --Wissenschaftler, die nach ähnlichen oder im Zusammenhang stehenden Geodatensätzen suchen
- --Betreiber von wissenschaftlichen Repositorien
- --Archivare, welche den Zugang zu vergleichbaren wissenschaftlichen Daten erleichtern wollen

**Betriebsbedingungen**

- --Die Software/API ist als Anknüpfung zur Nutzung des Repositories ausgelegt
- --Die Nutzung ist nur mit bereits vorhandener Netzwerkverbindung möglich

3. Produktfunktionen

**Metadatenextraktion**

**FE010** Unterstützte Geo-(Meta)-Datenformate beim Hochladen und Speichern der Daten: [GeoPackage, NetCDF, GeoJSON, Shapefile, CSV im Web, ISO 19xxx, GeoTIFF]

**FE015** Erstellung des CLI Tools mit Hilfe von &quot;[argparse](https://docs.python.org/3/library/argparse.html)&quot;

**FE020** Ein CLI-Tool zum Extrahieren der räumlichen Ausdehnung auf verschiedenen Detailebenen. Der Benutzer kann in Form einer Parameterübergabe entscheiden, ob er dabei die räumliche Ausdehnung als Bounding Box oder als einzelnes Feature aus einer einzelnen Datei erhalten möchte.

**FE030** Ein CLI-Tool zum Extrahieren der zeitlichen Ausdehnung als Zeitintervall oder als Zeitpunkt nach dem  [ISO8601](https://www.w3.org/TR/xmlschema11-2/#ISO8601) Standard aus einer einzelnen Datei

**FE040** Ein CLI-Tool zum Extrahieren der räumlichen Ausdehnung mithilfe einer Bounding Box und der zeitlichen Ausdehnung als Intervall nach dem  [ISO8601](https://www.w3.org/TR/xmlschema11-2/#ISO8601) Standard aus einem Dateiverzeichnis

**FE050** Die Metadatenextraktion für einen bestimmten Datensatz kann über einen API-Aufruf ([https://zenodo.org/record/[ID]/metadata](https://zenodo.org/record/1490234#.W_Ph3stKjeQ/metadata)) von allen Benutzern ausgelöst werden, wodurch die Metadaten des Datensatzes (bezüglich der bereits erfolgten Metadatenextraktionen) sofort aktualisiert werden

**FE060** Die Metadatenextraktion wird automatisch für neu hochgeladene Datensätze in der Basissoftware ausgelöst mit Hilfe von [ApacheTika](https://github.com/chrismattmann/tika-python) und [GDAL](https://pypi.org/project/GDAL/)[¹](https://wiki.apache.org/tika/TikaGDAL).

**FE070** Die Metadatenextraktion während des Hochladens eines neuen Datensatzes wird als unabhängiger Prozess ausgeführt (d.h., sie muss nicht abgeschlossen werden, damit die Datensatzerstellung abgeschlossen werden kann).

**API**

**FA010** Alle benutzerbezogenen Funktionen sind über diese REST-konformen HTTP-API-Endpunkte verfügbar

        Rekord:                 &quot;https://zenodo.org/record/[ID]&quot;

Metadaten:                 &quot;https://zenodo.org/record/[ID]/metadata&quot;,
            Daten:                         &quot;https://zenodo.org/api/files&quot;,
            Lizenzen:                 &quot;https://zenodo.org/api/licenses/&quot;,
            Dokumentation:         &quot;https://zenodo.org/api/records/&quot;

**FA020** API-Endpunkte geben als Antwort eine gültige JSON-Datei, im Body der Seite konform der bereits vorhandenen Endpunkte einschließlich Fehlern in der englischen Sprache, zurück.

**FA030** API-Endpunkte verwenden diese HTTP-Statuscodes:

| Code | Name | Description |
| --- | --- | --- |
| 200 | OK | Request succeeded, response included (GET/PUSH/PATCH) |
| 201 | Created | Request succeeded, response included (POST) |
| 202 | Accepted | Request succeeded, response included with background process |
| 204 | No Content | Request succeeded, no response |
| 400 | Bad Request | Request failed, error included |
| 401 | Unauthorized | Request failed, invalid access token |
| 404 | Not Found | Request failed, resource not found |
| 405 | Method Not Allowed | Request failed, unsupported HTTP error |
| 409 | Conflict | Request failed, current state of resource |
| 415 | Unsupported Media Type | Request failed, missing/invalid header |
| 429 | Too Many Requests | Request failed, rate limiting |
| 500 | Internal Server Error | Request failed, internal server error |

**FA040** Geodaten in der API werden mit [GeoJSON](http://geojson.org/)(RFC 7946) kodiert

**FA050** Erweiterte Metadaten, d.h. einschließlich der aus Dateien extrahierten zeitlichen und räumlichen Informationen, sind in den regulären Metadaten für Datensätze enthalten. Falls Datensätze keine raumzeitlichen Informationen enthalten, werden in den Metadaten diese Eigenschaften (spatial extent, temporal extent) mit Nullwerten gefüllt.

**FA060** Wenn der Parameter _&quot;similar=n_&quot; zu einer Anforderung hinzugefügt wird (mit dem API Endpunkt: [https://zenodo.org/record/[ID]/?similar=n](about:blank)), einen Datensatz zu lesen, wird die Antwort um IDs und Ähnlichkeitswerte für n viele ähnliche Datensätze erweitert.

**Ähnlichkeitsberechnung**

**FS010** API-Endpunkt der Anzeige des Datensatzes ([https://zenodo.org/record/[ID]](about:blank)) stellt den  Ähnlichkeitswert des Datensatzes zu ähnlichen Datensätzen bereit; der Ähnlichkeitswert basiert auf der Bounding Box aus der bestehenden GeoJSON-Definition (bbox = min lon, min lat, max lon, max lat) aller Daten im Datensatz; Datensätze werden als ihre repository-spezifische ID bereitgestellt _(siehe_ _11.__)._

**FS015** Zur Berechnung der Ähnlichkeit berechnen wir die Ähnlichkeit der Distanz (⅔) und die Ähnlichkeit der Flächenausdehnung (⅓) . _Die genauen Formeln lassen sich unserem Anhang entnehmen (siehe_ _11.__)_.

**FS020** API-Endpunkt, der eine sortierte Liste ähnlicher Datensätze für eine repository-spezifische Datensatz-ID bereitstellt; Die Länge der zurückgegebenen Liste kann vom Benutzer definiert werden und ist standardmäßig auf 5 gesetzt. Eine maximale Länge ist serverseitig auf 20 festgelegt, weil mehr Datensätze zu einer Reizüberflutung des Benutzers führen könnten und dies besser zum Design der Seite passt.

**FS030** Der Ähnlichkeitswert liegt im Intervall ]0, 1], wobei ein Wert nahe Null einer großen Ähnlichkeit entspricht.

**FS040** Der Eingabedatensatz wird niemals in die Liste ähnlicher Datensätze aufgenommen

**FS050** Der Ähnlichkeitswert berücksichtigt den Datentyp für die Typen Vektor, Raster oder Zeitreihen, d.h. ein Ähnlichkeitswert für zwei Datensätze mit gleichem Umfang ist höher, wenn die Datentypen auch übereinstimmen

**FS055** Der Einfluss des gleichen Datentyps beeinflusst in folgender Weise die Ähnlichkeit:

Ähnlichkeit❑ungleicherDatentyp=Ähnlichkeit∗54

FallsÄhnlichkeit❑ungleicherDatentyp\&gt;1→Ähnlichkeit❑ungleicherDatentyp=1

Falls der Datentyp verschieden ist, vergrößert sich der Ähnlichkeitswert um 25%. In der Regel ist es z.B. nicht erstrebenswert Zeitreihen mit Vektordaten zu vergleichen.

5. Produktdaten

**D010** Metadaten:

- --Autor (String)
- --zeitliche Ausdehnung (nach XML S[chema 11.2](https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/#bib-xmlschema11-2))
- --Dateityp (String)
- --Angaben zu Rechten (String)

Beispiel:

- --Carolin Bronowicz
- --P1Y2M3DT4H5M6S
- --Shapefile
- --[Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)

6. Benutzeroberfläche

**FU010** Eine konfigurierbare Anzahl ähnlicher Datensätze wird auf einer Seite angezeigt, um einen einzelnen Datensatz anzuzeigen (darf nicht in vorhandene Benutzeroberflächen für die Basissoftware integriert sein)

**Abbildung 1** : Beispielhafte Darstellung eines Datensatzes auf Zenodo mit Empfehlung zu weiteren ähnlichen Datensätze

In Abb. 1 befindet sich im unteren Bereich der Seite ein Block mit einer Liste empfohlener Datensätze, die durch unsere Ähnlichkeitsberechnung erstellt wurde. Um den Gedankenfluss des Benutzers nicht zu unterbrechen, befinden sich die Empfehlungen unter dem betrachteten Datensatz. So kann der Anwender zu ähnlichen Themen weitergeleitet werden, nachdem er sich diesen Datensatz angeguckt hat. Zudem haben wir diese Anordnung gewählt, um unsere Erweiterung bestmöglich in das bestehende Design von Zenodo zu integrieren, ohne dass die Seite überladen und unübersichtlich wirkt.

**Konfiguration**

**FC010** Die Konfiguration zusätzlicher Funktionen ist über Textdateien im YAML-Format möglich und in die Konfigurationsmechanismen der Basissoftware integriert.

**FC020** Die Konfiguration ist mindestens nach dem Neustart des Dienstes aktiv

7. Nichtfunktionale Anforderungen

**Wartbarkeit**

- --Lizenz: Creative Commons - Namensnennung 4.0 International - CC BY 4.0
- --Link zum Linzenzvertrag: [https://creativecommons.org/licenses/by/4.0/legalcode.de](https://creativecommons.org/licenses/by/4.0/legalcode.de)

- --Ein etabliertes Erstellungs- und Konfigurationssystem sowie ein Abhängigkeitsmanagement müssen für die verwendete Programmiersprache angewendet werden, wir verwenden pip für Python.
- --Gemäß der Dokumentation zum Aufbau wird die Konfiguration in Markdown-formatierten Dokumentations-Dateien bereitgestellt

**Benutzerfreundlichkeit**

- --Das Layout wird dem Zenodo Layout angepasst, damit die Benutzerfreundlichkeit erhalten wird

**Performanz**

- --Die Antwortzeit eines API-Aufrufs an ein Repository erhöht sich möglicherweise um den Faktor 2, wenn verwandte Projekte aufgelistet werden, im Vergleich dazu, dass verwandte Projekte nicht angezeigt werden.
- --Komplexe Seiteninhalte können asynchron geladen werden.
- --Der Auftragnehmer stellt ein Testskript bereit, um die Leistung anhand von mindestens 10 verschiedenen URLs oder Ansichten mit einer angemessenen Anzahl von Wiederholungen zu bewerten.

8. Technische Produktumgebung

**Software**

- --Betriebssystem
  - --Linux

- --Plattform
  - --Zenodo (basierend auf INVENIO)

_Wir verwenden Zenodo für die Entwicklung unserer Zusatzfunktion, weil Zenodo eine bereits implementierte Benutzeroberfläche bereitstellt, welche uns beim Testen und Überprüfen unserer Funktionalitäten behilflich ist._
_Da Zenodo auf Invenio basiert sind die zusätzlichen Funktionalitäten ohne großen Aufwand auf andere Repositorien, die ebenfalls auf Invenio basieren übertragbar._

- --Datenbank
  - --PostgreSQL 9.2
- --Browser
  - --Google Chrome 70.0.3538
  - --Mozilla Firefox 63.0
- --Message-Broker
  - --rabbitMQ
- --Search-Engine
  - --ElasticSearch
- --genutzte zusätzliche Dienste/Plattformen
  - --GitHub, GitKraken

9. Anhang

Ähnlichkeitsberechnung

Wir nehmen an, dass die Erde eine Kugel ist, da dies unseren Genauigkeitsansprüchen genügt.

- --Unsere Bounding BoxesUnsere Bounding Boxe (bbox) bestehen aus vier Werten: min lon, min lat, max lon, max lat (bbox) bestehen aus vier Werten: min lon, min lat, max lon, max lat
- --min lat und max lat sind dabei Dezimalzahlen zwischen -90.0 und 90.0
- --min lon und max lon sind Dezimalzahlen zwischen -180.0 und 180.0
- --lat1, lat2 bezeichnen im folgenden den mittleren Breitengrad (max lat+min lat)/2 der beiden Bounding Boxes, welche verglichen werden
- --lon1, lon2 bezeichnen im folgenden den mittleren Längengrad (max lon+min lon)/2 der beiden Bounding Boxes, welche verglichen werden

Entfernungsberechnung

Anwendung von Seitenkosinussatz: cos(g)=sin(lat1)∗sin(lat2)+cos(lat1)∗cos(lat2)∗cos(lon2−lon1)
mit g: Gesuchter Großkreisbogen
lat1, lat2, lon1, lon2: Breite, Länge in Grad
dist=6378.388∗acos(cos(g))
mit dist: Entfernung in km

Flächenberechnung

x=(maxlon−minlon)∗111.3∗cos(maxlat+minlat)/2
y=(maxlat−minlat)∗111.3

mit x, y: Breite, Länge in km

A=x∗y

mit A: Fläche in km²

Ähnlichkeitsberechnung

Aufteilung in Ähnlichkeit Distanz(⅔) und Ähnlichkeit Fläche (⅓)
=(2∗simdis+simA)/3
mit Fallsdist\&lt;20000:simdis=dist/20000
       Sonst:simdis=1
und         AA(bbox1−Abbox2)∨1000000(bbox1−Abbox2)∨1000000:simA=Falls∨
Sonst: simA=1

Erläuterung:

Wir behaupten, dass 0 km Distanz für 100% Ähnlichkeit steht und 20000 km Distanz für 0% Ähnlichkeit steht, weil 20000km ungefähr die Hälfte des Äquatorumfangs ist. Auch wenn es Orte gibt, die noch etwas weiter entfernt liegen, geben wir hier allen, die sich mindestens 20000 km entfernt befinden eine Ähnlichkeit von 0% aufgrund der weiten Entfernung.
Bei der Fläche setzen wir die Grenze für 0% Ähnlichkeit bei 1 000 000km² Differenz. Selbsterklärend ist die 100% Ähnlichkeit für die Fläche bei einer Differenz von 0 km².
Zwei Gebiete sind ähnlicher je näher der sim - Wert Richtung 0 geht.

Beispiele

|   | Münster | Greven | Deutschland | Polen | Mexiko |
| --- | --- | --- | --- | --- | --- |
| min lon | 7.473785 | 7.5234 | 5.866315 | 14.122971 | -118.6 |
| min lat | 51.840145 | 52.0326 | 47.270111 | 49.002048 | 14.39 |
| max lon | 7.774364 | 7.7556 | 15.041932 | 24.145782 | -86.49 |
| max lat | 52.060024 | 52.152 | 55.099159 | 55.033695 | 32.72 |
| A | 504.6131119 | 211.0094404 | 557792.1616 | 460876.2449 | 3341918.865 |

|   | dist | simdis | simA | **sim** |
| --- | --- | --- | --- | --- |
| Münster - Greven | 15.86379531 | 0.0007931 | 0.000293 | **0,0006** |
| Deutschland - Münster | 213.5518683 | 0.0106776 | 0.5573 | **0,1929** |
| Deutschland - Mexiko | 10236.11386 | 0,5118 | 1 | **0,6745** |
| Deutschland - Polen | 606.9570157 | 0,0303 | 0,0969 | **0,0525** |
