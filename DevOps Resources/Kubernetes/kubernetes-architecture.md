## Hey everyone, Let's talk about KUBERNETES ARCHITECTURE.
And various components of the Kubernetes cluster.

So, is the overall Architecture of the Kubernetes Cluster. Kubernetes cluster contains one Master node/control plane, and one or more 'Worker nodes'.
Every cluster has at least one worker node.
Now let us talk more about the components of a Kubernetes cluster

### Control Plane
- It is also known as the Master node.
- The control plane's components make global decisions
about the cluster (for example, scheduling) and detect
and respond to cluster events.
- Control plane is the entry point for all administrative
tasks.

### kube-apiserver
- The API server is the front end of the Kubernetes control plane.
-API server is like a cluster a gateway which gets the initial requests of any updates into the cluster or even
the queries from the cluster and it also acts as a gatekeeper for authentication.

### etcd
-The consistent and highly-available key-value store is used as Kubernetes' backing store for all cluster data.
-If your Kubernetes cluster uses etcd as its backing store, make sure you have a backup plan for those data.
NOTE: etcd does not store the application data.

### kube-Scheduler
-Control plane component that watches for newly created Pods with no assigned node, and selects a healthy node for them to run on.
-If there are no nodes, then the pods are put in a pending state until a healthy node becomes free.

### kube-controller-manager
When pods die on any node there must be a way to detect that node died and then reschedule those pods as soon as possible so what the CONTROLLER MANAGER does is detect state changes like the crashing of pods.
For example so when pods die, the controller manager detects that and tries to recover the cluster state as soon as possible and for that, it makes a request to the scheduler to reschedule those dead pods.

### Worker Node
- Worker Node is the place where the application is running.
-The worker node host the pods that are the components of the application workload.
-In the Kubernetes cluster there must be at least one worker node.

### kubelet
-An agent that runs on each node in the cluster.
-It makes sure that containers are running in a Pod.
-The kubelet doesn't manage containers which were not created by Kubernetes.

### kube-proxy
-kube-proxy is a network proxy that runs on each node in your cluster, implementing part of the Kubernetes Service concept.
-It ensures each pod gets a unique IP address and makes it possible that all containers in a pod to share a single IP.

### Container runtime
-The container runtime is the software that is responsible for running containers in the pods.
-Kubernetes supports several container runtimes like Docker and CRI-O.
