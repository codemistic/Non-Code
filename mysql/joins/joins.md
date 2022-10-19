
Joins are used along with SELECT statement when ever there is a need to retrieve data from multiple tables.

Commonly used Joins in MySQL are as follows:

1. INNER JOIN
2. LEFT JOIN
3. RIGHT JOIN
4. CROSS JOIN

Let us consider the below tables for our understanding:


TABLE1: 


|A|Z|
|---|---|
|a|1|
|b|4|
|d|5|


TABLE2:                    

|A|X|
|---|---|
|a|10|
|e|17|
|d|30|

## 1. INNER JOIN
INNER JOIN combines the values from both the tables based on matching criteria.

Below is a basic example of how inner join works:
```sql
SELECT * FROM TABLE1 INNER JOIN TABLE2 where TABLE1.A=TABLE2.A;
```

#### Result:

|A|Z|A|X|
|--|--|--|--|
|a|1|a|10|
|d|5|d|30|

## 2. LEFT JOIN
LEFT JOIN returns all the values from the Left hand table of the condition and returns only the matching values from the second table. The unmatched row values of right hand table will be represented as NULL.
```sql
SELECT * FROM TABLE1 LEFT JOIN TABLE2 ON TABLE1.A=TABLE2.A;
```
#### Result:

|A|Z|A|X|
|---|---|---|---|
|a|1|a|10|
|d|5|d|30|
|b|4|null|null|

## 3. RIGHT JOIN
RIGHT JOIN returns all the values from the right hand table of the condition and returns only the matching values from the left hand table. The unmatched row values of left hand table will be represented as NULL.
```sql
SELECT * FROM TABLE1 RIGHT JOIN TABLE2 ON TABLE1.A=TABLE2.A;
```
#### Result:

|A|Z|A|X|
|---|---|---|---|
|a|1|a|10|
|d|5|d|30|
|null|null|e|17|

## 4. CROSS JOIN
CROSS JOIN matches each row of the first table with every row of the second table.
```sql
SELECT A,Z,X from TABLE1 CROSS JOIN TABLE2;
```
#### Result:

|A|Z|X|
|---|---|---|
|a|1|10|
|a|1|17|
|a|1|30|
|b|4|10|
|b|4|17|
|b|4|30|
|d|5|10|
|d|5|17|
|d|5|30|
