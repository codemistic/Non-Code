## 1. Integer Family

| Data Type |	Unsigned Min Value | Unsigned Max Value | Signed 	Min Value | Signed	Max Value |	
| --------- | -------------------- | ------------------ | ----------------- | ----------------- |
| INT	|0	| 4294967295 |	-2147483648 |	2147483647 |
| SMALLINT  | 0	| 65535	| -32768 |	32767|
| MEDIUMINT	| 0	| 16777215 |	-8388608 |	8388607 |
| BIGINT	| 0	| 18446744073709551615| 	-9223372036854775808 |	9223372036854775807 |
| TINYINT	| 0	| 255 |	-128 |	127 |

## 2. FLOAT(d)
where d is number of decimals. If the d value is in between  0-24 then the data type becomes FLOAT() else if the d value is >24 and <53 then the  data type becomes DOUBLE()
## 3. DECIMAL(l,d)
where l is number of digits displayed before the decimal point and d is number of digits after the decimal point. Default value is DECIMAL(10,2).


