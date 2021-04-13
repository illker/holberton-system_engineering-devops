# Add a custom HTTP header with Puppet

exec { 'eNginx':
    command  =>'apt-get -y update && sudo apt-get -y upgrade && apt-get -y install nginx
    && ufw allow 'Nginx HTTP' && "Holberton School" > /var/www/html/index.nginx-debian.html
    && sed -i "/server_name _;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
    && service nginx restart',
}


