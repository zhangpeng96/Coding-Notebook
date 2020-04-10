# FFmpeg 安装



### CentOS 7

更新源

```bash
yum update -y
```

安装EPEL Release ，因为安装需要使用其他的repo源，所以需要EPEL支持 

```bash
yum install epel-release -y
```
如果出现缺少Code提示，可以执行

```bash
rpm –-import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
```
查看是否成功导入可以执行
```bash
yum repolist 
```
```
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: sjc.edge.kernel.org
 * epel: mirrors.sonic.net
 * extras: mirror.fileplanet.com
 * nux-dextop: mirror.li.nux.ro
 * updates: mirror.fileplanet.com
repo id                   repo name                                              status
!base/7/x86_64            CentOS-7 - Base                                        10,019
*!epel/x86_64             Extra Packages for Enterprise Linux 7 - x86_64         13,291
!extras/7/x86_64          CentOS-7 - Extras                                         419
!nux-dextop/x86_64        Nux.Ro RPMs for general desktop use                     2,702
!updates/7/x86_64         CentOS-7 - Updates                                      2,231
repolist: 28,662

```

导入Code

```bash
rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
```

安装Nux-Dextop源

```bash
rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
```
然后执行安装即可
```bash
yum install ffmpeg
```


### 参考链接

- centos7下yum安装ffmpeg <https://www.jianshu.com/p/5806c9879df9>