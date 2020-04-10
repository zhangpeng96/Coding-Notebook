# 使用 SSH 密钥登录 Git 托管平台

### Linux 系统

首先切换到当前用户的`.ssh`目录（如果没有手动创建）

```bash
$ cd ~/.ssh/
```

使用指令随机生成 SSH 密钥，可以输入 passphrase 生成有口令的密钥，也可以不填忽略

```bash
$ ssh-keygen -t rsa -b 4096

Generating public/private rsa key pair.
Enter file in which to save the key (/home/cooler/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/cooler/.ssh/id_rsa.
Your public key has been saved in /home/cooler/.ssh/id_rsa.pub.
The key fingerprint is:
fe:cc:00:8e:00:b2:3d:ec:00:00:00:00:00:00:00:00 cooler@vps
```

最后会生成

- `id_rsa`私钥文件，保留在用户手中，
- `id_rsa.pub`公钥文件，提交给 Git 托管平台用于 RSA 验证功能

密钥指纹可以用作密钥的简单识别，

查看公钥内容，复制公钥全部内容

```bash
$ cat id_rsa.pub
```

进入 Git 托管平台（如 Github，https://github.com/settings/keys），选择 New SSH Key，Key 中填入公钥内容，确认添加就可以使用。如果不再使用该密钥，点 Delete 删除即可。



### 参考链接

- <https://blog.csdn.net/zhangpeterx/article/details/97375233>
- <https://stackoverflow.com/questions/17668283/failed-to-add-the-host-to-the-list-of-know-hosts>