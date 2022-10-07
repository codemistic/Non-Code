
## The problems faced !

Actually not problems, its more like a social issue for developers 😅😂. . Say for example , that you have worked hard and you developed an application. The application is running smoothly in your machine. But when you send it to production, your co-developers are experiencing errors. Don't worry we developers face it a lot. That is when we yell "the application works well on my machine !! "😅. There may be many reasons for this problem. It may be the issues with
> Frameworks, OS, Versions and libraries, Services.

_We never know .. !_, Some of these in your machine will not be there in the production environment.

Therefore, to solve this problem we need a standardized solution available to every developers.

## Why should we use docker ?





# Getting Started with Docker

- Docker is a container platform which simplifies and accelerates your workflow, while giving developers the freedom to innovate with their choice of tools, application stacks, and deployment environments for each project.
- A container is nothing but a standardized unit of software that allows developers to isolate their app from its environment, solving the “it works on my machine” headache.It is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another
- A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings

## How to install Docker on your machine ?

- Using docker is pretty simple, but for that you need to install Docker on your machines.
- To install for all devices [click me](https://docs.docker.com/get-docker/).
- After downloading the suitable file your device, 
  * Run the program and follow along with the instructions.
- You can verify docker is ready by running the following commands in your terminal :  ```docker -v ``` and ``` docker-compose-v ```
- This is how it should be :



## 10 essential commands a beginner should know![_Pvjt-NEA](https://user-images.githubusercontent.com/91843271/194473414-0c84db40-cc15-4241-83eb-b71b66230e82.png)


These are 10 essential commands a beginner should know, when they are starting to use docker. These commands are those which I think will help beginner get familiarized with docker

### 1 .  docker  images

Docker is all about containers and their images. To check if have  any images in our local machine we can use ```docker images ``` 

If you do not have any images, don't worry   

### 2 . docker  search

We can use the command ```docker search``` to search for public images on the Docker hub. It will return information about the image name, description, stars, official and automated.

```
docker  search name_of_the_image
```

### 3.  docker pull

Once you have searched for the image, we can pull that image from docker hub using the command 
```
docker  pull name_of_the_image
```

for reference , you can always refer the [docker hub](https://hub.docker.com/)


### 4. docker  run

Our main aim is to run a container in our local machine, now that we have some images, we can try to create a container. This command will create a docker container in which * name_of_the_image * will run .
```
docker run the_image
```

### 5 . docker  ps

This command is used to list all the the running containers.
```
docker ps
```

### 6. docker  stop

To stop a running container use the ```docker stop``` command with either the container id or container name. We may stop a container if we want to change our docker run command.

```
docker stop container_id 
```
### 7. docker  restart

Now that we have stopped a container from running, we can use the restart command ``` docker restart  ```  to once again start the container.

``` 
docker restart container_id 
```

###  8 . docker rename

We can rename a docker container to our liking, so that it is more convenience. If we want to change the name from mySQL to dear (  you can use a pretty decent name 😅)
```

docker rename mySQL dear
```

### 9. docker rm

In case we want to remove a container, we can use the following command.
```
docker rm container_id
```
If the container is not stopped then use the stop command followed by the rm command

```
docker stop container_id
docker rm container_id
```
after , if you want to **_free up the memory space _**, we can use 
```
docker rmi container_id
```

### 10 . docker kill

In case, if you want to stop a running container immediately we can use 
```
docker kill container_id
```
You can actually skip the stop command when using the kill command.


#### So, this is the list of 10 useful command for beginners that I found useful. Hope this helped you to get started with docker.

