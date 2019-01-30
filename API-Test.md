# API Test fuer die zenodo Entwicklungsumgebung

### 1 Testen der records API

http://localhost:5000/api/records/

Diese ist von zenodo vorgegeben, wird aber durch unsere Bereitstellung der Bounding Box ergaenzt.
Standardmaessig werden die letzten 10 gepublishten Records in der API angezeigt. 

![Alt-Text](API-Images/Screenshot from 2019-01-30 04-33-44.png)

http://localhost:5000/api/records/[ID]

Ueber die ID kommt man auf die einzelnen Ansichten der Records.

![Alt-Text](API-Images/Screenshot from 2019-01-30 04-32-55.png)

http://localhost:5000/api/records/[ID]/similar

An diese ID wird dann noch der Suffix similar gehaengt um auf den Similarity endpunkt zu gelangen.

![Alt-Text](API-Images/Screenshot from 2019-01-30 04-33-44.png)

### Tests

__sollten nicht durchgehen:__<br>
http://localhost:5000/api/records/[ID]/similar?size <br>
http://localhost:5000/api/records/[ID]/similar?size= <br>
http://localhost:5000/api/records/[ID]/similar?size=langweilig <br>
http://localhost:5000/api/records/[ID]/similar?size=10000 <br>

__sollten durchgehen:__<br>
http://localhost:5000/api/records/[ID]/similar?size=0 <br>
http://localhost:5000/api/records/[ID]/similar?size=1 <br>
http://localhost:5000/api/records/[ID]/similar?size=20 <br>