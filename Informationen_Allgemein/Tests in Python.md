# Tests in Python (NOTIZEN)

## Optionen

- Unit Tests
- [pytest](https://docs.pytest.org/en/latest/contents.html#toc)

## pytest
die Python Dateien müssen mit test_ anfangen (Konvention)
Beispieldateiname: test_sample.py

Tests werden normalerweise in Python geschrieben.
Dies ist aber theoretisch (zum Beispiel zum Testen einer API) nicht notwendig.

### Inhalt der Datei:
`def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5`

Wenn assertion nicht erfüllt ist, dann schlägt der Test fehl.
Man kann mehrere assertions hintereinander setzen. Sobald ein Test fehlschlägt wird der gesamte Durchlauf beendet.

### Beispiel assertion
assert ret.success, "process should return success"
...

## weitere Funktionen:
script_runner.run -> man kann parameter übergeben, genau wie beim CLI-Tool

pytest --help

pytest --last-failed -> merkt sich den letzten falschen Test -> kann man dann ab diesen test starten lassen

# vorher - nacher Bedingung
um die Umgebung so zu erstellen wie sie für die tests gewollt ist 

## Imports
- pip install pytest
- pip install requests *(for testing the api)*
