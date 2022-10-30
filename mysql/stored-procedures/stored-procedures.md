
Stored Procedure is a sub-program/function which consists of a set of statements stored in the database server. Stored procedures usually consists of a generic code which can be reused at multiple places. We can also pass parameters while calling the stored procedures.

#### Syntax:
```sql
CREATE PROCEDURE sp_name(p1 datatype)
BEGIN
/*Stored procedure code*/
END;
```
## How to call Stored procedure
```sql
CALL sp_name;
```

## How to delete stored procedure
```sql
DROP PROCEDURE sp_name;
```

#### Example:
Consider you are writing a procedure to retrieve all the order details of a particular Customer.
```sql
DELIMITER $$
CREATE PROCEDURE ORDER_SUMMARY(IN customerid Varchar(30) )
BEGIN
SELECT * from ORDERS where CUSTOMERID=customerid;
END$$
DELIMITER ;
```
## How to call Stored Procedure
```sql
CALL ORDER_SUMMARY('C10');
```
#### Result:
|ORDERID|CUSTOMERID|ITEM|BILLAMOUNT|
|---|---|---|---|
|123|C10|Mango|5.00|
