#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create a fake HTML file
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data

# Define the Nginx configuration file path
nginx_conf="/etc/nginx/sites-available/default"

# Update Nginx configuration using sed
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' "$nginx_conf"

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0
