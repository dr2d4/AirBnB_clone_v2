#!/usr/bin/env bash
# Install and config nginx
sudo apt update
sudo apt -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "30i location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart