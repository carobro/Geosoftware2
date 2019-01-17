# Commands for working with virtualenvwrapper and virtual environments:

## Folgendes muss anscheinend immer ausgeführt werden, bevor mit virtualenvwrapper gearbeitet werden kann:

$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source '/home/cornelia/.local/bin/virtualenvwrapper.sh'

-> Pfad kann auch anders aussehen  


## ZUM IN-DIE-KONSOLE-KOPIEREN
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source '/home/cornelia/.local/bin/virtualenvwrapper.sh'  



## Erstellen eines neuen virtualenvs (hier zendo genannt):
$ mkvirtualenv zendo

## verlassen eines virtualenvs:
$ deactivate

## switchen zwischen verschiedenen environments (hier von irgendwo in zendo reingeswitcht):
$ workon zendo

## löschen eines environments (hierfür darf man sich nicht in entsprechendem befinden):
$ rmvirtualenv zendo




