---
title: "Yarn - Yarn upgrade"
date: "2017-07-10 23:18:45"
tags: [Yarn]
---


Yarn upgrade 命令可用來更新套件版本。  

<!-- More -->

<br/>


假設今天使用的是舊版的套件。  

![1.png](1.png)

<br/>


![2.png](2.png)

<br/>


就可以使用 Yarn upgrade 帶上套件的名稱進行套件版本的更新。  

    yarn upgrade <PackageName>

![3.png](3.png)

<br/>


或是在套件名稱後用小老鼠串接套件的版本，指定套件更新到特定的版本。  

    yarn upgrade <PackageName>@<PackageVersion>

![4.png](4.png)

<br/>


命令調用後套件即更新完成，若有需要，可以從設定檔內依賴的套件版本做個確認。  

![5.png](5.png)

<br/>


Link
----
* [yarn upgrade | Yarn](https://yarnpkg.com/en/docs/cli/upgrade)
