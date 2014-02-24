---
layout: post
title: "Remote desktop with Microsoft Terminal Services control"
date: 2013-12-07 09:03
comments: true
categories: [C#]
keywords: "RDP, Remote Desktop, CSharp"
description: "Remote desktop with Microsoft Terminal Services control"
---

要使用.NET來開發具備遠端桌面功能的程式，我們可以使用 `Microsoft Terminal Services control` 這個 Com 元件來做。  

<!--More-->>

首先將 `Microsoft Terminal Servics control` 這個 Com 元件加入工具箱，並將之拖曳至設計頁面擺放至適當的位置。  

{% img /images/posts/MicrosoftTerminalServicesControl/1.png %}


然後接著進行程式的開發動作。  

設定遠端桌面的 Server 位置。  

<script src="http://gist-it.appspot.com/github/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?slice=31&footer=0"></script>


設定Domain。  

<script src="http://gist-it.appspot.com/github/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?slice=32&footer=0"></script>


設定使用者名稱與密碼。  

<script src="http://gist-it.appspot.com/github/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?slice=33:35&footer=0"></script>

這邊的設定都很單純，只有密碼這塊設定需要特別的處理，需要叫用 GetOcx 方法取得 IMsTscNonScriptable 物件，再對其 ClearTextPassword 欄位設定。


該做的設定做完後，呼叫 Connect 方法就可以開始進行遠端桌面的連線。   

<script src="http://gist-it.appspot.com/github/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?slice=37&footer=0"></script>


若要斷開遠端桌面連線，可呼叫 Disconnect 方法。 

<script src="http://gist-it.appspot.com/github/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?slice=29&footer=0"></script>


另外連線的狀態可透過 Connected 欄位取得，欄位值是1時代表正在連線。所以在程式撰寫的時候我們可以在連線時進行連線狀態的確認，依此狀態決定是否要先將連線斷開。

<script src="http://gist-it.appspot.com/github/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?slice=28:29&footer=0"></script>
  

最後附上完整的程式範例。    

<script src="http://gist-it.appspot.com/github/larrynung/RDPDemo/blob/bdc43c40e50305f2e12f29c5ff7e8b376b73d90b/Source/RDPDemo/Form1.cs?footer=0"></script>


運行起來會像下面這樣：

{% img /images/posts/MicrosoftTerminalServicesControl/2.png %}


若有需要，範例程式也可至 [larrynung / RDPDemo](https://github.com/larrynung/RDPDemo) 這邊下載。  

Link
----
* [Remote Desktop using C#.NET - CodeProject](http://www.codeproject.com/Articles/43705/Remote-Desktop-using-C-NET)
