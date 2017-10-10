---
title: Calibre Web - Install on windows
date: 2017-10-10 23:43:59
tags: [Calibre Web]
---

要在 Windows 安裝 Calibre Web，可先在 Windows 安裝 Python 與 Pip。  

<!-- More -->

<br/>


然後將 Calibre Web 下載下來。  

    git clone https://github.com/janeczku/calibre-web.git    

{% asset_img 1.png %}

<br/>


將 KindleGen 放至 Calibre Web 下的 vendor 目錄。  

<br/>


使用 pip 安裝 dependencies。  

    sudo pip install --target vendor -r requirements.txt


{% asset_img 2.png %}

<br/>


將 Calibre Web 服務運行起來。  

    python cps.py

{% asset_img 3.png %}

<br/>


訪問 http://localhost:8083，指定 Calibre database 位置，這邊的 Calibre 資料庫指的是 Calibre 桌機版的 Calibre library 目錄下的 metadata.db，可以直接指到同一個檔案，或是將之複製一份放置在欲放置的位置。   

{% asset_img 4.png %}

<br/>


設定完導回 http://localhost:8083 首頁，輸入帳密 admin/admin123 登入。  

<br/>


即可開始使用 Calibre Web。
