---
title: npm - Update npm with powershell
date: 2016-11-13 22:28:21
tags: npm
---

npm 的版本如果過舊要更新版本，除了用 npm install 去安裝更新版本的 npm，也可以用 powershell 去進行更新.  

<!-- More -->

<br/>


先用 npm 安裝 npm-windows-upgrade。  

    Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
    npm install -g npm-windows-upgrade

{% asset_img 1.png %}

<br/>


再呼叫 npm-windows-upgrade，選取要安裝的 npm 版本，然後等待更新完成即可。  

{% asset_img 2.png %}

<br/>
