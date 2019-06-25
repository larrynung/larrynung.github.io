---
title: Termux - Vue.js in Termux
date: 2018-10-16 19:37:07
tags: [Termux, Vue.js]
---

要在 Termux 內建立 Vue.js 環境，需要安裝 Vue CLI 到全域。  

<!-- more -->

    npm i vue-cli -g

{% asset_img 1.jpg %}

</br>


安裝後透過 Vue CLI 初始 Vue 專案。  

    vue init webpack <Project>

{% asset_img 2.jpg %}

</br>


進入初始完的專案目錄。  

{% asset_img 3.jpg %}

</br>


還原專案需要的套件。  

    yarn install

{% asset_img 4.jpg %}

</br>


運行 Vue 專案。  

    yarn run start

{% asset_img 5.jpg %}

</br>


{% asset_img 6.jpg %}

</br>


訪問 http://127.0.0.1:8080 即可看到運行結果。  

{% asset_img 7.jpg %}
