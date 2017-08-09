---
title: Hexo - Optimize with hexo-console-optimize
date: 2017-08-09 12:37:04
tags: [Hexo]
---

hexo-console-optimize 是 Hexo 的套件，可讓 Hexo 對 HTML、CSS、JS、Image 進行壓縮優化。  

<!-- More -->

<br/>


可透過 npm 進行安裝。  

    npm install hexo-console-optimize --save

{% asset_img 1.png %}

<br/>


要使用時調用 Hexo 的 Optimize 命令，即會對 HTML、CSS、JS、Image 檔案進行壓縮優化。  

    hexo optimize
    hexo o

{% asset_img 2.png %}

<br/>


{% asset_img 3.png %}

<br/>


如有需要，也可加帶 -d 參數在壓縮優化後直接進行佈署。  

    hexo o -d

<br/>


Link
----
* [FlashSoft/hexo-console-optimize: Hexo输出内容优化](https://github.com/FlashSoft/hexo-console-optimize)
* [hexo-console-optimize](https://www.npmjs.com/package/hexo-console-optimize)