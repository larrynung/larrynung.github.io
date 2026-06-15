---
title: "RAML Tools for .NET - Generate client from RAML"
date: "2015-03-14 10:46:00"
description: "RAML Tools for .NET - Generate client from RAML"
tags: [RAML]
---

之前筆者在 [RAML - RESTful API Modeling Language - Level Up](http://larrynung.github.io/2013/11/28/raml-restful-api-modeling-language/) 這篇介紹過的 RAML，近期推出了 RAML Tools for .NET，是一 Visual Studio 的擴充套件，可輔助我們用 RAML 開發 Client 與 Server 端的程式。

使用前需先透過 `Extensions and Updates` 功能安裝 RAML Tools for .NET 這擴充套件。

![1.png](/images/posts/GenerateClientFromRAML/1.png)

安裝完後要輔助開發 Client 端程式的話，我們只要透過方案總管在專案的 Reference 上按下滑鼠右鍵，選取 `Add RAML Reference...` 選單選項。

![2.png](/images/posts/GenerateClientFromRAML/2.png)

`Add RAML Reference` 視窗即會跳出，這邊可透過網址或是檔案的方式來指定 RAML 檔案。

![3.png](/images/posts/GenerateClientFromRAML/3.png)

這邊筆者用 Twitter 的 RAML 來做個示範，複製其 RAML 的網址。

![4.png](/images/posts/GenerateClientFromRAML/4.png)

貼到 `Add RAML Reference` 視窗內的輸入框，按下 `GO` 按鈕，RAML Tools for .NET 會進行下載並解析，解析後會秀出可以使用的 Resources，下方也會幫我們帶出存放在專案時要使用的檔名以及命名空間。沒什麼問題的話按下 OK 繼續即可。

![5.png](/images/posts/GenerateClientFromRAML/5.png)

接著 RAML Tools for .NET 會幫我們將 RAML 檔依剛帶的設定加入專案中，會放在 API References 的目錄之內，也會透過 NuGet 加入一些必要的套件。

![6.png](/images/posts/GenerateClientFromRAML/6.png)

RAML 檔下面也可以看到該擴充套件會幫我們產生好對應的強型別類型。

![7.png](/images/posts/GenerateClientFromRAML/7.png)

跟本來的 RAML 定義是一致的，開發 Client 端程式時直接叫用即可，不用在依 Spec 下去串 API。

![8.png](/images/posts/GenerateClientFromRAML/8.png)

最後一提，後續 RAML 若有變更，RAML Tools for .NET 也可以讓我們隨時更新，只要在 RAML 上面按下滑鼠右鍵，就會看到更新的選單選項。

Link
----
* [mulesoft-labs/raml-dotnet-tools](https://github.com/mulesoft-labs/raml-dotnet-tools)