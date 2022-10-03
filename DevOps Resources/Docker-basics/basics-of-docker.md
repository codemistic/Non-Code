<h1 align="center"> Containerization and Basics of Docker </h1>

If you’ve ever wondered how to run multiple operating systems concurrently on a single laptop/PC without having to worry about failures, Docker is here to help.

It's likely that as a techie, you’ve heard of docker. If you haven’t, there’s no better time than now.


To summarize docker in one picture: 
 
<p align="center">
  <img width="660" height="400" src="https://images.unsplash.com/photo-1605745341112-85968b19335b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80">
</p>

If you lookup docker on google it reads:  
 *Docker is a set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers.*  
That’s a lot to digest, right ? How about a bit of history on why it’s needed? 

Previously, there was only one system. Anybody who wanted to use it had to travel to that particular location and use it, while others had to wait. Clearly, this was inefficient. This led to the introduction of ***"virtualization"***.

## What is virtualization and why is it needed?
The term virtualization refers to creating a virtual representation of computer hardware. Data transfer becomes faster, system failures are prevented, costs are reduced, and data is saved. As a result of virtualization, development and operations teams are more efficient since they do not need to build physical systems. In service to this, in the 1960s, IBM came up with a ***hypervisor***.


## What is a hypervisor?
A hypervisor is computer software, firmware or hardware that partitions the resources of a CPU among independent programs or multiple operating systems. In this system, you can install numerous virtual machines (VMs), which are essentially other operating systems or applications. 
This sounds excellent, but the problem remains that you need those resources allocated to it, meaning it’s heavy, expensive and bulky. To tackle this problem, ***docker*** was introduced in 2013.

<p align="center">
  <img width="660" height="400" src="https://user-images.githubusercontent.com/38884247/193451099-665248f3-41b3-4bcf-838b-0ddf96596682.png" />
</p>

## What is docker?
In simpler terms, just like in the hypervisor, we virtualize the hardware, in docker, we virtualize the operating system. So essentially we have our local operating system in which we install “docker”, on top of which you can install various applications(OS, Databases etc) which are stored in ***containers***.


## What are containers?
A docker container is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings. Containers take up less space than VMs (container images are typically tens of MBs in size), can handle more applications and require fewer VMs and Operating systems.
<p align="center">
  <img width="660" height="400" src="https://www.docker.com/wp-content/uploads/2021/11/docker-containerized-appliction-blue-border_2.png">
</p>


### So why use docker?
1. *Consistent & Isolated Environment*:
	It does not depend on other containers for resources meaning you can run multiple containers without hassle.
2. *Rapid Application Deployment*:
    The docker containers come up with the minimal runtime requirements of the application that allows them to deploy faster. To illustrate, my old laptop (which has only 4GB RAM) has deployed applications faster with Docker than with pretty much any other option.

3. *Better Portability*:
   The applications created with Docker containers are immensely portable. The Docker containers can run on any platform whether it be Amazon EC2, Google Cloud Platform, VirtualBox, Rackspace server, or any other – though the host OS should support Docker. As the application and all its dependencies are packaged together in a Docker container – you can deploy it to any system that supports Docker and the application will perform similarly. So no more compatibility issues.

4. *It’s open-source*:
     I don’t think any explanation is required. Tons of people are working on this open-source project. The support you get from the community is truly amazing.

These are only a few of its varied advantages.

So what’s stopping you from installing docker?
Look at the [official documentation](https://docs.docker.com/get-docker/) on its installation.
