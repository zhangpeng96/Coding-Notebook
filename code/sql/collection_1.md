# SQL查询语句



#### 查询某字段的所有现有数据（分组）并统计数量

```mysql
SELECT
    `modian_id`, COUNT(*)
FROM
    `modian_order` 
GROUP BY `modian_id`
```

查询得到的结果是

| modian_id | COUNT(*) |
| :-------: | :------: |
| 99200558  |    8     |
| 99200559  |    6     |

采用Python相关库通过`fetchall()`得到的是`dict`

```json
[{'modian_id': 99200558, 'COUNT(*)': 8}, {'modian_id': 99200559, 'COUNT(*)': 6}]
```

如果要改`COUNT(*)`的key，可以添加`as <改为的key>`

```mysql
SELECT
    `modian_id`, COUNT(*) as `count`
FROM
    `modian_order` 
GROUP BY `modian_id`
```

查询得到的结果是

| modian_id | count |
| :-------: | :---: |
| 99200558  |   8   |
| 99200559  |   6   |