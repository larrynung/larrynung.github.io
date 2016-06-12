---
title: Hexo - Restore blog envirement from remote repository
date: 2016-06-12 19:02:14
tags: Hexo
---

要從遠端 repository 還原 blog 撰寫的環境，我們需先確定 Hexo 需要的環境是否已經準備妥當（是否有安裝 git？是否有安裝 Node.js？是否有安裝 hexo-cli？）。  

<!-- More -->

<br/>


Hexo 需要的環境準備好後，可將 repository 的資料 clone 下來。  

    git clone [repository url] [folder]

<br/>


接著進到 clone 下來的目錄。  

    cd [folder]

<br/>


切換 branch 至 source 放置的 branch。  

    git checkout [branch]

<br/>


再還原 npm 的套件即可。  

    npm install

<br/>


後續如果有需要，都可從 remote repository 更新 source。

    git pull origin [branch]  
