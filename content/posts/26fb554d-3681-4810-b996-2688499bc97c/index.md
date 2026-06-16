---
title: "Convert winform to wpf window with Win2WPF"
date: "2013-11-06 12:00:00"
description: "Win2WPF是一有趣的線上服務，能將我們現有的WinForm轉換成WPF Window。目前僅只支援C#的WinForm，在轉換上也有些限制，可能不是能很完整的完全轉換過去，像是非系統的控制項Win2WPF就沒有辦法做對應的替換，但起碼Win2WPF能讓我們有機會不需要重頭下去刻一遍一樣的版面。"
---

Win2WPF是一有趣的線上服務，能將我們現有的WinForm轉換成WPF Window。目前僅只支援C#的WinForm，在轉換上也有些限制，可能不是能很完整的完全轉換過去，像是非系統的控制項[Win2WPF](http://www.win2wpf.com/)就沒有辦法做對應的替換，但起碼[Win2WPF](http://www.win2wpf.com/)能讓我們有機會不需要重頭下去刻一遍一樣的版面。

這邊筆者以ProcessPro Extension的Detail Dialog下去做示範，Detail Dialog的外觀如下：

![image_thumb_4.png](/images/posts/26fb554d-3681-4810-b996-2688499bc97c/image_thumb_4.png)

切至Designer.cs檔，將程式碼整個複製。

![image_thumb_5.png](/images/posts/26fb554d-3681-4810-b996-2688499bc97c/image_thumb_5.png)

至[Win2WPF](http://www.win2wpf.com/)這邊貼上複製的程式碼，並按下Convert按鈕，下方會呈現轉換後的Xaml code。將轉換後的Xaml code全選複製以備後續使用。

![image_thumb_1.png](/images/posts/26fb554d-3681-4810-b996-2688499bc97c/image_thumb_1.png)

接著回到Visual Studio，建立一個新的WPF window。

![image_thumb_2.png](/images/posts/26fb554d-3681-4810-b996-2688499bc97c/image_thumb_2.png)

將剛所複製的Xaml code貼上，可以看到轉換後的WPF window確實有點像本來我們的WinForm，但因為筆者的使用到的WinForm元件可能有些跟WPF元件對應不起來，加上layout的方式無法轉換，所以轉換後的外觀有點跑掉。

![image_thumb_3.png](/images/posts/26fb554d-3681-4810-b996-2688499bc97c/image_thumb_3.png)

稍微在做個調整，畫面就差不多了。

![image_thumb.png](/images/posts/26fb554d-3681-4810-b996-2688499bc97c/image_thumb.png)

## Link

* [Win2WPF](http://www.win2wpf.com/)
