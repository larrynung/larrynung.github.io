---
title: git - Commit template
date: 2020-05-29 07:04:25
tags: [git]
---

如果 git commit 的 message 想要有一定的規範，可為 git 設定 commit template，設定完後 template 會在 commit 時帶出範本，供編輯修改 commit message。  

<!-- More -->

<br>


要設定 git commit template，我們需先建立範本檔。  

    vim .gitmessage.txt

{% asset_img 1.png %}

<br>


設定範本檔的內容。  

{% asset_img 2.png %}

<br>


然後將範本檔設定到設定檔中。  

    git config commit.template .gitmessage.txt

{% asset_img 3.png %}

<br>


設定好後 commit 時就會自動帶出設定好的範本了。  

    git add .

{% asset_img 4.png %}

<br>


    git commit

{% asset_img 5.png %}

<br>


{% asset_img 6.png %}

<br>


這邊需特別注意一點，如果使用的是 GUI 而非命令列的話，多半範本是不支援註釋的，也就是說如果範本中有使用到註釋，都需自行刪除註釋後才能 commit，不然都會當成 commit message。  

<br>


Link
====
*[一份建议的git commit模板](https://gist.github.com/jmaxhu/8e7fb69a7dcec1b9b953)
*[Git 如何在Commit時加入樣板template的機制](https://ukyoappdev.blogspot.com/2018/03/git-committemplate.html)
*[如何使用 git commit template 與 git hooks 管理團隊的 git log | AllenHsu的技術手扎](https://allen-hsu.github.io/2017/07/02/git-message-template-and-githook/)
*[使用 git commit template 管理 git log - Dev Chill - Medium](https://medium.com/dev-chill/%E4%BD%BF%E7%94%A8-git-commit-template-%E7%AE%A1%E7%90%86-git-log-cb70f95fda2f)
*[3. Git Commit Template · CodeDoesGood/business Wiki](https://github.com/CodeDoesGood/business/wiki/3.-Git-Commit-Template)
*[Git: Write a good commit message for an atomic commit · Hello, World!](http://pre.tir.tw/008/blog/output/git-write-a-good-commit-message-for-an-atomic-commit.html)
*[Karma - Git Commit Msg](http://karma-runner.github.io/0.10/dev/git-commit-msg.html)
*[Git Commit Message Conventions - Google 文件](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit)
