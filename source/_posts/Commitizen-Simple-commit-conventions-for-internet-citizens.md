---
title: Commitizen - Simple commit conventions for internet citizens
date: 2020-06-11 07:59:27
tags: [git]
---

Commitizen 可輔助 git 操作人員使用 commit message 的規範。  

<!-- More -->

<br>


使用上先全域安裝 commitizen 命令列工具。  

    npm install -g commitizen

{% asset_img 1.png %}

<br>


這邊準備一個 git 版控的專案。  

    git init

{% asset_img 2.png %}

<br>


加入 package.json。  

    npm init

{% asset_img 3.png %}

<br>


調用命令讓專案符合 commitizen friendly。  

    commitizen init cz-conventional-changelog --save-dev --save-exact

{% asset_img 4.png %}

<br>


將修改加入版控實際做個測試。  

    git add .

{% asset_img 5.png %}

<br>


commit 時改用 git cz，會改成用互動方式輸入符合規範的 commit message。  

    git cz

{% asset_img 6.png %}

<br>


    git log

{% asset_img 7.png %}

<br>


Link
=====
* [Commitizen by commitizen](http://commitizen.github.io/cz-cli/#making-your-repo-commitizen-friendly)
