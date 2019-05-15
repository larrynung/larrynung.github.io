---
title: Git - Reset local branch to remote state
date: 2019-05-15 08:57:48
tags: [Git]
---

若在本地操作 Git 錯誤，想將本地分支還原到跟遠端分支一樣狀態的話。

<!-- More -->

</br>


可以將遠端分支 fetch 下來。  

    git fetch ${RemoteName} ${BranchName}

</br>


然後強制將本地分支還原至遠端分支的狀態。  

    git reset --hard ${RemoteName}/${BranchName}

</br>


像是筆者這邊不小心做錯，搞出了 Revert Commit。  

{% asset_img 1.png %}

</br>


這時可以像下面這樣調用。  

    git fetch origin source
    git reset --hard origin/source

{% asset_img 2.png %}

</br>


本地分支就會變為跟遠端分支一樣的狀態，本地做錯的動作就會被還原。  

{% asset_img 3.png %}

</br>


Link
----
* [Reset a Branch to Remote State with git](https://davidwalsh.name/reset-branch-remote)
