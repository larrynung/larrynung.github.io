---
title: Delete folder when Source Path Too Long
tags: []
date: 2016-06-08 12:53:00
---

筆者使用 npm 安裝套件，因為套件的巢狀目錄過多造成路徑過長，透過檔案總管或是 Dos 的 rd 命令都無法將目錄刪除。  

<!-- More -->

{% asset_img 1.png %}

<br/>


最後使用 rimraf 才得以將之刪除。  

<br/>


rimraf 安裝方式如下：

    npm install -g rimraf

{% asset_img 2.png %}

<br/>


使用時只要在命令列後帶入欲刪除的目錄即可。  

    rimraf [Folder]

{% asset_img 3.png %}

<br/>


Link
----
* [windows - How to delete directories with path/names too long for normal delete - Super User](http://superuser.com/questions/78434/how-to-delete-directories-with-path-names-too-long-for-normal-delete#)
