---
title: "Visual Studio - Use 64 Bit IISExpress"
date: "2014-07-27 23:11:00"
description: "Visual Studio - Use 64 Bit IISExpress"
tags: [Visual Studio]
---


雖然 .Net 程式支援位元適應性，Visual Studio 也允許我們做 64 位元的網站開發，但 Visual Studio 預設啟用的 IISExpress 是 32位元的。  

<!-- More -->

{% img /images/posts/x64IISExpress/1.png %}

<br/>


所以當在做 64 位元的網站開發時，在本地端測試我們會發現網站會跑不起來，因為 64 位元的網站無法跑在 32 位元的 IISExpress 上。

<br/>


這時要馬要改用 IIS 去跑，要馬就是要像像下面這樣輸入命令修改登錄檔，將 Visual Studio 設定為使用 64 位元的 IISExpress：

    reg add HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\11.0\WebProjects /v Use64BitIISExpress /t REG_DWORD /d 1

注意到這邊，登錄檔位置依 Visual Studio 版本不同會有所差異，可參閱 [Microsoft Visual Studio - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Microsoft_Visual_Studio) 內的 Internal version 部分下去調整。  

{% img /images/posts/x64IISExpress/2.png %}

<br/>


設定完後重起 Visual Studio，再次運行跑起來的就會是 64 位元的 IIS Express。

{% img /images/posts/x64IISExpress/3.png %}
