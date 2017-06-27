---
title: Yarn - Yarn add
date: 2017-06-27 23:40:27
tags: [Yarn]
---

yarn add 命令可以用來載入要使用的套件。  

<!-- More -->

<br/>


調用 yarn add，帶入套件名稱，即可將指定的套件載入。  

    yarn add <PackageName>

{% asset_img 1.png %}

<br/>


若要指定版本，可在套件名稱後面加上套件的版本號。  

    yarn add <PackageName>@<PackageVersion>

{% asset_img 2.png %}

<br/>


套件載入的同時會寫入 package.json 的 dependencies。  

{% asset_img 3.png %}

<br/>


如果要將套件載入的同時寫入 package.json 的 devDependencies，可帶入參數 --dev 或是 -D。  

    yarn add <PackageName> --dev
    yarn add <PackageName> -D

{% asset_img 4.png %}

<br/>


{% asset_img 5.png %}

<br/>


要在套件載入的同時寫入 package.json 的 peerDependencies，可帶入參數 --peer 或 -P。

    yarn add <PackageName> --peer
    yarn add <PackageName> -P

{% asset_img 6.png %}

<br/>


{% asset_img 7.png %}

<br/>


要在套件載入的同時寫入 package.json 的 optionalDependencies，可帶入參數 --optional 或 -O。

    yarn add <PackageName> --optional
    yarn add <PackageName> -O

{% asset_img 8.png %}

<br/>


{% asset_img 9.png %}

<br/>


Link
----
* [yarn add | Yarn](https://yarnpkg.com/en/docs/cli/add)
