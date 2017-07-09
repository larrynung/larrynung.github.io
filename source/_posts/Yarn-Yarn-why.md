---
title: Yarn - Yarn why
date: 2017-07-09 23:14:07
tags: [Yarn]
---

Yarn why 命令可用來查閱套件安裝的原因。  

<!-- More -->

<br/>


使用上只要用 yarn why 帶上套件的名稱即可。  

    yarn why <PackageName>

<br/>


像是這邊安裝了 gulp 套件。  

{% asset_img 1.png %}

<br/>


用 yarn why 查驗，就會看到是因為在 dependencies 設定的關係。  

{% asset_img 2.png %}

<br/>


如果查驗 gulp 以外的套件，就會看到是因為被 gulp 套件依賴或是間接依賴才會被安裝進去。  


{% asset_img 3.png %}

<br/>


Link
----
* [yarn why | Yarn](https://yarnpkg.com/en/docs/cli/why)
