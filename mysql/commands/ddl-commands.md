In this sub section, let us learn the usage of below commands with examples.

## 1. CREATE 
CREATE command is used to create a table, schema or an index.
### Syntax:
```sql
         CREATE TABLE table_name (
                column1 datatype,
                column2 datatype,
                ....);
``` 
### Example:
```sql
        CREATE TABLE CUSTOMERS(
            InsuranceID INT,
            Name VARCHAR(50),
            DOB  DATE, 
            NIN INT, 
            Location VARCHAR(255)
        );
```
## 2. ALTER
 ALTER command is used to add, modify or delete columns or constraints from the database table.
        
###    Syntax: 
```sql 
ALTER TABLE Table_name ADD column_name datatype;
```
###    Example:
```sql
 ALTER TABLE CUSTOMERS ADD email_id VARCHAR(50);
```
## 3. TRUNCATE
 TRUNCATE command is used to delete the data present in the table but this will not delete the table.
###    Syntax: 
```sql
TRUNCATE table table_name;
```
### Example: 
```sql
TRUNCATE table CUSTOMERS;
```
## 4. DROP
DROP command is used to delete the table along with its data.

###    Syntax: 
```sql 
DROP TABLE table_name;
```
### Example: 
```sql 
DROP TABLE CUSTOMERS;
```
## 5. RENAME 
RENAME command is used to rename the table name.

###    Syntax:  
```sql
RENAME TABLE table_name1 to new_table_name1; 
```
### Example: 
```sql
RENAME TABLE CUSTOMERS to CUSTOMERINFO;
```
## 6. COMMENT

###  Single-Line Comments: 
Statements starting with `--` are treated as single line comments.
 ###   Example:

 ```sql
  --Line1;
  ```

 ###   Multi-Line comments: 

 Statements enclosed in `/**/` are treated as Multi-line comments

 ```sql
    /* Line1,
    Line2 */
 ````