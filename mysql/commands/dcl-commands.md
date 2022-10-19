In this sub section, let us learn the usage of below commands in detail.

# 1. GRANT
GRANT statement is used to provide access privileges to users to access the database.

## Syntax:
```sql
GRANT privileges ON object TO user;
```

**Note:** Privileges can be SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, ALL. You can also specify combination of these privileges in a statement.


### GRANT Connect to Database

```sql
GRANT CONNECT ON DATABASE database_name TO username;
```

### GRANT Usage on Schema

```sql
GRANT USAGE ON SCHEMA database_name TO username;
```

### Grant access to all tables in the database: 

```sql
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA schema_name TO username;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA schema_name TO username;
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```





### Grant permission to create database:
```sql
ALTER USER username CREATEDB;
```


### Grant superuser access to a user
```sql
ALTER USER myuser WITH SUPERUSER;
```


## 2. REVOKE
 REVOKE statement is used to withdraw the access priviliges given to a user by GRANT statement.

### Syntax:

```sql
REVOKE privileges ON object FROM user;
```

### Example:
```sql
 REVOKE DELETE, UPDATE ON ORDERS FROM customer1;
 ```
