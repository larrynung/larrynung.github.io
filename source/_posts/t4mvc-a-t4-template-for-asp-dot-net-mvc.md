---
layout: post
title: "T4MVC - A T4 template for ASP.NET MVC"
date: 2014-07-17 13:04:00
comments: true
categories: [T4MVC, T4]
keywords: "T4MVC, ASP.NET, MVC"
description: "T4MVC - A T4 template for ASP.NET MVC"
---

玩過 ASP.Net MVC 的應該都有注意到，在寫 ASP.Net MVC 時會用到很多 Magic String。像是在取網址位置時，會需要帶入 Controller Name 以及 Action Name。  

<!-- More -->

    @Url.Action("Home", "Index")


在設定連結時，會需要帶入連結名稱、 Controller Name 以及 Action Name。

    @Html.ActionLink("Home", "Index", "Home")



導到另外一個 Action 去處理時，又需要 Action Name。  

    return RedirectToAction("About");


可以看到這些叫用帶入的都是字串，而且類似的地方還有很多，所以整個 ASP.Net MVC 寫下來會發現 Magic String 充斥在程式中。這樣的問題不僅讓我們開發上無 Intellisense 可用，編寫時不是那麼便利，修改時也容易因此而有所遺漏。 

<br/>

這篇要介紹的 T4MVC 就是一能解決這樣問題的 T4 範本套件。 T4MVC 透過 T4 去遍巡專案內的檔案，產生一些輔助的類別與方法的多載，巧妙的避開 Magic String 的問題。這邊可先快速的瀏覽一下 Channel 9 的相關影片，體驗一下 T4MVC 的魅力。  

<iframe src="http://channel9.msdn.com/Blogs/jongalloway/Jon-Takes-Five-with-David-Ebbo-on-T4MVC/player?h=540&w=960" style="height:540px;width:960px;" allowFullScreen frameBorder="0" scrolling="no"></iframe>  

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

    @Html.ActionLink("Home", MVC.Home.Index())


在 View 中取用 Action 網址的部分...  

    @Url.Action(MVC.Home.Index())


在 Controller 要將 Action 導向...    

    return RedirectToAction(MVC.Home.About());


在 View 中使用 Form Action...     

    @Html.BeginForm(MVC.Home.Index(Model.Id), FormMethod.Post)


在 Action 回傳指定的 View...   

    return View(Views.About);


在 View 中顯示 Partial View...    

    @{Html.RenderPartial(MVC.Dinners.Views.DinnerForm);}


在 View 中引用 JavaScript...   

    <script src = " @Links.Scripts.jquery_validate_js " type = "text/javascript" ></script>


在 View 中載入圖片...     

    <img src = "@Links.Content.install.images.bg_gif " >


更為詳細的使用介紹請參閱 [T4MVC - Home](http://t4mvc.codeplex.com/)。

Link
----
* [T4MVC - Home](http://t4mvc.codeplex.com/)
