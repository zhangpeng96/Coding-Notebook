# Branch 操作

### 合并冲突解决

当出现合并冲突后，需要人工解决冲突。这时 Git 会在冲突的文件中做出标记，如下文件

```prolog
three_card_poker(M, N, Winner) :-
  nb_setval(bags, M),
<<<<<<< HEAD
  repeat(N, _, _),
=======
  repeat(N, Bag1, Bag2),
>>>>>>> 0f20004cfe61114485fccc298643002880000000
  nb_getval(winner, Winner).
```

`<<<<<<< HEAD` 与`>>>>>>> 0f20004cfe61114485fccc298643002880000000`包围的就是产生冲突的代码段，以`=======`分割两个不同的版本

上面的代码是 HEAD 版本也就是当前版本的更改

```prolog
  repeat(N, _, _),
```

下面的代码时 commit 为 0f20004cfe61114485fccc298643002880000000 的版本的更改

```prolog
  repeat(N, Bag1, Bag2),
```

这时候需要人工删改决定如何解决冲突，比如选择采用如下代码，
```prolog
  repeat(N, _, _),
```

那么保留该代码，**删除**剩下的内容**包括 Git 的冲突标记**，

```prolog
three_card_poker(M, N, Winner) :-
  nb_setval(bags, M),
  repeat(N, _, _),
  nb_getval(winner, Winner).
```

保存，将改动加入到暂存区，提交 commit，推送到远程仓库，按照正常的流程即可。