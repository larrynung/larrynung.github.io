---
title: Enable fusion assembly binding logging
date: 2017-09-01 23:38:00
tags:
---

Assembly binding 如果出錯，資訊不足以查出問題的話。  

<!-- More -->

{% asset_img 1.png %}

<br/>


可開啟 Assembly binding logging 功能查閱更為詳細的訊息。

<br/>


只要在 HKLM\Software\Microsoft\Fusion 加入 EnableLog 的 DWORD Key，其值設為 1，Assembly binding logging 即會開啟。  

    reg add "HKLM\Software\Microsoft\Fusion" /v EnableLog /t REG_DWORD /d 1 /f

{% asset_img 2.png %}

<br/>


開啟後再次運行，當 Assembly binding 發生錯誤時，就會有更為詳細的資訊。  

{% asset_img 3.png %}

<br/>


Link
----
* [Enable Fusion Assembly Binding Logging | Williams notatblog](https://williamwmy.wordpress.com/2013/05/23/enable-fusion-assembly-binding-logging/comment-page-1/)
* [.NET enable and disable Fusion log](https://gist.github.com/jpluimers/2f2e3acdd53a2d6b9ec0)
* [Debugging Assembly Loading Failures – Suzanne Cook's .NET CLR Notes](https://blogs.msdn.microsoft.com/suzcook/2003/05/29/debugging-assembly-loading-failures/)
