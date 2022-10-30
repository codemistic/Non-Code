
## 1. CHAR(l)
CHAR is a fixed length string data type. Range can be from 0 to 255. Character values are stored with the specified length(l) and they are right padded with spaces.
## 2. VARCHAR(l)
VARCHAR is a variable length string data type. Range can be from 0 to 65,535 but 65,535 is the maximum row length which is shared among all columns. 
## 3. BINARY and VARBINARY 
BINARY and VARBINARY are very similar to CHAR and VARCHAR except that the data is stored as bytes where as the data is stored as characters for CHAR and VARCHAR. BINARY values are right padded with spaces. 

## 4. BLOB and TEXT 
BLOB values are treated as byte strings where as text values are treated as character strings.

| Data Type | Maximum Size Limit |
| --------- | ------------------ |
| BLOB, TEXT | 65,535 |
| TINYBLOB, TINYTEXT | 255 |
| MEDIUMBLOB, MEDIUMTEXT | 16,777,215 |
| LONGBLOB, LONG TEXT | 4,294,967,295 |

