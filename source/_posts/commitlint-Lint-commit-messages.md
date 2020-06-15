---
title: commitlint - Lint commit messages
date: 2020-06-13 22:52:26
tags: [git]
---

commitlint 是一檢測 commit message 的工具。

<!-- More -->

<br>


使用上需先全域安裝 commitlint cli。  

    npm install -g @commitlint/cli 

{% asset_img 1.png %}

<br>


加入 package.json。  

    npm init

{% asset_img 2.png %}

<br>


加入套件 @commitlint/config-conventional。  

    npm install -save @commitlint/config-conventional

{% asset_img 3.png %}

<br>


加入 commitlint 設定檔。  

    echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js

{% asset_img 4.png %}

<br>


準備好後可簡易的用 echo 將訊息透過 pipeline 送到 commitlint 做些測試。  

    echo 'foo: bar' | commitlint

{% asset_img 5.png %}

<br>


    echo 'feat: bar' | commitlint

{% asset_img 6.png %}

<br>


若要針對 git commit message 也是可以，這邊直接將當前專案加入 git 版控。  

    git init

{% asset_img 7.png %}

<br>


設定 .gitignore。  

    vim .gitignore

{% asset_img 8.png %}

<br>


將 node_modules 這些不必要版控的部分設定上去。  

{% asset_img 9.png %}

<br>


實際 commit 一個不符合規範的 commit message。    

    git add .

{% asset_img 10.png %}

<br>


    git commit -m "foo: bar"

{% asset_img 11.png %}

<br>


    git log

{% asset_img 12.png %}

<br>


調用 commitlint 並帶入 --from=，commitlint 會去驗證 git commit message。  

    commitlint --from=

{% asset_img 13.png %}

<br>


Link
====
* [commitlint - Lint commit messages](https://commitlint.js.org/#/?id=commitlint-nbsp-)
