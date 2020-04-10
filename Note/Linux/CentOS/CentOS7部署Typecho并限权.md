# CentOS 7 环境下部署 Typecho 并处理权限问题

近日在使用 CentOS 7（Linux）部署 Typecho 遇到一些问题，尤其是不再直接使用 root 账户管理系统后遇到诸多涉及权限的问题，在这里做好记录，以备后续运维参考。

### 涉及环境

- CentOS 7 (Redhat) （Linux 均可）
- Typecho ，采用 SQLite3 数据库（2014 年之后的版本，PHP 环境 > 5.3）
- 非管理员权限账号

### 下载程序，设置用户与用户组

下载 Typecho，并解压（目录为`/data/www/web/`）

```bash
$ wget http://typecho.org/build.tar.gz
$ tar xvzf build.tar.gz
```

一般来说，浏览器上所有的操作执行是 Web 服务器及 PHP 的进程执行的，它们所在的用户组是 www，因此需要将给定的用户（如 cooler）加入到 www 用户组中，方便权限控制（需要管理权限）

```bash
$ usermod -a -G www cooler
```

输入`id`查询用户，检查是否成功添加

```bash
$ id cooler
uid=1001(cooler) gid=1001(cooler) groups=1001(cooler),1003(www)
```

然后设置 Typecho 目录及文件所在的用户与用户组（需要管理权限）

```bash
$ chown -R cooler:www /data/www/web
```

输入指令`ll`或`ls -l`检查用户与用户组信息

```bash
$ ll
total 1
drwxr-xr-x 8 cooler www 4096 Apr  7 16:20 web
```

检查无误，继续

### 安装前设置权限

由于 Typecho 安装需要在根目录写入`config.inc.php`，在`usr`写入 SQLite3 数据库文件，因此需要较高权限，建议先将整个目录设置为 777 权限

```bash
$ chmod -R 777 /data/www/web
```

然后在浏览器进入网站，正常安装。

### 安装后改回权限

安装完成后将权限改回 文件 644，目录 744（可能需要请求管理权限）

```bash
$ find /data/www/web -type d -exec chmod 744 {} \;
$ find /data/www/web -type f -exec chmod 644 {} \;
```

然而 usr 目录和数据库文件需要更高的权限，再去做修改

```bash
$ chmod 775 /data/www/web/usr/
$ chmod 775 /data/www/web/usr/*.db
```

如果上传文件时遇到文件再将 uploads 设置更高的权限

```bash
$ chmod -R 775 /data/www/web/usr/uploads
```



### 参考链接

- https://github.com/typecho/typecho/issues/686
- https://linux.cn/article-10768-1.html