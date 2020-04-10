# WSGI 服务器相关包

### 使用 wsgiserver 包

#### 安装

```bash
$ pip install WSGIserver
```

#### 使用示例

```python
import wsgiserver

server = wsgiserver.WSGIServer(
    webapp, host = '127.0.0.1', port = 80
)
server.start()
server.stop() 　# 停止
```

#### 存在问题

在实际的使用中发现，使用捕获异常来捕获终止程序的键盘指令是无效的，根本不会触发异常，如下所示：

```python
try:
    server.start()
except (KeyboardInterrupt, SystemExit):
    server.stop()
    print('实例已停止')
```

经过查阅资料，可能与包本身设计缺陷有关，故不推荐使用该包。



### 使用 CherryPy 包的 WSGI 服务器功能

CherryPy 是开源、悠久、成熟的 Web 服务包，含有 WSGI 服务器功能，但在 2017 年后将 WSGI 功能与其它组件抽出组成 Cheroot 包，作为 CherryPy 的前置模块。

#### 安装

安装 CherryPy

```bash
$ pip install cherrypy
```

安装 Cheroot

```bash
$ pip install cheroot
```

#### 使用示例

```python
from cheroot.wsgi import Server as WSGIServer
from cheroot.wsgi import PathInfoDispatcher as WSGIPathInfoDispatcher

webapp = WSGIPathInfoDispatcher({'/': app})
server = WSGIServer(('0.0.0.0', 80), webapp, server_name = 'my_webapp')

if __name__ == '__main__':
   try:
      server.start()
   except KeyboardInterrupt:
      server.stop()
```



### 参考链接

- 可能与 WSGI 的异常捕获无效有关：<https://github.com/mopemope/meinheld/issues/96>
- 消息捕获迂回解决方法（未尝试）：<https://github.com/getsentry/sentry-python/issues/149#issuecomment-434448781>
- CherryPy 示例：<https://helpful.knobs-dials.com/index.php/General_WSGI_notes>
- CherryPy 不含 WSGI 的原因查找：<https://stackoverflow.com/questions/59372836/python-importerror-cannot-import-name-wsgiserver>
- 推荐可用的 WSGI 调用：<https://stackoverflow.com/questions/55366395/how-to-run-a-flask-app-on-cherrypy-wsgi-server-cheroot-using-https>