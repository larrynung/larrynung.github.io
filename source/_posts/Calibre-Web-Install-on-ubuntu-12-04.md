---
title: Calibre Web - Install on ubuntu 12.04
date: 2017-09-29 00:20:23
tags:
---

要在 ubuntu 12.04 安裝 Calibre Web，可先將 apt-get 更新。  

<!-- More -->

    sudo apt-get update

{% asset_img 1.png %}

<br/>


因為會用到 pip 與 git，所以用 apt-get 安裝 python-setuptools 與 git。  

    sudo apt-get install python-setuptools git -y

{% asset_img 2.png %}

<br/>


使用 easy_install 安裝 pip。  

    sudo easy_install pip

{% asset_img 3.png %}

<br/>


將 Calibre Web 下載下來。  

    git clone https://github.com/janeczku/calibre-web.git	

{% asset_img 4.png %}

<br/>


下載 KindleGen。  

    wget http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz

{% asset_img 5.png %}

<br/>


將 KindleGen 放至 Calibre Web 下的 vendor 目錄。  

    sudo mkdir calibre-web/vendor 	
    sudo tar -C calibre-web/vendor -xzvf kindlegen_linux_2.6_i386_v2_9.tar.gz

{% asset_img 6.png %}

<br/>


{% asset_img 7.png %}

<br/>


使用 pip 安裝 dependencies。  

    sudo pip install --target calibre-web/vendor -r calibre-web/requirements.txt

{% asset_img 8.png %}

<br/>


如果要讓 Calibre Web 在上傳時從 PDF 擷取書本封面，可加裝 ImageMagick

    sudo apt-get install imagemagick -y

{% asset_img 9.png %}

<br/>


如果 urlib3 與 chardet 套件版本不對，Calibre Web 會無法運行，因此這邊筆者會重裝 urlib3 套件。  

    sudo pip uninstall urllib3 -y
    sudo pip install urllib3

{% asset_img 10.png %}

<br/>


{% asset_img 11.png %}

<br/>


重裝 chardet 套件。  

    sudo pip uninstall chardet -y
    sudo pip install chardet

{% asset_img 12.png %}

<br/>

{% asset_img 13.png %}

<br/>


將 Calibre Web 服務運行起來。  

    sudo python calibre-web/cps.py

{% asset_img 14.png %}

<br/>


訪問 http://localhost:8083，指定 Calibre database 位置，這邊的 Calibre 資料庫指的是 Calibre 桌機版的 Calibre library 目錄下的 metadata.db，可以直接指到同一個檔案，或是將之複製一份放置在欲放置的位置。  

{% asset_img 15.png %}

<br/>


設定完導回 http://localhost:8083 首頁，輸入帳密 admin/admin123 登入。  

{% asset_img 16.png %}

<br/>


即可開始使用 Calibre Web。  

{% asset_img 17.png %}

<br/>


Link
----
* [janeczku/calibre-web: Web app for browsing, reading and downloading eBooks stored in a Calibre database](https://github.com/janeczku/calibre-web)
