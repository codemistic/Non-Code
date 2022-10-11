# Installation of MySQL Server on AWS EC2 Instance

## Step 1: Create an EC2 Instance

1. Login to AWS Console
2. Click on EC2
3. Click on Launch Instance
4. Choose an AMI
5. Choose an Instance Type
6. Configure Instance Details
7. Select an existing key pair or create a new key pair
8. Select an existing security group or create a new security group
9.  Select an existing subnet or create a new subnet
10. Select an existing VPC or create a new VPC
11. Select an existing IAM role or create a new IAM role
12. Select an existing Elastic IP or create a new Elastic IP
13. Add tags
14. Add storage
15. Set auto-assign public IP
16. Set termination protection
17. Click on Launch
18. Click on View Instances

## Step 2: Connect to the EC2 Instance

1. Open the terminal
2. Open the folder where the key pair is stored
3. Change the permission of the key pair file
4. Connect to the EC2 instance using the key pair file

## Step 3: Install MySQL Server

1. Update the package list

```bash
     $ sudo apt-get update -y
```

2. Install MySQL Server

```bash
     $ sudo apt-get install mysql-server -y
```

3. Check the status of MySQL Server

```bash
     $ sudo systemctl status mysql
```

4. Check the version of MySQL Server

```bash
     $ mysql --version
```

## Step 4: Configure MySQL Server

1. Login to MySQL Server

```bash
     $ sudo mysql 
```

2. Check User, AUTHENTICATION_PLUGIN, PLUGIN

```bash
     $mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;

```

3. Change the password of MySQL Server

```bash
     $mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

4. Create a new database

```bash
     $mysql> CREATE DATABASE database_name;
```

5. Create a new user

```bash
     $mysql> CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'password';
```

6. Grant privileges to the user

```bash
     $mysql> GRANT ALL PRIVILEGES ON database_name.* TO 'user_name'@'localhost';
```

7. Flush privileges

```bash
     $mysql> FLUSH PRIVILEGES;
```

8. Exit from MySQL Server

```bash
     $mysql> exit
```

## Step 5: Install PHPMyAdmin

1. Update the package list

```bash
     $ sudo apt-get update -y
```

2. Install PHPMyAdmin

```bash
     $ sudo apt-get install phpmyadmin -y
```

3. Select Apache2 as the web server, when the first option is appear, you need to select apache2. Now it hasn’t been selected.
   
4. Use space bar to select apache2 web server. Then press Tab key that takes us to the Ok button. After that, press enter.

5. The next option is to configure the database for PHPMyAdmin with dbconfig-common. Select the Yes option here.

6. Select the MySQL option.
7. Select the Yes option to allow the dbconfig-common to configure the database for PHPMyAdmin with dbconfig-common.
8. Select the password for the MySQL administrative account. After that, password configuration is appear on your terminal screen. And it is asked for login to phpmyadmin. So, you can set your phpmyadmin access password here:

9. Re-enter the password for the MySQL administrative account to confirm it.

## Step 6: Configure PHPMyAdmin

1. Open the config file

```bash
     $ sudo nano /etc/apache2/conf-available/phpmyadmin.conf
```

2. Add the following lines to the config file

```bash
     <Directory /usr/share/phpmyadmin>
     Options FollowSymLinks
     DirectoryIndex index.php
     AllowOverride All
     Require all granted
     </Directory>
```

3. Restart Apache2

```bash
     $ sudo systemctl restart apache2
```

4. Open the browser and type the public IP address of the EC2 instance
5. Open phpMyAdmin
6. Enter the username and password of MySQL Server
7. Select the database
8. Done

## Step 7: Install certbot to enable HTTPS

1. Update the package list

```bash
     $ sudo apt-get update -y
```

2. Install certbot

```bash
     $ sudo apt-get install certbot python3-certbot-apache -y
```

3. Enable HTTPS

```bash
     $ sudo certbot --apache
```

4. Enter the email address
5. Enter the domain name
6. Select the redirect option
7. Select the Yes option to agree the terms of service
8. Done

## Step 8: Disable Firewall (Optional)

1. Check the status of the firewall

```bash
     $ sudo ufw status
```

2. Disable the firewall

```bash
     $ sudo ufw disable
```

3. Check the status of the firewall

```bash
     $ sudo ufw status
```




