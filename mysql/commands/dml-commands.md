In this sub section, let us learn the usage of below commands with examples.

## 1. INSERT  
INSERT Statement  is used to insert new records into the database table.
### Syntax:
```sql
INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
```

 Note: Column names are optional.

 ###   Example: 
 Both the below ways are correct.
```sql
     
INSERT INTO CUSTOMERS (InsuranceID, Name, DOB, NIN, Location,email_id) VALUES ('123', 'Mango','2000-01-01','56789','LO','Mango@xyz.com');
INSERT INTO CUSTOMERS VALUES ('123', 'Mango','2000-01-01','56789','LO','Mango@xyz.com'); 
```
## 2. SELECT 
Select statement is used to select data from database tables.

###   Syntax:
```sql
SELECT column1, column2, ...
FROM table_name
[where condition]; 
```
### Example: 
```sql
SELECT * FROM CUSTOMERS; 
```    
## 3. UPDATE 
UPDATE statement is used to modify the existing values of records present in the database table.
   ### Syntax:
```sql
 UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition; 
```
 ###   Example: 
 ```sql
 UPDATE CUSTOMERS SET email_id = 'mango.lo@xyz.com' WHERE InsuranceID='123';
```
## 4. DELETE 
DELETE statement is used to delete the existing records present in the database table.

###    Syntax: 
```sql 
DELETE FROM table_name where condition;
```
###    Example: 
```sql
DELETE FROM CUSTOMERS where InsuranceID='123';
```