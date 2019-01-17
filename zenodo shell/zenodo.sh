gnome-terminal -- bash ./zenodo_docker.sh &
echo "zenodo docker-service started"
sleep 2
gnome-terminal -- bash ./zenodo_celery.sh &
echo "zenodo celery-worker started"
sleep 2
gnome-terminal -- bash ./zenodo_run.sh &
echo "zenodo instance started"
sleep 2
gnome-terminal -- bash ./zenodo_venv.sh