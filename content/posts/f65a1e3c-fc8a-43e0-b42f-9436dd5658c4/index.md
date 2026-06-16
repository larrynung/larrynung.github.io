---
title: "[C++][Visual Studio]How to generate XML Documentation Files with visual studio C++"
date: "2013-11-06 12:00:00"
tags: [C++, Visual Studio, XML]
description: "這幾天又看到有人在論題上發問要如何在叫用所開發C++的函式庫時，能夠顯示自己在編寫所加註的註解。這問題也滿常重複問到的，稍稍的紀錄一下。 其實在Visual Studio中要顯示註解，不論是什麼語言，都要在成員上加註特定的註解格式。格式上也都大同小異，寫起來就跟在C#或是VB.NET中沒什麼兩樣。"
---

這幾天又看到有人在論題上發問要如何在叫用所開發C++的函式庫時，能夠顯示自己在編寫所加註的註解。這問題也滿常重複問到的，稍稍的紀錄一下。

其實在Visual Studio中要顯示註解，不論是什麼語言，都要在成員上加註特定的註解格式。格式上也都大同小異，寫起來就跟在C#或是VB.NET中沒什麼兩樣。![image_thumb_3.png](/images/posts/f65a1e3c-fc8a-43e0-b42f-9436dd5658c4/image_thumb_3.png)

但是為甚麼C++中常會有人碰到這樣的問題呢。有興趣的可以開啟個新專案試著建置看看就知道了，可以看到真的還是沒有產生。

![image_thumb_7.png](/images/posts/f65a1e3c-fc8a-43e0-b42f-9436dd5658c4/image_thumb_7.png)

這是因為專案預設沒有啟動這樣的功能，所以雖然你有標註註解，但他就是不會產生對應的XML文件。若要啟動我們必須參閱[/doc (Process Documentation Comments) (C/C++)](http://msdn.microsoft.com/en-us/library/ms173501(v=vs.80).aspx)。

![image_thumb_9.png](/images/posts/f65a1e3c-fc8a-43e0-b42f-9436dd5658c4/image_thumb_9.png)

叫出Project Properties，依序點開 Cofiguration Properties => C/C++ => Output Files，將右側的Generate XML Documentation Files選項調為Yes(/doc)。

![image_thumb_10.png](/images/posts/f65a1e3c-fc8a-43e0-b42f-9436dd5658c4/image_thumb_10.png)

![image_thumb.png](/images/posts/f65a1e3c-fc8a-43e0-b42f-9436dd5658c4/image_thumb.png)

調完後再次編譯，就會在輸出目錄中看到產生出了對應的XML。

![image_thumb_5.png](/images/posts/f65a1e3c-fc8a-43e0-b42f-9436dd5658c4/image_thumb_5.png)

![image_thumb_6.png](/images/posts/f65a1e3c-fc8a-43e0-b42f-9436dd5658c4/image_thumb_6.png)

連帶XML檔跟著組件一起佈署，引用後叫用函式庫時就會帶出對應的註解。

![image_thumb_4.png](/images/posts/f65a1e3c-fc8a-43e0-b42f-9436dd5658c4/image_thumb_4.png)

## Link

* [XML Documentation (Visual C++)](http://msdn.microsoft.com/zh-TW/library/ms177226(v=vs.80).aspx)
* [/doc (Process Documentation Comments) (C/C++)](http://msdn.microsoft.com/en-us/library/ms173501(v=vs.80).aspx)
* [Recommended Tags for Documentation Comments (Visual C++)](http://msdn.microsoft.com/zh-TW/library/ms177227(v=vs.80).aspx)
* [Delimiters for Visual C++ Documentation Tags](http://msdn.microsoft.com/zh-TW/library/ms177246(v=vs.80).aspx)
