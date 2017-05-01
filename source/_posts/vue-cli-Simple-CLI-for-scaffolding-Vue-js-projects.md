---
title: vue-cli - Simple CLI for scaffolding Vue.js projects
date: 2017-05-01 17:08:44
tags:
---

vue-cli 是 vue 官方提供的 cli 工具，能用來建立 vue 的專案。  

<!-- More -->

<br/>


vue-cli 需要在 Node.js 4.x+、npm 3+ 以上，並要在有 git 的環境下使用。  

<br/>


可直接透過 npm 安裝到全域使用。  

    npm install -g vue-cli

{% asset_img 1.png %}

<br/>


安裝後可打 vue 查看一下使用方式。  

{% asset_img 2.png %}

<br/>


他只有提供簡單的幾個命令，像是 vue list 可查閱可供使用的專案範本。  

{% asset_img 3.png %}

<br/>


vue init 可用指定的專案範本建立專案。  

    vue init <TemplateName> <ProjectName>

{% asset_img 4.png %}

<br/>


專案建立後就可以進到專案目錄開始開發了，開發告一段落可以用 npm init 將需要使用到的套件下載下來。  

{% asset_img 5.png %}

<br/>


然後用 npm run 將服務運行起來。  

    npm run dev

{% asset_img 6.png %}

<br/>


服務運行起來後開啟瀏覽器瀏覽 'http://localhost:8080' 即可看到專案運行起來的樣子。  

{% asset_img 7.png %}

<br/>


Link
----
* [vuejs/vue-cli: Simple CLI for scaffolding Vue.js projects](https://github.com/vuejs/vue-cli)
* [vue & vuex 02 - 使用 Vue-cli 安裝 vue 和 webpack 環境與相關套件 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](http://ithelp.ithome.com.tw/articles/10184919)
* [Installation — Vue.js](https://vuejs.org/v2/guide/installation.html)
* [一些平鋪直敘技術相關文: 使用 Vue-cli 快速建立 Vue 專案樣板](http://www.winwu.cc/2016/06/vue-cli-vue.html)
