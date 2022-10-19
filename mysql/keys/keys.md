let's consider the below two tables to understand the different keys present in SQL. 

#### Table 1: 
customer(InsuranceID, Name, DOB, NIN, Location)

#### Table 2: 
patient(HospitalID, Name, DOB, InsuranceID)

## 1. Primary key 
Primary key is a column or set of columns which is used to uniquely identify a row in the database table. In the above customer table, You can either choose InsuranceID or National Insurance Number(NIN) as primary keys, but Insurance ID is preferable as NIN can be considered as personal information.
## 2. Super key 
Super key is a superset of Primary key with other columns. In the above customer table, InsuranceID+Name can be a Super key. 
## 3. Foreign key 
Foreign key is a column in one table which references a primary key in other table. In the above two tables, InsuranceID of patient table can be considered as a foreign key which can be pointed to InsuranceID in customer Table.
## 4. Unique key 
Unique key is a column or set of columns which is used to uniquely identify a row in the database table. 

Unique key is similar to primary key but differs in  below cases.
* Unique key accepts only one null value where as primary key can never be null.
* There can be multiple unique keys in a table where as primary key should be only one.
* Primary key creates a clustered index where as unique key creates a non-clustered index. 
## 5. Candidate key: 
Candidate key is a column or set of columns which are eligible to become a primary key. In the customer table, InsuranceID and NIN can be candidate keys. As InsuranceID is a primary key, NIN can be a candidate key.
