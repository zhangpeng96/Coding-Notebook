# SQL查询语句



#### 查询某字段的所有现有数据（分组）并统计数量

```mysql
SELECT
    `modian_id`, COUNT(*)
FROM
    `modian_order` 
GROUP BY `modian_id`
```



