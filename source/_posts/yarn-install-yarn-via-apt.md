---
title: "Yarn - Install Yarn via apt"
date: 2017-06-24 23:15:06
tags: [Yarn]
---

要透過 APT 安裝 Yarn，需要先設定 Repository。  

<!-- More -->

    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -

{% asset_img 1.png %}

<br/>



    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

{% asset_img 2.png %}

<br/>


Repository 設定完後，更新 apt-get，更新完即可進行 Yarn 的安裝。  

    sudo apt-get update && sudo apt-get install yarn

{% asset_img 3.png %}

<br/>


Link
----
* [Installation | Yarn](https://yarnpkg.com/en/docs/install#linux-tab)
