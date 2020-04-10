# SQL 查询语句



### 将 GROUP 分组后的多条数据的单个字段合并为一条数据

#### 示例数据

#### 用 GROUP_CONCAT 函数合并

`GROUP_CONCAT([DISTINCT] 要连接的字段 [ORDER BY ASC/DESC 排序字段] [separator '分隔符'])`

```sql
SELECT uptime, GROUP_CONCAT(aid SEPARATOR ' ') AS result FROM scheduler GROUP BY uptime;
```

结果

```
uptime	result
10:00:00	95079809
20:00:00	25079809 55079809
```



