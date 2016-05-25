---
layout: post
title: "ASP.NET MVC - Replacing MVC JavascriptSerializer with JSON.NET JsonSerializer"
date: 2015-01-13 21:11:00
comments: true
categories: [ASP.NET MVC]
keywords: "ASP.NET, MVC, JSON.NET"
description: "ASP.NET MVC - Replacing MVC JavascriptSerializer with JSON.NET JsonSerializer"
---

使用 ASP.NET MVC 或是 Web API 做 JSON 格式的回傳，只要將 Model 帶入去建構 JsonResult 物件回傳即可，像是下面這樣：

<!-- More -->

{% codeblock lang:c# %}
...
return new JsonResult(model);
...
{% endcodeblock %}

<br/>

這樣的寫法預設會採用 JavaSriptSerializer 去做 JSON 的序列化，有著效能不佳的問題，且序列化出來的資料有時也不是我們所期望的，像是 DateTime 物件會被序列化成下面這樣：  

    "/Date(1290181373164)/"


Json.Net 提供了 JsonNetResult 可解決這樣的問題，可將程式直接加到專案內使用。

{% codeblock lang:c# %}
/// <summary> 
/// Simple Json Result that implements the Json.NET serialiser offering more versatile serialisation 
/// </summary> 
public class JsonNetResult : ActionResult 
{ 
    public JsonNetResult() 
    { 
    }

    public JsonNetResult (object responseBody) 
    { 
        ResponseBody = responseBody; 
    }

    public JsonNetResult(object responseBody, JsonSerializerSettings settings) 
    { 
        Settings = settings; 
    }

    /// <summary>Gets or sets the serialiser settings</summary> 
    public JsonSerializerSettings Settings { get; set; }

    /// <summary>Gets or sets the encoding of the response</summary> 
    public Encoding ContentEncoding { get; set; }

    /// <summary>Gets or sets the content type for the response</summary> 
    public string ContentType { get; set; }

    /// <summary>Gets or sets the body of the response</summary> 
    public object ResponseBody { get; set; }

    /// <summary>Gets the formatting types depending on whether we are in debug mode</summary> 
    private Formatting Formatting 
    { 
        get 
        { 
            return Debugger.IsAttached ? Formatting.Indented : Formatting.None; 
        } 
    }

    /// <summary> 
    /// Serialises the response and writes it out to the response object 
    /// </summary> 
    /// <param name="context">The execution context</param> 
    public override void ExecuteResult(ControllerContext context) 
    { 
        if (context == null) 
        { 
            throw new ArgumentNullException("context"); 
        }

        HttpResponseBase response = context.HttpContext.Response;

        // set content type 
        if (!string.IsNullOrEmpty(ContentType)) 
        { 
            response.ContentType = ContentType; 
        } 
        else 
        { 
            response.ContentType = "application/json"; 
        }

        // set content encoding 
        if (ContentEncoding != null) 
        { 
            response.ContentEncoding = ContentEncoding; 
        }

        if (ResponseBody != null) 
        { 
            response.Write(JsonConvert.SerializeObject(ResponseBody, Formatting, Settings));             
        } 
    } 
}
{% endcodeblock %}

<br/>


使用上把本來的 JsonResult 替換成 JsonNetResult 就可以了。  

{% codeblock lang:c# %}
...
return new JsonNetResult(model);
...
{% endcodeblock %}

<br/>


或是撰寫基底的 Controller 來處理也可以。

{% codeblock lang:c# %}
public class BaseController:Controller
{
   protected internal override JsonResult Json(object data)
   {
       return new JsonNetResult(data);
   }
}

public class MyController:BaseController
{
    ...
        return Json(model);
    ...
}
{% endcodeblock %}

Link
-------
* [ASP.NET MVC小改裝 - 以Json.NET取代JavaScriptSerializer - 黑暗執行緒](http://blog.darkthread.net/post-2012-08-30-asp-net-mvc-and-json-net.aspx)
* [Replacing MVC JavascriptSerializer with JSON.NET JsonSerializer | Ricky Wan's Technical Blog](http://wingkaiwan.com/2012/12/28/replacing-mvc-javascriptserializer-with-json-net-jsonserializer/)
* [Better JSON Serialisation for ASP.NET MVC](http://yobriefca.se/blog/2010/11/20/better-json-serialisation-for-asp-dot-net-mvc/)
* [James Newton-King - ASP.NET MVC and Json.NET](http://james.newtonking.com/archive/2008/10/16/asp-net-mvc-and-json-net)
