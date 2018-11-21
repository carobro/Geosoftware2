from setuptools import setup
setup(
    name = 'CLI-cli',
    version = '0.1.0',
    packages = ['CLI'],
    entry_points = {
        'console_scripts': [
            // Das was wir in der cmd ausführen habe ich CLI genannt, 
            //und wenn es ausgeführt wird, wird die Hauptfunktion (main Funktion) im Modul __main__ ausgeführt, 
            //welches Teil des Pakets CLI ist.
            'CLI = CLI.__main__:main'
        ]
    })
