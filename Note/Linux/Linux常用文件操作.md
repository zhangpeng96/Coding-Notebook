# Linux 常用文件操作



### 利用节点号删除文件名乱码的文件

首先列出当前目录下各个文件的节点号，找到要删除的文件节点号

```shell
$ ls -i
```

得到如下所示的结果

```shell
408271 blackboard.html  408378 ????.md                                393839 test.html
395590 index.html
```

要删除`????.md`文件，节点号为`408378`

#### 用`find`命令删除

文件会直接被删除，不会询问是否删除

```shell
$ find ./* -inum 408378 -delete
```

#### 用`find`命令调用`rm`命令删除

会询问是否删除，确认后删除

```shell
$ find ./* -inum 408378 -exec rm -i {} \;
```

加上`-rf`后不会提示，文件直接被删除

```shell
$ find ./* -inum 393984 -exec rm -rf {} \;
```





### 参考来源

[linux下利用inode(i节点号)删除指定文件_performance-CSDN博客](https://blog.csdn.net/realdonaldtrump/article/details/78173829)

[Linux使用inode(i节点号)删除文件 - 春告鳥 - 博客园 (cnblogs.com)](https://www.cnblogs.com/Cl0ud/p/12210707.html)