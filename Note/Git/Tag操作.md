# Tag 操作

### 列出已有 tag

```shell
git tag
```

### 新建 tag

```shell
git tag tag_name
```

带上参数：`-a`为 tag 名，`-m`为 tag 的备注内容

```shell
git tag -a tagName -m "my tag"
```

在当前的 commit 上打（HEAD）

```shell
git tag -a v1.2
```

在指定的 commit 打 tag

```shell
git tag -a v1.2 9fceb02
```

### 同步 tag

需要的注意的是，tag 并不与 commit 一同同步到远程服务器，需要手动推送，如

```shell
git push origin v1.0
```

或者同步所有 tag
```shell
git push origin --tags
```

### 切换到某个 tag

与分支类似，可以使用`checkout`命令直接切换到指定 tag，此时不位于任何分支，处于游离状态，可以基于这个 tag 创建一个分支。

```shell
git checkout v1.5.8

Note: switching to 'v1.5.8'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at <commit_id> <commit_comment>
```

### 删除 tag

本地删除

```shell
git tag -d v0.1.2 
```

远端删除

```shell
git push origin :refs/tags/v0.1.2
```