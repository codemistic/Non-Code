### What is data ?

To know about database, first you should know about the concept of **data**. Data can be said as a collection of distinct small unit of information. We know that in these times there are loads of data available to us. Most of the data may or may not be important to us. It is important for these data to be stored and to provide it with proper accessibility, maintenance and privacy. So to conclude data can be used in a variety of forms like text, number, media, etc. These data should be stores d somewhere , so for that we use Database

### What is a database?

A **Database**  is an organized collection of data, which can be easily accessed, managed and protected. The data is organized so that any further updation, deletion or any operations on the data can be easily done. It's one of the main advantage of storing data in a database.  That is, a database is a collection of inter-related data which is used to retrieve, insert, read, delete data efficiently.

In a database, a data can be stored or organized in different ways like, table ,schema, views, reports, etc. If large amount of data needs to be stored in a database then it will be quite cumbersome to handle. For, managing such database we have to use Database Software.

There is an approximate of 50 to 70 years of history database. There are many types of databases. Some of them are

- File model
- Document model
- Network model
- Hierarchical model
- Object-oriented model
- Entity-relationship model

### Database Software

**The DBMS (Database Management System) software or the Database Software** provide an interface to perform various operations like creation, insertion, deletion, etc. It provides protection and security. Database software makes data management simpler by enabling users to store data in a structured form and then access it. The data is stored in a centralized way, so that means multiple users can access the data simultaneously.

Some examples of popular database software or DBMSs include

- MySQL
- Microsoft Access,
- Microsoft SQL Server
- FileMaker Pro
- Oracle Database
- dBASE.

### Reference

For more details , or to know more about database use the following links :

1. [Database by oracle](https://www.oracle.com/in/database/what-is-database/#:~:text=A%20database%20is%20an%20organized,database%20management%20system%20(DBMS).)
2. [What is a Database ? ](https://www.techtarget.com/searchdatamanagement/definition/database)
3. [Database](https://intellipaat.com/blog/what-is-database/)
4. [Database - Wikipedia](https://en.wikipedia.org/wiki/Database)



As said a **database** is a collection of organized data or information stored electronically and can be controlled by Database Management System. As said there are different types of users for a database : **Users ** and **Administrators**.

![0712-Bad_Practices_in_Database_Design_-_Are_You_Making_These_Mistakes_Dan_Social-754bc73011e057dc76e55a44a954e0c3](https://user-images.githubusercontent.com/91843271/194546333-dc0d74c0-dbf7-4720-8f68-af13eff39de8.png)

## Who are Database Users ?

Database users are those who make use of the data stored in the database. They can also be said as those who actually make use of the database. They can classified on the basis of their needs and the way in which they access data.
![Database-Administrator-Roles-Responsibilities-Skills-Backgroud-Salary](https://user-images.githubusercontent.com/91843271/194546456-77de07a9-2da8-4e4c-8663-796211d837e4.jpg)

- **Application programmers :**
  They are the developers who actually create or can be said as to interact with the database using [DML queries](https://www.javatpoint.com/dml-commands-in-sql). These queries are written in programs like C, C++,Java, etc.
- **Sophisticated Users :**
  They are database designers. That is, they are developers who write [SQL Queries](https://www.w3schools.com/sql/default.asp) to insert, create, delete data. They directly interact with the database using the query languages. In short we can say that these users are developers and designers of the database.
- **Specialized Users :**
  These are a type of sophisticated users, who develop special application programs on database.
- **Standalone Users :**
  They are users which use the database for their personal use. They also use ready-made database packages.
- **Native Users :**
  They are those who use the existing application to interact with the database.

## Who are Database Administrators ?

The lifecycle of a database starts from designing, implementing to administration of it. The database grows as the data stored increases. As the database grows it should be organized and it should be maintained. If such huge databases are not maintained properly then the performance will comes down. There will be unused memory in database making memory inevitably huge. So this creates a problem for the database users. That's were **Database Administrators** comes in.

The **Database Administrators (DBA)** take care of these functions. A good-performing database is in the hands of the Database Administrator. The DBA  is responsible for upgrading these servers as there are new versions in market and they are responsible for all services of the DBMS. The DBA also provide performance tuning to the database. The administrator should make sure all the  queries and program work correctly. Also the DBA is responsible to provide security for the database as well as for backing up of data. There are various types of administrators on the basis of the responsibility he/she owns :

- **Administrative DBA :** They are mainly concerned with installing and maintaining DBMS servers. They are responsible for keeping backup, installing, recovery, security, replications, memory management, configurations, and tuning.
- **Development DBA :**  They are responsibility is to creating queries and procedures as per the requirement.
- **Database Architect :** They are responsible for creating and maintaining the users, roles, indexes, views, constraints, keys . His/her main responsibility us to design the database  as per the requirement of the user.
- **Application DBA :** They act like a bridge between applications program and the database. He/she ensures all the activities from installing, upgrading, and patching, maintaining, backup, recovery to executing the records work without any issues.


To know about concepts better and to understand concepts we mainly use _visual representations_. They help make development of effective information systems. Similarly for better understanding of database we can define a tree like structure or something similar. In the database we use data models. A **database model** is a type of data model that determines the logical structure of a database.

A **Database model** defines the logical design and structure of a database and defines how data will be stored, accessed and updated in a database management system(DBMS). Among the many database models, the Relational Model is the most widely used database model, there are other models too:

- **Hierarchical Model :** This type of model organizes data  like a tree-like structure. The hierarchy starts from the Root data , and can be made to expand like a tree, which can add child node to the parent nodes. If you data structures, then you can relate it to the tree data structures. It establishes a one-to-many relations between two different types of data.
  ![WyCdooxY3](https://user-images.githubusercontent.com/91843271/194544887-d4eed35c-d681-46bc-a41e-343ecdff0f7c.png)
- **Network Model :** This type of data model organizes data like a graph. It is like an extension to the hierarchical model. This database model was used to map many-to-many data relationships. As the data is more related, accessing the data is also much easier.
  This was the most widely used data model before  relational data model was introduced.
  ![lqt8Rvrfy](https://user-images.githubusercontent.com/91843271/194544863-f5343d3e-31d9-4b0c-b58b-10288ba86bbe.png)
- **Entity-Relationship Model :** E-R Models are defined to represent the relationships into pictorial form to make it easier for different users to understand.
  In this database model, relationships are created by dividing object of interest into entity and its characteristics into attributes. Different entities are related using relationships.

![images](https://user-images.githubusercontent.com/91843271/194545305-f72ebbe3-588e-41ba-ab24-a26c2ddf61bc.jpg)

- **Relational Model :** In these types of model the data is organized in two-dimensional tables  .These relations are maintained by common relational fields. The basic structure of data in the relational model is tables. All the information related to a particular type is stored in rows of that table. Hence, _tables_ are also known as relations in relational model.
  ![download](https://user-images.githubusercontent.com/91843271/194545439-339a21e0-895d-4c78-85c9-1f807042abb8.png)
