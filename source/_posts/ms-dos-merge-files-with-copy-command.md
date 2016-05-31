---
layout: post
title: "MS-DOS - Merge files with copy command"
date: 2013-12-18 23:07:00
comments: true
tags: MS-Dos
keywords: MS-Dos,Merge,Copy
description: MS-DOS - Merge files with copy command
---

若要在 MS-Dos 下撰寫 Script 去合併檔案，很直覺得會想到用 Type Command 將內容秀出並將之導到指定的檔案流做存放。

<!--More-->
像是要將所有的 txt 檔進行合併並儲存到 outputFile.txt 的話，就可以像下面這樣叫用：  

    type *.txt >> outputFile.txt


但在 MS-DOS 下的 Copy Command 也能做到一樣的效果，只要像下面這樣叫用：  

    copy *.txt outputFile.txt


就可以將所有的 txt 合併儲存至outputFile.txt 內。  

若是要合併的檔案不是單純的可用萬用字元濾出，或是需要精確的控制合併的順序，我們可以像下面這樣透過 `+` 去串接多個來源檔案：

    Copy file1.txt+file2.txt+file3.txt outputFile.txt


Link
----
* [Copy /b 合併檔案語法](http://anti-hacker.blogspot.tw/2007/05/copy-b.html)
* [你知道 Windows 命令提示字元 的 copy 指令也可以合併檔案嗎？](http://www.dotblogs.com.tw/hunterpo/archive/2009/10/30/11362.aspx)
* [複製串連命令語法為基礎的檔案](http://support.microsoft.com/kb/69575/zh-tw)

