# DOM 解析相关用法

## xmltodict 处理 XML 文件

### 解析

```python
xml_dict = xmltodict.parse(res.text)
```

### 基本数据获取

xmltodict 可以将xml转换为 OrderDict 数据类型，与普通dict类型操作相同。

对于 DOM 节点 xmltodict 将其解析为对应维度的 dict，键名为节点名称。

对于某一节点，获得其属性是获得`@属性值`键的 dict 值，获得值是获得`#text`键的dict值。

如下的一条弹幕记录

```xml
<d p="142.57800,1,25,16777215,1558209767,0,899f7b28,16288365831782402">包包这衣服好靓啊</d>
```

获得属性`p`的值：

```python
record['@p']
```

获得节点的值：

```python
record['#text']
```
