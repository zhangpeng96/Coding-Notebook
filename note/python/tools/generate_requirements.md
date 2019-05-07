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



不推荐使用`freeze`

```
pip freeze > requirements.txt
```



### 使用（安装）

```
pip install -r requirements.txt
```

