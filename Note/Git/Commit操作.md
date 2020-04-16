# Commit 操作



### 撤销到某个 commit（已经同步到远程仓库上）

1. 首先查询 commit ID，如现在要丢掉`ADD SNH48-GroupSoul`，那么就回退到`commit ec84c0c109063f5bc3ee158a583888de1d5cd871`

   ```bash
   $ git log
   commit c89526fd958e05fa883fa83865ab371d793ea018 (HEAD -> master)
   Author: zhangpeng96 <sjiaomail@gmail.com>
   Date:   Wed May 8 20:33:43 2019 +0800
   
       ADD SNH48-GroupSoul
   
   commit ec84c0c109063f5bc3ee158a583888de1d5cd871
   Author: ZhangPeng <sjiaomail@gmail.com>
   Date:   Wed May 8 20:20:19 2019 +0800
   
       Update README.md
   
   commit 4d415fe67b80fb4038a495335aa6599a09adcb3d
   Author: zhangpeng96 <sjiaomail@gmail.com>
   Date:   Wed May 8 20:19:11 2019 +0800
   
       UPDATE Readme
   ```

   

2. 输入指令回退到相应的版本，注意使用` --hard`参数会抛弃当前工作区的修改；使用`--soft`参数的话会回退到之前的版本，但是保留当前工作区的修改，可以重新提交。

   ```bash
   $ git reset --hard ec84c0c109063f5bc3ee158a583888de1d5cd871
   HEAD is now at ec84c0c Update README.md
   ```

   执行之后会提示指针现在在`ec84c0c`版本，这时候如果选择的是`--hard`参数，更改过的文件也会改变。

   

3. 执行指令，同步到远程仓库，`--force`可强制覆盖远程仓库，避免出现`rejected`提示。

   ```bash
   $ git push -u origin master --force
   ```

   ```bash
    ! [rejected]        master -> master (non-fast-forward)
   error: failed to push some refs to 'git@github.com:zhangpeng96/ECharts-Practice.git'
   hint: Updates were rejected because the tip of your current branch is behind
   hint: its remote counterpart. Integrate the remote changes (e.g.
   hint: 'git pull ...') before pushing again.
   hint: See the 'Note about fast-forwards' in 'git push --help' for details.
   ```

   

4. 执行`push`可能会出现错误提示

   ```bash
   fatal: 'origin' does not appear to be a git repository
   fatal: Could not read from remote repository.
   
   Please make sure you have the correct access rights
   and the repository exists.
   ```

   可以有下面的解决方法：

   执行指令，将远程仓库上面的文件拉下来，再执行`push`

   ```bash
   $ git pull origin master
   ```
   如果无效，执行下面指令，再执行`push`即可解决

   ```bash
   $ git remote add origin git@github.com:zhangpeng96/ECharts-Practice.git
   ```

   成功如下：

   ```bash
   $ git push -u origin master --force
   Total 0 (delta 0), reused 0 (delta 0)
   To github.com:zhangpeng96/ECharts-Practice.git
    + c89526f...ec84c0c master -> master (forced update)
   Branch 'master' set up to track remote branch 'master' from 'origin'.
   ```



### 删除文件相关操作

#### 删除本地文件

```bash
$ git rm <filename>
```

#### 删除文件并修改Git仓库/分支

```bash
$ git rm --cached <filename>
```

这个操作可以删除暂存区或分支上的文件，但是保留本地文件，只是不被版本控制。在下次commit的时候会修改Git仓库。

以上操作，如果要处理的是文件夹可以写为：

```bash
$ git rm -r <folder_name>
```



### 完全删除某个敏感文件（包括在 commit 历史中）

如果不小心上传了某个敏感文件（如含 token、ssh 的文件），采用 `git rm` 指令是无法彻底删除的。需要切换到项目主目录（注意**一定要切换到主目录**，否则会出现路径报错），假如要删除 `./dist/pass.ssh` 文件，输入下面完整的指令，（注意文件路径要**用完整的相对路径**）

```bash
$ git filter-branch --force --index-filter "git rm --cached --ignore-unmatch ./dist/pass.ssh" --prune-empty --tag-name-filter cat -- --all
```

执行，出现 WARNING，按 `Ctrl+C` 可中止操作，忽略则继续执行

```bash
WARNING: git-filter-branch has a glut of gotchas generating mangled history
         rewrites.  Hit Ctrl-C before proceeding to abort, then use an
         alternative filtering tool such as 'git filter-repo'
         (https://github.com/newren/git-filter-repo/) instead.  See the
         filter-branch manual page for more details; to squelch this warning,
         set FILTER_BRANCH_SQUELCH_WARNING=1.
Proceeding with filter-branch...

Rewrite add40dc47521d1bdd957029e14abce2c50000000 (1/125) (0 seconds passed, remains 10 predicted)
```

等进度完成后会提示，已经删除的文件和发生更改的分支

```bash
rm 'dist/pass.ssh'

Ref 'refs/heads/master' was rewritten
Ref 'refs/remotes/origin/master' was rewritten
WARNING: Ref 'refs/remotes/origin/gh-pages' is unchanged
WARNING: Ref 'refs/remotes/origin/master' is unchanged

```

再强制推送到远程仓库，即可完全清除

```bash
$ git push --force
```

需要注意的是，该操作会删除指定文件的本地的版本，必要时请做好备份。

### Commit 提交其它信息

#### 指定 commit 的时间戳

```bash
$ git commit --date="2020-03-19 17:21:00 +0800" -am "修改"
```

### 分支处理

#### 配置远程仓库

```bash
$ git remote add origin https://github.com/user/repo-name.git
```

#### 克隆单个分支

```bash
$ git clone -b branchName https://github.com/user/repo-name.git
```

#### 推送本地仓库到远程分支

>  一般远程主机名为`origin`，本地分支名为`master`

```bash
$ git push <远程主机名> <本地分支名>:<远程分支名>
```



### 将本地的 Git 项目同步到远程 Git 仓库

首先有了本地和远程的仓库，配置完成 SSH key。

进入本地的仓库，执行命令关联远程仓库：

```bash
$ git remote and origin <远程仓库地址>
```

（远程仓库地址使用HTTPS或SSH均可）

然后将本地所有内容推送到远程仓库：

```bash
$ git push -u origin master
```

（注意不要仅仅执行`git push`，这样是无法完全同步的）

如果有遇到问题强制覆盖即可

```bash
git push -u origin master --force
```





---



### 引用

1. 分支项目的单个处理：<https://blog.csdn.net/she_lock/article/details/79453484>
2. 本地项目推送远程分支：<https://blog.csdn.net/qq827245563/article/details/82466521>
