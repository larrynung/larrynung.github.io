---
title: Filebeat - Install Filebeat on Windows
date: 2017-04-26 23:10:11
tags: [Filebeat]
---

要在 Windows 下使用 Filebeat，可先至官網下載下來解壓縮。  

<!-- More -->

<br/>


裡面比較會要用到的檔案有 filebeat.exe、install-service-filebeat.psl、uninstall-service-filebeat.psl 與 filebeat.yml。  

<br/>


{% asset_img 1.png %}

<br/>


filebeat.yml 是 Filebeat 的設定檔，設定完後直接點擊 filebeat.exe 就會開始作用。

<br/>


也可以執行 install-service-filebeat.psl 註冊成 Windows 服務，讓 Filebeat 在背景服務。  

{% asset_img 2.png %}

<br/>


Windows 服務註冊完後記得將服務啟動才有效果。  

{% asset_img 3.png %}

<br/>


做到這邊 Filebeat 就能依照設定正常的傳送 Log。  

<br/>


若有需要後續也可執行 uninstall-service-filebeat.psl 將 Filebeat 的 Windows 服務移除。  

{% asset_img 4.png %}

<br/>


Link
----
* [Filebeat: Lightweight Log Analysis & Elasticsearch | Elastic](https://www.elastic.co/products/beats/filebeat)
