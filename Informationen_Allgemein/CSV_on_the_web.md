# CSV - CSV on the Web
Tabellendaten sind Daten, die in Zeilen strukturiert sind, von denen jede Informationen zu bestimmten Dingen enthält. 
Jede Zeile enthält dieselbe Anzahl von Zellen (obwohl einige dieser Zellen möglicherweise leer sind), 
die Werte der Eigenschaften der von der Zeile beschriebenen Sache angeben. In Tabellendaten liefern Zellen 
in derselben Spalte Werte für die gleiche Eigenschaft der in jeder Zeile beschriebenen Elemente. 
Dies unterscheidet tabellarische Daten von anderen zeilenorientierten Formaten.

Tabellendaten werden im Web routinemäßig in einem Textformat namens CSV übertragen. 
Die Definition von CSV ist in der Praxis jedoch sehr locker. Einige Leute verwenden 
den Begriff für jede Textdatei mit Trennzeichen. Andere halten sich stärker an die 
Standarddefinition von CSV, die es gibt, [ RFC4180 ]
https://www.w3.org/TR/tabular-data-model/#standards Abschnitt B.1 RFC 4180


## BEISPIEL 2 : CSV-Befehlszeilenverarbeitung mit Spaltentypen
$ csvlint data.csv --datatypes: string, float, string, string
Um das Testen der Werttypen in den Spalten einer CSV-Datei zu ermöglichen, oder mit:

## BEISPIEL 3 : CSV-Befehlszeilenverarbeitung mit einem Schema
$ csvlint data.csv --schema: schema.json


## BEISPIEL 16 : Javascript-Implementierungskonfiguration
Daten . parse ({ "Spaltennamen" : [ "GID" , "on_street" , "species" , "trim_cycle" , "inventory_date" ]),    
   " "datatypes" : [ "string" , "string" , "string" , "string " , " Datum " ], " Formate " : [ null , null , null , null , " M / D / YYYY " ] });      
   { "@type" : "Table" , "url" : "http://example.org/tree-ops.csv" , "tableSchema" : { "Spalten" : [{ "name" : "GID" , " Datentyp " : " string " }, { " name " : " on_street " , " string " },
       " datatype " : " string " }, { " name " : " species " , " datatype " : " string " },{ "name" : "trim_cycle" , "datatype" : 
      { "name" : "inventory_date" , "datatype" : { "base" : "date" , "format" : "M / d / jjjj" } } } }}
       
## Zusammengeführte Metadaten
{ "@type" : "Table" , "url" : "http://example.org/tree-ops.csv" , "tableSchema" : { "Spalten" : [{ "name" : "GID" , " Titel " : " GID " , " Datentyp " : " Zeichenfolge " }, { " Name " : " On_Street " , " Titel " : " On Street " , " Datentyp " : " Zeichenfolge " },{ "Name" : "Spezies" , "Titel" : "Spezies"      
, " Datentyp " : " Zeichenfolge " }, { " Name " : " Trim_cycle " , " Titel " : " Trimmzyklus ", "datatype" : "string" }, { "name"  
: "inventory_date"  , "Titel" : "Inventardatum" , "Datentyp" : { "Basis" : "Datum" , "Format" : "M / T / JJJJ" } } } }}    

## BEISPIEL 19 : http://example.org/tree-ops.csv-metadata.json
{ "@context" : [ "http://www.w3.org/ns/csvw" , { "@language" : "de" }], "url" : "tree-ops.csv" , "dc: title " : " Tree Operations " , " dcat: keyword " : [ " tree " , " street " , " maintenance " ], " dc: publisher " : { " schema: name " : " Beispielgemeinde " , " schema: url " : { " @id ": "http://example.org" } }, "dc: license" :
{ "@id" : "http://opendefinition.org/licenses/cc-by/" }, "dc: modified" : { "@value" : "2010-12-31" , "@type" : " xsd: date " }, " tableSchema " : { " Spalten " : [{ " name " : " GID " , " title " : [ " GID " , " Generic Identifier " ], " dc: description " : " Ein Bezeichner für die Operation an einem Baum. " , " 
}, { "Name" : "on_street" , "Titel" : "On Street" , "dc: description" : "Die Straße , dass der Baum ist." , "datatype" : "string" }, { "name" : "species" , "title" : "species" , "dc: description" : "Die Spezies des Baumes." , "datatype" : "string" }, { "name" : "        
"dc: description" : "Die für den Baum ausgeführte Operation." , "datatype" : "string" }, { "name" : "inventory_date" , "title" : "Inventory Date" , "dc: description" : "Das Datum des durchgeführten Vorgangs." , "datatype" : { "base" : "date" , "format" : "M / d / jjjj" } }], "primaryKey" : "GID" 
        
http://www.greggkellogg.net/2015/04/implementing-csv-on-the-web/
http://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table
       
          
    
     
     

