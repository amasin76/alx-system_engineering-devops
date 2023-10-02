#!/usr/bin/env bash
# custom http response header

sudo apt -y update
sudo apt -y install nginx

echo "Hello World!" | sudo tee /var/www/html/index.html
new_str="server_name _;\n\trewrite ^\/redirect_me https:\/\/www.github.com\/amasin76 permanent;"
sudo sed -i "s/server_name _;/$new_str/" /etc/nginx/sites-enabled/default

echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html
new_str="listen 80 default_server;\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}"
sudo sed -i "s/listen 80 default_server;/$new_str/" /etc/nginx/sites-enabled/default

sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default

sudo nginx -t
sudo service nginx restart
