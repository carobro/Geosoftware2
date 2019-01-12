#Commands for working with virtualenvwrapper and virtual environments:

##Folgendes muss anscheinend immer ausgeführt werden, bevor mit virtualenvwrapper gearbeitet werden kann:

$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source '/home/cornelia/.local/bin/virtualenvwrapper.sh'  


ZUM IN-DIE-KONSOLE-KOPIEREN____________________________________
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source '/home/cornelia/.local/bin/virtualenvwrapper.sh'  
_______________________________________________________________
-> Pfad kann auch anders aussehen.


##Erstellen eines neuen virtualenvs (hier zendo genannt):
$ mkvirtualenv zendo

##verlassen eines virtualenvs:
$ deactivate

##switchen zwischen verschiedenen environments (hier von irgendwo in zendo reingeswitcht):
$ workon zendo

##löschen eines environments (hierfür darf man sich nicht in entsprechendem befinden):
$ rmvirtualenv zendo




