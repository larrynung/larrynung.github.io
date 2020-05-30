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

<% asset_img 1.png %>

<br>


設定範本檔的內容。  

<% asset_img 2.png %>

<br>


然後將範本檔設定到設定檔中。  

    git config commit.template .gitmessage.txt

<% asset_img 3.png %>

<br>


設定好後 commit 時就會自動帶出設定好的範本了。  

    git add .

<% asset_img 4.png %>

<br>


    git commit

<% asset_img 5.png %>

<br>


<% asset_img 6.png %>

<br>


這邊需特別注意一點，如果使用的是 GUI 而非命令列的話，多半範本是不支援註釋的，也就是說如果範本中有使用到註釋，都需自行刪除註釋後才能 commit，不然都會當成 commit message。  
