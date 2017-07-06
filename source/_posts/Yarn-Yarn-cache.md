---
title: Yarn - Yarn cache
date: 2017-07-07 00:01:40
tags: [Yarn]
---

yarn cache 命令可以針對 yarn 的快取做些相關的控制。  

<!-- More -->

<br/>


像是調用 yarn cache ls 可查閱現在有備快取的套件。  

{% asset_img 1.png %}

<br/>


yarn cache dir 可查閱套件快取的位置。  

{% asset_img 2.png %}

<br/>


yarn 快取的套件都會存放在測定的快取位置下。  

{% asset_img 3.png %}

<br/>


yarn cache clean 命令可以清除 yarn 的快取。  

{% asset_img 4.png %}

<br/>


清除完用 yarn cache ls 查看就會看到快取已被清除。  

{% asset_img 5.png %}

<br/>


設定的快取位置下所快取的檔案也會一併移除。  

{% asset_img 6.png %}

<br/>
