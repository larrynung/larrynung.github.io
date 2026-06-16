---
title: "[Visual Studio]使用Editbin命令讓Visual Studio突破2GB Memory使用限制"
date: "2011-11-03 01:09:29"
description: "目前我們所使用的Visual Studio都是32位元版本，被限制只能使用到2GB的記憶體。若要突破這樣的限制，我們可以使用Editbin指令將devenv.exe做些強制性的修改，"
tags: [Visual Studio]
---

目前我們所使用的Visual Studio都是32位元版本，被限制只能使用到2GB的記憶體。若要突破這樣的限制，我們可以使用Editbin指令將devenv.exe做些強制性的修改，devenv.exe檔案存放在C:\Program Files (x86)\Microsoft Visual Studio [Visual Studio 版本]\Common7\IDE下，由於這樣的修改有點暴力，使用前請將檔案備份。

![image_thumb_1.png](/images/posts/50945/image_thumb_1.png)

檔案備份好後開啟Visual Studio附帶的Visual Studio Command Prompt，這邊注意要以系統管理員身分執行。

![image_thumb.png](/images/posts/50945/image_thumb.png)

若是沒有以系統管理員身分執行的話，運行會發生"LINK : fatal error LNK1104: cannot open file 'devenv.exe'"這樣的錯誤。

![image_thumb_2.png](/images/posts/50945/image_thumb_2.png)

Visual Studio Command Prompt開啟後，切換至devenv.exe所在目錄，執行"editbin /LARGEADDRESSAWARE devenv.exe"就可以了。

![image_thumb_3.png](/images/posts/50945/image_thumb_3.png)

## Link

* [EDITBIN 參考](http://msdn.microsoft.com/zh-tw/library/xd3shwhf.aspx)
* [Hacking Visual Studio to Use More Than 2Gigabytes of Memory](http://stevenharman.net/blog/archive/2008/04/29/hacking-visual-studio-to-use-more-than-2gigabytes-of-memory.aspx)
* [讓 Visual Studio 跑 3GB](http://charlesbc.blogspot.com/2010/09/visual-studio-3gb.html)
