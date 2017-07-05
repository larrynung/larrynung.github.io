---
title: Yarn - Yarn install
date: 2017-07-02 23:16:26
tags: [Yarn]
---

yarn install 命令可用來還原套件。  

<!-- More -->

<br/>


若是在 package.json 中設定的套件並未在本地被載入，可調用 yarn install 命令將之還原。   

    yarn install

{% asset_img 1.png %}

<br/>



除了調用 yarn install 還原外，直接調用 yarn 也有相同的效果。  

    yarn

{% asset_img 2.png %}

<br/>



若有需要，也可以加帶參數 --force 強制運行套件還原，所有已載入的套件都會被重新進行載入。    

    yarn install --force

{% asset_img 3.png %}

<br/>


Link
----
* [yarn install | Yarn](https://yarnpkg.com/en/docs/cli/install)
