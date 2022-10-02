 <h1 align="center"> Cloud Fundamentals </h1>

## 1. What is Cloud ?
Cloud computing is a domain to make computer system resources available on-demand through few technologies. These resources include services like computing, storage.

###   1.1 Benefits of Cloud :

* Cost Efficient : Cloud is much cheaper than buying your own infrastructure.
* Pay-as-you-go Service : You only have to pay for how much resources you use.
* Flexible : Infrastructure can be modified as per need very quickly.
* Loss Prevention : Cloud Providers works with multiple data centers across the globe creating multiple backups.
* Latency and availability

    and much more….


###    1.2 How is the cloud providing such features ?

    Cloud uses modern technologies like Virtualisation, Hypervisors, Serverless and more which enables it to provide constant service and updates with a lots of features.


###    1.3 Some major Cloud Providers :

* Amazon Web Services - Best for projects and industrial use. It also provides a 12-month free tier subscription (Need credit or debit card for verification).
* Microsoft Azure - Best documentations and great for learning purposes. It provides 100$ credit on azure accounts for students (Need Student mail for verification) and 200$ credit on verification with a card valid for 1 year.
* Google Cloud Platform - Good learning resources and support of Qwiklabs. It can provide you practical experience on vast topics as it consists of many APIs and external services also.

Other Major Providers : DigitalOcean (Major sponser of HacktoberFest), Heroku (By Salesforce), IBMCloud and more.

## 2. Virtual Machine :

For better understanding of Cloud we will first learn about a service provided by Cloud i.e. Virtual Machines.

A VM is an emulation of a real computer that executes programs like a real computer. It’s literally a Virtual Computer. We can configure its RAM, Storage, Networking Services, Processors and Security as per need.

VMs run on top of a physical machine using a “Hypervisor”. Hypervisors will be explained in detail in later sessions and notes.

Architecture of an Virtual Machine

![](https://lh3.googleusercontent.com/xraaiBI85QOMfG0TA5QJ7hMtfh5DbDsA1CDgSfYaYoKB4O8ikmBflH5x_Nl1qXZuw3o948yWXElVYHgraZdktRP50qM7FEcy4HKF-zw4xqUMuan-DU4k1rx2ufYBgH7iceph4TccJJSEUiiGznLqQFaMUAD6oAiI_YvuWjJHGEsVj9kKU-v26iW7fw)

###    2.1 Creating Virtual Machine on AWS :

Step 1 :- Login to your AWS Console at [AWS Console](https://aws.amazon.com/console/)

![](https://lh4.googleusercontent.com/3lNnQe1eZVb9cLF8vCCK1BeObF5p6vgP-xfFUQxCZWp8SCtgqCE2EAD2xDF668uQDbOh3KCk0S0agmtrj8zRouNGXrBs4xfAUr_jNgXDIRayci_WHZHgfqKdBSEODW3ZR3V7x1fA5FlnNKe95w9m8gUqXz5N1UoTF19hTNFg_-3epf1Mti3lNjKoCg)

Step 2 :- Navigate to the top left corner at services and search for EC2.

![](https://lh6.googleusercontent.com/r1FU90_mxqjAeC7JfjzRcsEZ6oqOPjXJq2vKfaWvxPQC2P4XwCkgffEsl7n5bW5RPCCgw2-TH7kivqQgUDDaZrTttEBwzL7TsXmRbNndo5UJKtvMzScr2vUiezOaNr1Vtj64FiqYQT-bPuIlxZuXQqPX6gRyILTjCPLKDApxJYWHutBwLNSdbi8Zug)

Step 3 :- Scroll down and click on the “Launch Instance” option.

![](https://lh4.googleusercontent.com/zkV-D712-y9Vci3ZeVmQwJNKNS0UiiOGBfBY5mMGmgq_hnRvFwSHrT6In83_7YdcHQVLPTUzgnkU8bMG0bdi8T62quMfYJ1BHWV_qUwTtMACLtuUnQ0IS01_OH6TEYOjS7Bk7MlTYN4eUuHlt28NRAHhynlWghzjm4YYfrNS_BC5KgS_MjXVDz2UKw)

Step 4 :- Fill the configuration for Virtual Machine :

---

| Variable                                                        | Detail                                                                                    |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Amazon Machine Image                                            | Operating System and Kernel you want in your VM                                           |
| Instance Type                                                   | Hardware for VM                                                                           |
| Key Pair                                                        | Security Key to Login (Recommended to create new)                                         | 
| Network                                                         | Select Network settings as per need, leave it default if you don’t have any idea over it  |
| Storage                                                         | Configure storage as per need                                                             |

Step 5 :- Click on Launch Button at bottom right corner and your VM will start to build.

![](https://lh4.googleusercontent.com/GOBtqvfiyUvN7RYMUqmO4vMiQr11p8Za0X6IIgUfPRLwvlj67UmU1OpzM-caZGalYMs_KmleS_z_jWkN-FGi_RONKLoi_rYnTpGziQvezVdX6GFzc8HzE8bJu3SQKWwi0k8O9AYHWXaoLSTdMmIj9AmQ7A_F1IkGgsK5FikeqbJ04wiZyHuQuNwH2A)

Step 6 :- Click on “View all instances” and wait for 4 to 5 minutes to initialize the VM.
Step 7 :- Click on Instance name and click connect.**	**

![](https://lh4.googleusercontent.com/-qGWL1HykG6VexzxqSEdF-OPAo4Muy74Rs5BHjsaFXbzaE0CMppccNQb-5e6mmYMYJustFOHsm-dH5ge-PVhvlNfXs0aqFrhkvdwXyoU84oBy0FdpIzQwO8ChjeSuYGtwyN_trxVg0KzkGfpAJIrBnLiAGyzIIxDldPQq0wem7_H-pFopdsdtKw1)

Step 8 :- Click on Connect and a new tab will open with the CLI of our VM.

![](https://lh6.googleusercontent.com/co18j97PIKHoCUMVFmPn2bFBtExkoVYDWEdu3CX-wBCCi1webCFgKDJztXUx5RC8-h6DQNFQWmUgg6nIjpFH-H7eR2Ds9fOBL3Pk8sCT_fnldGYnD-LtN_MaFLPnP9TVLp7mq-YfqrjimkIGOM22_H--EI1IUaG_FerxlJphF4dusIYAWbuiutRI)

Note : VM can also be connected through SSH Clients like putty, which will be thought in further sessions.

Some details :

   EC2 : Elastic Compute Cloud is a compute platform under AWS that provides computation services with over 500 types of Instances (VM) with different processors including Intel, ARM and AMD with support of Linux, Windows and also Mac Images. Also it provides ethernet upto 400GBPS.

As we have a basic idea of cloud computing we can now jump to types of cloud computing :

## Types of Cloud Computing :
* IaaS :- Infrastructure as a Service provides access to hardware to configure systems as per requirements. It provides greatest flexibility and control over whole IT resources. Ex : Servers at Local IT Departments.
* PaaS :- Platform as a Service removes the access of hardware and troubles of infrastructure management and provides a platform to access different resources. PaaS enables one to focus on deployment and application management part rather than handling Infrastructure configurations. Ex : AWS
* SaaS :- Software as a Service is a direct user service where one does not have to think of Infrastructure management nor of application management, services can be directly used through a software. Ex : G-Mail
