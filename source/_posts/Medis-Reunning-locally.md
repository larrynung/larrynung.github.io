---
title: Medis - Reunning locally
date: 2019-12-02 07:44:24
tags: [Medis]
---

要在本地運行 Medis，先要將 Medis 下載下來。  

<!-- More -->

    git clone https://github.com/luin/medis

{% asset_img 1.png %}

</br>


進入 Media 目錄。  

    cd medis

{% asset_img 2.png %}

</br>


安裝需要的 npm 套件。

    npm install

{% asset_img 3.png %}

</br>


建置。  

    npm run build

{% asset_img 4.png %}

</br>


因為運行需依賴 electron，若未安裝，這邊可進行全域安裝。  

    npm install -g electron

{% asset_img 5.png %}

</br>


最後使用 npm 的 start 命令啟用程式即可。  

    npm start

{% asset_img 6.png %}

</br>

{% asset_img 7.png %}
