# starting zenodo
cd zenodo/
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source ~/.local/bin/virtualenvwrapper.sh
workon zenodo
FLASK_DEBUG=True zenodo run --reload --with-threads