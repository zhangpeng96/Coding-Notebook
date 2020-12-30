# Debian 常用配置

### 修改 SSH 端口

首先修改配置文件

```shell
$ vi /etc/ssh/sshd_config
```

将文件中`#Port 22`的`#`删去，修改为想要的端口号，保存

执行命令，重启SSH服务

```shell
$ /etc/init.d/ssh restart
```



### 包管理

Debian 常用的包管理有 apt，更新包的指令是

```shell
$ apt-get update
```



### 参考来源

- https://www.jiloc.com/45643.html