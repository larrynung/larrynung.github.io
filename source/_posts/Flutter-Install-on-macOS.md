---
title: Flutter - Install on macOS
date: 2018-03-06 23:06:24
tags: [Flutter]
---

要在 Mac 中使用 Flutter，首先要先用 Git 將 Flutter 抓取下來。  

<!-- More -->

    git clone -b beta https://github.com/flutter/flutter.git

{% asset_img 1.png %}
 
<br/>


然後設定 Flutter 路徑參考，可以在 Terminal 直接輸入設定。  

    export PATH=[PATH_TO_FLUTTER_GIT_DIRECTORY]/flutter/bin:$PATH

{% asset_img 2.png %}
 
<br/>


也可以開啟 HOME/.bash_profile 修改，加入上述設定，然後調用下面命令重新讀取設定值。  

    source $HOME/.bash_profile

<br/>


設定好後調用下面命令，檢驗環境中所缺少的依賴。  

    flutter doctor

{% asset_img 3.png %}
 
<br/>


{% asset_img 4.png %}
 
<br/>


運行完可以看到缺少的依賴有哪些，且會很詳細的顯示該怎麼處理，接著只要照著指示反覆將缺少的依賴修正即可。  

<br/>


Link
----
* [Get Started: Install on macOS - Flutter](https://flutter.io/setup-macos/)
