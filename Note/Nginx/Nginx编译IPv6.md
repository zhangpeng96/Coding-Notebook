

# Nginx 编译使用 IPv6

### 检查现有 Nginx 是否支持 IPv6

首先检查现有的 Nginx 是否支持 IPv6，输入命令

```bash
$ nginx -V

nginx version: nginx/1.16.1
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-39) (GCC)
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: --prefix=/usr/local/nginx --with-http_stub_status_module --without-http-cache --with-http_ssl_module --with-http_gzip_static_module
```

可以看到现有的模块并没有 IPv6 模块`--with-ipv6`，需要重新编译。

### 下载解压 Nginx

官网下载 http://nginx.org/en/download.html，解压

```bash
$ tar xzvf nginx-1.16.1.tar.gz
```

进入目录

```bash
$ cd nginx-1.16.1
```

### 编译 IPv6 模块

在原有的模块基础上加上`--with-ipv6`，

```bash
 ./configure --prefix=/usr/local/nginx --with-http_stub_status_module --without-http-cache --with-http_ssl_module --with-http_gzip_static_module --with-ipv6
checking for OS
 + Linux 2.6.32-042stab123.9 x86_64
checking for C compiler ... found
 + using GNU C compiler
 + gcc version: 4.8.5 20150623 (Red Hat 4.8.5-39) (GCC)
checking for gcc -pipe switch ... found
checking for -Wl,-E switch ... found
......
  nginx http uwsgi temporary files: "uwsgi_temp"
  nginx http scgi temporary files: "scgi_temp"

./configure: warning: the "--with-ipv6" option is deprecated
```

检查，最后报 warning 并没有出错，所以接下来可以编译

```bash
$ make
make -f objs/Makefile
make[1]: Entering directory `/home/sjiao/nginx-1.16.1'
cc -c -pipe  -O -W -Wall -Wpointer-arith -Wno-unused-parameter -Werror -g  -I src/core -I src/event -I src/event/modules -I src/os/unix -I objs \
        -o objs/src/core/nginx.o \
        src/core/nginx.c
cc -c -pipe  -O -W -Wall -Wpointer-arith -Wno-unused-parameter -Werror -g  -I src/core -I src/event -I src/event/modules -I src/os/unix -I objs \
        -o objs/src/core/ngx_log.o \
        src/core/ngx_log.c
......
objs/ngx_modules.o \
-ldl -lpthread -lcrypt -lpcre -lssl -lcrypto -ldl -lpthread -lz \
-Wl,-E
sed -e "s|%%PREFIX%%|/usr/local/nginx|" \
        -e "s|%%PID_PATH%%|/usr/local/nginx/logs/nginx.pid|" \
        -e "s|%%CONF_PATH%%|/usr/local/nginx/conf/nginx.conf|" \
        -e "s|%%ERROR_LOG_PATH%%|/usr/local/nginx/logs/error.log|" \
        < man/nginx.8 > objs/nginx.8
make[1]: Leaving directory `/home/sjiao/nginx-1.16.1'
```

编译完成，进入`objs`目录查看目标文件，

```bash
$ cd objs
```

### 安装替换编译完成的版本

停止 Nginx 服务，对原来 Nginx 备份，用编译好的替换

```bash
$ service nginx stop

$ cp /usr/local/nginx/sbin/nginx /usr/local/nginx/sbin/nginx.bak
/bin/systemctl stop  nginx.service
$ cp nginx /usr/local/nginx/sbin/nginx
cp: overwrite ‘/usr/local/nginx/sbin/nginx’? y
```

执行指令查看已安装的模块，看到`--with-ipv6`表明安装完成
```bash
$ nginx -V
nginx version: nginx/1.16.1
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-39) (GCC)
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: --prefix=/usr/local/nginx --with-http_stub_status_module --without-http-cache --with-http_ssl_module --with-http_gzip_static_module --with-ipv6
```
恢复服务，即可使用。
```bash
$ service nginx start
```


