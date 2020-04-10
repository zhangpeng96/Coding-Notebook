# PHP 常见报错解决



## 网络类问题

### Name or servicenot known

#### 报错信息

```
php_network_getaddresses: getaddrinfo failed: Name or servicenot known
```

#### 报错环境

- Linux (CentOS 7)
- PHP 7.1.12
- Nginx 

#### 原因

PHP 主机连不上 DNS 服务器

#### 解决方案

首先需要 ping 或 telnet 该域名是否可以访问，是否能响应。如果无法 ping 通，说明服务器连接有问题的 DNS 服务器，需要检查 DNS 服务器地址的配置情况。如果 ping 通问题无法解决，按照下列方法执行：

- 检查请求的远程主机是否在本机的`/etc/hosts`中，在`/etc/hosts`文件中手动绑定host

- 检查防火墙的规则，是不是被响应拦截


### 参考链接
- Name or servicenot known <https://blog.csdn.net/leyangjun/article/details/78985128>