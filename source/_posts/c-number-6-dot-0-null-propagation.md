---
layout: post
title: "C# 6.0 - Null propagation"
date: 2014-08-21 00:03:00
comments: true
tags: [CSharp, CSharp 7.0]
keywords: "C#"
description: "C# 6.0 - Null propagation"
---

Null propagation 是預計要在 C# 6.0 釋出的新功能，目前已可在 Visual Studio 14 中透過設定將功能開啟進行體驗，只要在方案檔中加上：

<!-- More -->

    <LangVersion>experimental</LangVersion>

Null propagation 能讓開發人員快速的在程式中做 Null 值的處理。  

<br/>

像是 Null 時直接回傳，非 Null 時取其成員屬性、方法、索引子的值，就可以像下面這樣撰寫:  

{% codeblock lang:c# %}
...
var firstChar = str?[0];          //get 1st char if str not null            
var length = str?.Length ?? 0;    //get str's length if str not null, and if null length will be zero
var hashCode = str?.GetHashCode(); //get hashcode if str not null
...
{% endcodeblock %}

<br/>


也可以用於委派的觸發，不僅簡易且 Thread Safe。    

{% codeblock lang:c# %} 
protected void OnNameChanged(EventArgs e) 
{ 
    NameChanged?Invoke(this, e); 
} 
{% endcodeblock %} 
<br/>


最後看個完整的範例：  

{% codeblock lang:c# %}
using System;
using System.Collections .Generic;


namespace ConsoleApplication2
{
    public class Program
    {
        public static void Main()
        {
            string str = null;
            PrintData(str);

            str = "Level Up, http://larrynung.github.io/index.html" ;
            PrintData(str);
        }


        private static void PrintData( string str)
        {
            var firstChar = str?[0];          //get 1st char if str not null
            var length = str?.Length ?? 0;    //get str's length if str not null, and if null length will be zero
            var hashCode = str?.GetHashCode(); //get hashcode if str not null
            Console.WriteLine( string.Format( "Str: {0}, FirstChar: {1}, Length: {2}, HashCode: {3}", str, firstChar, length, hashCode));
        }
    }
}
{% endcodeblock %}


及其運行結果：  

{% img /images/posts/NullPropagation/1.png %}
