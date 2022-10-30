In simpler terms, we can say INDEX is a pointer to some data in a table.INDEXES are very useful in attaining higher performance especially for large databases as it speeds up your search query execution.
Unindexed tables take more time when compared to Indexed tables. For example, you can consider the synopsis of a book as an example for Indexes. You can easily search for a particular topic by referring it's page number in synopsis.  


## 1. CREATE INDEX
CREATE INDEX is used to create an index. INDEXes can be created on multiple columns(if required) of a table. Search query corresponding to INDEX column will be much faster than on other columns.

### Syntax:
```sql
  CREATE INDEX index_name on table_name(column_name);
```

## 2. DROP INDEX
DROP INDEX is used to delete an existing index
### Syntax
```sql
DROP INDEX index_name ON table_name;
```