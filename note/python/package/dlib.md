# dlib

dlib在安装时需要使用cmake、boost手动编译dlib，可能会因为版本引发各种问题，推荐直接安装已编译的版本（.whl）

### 安装face recognition

```bash
pip install face_recognition  -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 安装dlib 19.17.0

下载地址：<https://pypi.org/project/dlib/19.17.0/#files>

pypi没有19.17.0的编译版本，可以使用编译好的版本（Python 3.6，win64位），直接安装：

<https://github.com/pzx521521/dlib-Python_whl_19.17.0_win_amd64/releases/tag/19.17.0>

```bash
pip install dlib*.whl
```



### 其它安装方法

python3.7成功安装dlib库（亲测成功喔）：<https://blog.csdn.net/sinat_38530349/article/details/86742523>

Anaconda安装Dlib库：<https://blog.csdn.net/weixin_44088439/article/details/87177561>