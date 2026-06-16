---
title: "解決Web安裝專案無法在IIS7下安裝的問題"
date: "2013-11-06 12:00:00"
tags: [IIS]
description: "若遇到透過Visual Studio包出的Web安裝程式在XP下運行正常，但卻無法在Vista、Windows Srever 2008、Win7下正常執行，出現下方的錯誤畫面。 此時若在Win7的話，可透過點選[控制台]→[程式集]→[開啟或關閉Windows功能]，開啟Windows功能對話框。"
---

若遇到透過Visual Studio包出的Web安裝程式在XP下運行正常，但卻無法在Vista、Windows Srever 2008、Win7下正常執行，出現下方的錯誤畫面。

![image_thumb.png](/images/posts/50ea14c4-3f55-41e8-a568-3a4a0aee86ff/image_thumb.png)

此時若在Win7的話，可透過點選[控制台]→[程式集]→[開啟或關閉Windows功能]，開啟Windows功能對話框。

![image_thumb_2.png](/images/posts/50ea14c4-3f55-41e8-a568-3a4a0aee86ff/image_thumb_2.png)

![image_thumb_3.png](/images/posts/50ea14c4-3f55-41e8-a568-3a4a0aee86ff/image_thumb_3.png)

在彈出的Windows功能對話框中，勾選[IIS Metabase及IIS 6設定相容性]，再次運行安裝程式即可正常運行。

![image_thumb_4.png](/images/posts/50ea14c4-3f55-41e8-a568-3a4a0aee86ff/image_thumb_4.png)

如果作業系統是Win2008的可自行參閱[VS2008 Web Setup Project and Win2008](http://www.galcho.com/Blog/PermaLink.aspx?guid=a22cbe3d-333e-4b15-b61a-aa6675c8ec27)。

## Link

* [Troubleshooting Windows Installer Deployment](http://msdn.microsoft.com/en-us/library/kz0ke5xt(vs.80).aspx)
* [Making Web Setup projects run on Windows Vista](http://lvildosola.blogspot.com/2007/07/making-web-setup-projects-run-on.html)
* [Visual Studio 2008 and IIS 7](http://blog.dragonsoft.us/2009/01/02/visual-studio-2008-and-iis-7/)
* [Windows 2008 & Visual Studio Web Setup: The installer was interrupted before ApplicationName could be installed](http://www.nerdpad.com/asp-net/windows-2008-visual-studio-web-setup-the-installer-was-interrupted-before-applicationname-could-be-installed)
* [Managing IIS 6.0 Servers from Windows Vista (and other Management Stuff)](http://blogs.iis.net/chrisad/archive/2007/01/03/managing-iis-6-0-servers-from-windows-vista-and-other-management-stuff.aspxhttp://blogs.iis.net/chrisad/archive/2007/01/03/managing-iis-6-0-servers-from-windows-vista-and-other-management-stuff.aspx)
* [VS2008 Web Setup Project and Win2008](http://www.galcho.com/Blog/PermaLink.aspx?guid=a22cbe3d-333e-4b15-b61a-aa6675c8ec27)
