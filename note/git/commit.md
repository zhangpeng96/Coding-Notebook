# Git的commit相关操作



### 撤销到某个commit（已经同步到GitHub上）

1. 首先查询 commit ID，如现在要丢掉`ADD SNH48-GroupSoul`，那么就回退到`commit ec84c0c109063f5bc3ee158a583888de1d5cd871`

   ```
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

   ```
   $ git reset --hard ec84c0c109063f5bc3ee158a583888de1d5cd871
   HEAD is now at ec84c0c Update README.md
   ```

   执行之后会提示指针现在在`ec84c0c`版本，这时候如果选择的是`--hard`参数，更改过的文件也会改变。

   

3. 执行指令，同步到远程仓库，`--force`可强制覆盖远程仓库，避免出现`rejected`提示。

   ```
   $ git push -u origin master --force
   ```

   ```
    ! [rejected]        master -> master (non-fast-forward)
   error: failed to push some refs to 'git@github.com:zhangpeng96/ECharts-Practice.git'
   hint: Updates were rejected because the tip of your current branch is behind
   hint: its remote counterpart. Integrate the remote changes (e.g.
   hint: 'git pull ...') before pushing again.
   hint: See the 'Note about fast-forwards' in 'git push --help' for details.
   ```

   

4. 执行`push`可能会出现错误提示

   ```
   fatal: 'origin' does not appear to be a git repository
   fatal: Could not read from remote repository.
   
   Please make sure you have the correct access rights
   and the repository exists.
   ```

   可以有下面的解决方法：

   执行指令，将远程仓库上面的文件拉下来，再执行`push`

   ```
   $ git pull origin master
   ```
   如果无效，执行下面指令，再执行`push`即可解决

   ```
   $ git remote add origin git@github.com:zhangpeng96/ECharts-Practice.git
   ```

   成功如下：

   ```
   $ git push -u origin master --force
   Total 0 (delta 0), reused 0 (delta 0)
   To github.com:zhangpeng96/ECharts-Practice.git
    + c89526f...ec84c0c master -> master (forced update)
   Branch 'master' set up to track remote branch 'master' from 'origin'.
   ```



