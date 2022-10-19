# Installation on Linux

## Using Yum

* Download the required version from [MySQL Repository](https://dev.mysql.com/downloads/repo/yum/)
* Install the downloaded release package with the below command, replace platform-and-version-specific-package-name with the name of the downloaded package:
```shell
shell> sudo rpm -Uvh platform-and-version-specific-package-name.rpm
```
* Install using below command
```shell
shell> sudo yum install mysql-community-server
```
* Start Mysql Server
```shell
shell> sudo service mysqld start
```
* Check status of the MySQL server
```shell
shell> sudo service mysqld status
```
# Installation on Windows

* Installation on windows is much easier using [MySQL Installer](http://dev.mysql.com/downloads/installer/)
* If you want to use online installation version, download mysql-installer-web-community.exe else mysql-installer-community.exe.
* Run the above executable file and the setup will walk you through the trivial process.
* select the Setup type based on your requirement among Developer default or server only or Client only or Full or Custom. 
* Configure the MySQL Server by providing port number, password etc.
* Installation will take few minutes to complete.
