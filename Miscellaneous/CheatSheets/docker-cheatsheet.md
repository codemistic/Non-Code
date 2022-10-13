# Docker Cheatsheet

This cheatsheet is a collection of useful docker commands along with a short explanation of what they do. 

## Table of Contents

- [Docker Cheatsheet](#docker-cheatsheet)
  - [Table of Contents](#table-of-contents)
  - [Container Management](#container-management)
  - [Container Inspection and Interaction](#container-inspection-and-interaction)
  - [Networking](#networking)
  - [Volumes](#volumes)


## Container Management

Command | Description | Documentation Link
--- | --- | ---
docker build [OPTIONS] | builds docker images from a ```Dockerfile``` | https://docs.docker.com/engine/reference/commandline/build/ 
docker run [OPTIONS] IMAGE [COMMAND] [ARG...] | creates a container from a specified IMAGE and then runs it | https://docs.docker.com/engine/reference/commandline/run/
docker create [OPTIONS] IMAGE [COMMAND] [ARG...] | creates a container from a specified IMAGE without running it | https://docs.docker.com/engine/reference/commandline/create/
docker start [OPTIONS] CONTAINER [CONTAINER...] | starts one or more stopped CONTAINERS | https://docs.docker.com/engine/reference/commandline/start/
docker stop [OPTIONS] CONTAINER [CONTAINER...] | stops one or more running CONTAINERS | https://docs.docker.com/engine/reference/commandline/stop/
docker kill [OPTIONS] CONTAINER [CONTAINER...]| kills one or more running CONTAINERS by sending the main process inside the container a ```SIGKILL``` signal | https://docs.docker.com/engine/reference/commandline/kill/
docker restart [OPTIONS] CONTAINER [CONTAINER...] | restarts one or more CONTAINERS | https://docs.docker.com/engine/reference/commandline/restart/
docker rm [OPTIONS] CONTAINER [CONTAINER...] | destroys one or more CONTAINERS | https://docs.docker.com/engine/reference/commandline/rm/


## Container Inspection and Interaction

Command | Description | Documentation Link
--- | --- | ---
docker ps [OPTIONS] | list all running containers. (to list all containers, use the ```-a``` flag) | https://docs.docker.com/engine/reference/commandline/ps/
docker logs [OPTIONS] CONTAINER | batch-retrieves logs present at the time of execution. | https://docs.docker.com/engine/reference/commandline/logs/
docker inspect [OPTIONS] | provides a detailed low-level information on constructs controlled by Docker. | https://docs.docker.com/engine/reference/commandline/inspect/
docker exec [OPTIONS] CONTAINER COMMAND [ARG...] | runs a new command in a running container | https://docs.docker.com/engine/reference/commandline/exec/
docker attach [OPTIONS] CONTAINER |  attaches your terminal’s standard input, output, and error (or any combination of the three) to a running container using the container’s ID or name. | https://docs.docker.com/engine/reference/commandline/attach/

## Networking

Command | Description | Documentation Link
--- | --- | ---
docker network create [OPTIONS] NETWORK | creates a new ```BRIDGE``` network by default | https://docs.docker.com/engine/reference/commandline/network_create/
docker network ls [OPTIONS] | lists all the networks the Engine ```daemon``` knows about | https://docs.docker.com/engine/reference/commandline/network_ls/
docker network inspect [OPTIONS] NETWORK [NETWORK...] | returns information about one or more networks(by default in a JSON format) | https://docs.docker.com/engine/reference/commandline/network_inspect/
docker network rm NETWORK [NETWORK...] | removes one or more networks by name or identifier | https://docs.docker.com/engine/reference/commandline/network_rm/

## Volumes

Command | Description | Documentation Link
--- | --- | ---
ddocker volume create [OPTIONS] [VOLUME] | creates a new volume that containers can consume and store data in | https://docs.docker.com/engine/reference/commandline/volume_create/
docker volume ls [OPTIONS] | lists all the volumes known to Docker | https://docs.docker.com/engine/reference/commandline/volume_ls/
docker volume inspect [OPTIONS] VOLUME [VOLUME...] | returns information about a volume(by default in a JSON  array format) | https://docs.docker.com/engine/reference/commandline/volume_inspect/
docker volume rm [OPTIONS] VOLUME [VOLUME...] | removes one or more volumes. (Note: Volumes that are already in use by a container cannot be removed) | https://docs.docker.com/engine/reference/commandline/volume_rm/
