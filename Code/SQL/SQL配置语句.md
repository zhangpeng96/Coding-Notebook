# SQL 配置语句

### MySQL 创建用户与授权

#### 创建用户

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

- `username`：创建的用户名
- `host`：指定该用户在哪个主机上可以登陆，若是本地用户用`localhost`，若让该用户可以从任意远程主机登陆，使用通配符`%`
- `password`：该用户的登陆密码，可以为空

如

```sql
CREATE USER 'query'@'%' IDENTIFIED BY 'password';
```

#### 更改用户密码

```sql
SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
```

如果是对当前登陆用户修改密码，可以用

```sql
SET PASSWORD = PASSWORD('newpassword');
```

如

```sql
SET PASSWORD FOR 'query'@'%' = PASSWORD('newpwd');
```

#### 删除用户

```sql
DROP USER 'username'@'host';
```

#### 用户授权

```sql
GRANT privileges ON databasename.tablename TO 'username'@'host';
```

- `privileges`：用户的操作权限，如`SELECT`，`INSERT`，`UPDATE`等，若要所有的权限则使用`ALL`
- `databasename`：数据库名
- `tablename`：表名，如果要授予该用户对所有数据库或对应所有表的相应操作权限则可用`*`表示，如`*.*`

如

```sql
GRANT INSERT,UPDATE,SELECT,CREATE ON *.* TO 'admin'@'%';
```

另外每当调整权限后，通常需要执行以下语句刷新权限：
```sql
FLUSH PRIVILEGES;
```

#### 查看用户权限

```sql
SHOW GRANTS FOR 'username'@'host'
```

#### 撤销用户权限

```sql
REVOKE privilege ON databasename.tablename FROM 'username'@'host';
```



### 参考来源

- <https://www.cnblogs.com/zhongyehai/p/10695659.html>