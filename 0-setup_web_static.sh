#1/usr/bin/env bash
# setup web static server
apt update -y
apt install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "Holberton School" > /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data

NAME=$(uname --all | cut -d ' ' -f 2)
LISTEN=80
ROOT="/var/www/html"
INDEX="index index.html index.htm index.nginx-debian.html"
HEADER="X-Served-By: $NAME"
REDIRECT="return 301 https://lemejiamo.tech"
PAGE_404="/custom_404.html"
HBNB_STATIC="/data/web_static/current/"

default="server {
	listen $LISTEN default_server;
	root $ROOT;
	$INDEX;
	server_name _;
	add_header $HEADER;
	location /redirect_me {
		$REDIRECT;
	}
	error_page 404 $PAGE_404;
	location /hbnb_static/ {
		alias $HBNB_STATIC;
		autoindex off;
	}
}"
echo "$default" > ~/default
mkdir -p /etc/nginx/sites-enabled
mv ~/default /etc/nginx/sites-enabled/default
service nginx restart
exit 0
