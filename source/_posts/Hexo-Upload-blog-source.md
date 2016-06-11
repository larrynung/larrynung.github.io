---
title: Hexo - Upload blog source
date: 2016-06-11 22:11:20
tags: Hexo
---

Hexo 架設完畢後，我們除了要將 blog deploy 上去外，source 的部分也要記得放到版控上面。  

<!-- More -->

<br/>


首先需進到部落格的目錄，初始 git。  

    git init

<br/>


接著設定遠端的 git 位置，這邊如果是用 GitHub，位置的部分就是 GitHub page 的 repository 位置。  

    git remote add origin [repository url]

{% asset_img 1.png %}

<br/>


接著開啟一個新的 branch 去放置 source。  

    git checkout -b [branch]

{% asset_img 2.png %}

<br/>


如果需要，放置 .gitignore 檔在部落格目錄，用以告知 git 要忽略版控的檔案與目錄。檔案內容如下：    

    .DS_Store
    Thumbs.db
    db.json
    *.log
    node_modules/
    public/
    .deploy*/

<br/>


再來要將未版控的檔案加入版控。  

    git add .

<br/>


commit 這次修改。  

    git commit -a -m "[comments]"

<br/>


最後將部落格的 source 送到遠端 repository 即可。  

    git push origin [branch]

{% asset_img 3.png %}

