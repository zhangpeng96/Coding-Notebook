# imgaug

### 安装报错
#### 报错信息

    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "C:\Users\sjiao\AppData\Local\Temp\pip-install-yryv4tgs\Shapely\setup.py", line 80, in <module>
        from shapely._buildcfg import geos_version_string, geos_version, \
      File "C:\Users\sjiao\AppData\Local\Temp\pip-install-yryv4tgs\Shapely\shapely\_buildcfg.py", line 200, in <module>
    
        lgeos = CDLL("geos_c.dll")
      File "d:\code\anaconda\lib\ctypes\__init__.py", line 348, in __init__
        self._handle = _dlopen(self._name, mode)
    OSError: [WinError 126] 找不到指定的模块。
    
    Command "python setup.py egg_info" failed with error code 1 in C:\Users\sjiao\AppData\Local\Temp\pip-install-yryv4tgs\Shapely\
#### 错误原因

imgaug 依赖的 shapely 安装失败或不正确

#### 解决方案

下载对应Python版本的 Shapely，可以在<https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely>查询、下载

```
Shapely, a package for creation, manipulation, and analysis of planar geometry objects based on GEOS.
Shapely‑1.6.4.post1‑cp27‑cp27m‑win32.whl
Shapely‑1.6.4.post1‑cp27‑cp27m‑win_amd64.whl
Shapely‑1.6.4.post1‑cp35‑cp35m‑win32.whl
Shapely‑1.6.4.post1‑cp35‑cp35m‑win_amd64.whl
Shapely‑1.6.4.post1‑cp36‑cp36m‑win32.whl
Shapely‑1.6.4.post1‑cp36‑cp36m‑win_amd64.whl
Shapely‑1.6.4.post1‑cp37‑cp37m‑win32.whl
Shapely‑1.6.4.post1‑cp37‑cp37m‑win_amd64.whl
```

将`whl`文件下载下来，手动安装：

```
PS D:\> python -m pip install .\Shapely-1.6.4.post1-cp36-cp36m-win_amd64.whl
Processing d:\shapely-1.6.4.post1-cp36-cp36m-win_amd64.whl
Installing collected packages: Shapely
Successfully installed Shapely-1.6.4.post1
```

安装成功，再次尝试安装 imgaug 即可

```
PS D:\> pip install imgaug
Collecting imgaug
  Using cached 
……
Installing collected packages: imgaug
Successfully installed imgaug-0.2.9
```

### 参考链接
- <https://blog.csdn.net/qq_16065939/article/details/85080630>







