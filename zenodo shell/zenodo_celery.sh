# starting celery worker
cd zenodo/
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source ~/.local/bin/virtualenvwrapper.sh
workon zenodo
celery worker -A zenodo.celery -l INFO --purge --loglevel=DEBUG