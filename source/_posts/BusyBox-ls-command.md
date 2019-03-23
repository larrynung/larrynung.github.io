---
title: BusyBox - ls command
date: 2019-03-22 17:33:32
tags: [BusyBox]
---

ls 命令可用來查看系統中的檔案。  

<!-- More -->

<br/>


使用方式如下:  

{% asset_img 1.jpg %}

<br/>


只是要顯示當前目錄下的檔案與目錄，可直接調用命令。  

    ls

{% asset_img 2.jpg %}

<br/>


帶入參數 -1，可指定輸出只有一欄。  

    ls -1

{% asset_img 3.jpg %}

<br/>


帶入參數 -a，可指定 . 開頭的檔案或目錄也要輸出。  

    ls -a

{% asset_img 4.jpg %}

<br/>

帶入參數 -l，可指定輸出比較詳細的資料，除了檔名外，還有檔案權限、檔案大小、建立時間等資訊。  

    ls -l

{% asset_img 5.jpg %}

<br/>


帶入參數 -p，可在輸出時加一個 "/" 在目錄的後面，幫助目錄與檔案的識別。  

    ls -p

{% asset_img 6.jpg %}

<br/>


帶入參數 -n，與 -l 參數效果類似，都是輸出詳細的資訊，只是 names 換成了 UUIDs 與 GIDS。  

    ls -n

{% asset_img 7.jpg %}

<br/>


帶入參數 -r，可將查詢內容反轉輸出。  

    ls -r

{% asset_img 8.jpg %}

<br/>


帶入參數 -R，可遞迴將目錄內的資料都輸出。  

    ls -R

{% asset_img 9.jpg %}

<br/>
