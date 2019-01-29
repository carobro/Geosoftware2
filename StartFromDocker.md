# Start Zenodo with Docker, which contains our tool

Because our tool lies on [PyPi](https://pypi.org/project/extractTool/) we added the extractTool version nto the `requirements.txt`from zenodo. So if you want to start zenodo with our extractTool you can follow these Steps:   
   
**1. You must clone our repository**
```bat
$ cd ~/src/
$ git clone https://github.com/corneliazy/zenodo.git
$ cd ~/src/zenodo
$ git checkout master
```   
```bat
$ docker-compose build   
$ docker-compose up
```
Then you can open http://localhost:5000 and you will see an instance of Zenodo.
