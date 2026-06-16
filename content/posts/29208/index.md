---
title: "[Visual Studio][C#]How to Customize Debug and Watch Messages for Built-in BCL Classes"
slug: "visual-studio-csharp-how-to-customize-debug-and-watch-messages-for-built-in-bcl-classes"
aliases: ["/posts/29208/"]
date: "2011-06-20 01:14:47"
description: "在[C#]使用DebuggerDisplayAttribute自訂除錯監看訊息與[[C#][Visual Studio]使用DebuggerTypeProxyAttribute客製除錯資訊這兩篇文章中，筆者稍微的帶出了如何去客制化除錯訊息與監看訊息。"
tags: [Visual Studio]
---

在[C#]使用DebuggerDisplayAttribute自訂除錯監看訊息與[[C#][Visual Studio]使用DebuggerTypeProxyAttribute客製除錯資訊這兩篇文章中，筆者稍微的帶出了如何去客制化除錯訊息與監看訊息。但是當初示範的都是用在自己所撰寫的類別，如果想要為BCL內建的類別去做客製化的動作，又該如何下手呢?](http://www.dotblogs.com.tw/larrynung/archive/2011/05/08/24528.aspx)

其實在概念大同小異，都是要透過DebuggerDisplayAttribute或是DebuggerTypeProxyAttribute下去完成，只是必須將這些設定設在AutoExp.dll，該檔案與其源碼我們都可在"[我的文件]\[Visual Studio XXXX]\Visualizers\"下面找到。

![image_thumb.png](/images/posts/29208/image_thumb.png)

這邊可以先將AutoExp.cs打開來看一下，裡面的程式就只是一些Attribute的設定，

![image_thumb_1.png](/images/posts/29208/image_thumb_1.png)

這邊筆者以Point的監看訊息來做說明，可以看到AutoExp.cs檔內前幾行就有一行為[assembly: DebuggerDisplay(@"\{X = {x} Y = {y}}", Target = typeof(Point))]，這行指定了是對於Point型態下去設定，並設定期顯示格式為"\{X = {x} Y = {y}}"，所以在運行時我們在監看視窗看到的Point型態變數其資訊就會是以這樣的格式呈現。

![image_thumb_3.png](/images/posts/29208/image_thumb_3.png)

若要針對BCL內建類別的除錯訊息與監看訊息做些調整，我們可以在Visual Studio中建立一個類別庫專案，將其名為AutoExp。接著將AutoExp.cs加入專案之中，修改後編譯，最後存回至"[我的文件]\[Visual Studio XXXX]\Visualizers\"，開啟編譯器除錯就可以看到修改後的除錯訊息了。

![image_thumb_2.png](/images/posts/29208/image_thumb_2.png)
