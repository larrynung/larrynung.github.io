---
title: "commitlint - Lint commit messages"
date: "2020-06-13 22:52:26"
tags: [git]
---


commitlint 是一檢測 commit message 的工具。

<!-- More -->

<br>


使用上需先全域安裝 commitlint cli。  

    npm install -g @commitlint/cli 

![1.png](1.png)

<br>


加入 package.json。  

    npm init

![2.png](2.png)

<br>


加入套件 @commitlint/config-conventional。  

    npm install -save @commitlint/config-conventional

![3.png](3.png)

<br>


加入 commitlint 設定檔。  

    echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js

![4.png](4.png)

<br>


準備好後可簡易的用 echo 將訊息透過 pipeline 送到 commitlint 做些測試。  

    echo 'foo: bar' | commitlint

![5.png](5.png)

<br>


    echo 'feat: bar' | commitlint

![6.png](6.png)

<br>


若要針對 git commit message 也是可以，這邊直接將當前專案加入 git 版控。  

    git init

![7.png](7.png)

<br>


設定 .gitignore。  

    vim .gitignore

![8.png](8.png)

<br>


將 node_modules 這些不必要版控的部分設定上去。  

![9.png](9.png)

<br>


實際 commit 一個不符合規範的 commit message。    

    git add .

![10.png](10.png)

<br>


    git commit -m "foo: bar"

![11.png](11.png)

<br>


    git log

![12.png](12.png)

<br>


調用 commitlint 並帶入 --from=，commitlint 會去驗證 git commit message。  

    commitlint --from=

![13.png](13.png)

<br>


Link
====
* [commitlint - Lint commit messages](https://commitlint.js.org/#/?id=commitlint-nbsp-)
