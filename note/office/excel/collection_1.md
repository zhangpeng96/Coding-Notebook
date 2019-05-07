# Excel 公式



#### 将timestamp转换为Excel日期时间格式

```
=(A1+8*3600)/86400+70*365+19
```



#### 删除单元格的换行符（及非打印字符）

```
=CLEAN(A1)
```



#### 返回匹配字符串模式（通配符）的位置后`length`长度的字符

```
=MID(A1,SEARCH("project/*.html",H1)+8,<length>)
```

