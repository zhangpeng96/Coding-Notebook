# SQL 删除语句

### 清空某个表格

清空表格`weather_data`并重制编号（SQLite）

```sqlite
DELETE FROM weather_data;
UPDATE sqlite_sequence SET seq = 0 WHERE name = 'weather_data';
```

