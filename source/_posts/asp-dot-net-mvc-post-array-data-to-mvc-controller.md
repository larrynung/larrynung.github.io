---
layout: post
title: "ASP.NET MVC - Post array data to MVC controller"
date: 2014-04-26 12:53:00
comments: true
tags: [ASP.NET MVC]
keywords: "ASP.NET, MVC, Array"
description: "ASP.NET MVC - Post array data to MVC controller"
---

最近在用 JQuery 傳送陣列資料給 MVC Controller，資料無法如預期般的被送過去。查看了一下送過去的資訊，看起來是送的資料格式不符合 Model Binder 預期的格式所導致。  

<!-- More -->

以基本型別的陣列來說， Model Binder 預期的格式為  

    arrayName = arrayValue1& arrayName = arrayValue2


但是透過 JQuery 發送的資料卻是  

    arrayName[] = arrayValue1& arrayName[] = arrayValue2


而以物件陣列來說， Model Binder 預期的格式為  

    arrayName[0] .propertyName1 = property1Value& arrayName[0] .propertyName2 = property2Value


但是透過 JQuery 發送的資料卻是  
    arrayName[0] [propertyName1] = property1Value& arrayName[0] [propertyName2] = property2Value

要解決這樣的問題要馬可以在 Client 這邊將資料做個轉換，要馬就是在 MVC 這邊要透過客製 Model Binder 的方式自行轉換。這邊筆者是比較傾向 Client Side 處理，且黑暗大那也已有現成又漂亮的解法，

<br/>

對於基本型態陣列的處理，可參閱[使用jQuery.post傳送字串陣列參數到ASP.NET MVC - 黑暗執行緒](http://blog.darkthread.net/post-2013-12-14-pass-string-array-to-aspnet-mvc.aspx)這篇，透過$.param()將參數序列化，並在traditional參數這邊帶入true，指定用傳統的陣列參數的序列化形式即可。

<br/>

對於非基本型態的陣列處理，可參閱[使用jQuery.ajax傳送物件陣列給ASP.NET MVC - 黑暗執行緒](http://blog.darkthread.net/post-2012-06-23-post-array-to-mvc-with-jquery-ajax.aspx)這篇，黑暗大刻了一個 JQuery Plugin 在發送資料前會將資料格式用正規表示式進行對應的轉換。

{% codeblock lang:c# %}
function ($) {
    $.extend($, {
        //Replace item[0][propName] to item[0].propName for MVC model binder
        postMvc: function (url, data, succ, dataType) {
            return $.ajax({
                url: url,
                type: "Post",
                dataType: dataType,
                data: data,
                success: succ,
                beforeSend: function (xhr, settings) {
                    settings.data =
                    settings.data.replace(/%5D%5B(.+?)%5D=/g, "%5D.$1=");
                }
            });
        }
    });
})(jQuery);
 {% endcodeblock %}

使用上只要將發送的動作改用這個 JQuery Plugin 去做就可以了。

Link
----
* [使用jQuery.post傳送字串陣列參數到ASP.NET MVC - 黑暗執行緒](http://blog.darkthread.net/post-2013-12-14-pass-string-array-to-aspnet-mvc.aspx)
* [使用jQuery.ajax傳送物件陣列給ASP.NET MVC - 黑暗執行緒](http://blog.darkthread.net/post-2012-06-23-post-array-to-mvc-with-jquery-ajax.aspx)
