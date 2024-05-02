---
title: "Yarn - Yarn global"
date: "2017-07-11 23:56:54"
tags: [Yarn]
---


Yarn global 命令可用來進行全域套件的管理。  

<!-- More -->

<br/>


像是可以使用 Yarn global add 將套件安裝到全域。  

    yarn global add <PackageName>

![1.png](1.png)

<br/>


或是在套件名稱後用小老鼠串接套件的版本，指定安裝指定的套件版本。  

    yarn global add <PackageName>@<PackageVersion>

![2.png](2.png)

<br/>


安裝完可用 Yarn global list 查閱安裝的套件。  

    yarn global list

![3.png](3.png)

<br/>


若要更新全域套件，可使用 yarn global upgrade，帶上要更新的套件名稱即可。  

    yarn global upgrade <PackageName>

![4.png](4.png)

<br/>


![5.png](5.png)

<br/>


若要移除全域套件，可使用 yarn global remove，後面帶上要移除的套件。  

    yarn global remove <PackageName>

![6.png](6.png)

<br/>


![7.png](7.png)

<br/>


Link
----
* [yarn global | Yarn](https://yarnpkg.com/en/docs/cli/global)
