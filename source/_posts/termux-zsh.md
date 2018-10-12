---
title: termux - zsh
date: 2018-10-12 15:07:32
tags: [termux]
---

要設定 termux zsh，可以下載 termux-ohmyzsh 並運行安裝。  

<!-- more -->

    sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"


{% asset_img 1.jpg %}

</br>


安裝過程會詢問要使用的背景色。  

{% asset_img 2.jpg %}

</br>


以及字型。  

{% asset_img 3.jpg %}

</br>


依自己喜好下去設定即可，後續如要變更，可呼叫命令重設。  

    ~/termux-ohmyzsh/install.sh

{% asset_img 4.jpg %}

</br>


安裝好後開啟 zsh 的設定。  

    vim .zshrc

{% asset_img 5.jpg %}

</br>


可以設定 zsh 的主題，有 agnoster、robbyrussell、jaischeema、re5et、junkfood、cloud、random 可供設定。    

{% asset_img 6.jpg %}

</br>


設定完起一個新的 session 就會看到 termux 的 zsh 主題被套用上去了。  

{% asset_img 7.jpg %}
