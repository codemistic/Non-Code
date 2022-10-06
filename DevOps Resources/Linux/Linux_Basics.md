# Linux Basics

**Linux** is a family of open-source Unix-like operating systems based on the Linux kernel developed by **Linus Torvalds**. It’s essential for a software developer to at least have an idea of how Linux works and how to use it. In this article, you’ll find some insights into the Linux kernel.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/6nxcimzhqk1fzyety9hs.png)

## Basic Commands

**1. pwd**
The `pwd` command to print the working directory.

**2. ls**
To list the contents of a directory, you use the `ls` command (short for list). When you run the `ls` command without any arguments, it lists the contents of the present working directory by default.

**3. cd**
You can change to a different directory using the `cd` command (short for change directory).

**4. rm**
It is used to remove objects such as computer files, directories, and symbolic links from file systems.

**5. cat**
It reads files sequentially, writing them to standard output. 

## The Linux Directory Structure

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/uhc3hiyfli6efyf9es74.png)

Let's understand the naming conventions.
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/9pq7kvzj7ftxs3b2o53x.png)

## Path

**PATH** is an environmental variable in Linux and other Unix-like operating systems that tells the shell which directories to search for executable files (i.e., ready-to-run programs) in response to commands issued by a user.

There are two basic types of paths:

**1. Absolute path**
It is also known as **full path**. It is the location of a filesystem object relative to the root directory. 

**2. Relative Path**
Relative paths are relative to the present working directory. A list of special relative paths is listed in the table below.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/lhx6jnq3ayrlz02x42kr.png)

## Flags
Linux commands can be tuned to our requirements by providing flags along with the command when calling them. These are usually a hyphen (-) followed by an alphabet eg: -a, -B etc or double-hyphen (--) followed by text eg: --all, --color

**Flags** are a way to set options and pass in arguments to the commands you run. Commands you run will change their behavior based on what flags are set.

But, how will we find a flag for our purpose?


Commands come with a "Manual" as well. We can access it using the `man` command followed by the name of the command we need to see the manual of. For `ls`, we do `man ls` and you will get this-.


![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/o2xc9zdjzocxs87psb3i.png)

* **NAME** - name of the command & short description of what it does

* **SYNPOSIS** - how the command is used

* **DESCRIPTION** - detailed info on the usage of the command

## Linux filesystems

A Linux file system is a structured collection of files on a disk drive or a partition. A partition is a segment of memory and contains some specific data. In our machine, there can be various partitions of the memory. Generally, every partition contains a file system. 

The Linux file system contains the following sections:

* The entire Linux directory structure starting at the top (/) root directory. 
* A specific data storage format (EXT3, EXT4, BTRFS, XFS and so on)
* A partition or logical volume having a particular file system.

The Linux filesystem security model helps to ensure that users only have access to their own files and not those of others or the operating system itself.

The final building block is the software required to implement all of these functions. Linux uses a two-part software implementation as a way to improve both system and programmer efficiency.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/3lng7pe475d2iq9r4cgt.png)

Check [this link](https://opensource.com/life/16/10/introduction-linux-filesystems) for more information.

### Directory structure
In Linux and many other operating systems, directories can be structured in a tree-like hierarchy. The Linux directory structure is well defined and documented in the **Linux Filesystem Hierarchy Standard** (FHS). Referencing those directories when accessing them is accomplished by using the sequentially deeper directory names connected by forward slashes (/) such as /var/log and /var/spool/mail. These are called paths.

##File Permissions

When we used `ls -l` in the terminal, it shows the file permissions. 
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/66xof127dt1dewwyccbd.png)

Let's understand it with a sample output of **ls -lh** which is given below.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/q2sbvci7z4ewewjw5s62.jpg)

For effective security, Linux divides authorization into 2 levels.

1.Ownership

2.Permission

**Ownership of Linux files**

Every file and directory on your Unix/Linux system is assigned 3 types of owners, given below.

* **User:**
A user is the owner of the file. By default, the person who created a file becomes its owner. Hence, a user is also sometimes called an owner.

* **Group:**
A user- group can contain multiple users. All users belonging to a group will have the same Linux group permissions access to the file.

* **Other:**
Any other user who has access to a file. This person has neither created the file, nor he belongs to a usergroup who could own the file. Practically, it means everybody else. Hence, when you set the permission for others, it is also referred as set permissions for the world.

**Permissions**

Linux divides the file permissions into **read**, **write** and **execute** denoted by r,w, and x.
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ymi0wqr6cgrfmz54xnfb.png)
```
**r:** read permission
**w:** write permission
**x:** execute permission
```
Octal values are used to represent permissions.
```
4 -> read permission
2 -> write permission
1 -> execute permission
```
Refer to [this link](https://www.pluralsight.com/blog/it-ops/linux-file-permissions) for more information.

