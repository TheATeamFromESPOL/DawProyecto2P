sudo -u postgres psql -U postgres -f datosBase/creadorBase.sql
sudo rm -rf SitioDeQuejas/SitioDeQuejas/__pycache__
sudo rm -rf SitioDeQuejas/appQuejas/migrations/*
sudo rm -rf SitioDeQuejas/appQuejas/__pycache__
python3 SitioDeQuejas/manage.py makemigrations appQuejas #Python3 debe estar con la versión 3.6.5, al menos.
python3.6 SitioDeQuejas/manage.py migrate
python3.6 SitioDeQuejas/manage.py shell < SitioDeQuejas/crearUsuarios.py
sudo -u postgres psql -U postgres -f datosBase/base.sql -d appquejas
