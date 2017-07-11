---
title: Yarn - Yarn global
date: 2017-07-11 23:56:54
tags: [Yarn]
---

Yarn global 命令可用來進行全域套件的管理。  

<!-- More -->

<br/>


像是可以使用 Yarn global add 將套件安裝到全域。  

    yarn global add <PackageName>

{% asset_img 1.png %}

<br/>


或是在套件名稱後用小老鼠串接套件的版本，指定安裝指定的套件版本。  

    yarn global add <PackageName>@<PackageVersion>

{% asset_img 2.png %}

<br/>


安裝完可用 Yarn global list 查閱安裝的套件。  

    yarn global list

{% asset_img 3.png %}

<br/>


若要更新全域套件，可使用 yarn global upgrade，帶上要更新的套件名稱即可。  

    yarn global upgrade <PackageName>

{% asset_img 4.png %}

<br/>


{% asset_img 5.png %}

<br/>


若要移除全域套件，可使用 yarn global remove，後面帶上要移除的套件。  

    yarn global remove <PackageName>

{% asset_img 6.png %}

<br/>


{% asset_img 7.png %}

<br/>


Link
----
* [yarn global | Yarn](https://yarnpkg.com/en/docs/cli/global)
