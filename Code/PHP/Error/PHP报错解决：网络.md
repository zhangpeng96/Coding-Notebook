# PHP常见报错解决方式



### 网络分类#1

#### 报错信息

`php_network_getaddresses: getaddrinfo failed: Name or servicenot known`

#### 报错环境

Linux (CentOS 7), PHP 7.1.12, Nginx 

#### 原因

PHP主机连不上DNS服务器

#### 解决方案

[^来源]: <https://blog.csdn.net/leyangjun/article/details/78985128>

首先需要ping或telnet该域名是否可以访问，是否能响应。如果无法ping通，说明服务器连接有问题的DNS服务器，需要检查DNS服务器地址的配置情况。如果ping通问题无法解决，按照下列方法执行：

- 检查请求的远程主机是否在本机的`/etc/hosts`中，在`/etc/hosts`文件中手动绑定host

- 检查防火墙的规则，是不是被响应拦截

