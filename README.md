# Geosoftware II - WiSe 2018/19
### Enhancing discovery of geospatial datasets in data repositories

:arrow_forward: Die Gruppe :one:   
# Zenodo - Installation:      
For Zenodo installation, please follow the instructions below: 
https://github.com/zenodo/zenodo/blob/master/INSTALL.rst   
(Who wants to save time, should not try is under Windows.   
 On Linux its much faster and easier :wink: )

# CLI-Tool   
## Installation Description   
This installation was previously tested only with Linux, but should also work under Windows.   
pip for pip install is required.   
To run our CLI tool, the following file must be executed in the project folder:   
   
`pip install -r requirements.txt --user` (or `sudo pip install -r requirements.txt`)   
   
In this file all required plugins are listed, which we use in our tool.      

In addition, the following commands must be executed:    
`apt-get install python-gdal`   
`apt-get install gdal-bin`   

`pip install pytest`   
      
Then you can navigate in any common console in the folder of the tool ("Metadataextraction") and
there, the following command must be executed   

`python detailebenen.py --path="Der Path zur Datei"`

behind it can still be added specifications:

`--bbox` &larr; for the bounding box of the file (is also set as default)
`--feature` &larr; to get all the coordinates of the file
`--single` &larr; to get only the coordinates of a file (also default)
`--whole` &larr; in combination with --bbox or --feature to read the respective one from an entire directory
`--time` &larr; to get the time of a file

# similarity calculation

Our similarity calculation code can be found in the `similar.py`file.
The associated tests are in the `test_similar.py` file.

# Tests

Our tests can be executed with the command `pytest`    

# Problems?
If problems or questions arise during installation, create an issue directly so we can help you and correct mistakes :blush:
