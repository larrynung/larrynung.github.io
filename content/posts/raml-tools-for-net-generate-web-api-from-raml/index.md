---
title: "RAML Tools for .NET - Generate Web API from RAML"
date: "2015-03-14 23:53:00"
description: "RAML Tools for .NET - Generate Web API from RAML"
tags: [RAML]
---


之前筆者在 RAML - RESTful API Modeling Language - Level Up 這篇介紹過的 RAML，近期推出了 RAML Tools for .NET，是一 Visual Studio 的擴充套件，可輔助我們用 RAML 開發 Client 與 Server 端的程式。

<!-- More -->

<br/>


使用前需先透過 Extensions and Updates 功能安裝 RAML Tools for .NET 這擴充套件。  
{% img /images/posts/GenerateClientFromRAML/1.png %}

<br/>


安裝完後要輔助開發 Server 端的 Web API 程式的話，我們只要開啟 Web API 專案，透過方案總管在專案的 Reference 上按下滑鼠右鍵，選取 `Add RAML Contract...` 這個選單選項。  

{% img /images/posts/GenerateWebAPIFromRAML/1.png %}

<br/>


Add RAML Contract 視窗即會跳出，這邊可為該 Web API 創建個新的 RAML contract，或是透過網址及檔案的方式來指定已存在的 RAML 檔案。  

{% img /images/posts/GenerateWebAPIFromRAML/2.png %}

<br/>


這邊筆者一樣用 Twitter 現成的 RAML 來做個示範，貼上 RAML 位置後按下 `Go` 按鈕，RAML Tools for .NET 會進行下載並解析，解析後會秀出可以使用的 Resources，下方也會幫我們帶出存放在專案時要使用的檔名以及命名空間。沒什麼問題的話按下 OK 繼續即可。  

{% img /images/posts/GenerateWebAPIFromRAML/3.png %}

<br/>


接著 RAML Tools for .NET 會幫我們將 RAML 檔依剛帶的設定加入專案中，會將 RAML 設定放在 Contracts\inculdes 的目錄之內，同時會幫我們將需要的 Controller 產生好。

{% img /images/posts/GenerateWebAPIFromRAML/4.png %}

<br/>


接著只要將 Controller 內的動作完成即可。  

{% img /images/posts/GenerateWebAPIFromRAML/5.png %}

<br/>


後續若 RAML 有所變更，RAML Tools for .NET 也支援我們進行更新，只要在 RAML 上按下滑鼠右鍵，點選 `Implement RAML Contract` 就會重新依照 RAML 在產生一次對應的程式，該動作會保留我們現有的實作，更新上不必太過擔心。  

{% img /images/posts/GenerateWebAPIFromRAML/6.png %}

<br/>


Link
----
* [mulesoft-labs/raml-dotnet-tools](https://github.com/mulesoft-labs/raml-dotnet-tools)
