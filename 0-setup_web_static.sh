#!/usr/bin/env bash
# The script sets up web servers for web_static deployment

sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Hello World
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "42i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-available/default
sudo service nginx reload
sudo service nginx restart
