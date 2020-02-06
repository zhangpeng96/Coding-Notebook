# SVN 基本操作

### SVN 与 Git 的区别

Subversion(SVN) 是一个开源的版本控制系統，与Git的区别在于Git是分布式版本控制，而SVN是集中式版本控制。相应的，SVN的操作、指令要比Git简化的多，而且没有Git的“暂存区”概念。

### SVN 检出操作（类似 Git 的 Clone）

```shell
> svn checkout svn://example.com/repo --username=user01 folder_name
A    repo/src
A    repo/docs
A    repo/builds
```

### SVN 修改、更新操作（类似 Git 的 add、commit）

与Git不同，SVN没有暂存区，所以修改后的文件可以直接Commit提交。对于新增的文件改动，需要执行`add`操作。

```
> svn add *
A  (bin)  src\splash.jpg
```

显示`A`表明文件已添加。如果要检查文件是否成功添加需执行`status`操作，

```shell
> svn status
?       src\splash.jpg
```

若显示`?`则表明文件未被添加。

> 注：`add *`可能无法添加子目录内的文件，是否需要加`-r`参数还未验证

添加后执行`commit`，完成新版本提交。

```shell
> svn commit -m "已有库存重新整理"
正在发送       README.md
正在增加       new
正在增加 (二进制) src\splash.jpg
正在增加 (二进制) new\post.jpg
传输文件数据....................done
正在读取事务
提交后的版本为 3。
```

### SVN UPDATE操作

与Git不同，SVN在Commit操作后将改动传输给主（远程）仓库，之后需要进行update操作拉取主（远程）仓库的版本信息，使本地信息与之同步。

```shell
> svn update
正在升级 '.':
版本 4。
```

### SVN 其它指令

**log**：查看SVN的提交日志

**info**：查看SVN仓库的详细信息，如副本目录、主仓库（版本库根）、最后修改的信息等等

