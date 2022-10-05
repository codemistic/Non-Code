## Hey everyone, let's talk about:
###-What is Minikube
###-What is kubectl
###-how to install minikube and kubectl
###-creating and starting a minikube cluster

### 🟢 What is Minikube
Minikube is basically one node cluster where the master processes and the work processes run on one node. This node will have a docker container runtime pre-installed so you will be able to run the containers or the pods with containers on this node.

In short, Minikube is a one-node Kubernetes cluster that runs in VirtualBox on your laptop which you can use for testing Kubernetes on your local set-up

### 🟢 What is Kubectl
The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs.

### 🟢 How to install Minikube and Kubectl

Prerequisite: you need a Virtual Machine environment or if you have a docker desktop then it will be fine.
Now for MacOs, I directly used this command:
'brew install minikube'

![](images/image1.png)

If you have a Different OS then click on this link :
link

### 🟢Creating and starting a Minikube cluster
There are some basic commands for Minikube:
minikube start : To start minkube cluster.

![](images/image2.png)


### kubectl get node: to know which pods are running

![](images/image3.png)


### minikube status: to know the status of the cluster.
### minikube delete: to delete minikube cluster.

![](images/image4.png)
