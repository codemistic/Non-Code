
View is a query which is stored in the database to reuse later. Views are nothing but a pseudo table. Views can contain a complex query which retrieves data from multiple tables. So, instead of writing a complex query everytime, you can simply create a view and call it when ever required.

#### Syntax:
```sql
Creating a View:
CREATE VIEW View_name AS 
Query;
```

#### How to call view
```sql
SELECT * FROM View_name;
```
#### Altering a View
```sql
ALTER View View_name AS 
Query;
```
#### Deleting a View
```sql
DROP VIEW View_name;
```
#### Example:
Let us consider the below two tables:
```sql
CREATE TABLE ORDERS(ORDERID INT,CUSTOMERID VARCHAR(50),ITEM VARCHAR(50),BILL_AMOUNT DECIMAL(10,2));
CREATE TABLE ORDER_HISTORY(ORDERID VARCHAR(50),ITEMS VARCHAR(50),BILL_AMOUNT DECIMAL(10,2),DATE_OF_ORDER DATE);

-- creating view
CREATE VIEW ORD_VIEW AS SELECT O.ORDERID,O.CUSTOMERID,H.ITEM,H.DATE_OF_ORDER from ORDERS O INNER JOIN ORDER_HISTORY H; 

-- to display the view
select * from ORD_VIEW;
```
In this way, we can also restrict the visibility of columns of the table to the users.