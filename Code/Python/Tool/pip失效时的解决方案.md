# PIP 失效时的解决方案

### 使用 PIP 时报错`No module named pip`

在命令行使用 pip 时出现报错代码`ModuleNotFoundError: No module named 'pip'`，常见于升级 pip 版本发生未知错误后导致 pip 无法使用。

几种解决方案如下

#### 1. 以模块模式启动 pip

```python
python -m pip install -U pip
```

#### 2. 使用`ensurepip`

（未经测试）

```python
python -m ensurepip
```

### 3. 使用`get-pip.py`脚本

在 Anaconda 环境下上述方法均无效，可使用特定的脚本进行安装。在https://bootstrap.pypa.io/网站中下载`get-pip.py`，手动安装即可

```python
python get-pip.py
```



#### 注

`pip`应用的路径一般在`Anaconda\Scripts`或`Python\Scripts`中