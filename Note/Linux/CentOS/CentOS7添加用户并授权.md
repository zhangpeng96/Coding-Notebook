# CentOS 7 添加用户并授权 root 权限

为了保护服务器安全，一般会禁用 root 用户登录，辅之以 root 权限的用户管理，设置如下。

#### 创建用户并授权

创建用户并设置密码

```bash
$ adduser cooler
$ passwd cooler
```

配置`sudoers`文件为用户授权，由于`sudoers`文件是只读的，因此要修改文件读写权限

```bash
$ chmod -v u+w /etc/sudoers
```

然后修改`sudoers`文件，在下面一行中仿照`root`用户添加一行

```bash
$ vi /etc/sudoers
-------------------------------------------------------
## Allow root to run any commands anywhere
root    ALL=(ALL)       ALL
cooler  ALL=(ALL)       ALL
-------------------------------------------------------
```

保存，退出，再将读写权限改回去

```bash
$ chmod -v u-w /etc/sudoers
```

需要注意的是，有的系统没有安装`sudo`（比如 CentOS 7 minimal），因此在`etc`目录中找不到`sudoers`文件，需要手动安装

```bash
$ yum install sudo
......
Installed:
  sudo.x86_64 0:1.8.23-4.el7_7.2

Complete!
```



#### 禁用 root 用户 SSH 登录

修改`sshd_config`文件，将`#PermitRootLogin yes`改为`PermitRootLogin no`即可

```bash
$ vi /etc/ssh/sshd_config
---------------------------------------
PermitRootLogin no
---------------------------------------
```

保存，退出。重启一下 sshd 服务

```bash
$ service sshd restart
```

或者是

```bash
$ systemctl restart sshd
```

这样就不能通过 SSH 登录 root 账号了，如果需要使用 root 账号时，可以在其它用户下切换

```bash
$ su
Password:
```

键入 root 账号的密码后即可切换