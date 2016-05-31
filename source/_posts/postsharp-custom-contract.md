---
layout: post
title: "PostSharp - Custom Contract"
date: 2015-02-06 20:33:00
comments: true
tags: [PostSharp]
keywords: "PostSharp, Contract"
description: "PostSharp - Custom Contract"
---

PostSharp 內建的 Contracts 能支援我們做些常見的檢查，若是內建的無法滿足，我們也可以自行擴建 Contract。  

<!-- More -->

<br/>


擴建時要先確保 PostSharp.Patterns.Model 的引用已加入專案中，若無可透過 NuGet 將套件安裝起來。  

{% img /images/posts/CustomPostSharpContract/1.png %}

<br/>


接著建立個繼承自 LocationContractAttribute 的 Contract 類別，LocationContractAttribute 會提供我們建立 Contract Attribute 所需的基本功能，像是 CreateArgumentException、CreateArgumentNullException、CreateArgumentOutOfRangeException、及 ErrorMessage 等。  

{% img /images/posts/CustomPostSharpContract/2.png %}

<br/>


並實作 ILocationValidationAspect\<T\> ，在 ValudateValue 方法中撰寫自己的判斷邏輯，當不符合規範時叫用繼承自 LocationContractAttribute 的方法拋出例外即可。  

<br/>


筆者這邊以建立個 RegexMatch 的 Contract 為例，讓使用上可以帶上不同的正規表示式進行驗證。建立個繼承自 LocationContractAttribute 的類別 ，因為這邊要檢查的參數型態為字串，故還要實作 ILocationValidationAspect\<string\> 介面，在 ValudateValue 方法中會去判斷值是否符合我們設定的 Pattern，若否則叫用 CreateArgumentException 丟出例外。  

{% codeblock lang:c# %}
    public class RegexMatchAttribute : LocationContractAttribute , ILocationValidationAspect <string>
    {
        public String Pattern { get; set; }

        public RegexMatchAttribute(string pattern)
            : base()
        {
            this.Pattern = pattern;
        }

        public Exception ValidateValue(string value, string locationName, PostSharp.Reflection.LocationKind locationKind)
        {
            if (Regex .IsMatch(value, this.Pattern))
                return null ;

            return this .CreateArgumentException(value, locationName, locationKind);
        }
    }
{% endcodeblock %}

<br/>


寫完後就可以實際套用到程式中去做參數的驗證。  

{% codeblock lang:c# %}
namespace ConsoleApplication32
{
    class Program
    {
        static void Main(string[] args)
        {
            var blog = new Blog( "LevelUp", "http://larrynung.github.io" );
            blog = new Blog ("!@##&", "http://larrynung.github.io" );
        }
    }

    public class Blog
    {
        public string Name { get; set; }
        public string Url { get; set; }

        public Blog([RegexMatch (@"[\w\d]+")] string name, string url)
        {
            this.Name = name;
            this.Url = url;
        }
    }
}
{% endcodeblock%}

<br/>


運行結果如下，當代入不符合 Pattern 的參數時就會丟出例外。    

{% img /images/posts/CustomPostSharpContract/3.png %}

<br/>


這邊若有需要，我們也可以用上面提到的 ErrorMessage 屬性將錯誤訊息進行客製。  

<Br/>


Link
----
* [Contracts](http://doc.postsharp.net/contracts)
