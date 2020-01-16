# Python/Pip 生成、使用requirements

### 生成

推荐使用`pipreqs`生成`requirements`，可避免将所有包索引进来。

#### 安装`pipreqs`

```
pip install pipreqs
```

#### 生成requirements

```
pipreqs <project_folder>
```

会自动在该目录下生成`requirements.txt`，如果文件已存在，需要加参数`-force`强制覆盖。

或者在当前目录下：

```
pipreqs ./
```

#### 常见错误

报错信息：`UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 259: illegal multibyte sequence`

Windows下引发的编码报错，指定编码格式即可

```
pipreqs ./ --encoding=utf8
```



不推荐使用`freeze`（会将环境中所有的包写入）

```
pip freeze > requirements.txt
```



### 使用（安装）

```
pip install -r requirements.txt
```

