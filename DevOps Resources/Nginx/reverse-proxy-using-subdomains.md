## Table of Contents

- [Table of Contents](#table-of-contents)
- [What is a reverse proxy?](#what-is-a-reverse-proxy)
- [Some benefits of using NGINX as a reverse proxy](#some-benefits-of-using-nginx-as-a-reverse-proxy)
- [Problem Statement](#problem-statement)
- [Installing NGINX](#installing-nginx)
- [Working with the NGINX process](#working-with-the-nginx-process)
- [Editing the config](#editing-the-config)
- [Additional configuration](#additional-configuration)
- [Conclusion](#conclusion)

## What is a reverse proxy?

A reverse proxy is a type of a proxy server that sits inside a private network, behind a firewall and forwards incoming requests to the appropriate upstream backend server. A reverse proxy provides an additional level of abstraction to ensure smooth flow of traffic between multiple clients and servers.

## Some benefits of using NGINX as a reverse proxy

- **Security and Anonymity** : Reverse proxy provides a certain bit of anonymity by protecting the identity or the public IP of our actual backend servers.  It also provides a single point of access for clients to multiple upstream backend servers or services that might be running regardless of the backend network architecture. NGINX also helps in terminating HTTPS traffic from clients, as it can be quite painful to setup/manage TLS in upstream servers individually. 

- **Load Balancing** : NGINX can also be used to load balance incoming requests to a group of backend servers in a manner that maximizes speed and capacity utilization to improve performance, and at the same time provide redundancy in case of server failure. 

- **Caching** : NGINX can also cache static content like images, videos etc to improve response times and reduce the load on the upstream backend servers

## Problem Statement

Assume that there are 2 webservers running in a machine, listening on 2 seperate ports (let's say 8000 and 9000). Now, we would like to access these webservers through 2 different subdomains,(ex: site1.yourdomain.com and site2.yourdomain.com).Exposing such custom ports and asking the users to access our servers using these ports would be a pretty bad idea. We would like to access them over port 80, i.e. HTTP (we can setup HTTPS later), and route the incoming traffic to the appropirate upstream server using NGINX.  

## Installing NGINX

- Update your local package index, so that we have access to the most latest package listings.

        sudo apt update

- Install NGINX

        sudo apt install nginx

- Check whether NGINX is running successfully

        sudo systemctl status nginx

    You should be able to see the status of NGINX as active

        ● nginx - A high performance web, http and reverse proxy server 
        Loaded: loaded (/lib/systemd/system/nginx.service; enabled;)
        Active: active (Nginx server running)

## Working with the NGINX process

Although not super necessary for this tutorial, it is good to be aware of a few basic NGINX process management commands

Command | Description
--- | ---
sudo systemctl stop nginx | stops the running NGINX service
sudo systemctl start nginx | starts the NGINX service
sudo systemctl restart nginx | stops and restars the NGINX service
sudo systemctl reload nginx | reloads the NGINX service without dropping connections (useful for making config changes)
sudo systemctl enable nginx | starts the NGINX service on boot

## Editing the config

In order to configure NGINX, we need to make some changes in the NGINX config file located in ```/etc/nginx/nginx.conf``` . You can use your favourite editor, (Vim/Nano/VSCode) to edit the file.

The config file should look like this 

```
server {
        listen 80;
        server_name site1.yourdomain.com;
        location / {
                proxy_pass http://localhost:8000;
        }
}

server {
        listen 80;
        server_name site2.yourdomain.com;
        location / {
                proxy_pass http://localhost:9000;
        }
```
Then reload the NGINX service in order to load the updated configuration. 

```
sudo systemctl reload nginx
```

Voila, now you can access both the webservers using ```site1.yourdomain.com``` and ```site2.yourdomain.com```

## Additional configuration

By default, NGINX is going to send it's own IP address, host and port to the reverse proxy targets. 

To have NGINX forward the actual IP, port and the protocol to the upstream backend server, add the ```proxy_set_header``` directive, like this

```
server {
        listen 80;
        server_name site1.yourdomain.com;
        location / {
                proxy_pass http://localhost:8000;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-Host $host;
                proxy_set_header X-Forwarded-Port $server_port;
                proxy_set_header X-Forwarded-Proto $scheme;
        }
}

server {
        listen 80;
        server_name site2.yourdomain.com;
        location / {
                proxy_pass http://localhost:9000;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-Host $host;
                proxy_set_header X-Forwarded-Port $server_port;
                proxy_set_header X-Forwarded-Proto $scheme;
        }
```

## Conclusion

This was a very simple, introductory tutorial about NGINX, where we primarily explored it's reverse proxy capabilities. NGINX is a really powerful application and has a lot of other use cases other than acting as a reverse proxy which we discuessed in the previous sections. NGINX is used in multiple mission-critical production deployments, hence you should definately explore it more, if you are an aspiring backend or a devops engineer. 