---
title: wget - Download file via proxy
date: 2019-05-14 08:25:17
tags: [wget]
---

要讓 wget 透過 proxy 抓取檔案，可設定 http_proxy、https_proxy、或是 ftp_proxy。  

<!-- More -->

</br>


如果一次性的調用，可直接在終端機手動輸入 Proxy 設定。  

    export http_proxy=http://${ProxyServer}:${port}
    export https_proxy=$http_proxy
    export ftp_proxy=$http_proxy

</br>


如果每次都需要走 Proxy，可修改 .wgetrc 檔。  

    vim ~/.wgetrc

{% asset_img 1.png %}

</br>


在 .wgetrc 中做 Proxy 設定。  

    http_proxy = http://${ProxyServer}:${port}
    https_proxy = http://${ProxyServer}:${port}
    ftp_proxy = http://${ProxyServer}:{port}

{% asset_img 2.png %}

</br>


調用 wget 時可用 --proxy 決定是否透過 proxy 連線。  

    wget --proxy=on|off

</br>


或是直接在 .wgetrc 中設定是否是否透過 Proxy 連線。  

    use_proxy = on

</br>


如果 Proxy 設需要驗證，且 Proxy 設定未輸入驗證資訊，可透過 --proxy-user 與 --proxy-password 將 Proxy 的驗證資訊帶入。  

</br>


Link
----
* [How to use wget to download file via proxy – The Geek Diary](https://www.thegeekdiary.com/how-to-use-wget-to-download-file-via-proxy/)
