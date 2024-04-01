---
title: "Calibre Web - Install on ubuntu 12.04"
date: "2017-09-29 00:20:23"
tags: [Calibre Web]
---


要在 ubuntu 12.04 安裝 Calibre Web，可先將 apt-get 更新。  

<!-- More -->

    sudo apt-get update

![1.png](1.png)

<br/>


因為會用到 pip 與 git，所以用 apt-get 安裝 python-setuptools 與 git。  

    sudo apt-get install python-setuptools git -y

![2.png](2.png)

<br/>


使用 easy_install 安裝 pip。  

    sudo easy_install pip

![3.png](3.png)

<br/>


將 Calibre Web 下載下來。  

    git clone https://github.com/janeczku/calibre-web.git	

![4.png](4.png)

<br/>


下載 KindleGen。  

    wget http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz

![5.png](5.png)

<br/>


將 KindleGen 放至 Calibre Web 下的 vendor 目錄。  

    sudo mkdir calibre-web/vendor 	
    sudo tar -C calibre-web/vendor -xzvf kindlegen_linux_2.6_i386_v2_9.tar.gz

![6.png](6.png)

<br/>


![7.png](7.png)

<br/>


使用 pip 安裝 dependencies。  

    sudo pip install --target calibre-web/vendor -r calibre-web/requirements.txt

![8.png](8.png)

<br/>


如果要讓 Calibre Web 在上傳時從 PDF 擷取書本封面，可加裝 ImageMagick

    sudo apt-get install imagemagick -y

![9.png](9.png)

<br/>


如果 urlib3 與 chardet 套件版本不對，Calibre Web 會無法運行，因此這邊筆者會重裝 urlib3 套件。  

    sudo pip uninstall urllib3 -y
    sudo pip install urllib3

![10.png](10.png)

<br/>


![11.png](11.png)

<br/>


重裝 chardet 套件。  

    sudo pip uninstall chardet -y
    sudo pip install chardet

![12.png](12.png)

<br/>

![13.png](13.png)

<br/>


將 Calibre Web 服務運行起來。  

    sudo python calibre-web/cps.py

![14.png](14.png)

<br/>


訪問 http://localhost:8083，指定 Calibre database 位置，這邊的 Calibre 資料庫指的是 Calibre 桌機版的 Calibre library 目錄下的 metadata.db，可以直接指到同一個檔案，或是將之複製一份放置在欲放置的位置。  

![15.png](15.png)

<br/>


設定完導回 http://localhost:8083 首頁，輸入帳密 admin/admin123 登入。  

![16.png](16.png)

<br/>


即可開始使用 Calibre Web。  

![17.png](17.png)

<br/>


Link
----
* [janeczku/calibre-web: Web app for browsing, reading and downloading eBooks stored in a Calibre database](https://github.com/janeczku/calibre-web)
