---
layout: post
title: "T4MVC - A T4 template for ASP.NET MVC"
date: 2014-07-17 13:04
comments: true
categories: [T4MVC]
keywords: "T4MVC, ASP.NET, MVC"
description: "T4MVC - A T4 template for ASP.NET MVC"
---

玩過 ASP.Net MVC 的應該都有注意到，在寫 ASP.Net MVC 時會用到很多 Magic String。像是在取網址位置時，會需要帶入 Controller Name 以及 Action Name。  

<!-- More -->

{% codeblock lang:xml %}
@Url.Action("Home", "Index")
{% endcodeblock %}

<br/>

在設定連結時，會需要帶入連結名稱、 Controller Name 以及 Action Name。  

{% codeblock lang:xml %}
@Html.ActionLink("Home", "Index", "Home")
{% endcodeblock %}

<br/>

導到另外一個 Action 去處理時，又需要 Action Name。  

{% codeblock lang:c# %}
return RedirectToAction("About");
{% endcodeblock %}

<br/>

類似的地方還有很多，所以整個 ASP.Net MVC 寫下來會發現 Magic String 充斥的問題很嚴重。這樣的問題不僅讓我們開發上無 Intellisense 可用，編寫時不是那麼便利，修改時也容易因此而有所遺漏。 

<br/>

這篇要介紹的 T4MVC 就是一能解決這樣問題的 T4 範本套件。 T4MVC 透過 T4 去遍巡專案內的檔案，產生一些輔助的類別與方法的多載，巧妙的避開 Magic String 的問題。 

<br/>

使用前需先透過 NuGet 搜尋並安裝 T4MVC 套件。 

{% img /images/posts/T4MVC/1.png %}

<br/>

{% img /images/posts/T4MVC/2.png %}

<br/>

安裝完畢專案根目錄會多出幾個檔案(若想更動檔案位置，直接搬動這幾個檔案即可)，比較重要的是用來生成程式部分的 T4 主檔，另外則是用來調整生成設定的 Setting 檔。  

{% img /images/posts/T4MVC/3.png %}

<br/>

接著我們將程式中的 Magic Sting 做些處理。像是本來在寫連結的部份，可以這樣修改：  

{% codeblock lang:xml %}
@Html.ActionLink("Home", MVC.Home.Index())
{% endcodeblock %}

<br/>

取 Action 網址的部分：  

{% codeblock lang:xml %}
@Url.Action(MVC.Home.Index())
{% endcodeblock %}

<br/>

導向到其它 Action：   

{% codeblock lang:c# %}
return RedirectToAction(MVC.Home.About());
{% endcodeblock %}

<br/>

設定 Form Action：  

{% codeblock lang:xml %}
@Html.BeginForm(MVC.Home.Index(Model.Id), FormMethod.Post)
{% endcodeblock %}

<br/>

回傳顯示指定的 View：  

{% codeblock lang:c# %}
return View(Views.About);
{% endcodeblock %}

<br/>

顯示 Partial View：  

{% codeblock lang:xml %}
<% Html.RenderPartial(MVC.Dinners.Views.DinnerForm); %>
{% endcodeblock %}

<br/>

引用 JavaScript：  

{% codeblock lang:xml %}
<script src = " @Links.Scripts.jquery_validate_js " type = "text/javascript" ></script>
{% endcodeblock %}

<br/>

載入圖片：  

{% codeblock lang:xml %}
<img src = "@Links.Content.install.images.bg_gif " >
{% endcodeblock %}

<br/>

更為詳細的使用介紹請參閱 [T4MVC - Home](http://t4mvc.codeplex.com/)。

Link
----
* [T4MVC - Home](http://t4mvc.codeplex.com/)
