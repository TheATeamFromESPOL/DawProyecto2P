sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt install python3
sudo apt install python3-pip
alias python=python3
alias pip=pip3
pip install Django==2.1
pip install djangorestframework
pip install markdown
pip install django-filter
pip install djongo
pip install django-bootstrap-form
pip install chartjs
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo apt-get install -y mongodb-org=4.0.1 mongodb-org-server=4.0.1 mongodb-org-shell=4.0.1 mongodb-org-mongos=4.0.1 mongodb-org-tools=4.0.1
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-org-shell hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections
sudo apt-get install libcurl3 openssl
sudo service mongod start
sudo apt-get update
sudo apt install postgresql postgresql-contrib
pip install psycopg2
pip install psycopg2-binary
sudo -u postgres psql postgres 
\password





