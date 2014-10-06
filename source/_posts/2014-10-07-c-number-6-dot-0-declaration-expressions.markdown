---
layout: post
title: "C# 6.0 - Declaration expressions"
date: 2014-10-07 00:42
comments: true
categories: [C#]
keywords: "C#"
description: "C# 6.0 - Declaration expressions"
---

Declaration expressions 是預計要在 C# 6.0 釋出的新功能，目前已可在 Visual Studio 14 中透過設定將功能開啟進行體驗，只要在方案檔中加上：

<!-- More -->

    <LangVersion>experimental</LangVersion>

Declaration expressions 能讓我們在撰寫陳述式的同時就順帶做宣告的動作，不需特別在另外一行宣告。用在呼叫具有 out 參數的方法上面特別的好用。  

{% codeblock lang:c# %}
...
if (int.TryParse(str, out int value))       
    Console.WriteLine(value);
...
{% endcodeblock %}

<br/>


Declaration expressions 也支援型別推斷的使用方式。  

{% codeblock lang:c# %}
...
if (int.TryParse(str, out var value))               
    Console.WriteLine(value);   
...    
{% endcodeblock %}

<br/>


最後來看個完整的使用範例：  

{% codeblock lang:c# %}
using System;

public class Program(string name)
{
    public static void Main()
    {
        TryParseValue( @"Level Up (http://larrynung.github.io/index.html)" );
        TryParseValue( @"123");


        Console.WriteLine();


        Console.WriteLine(string guid = Guid. NewGuid().ToString());
        Console.WriteLine(guid);
    }


    private static void TryParseValue(string str)
    {
        if (int.TryParse(str, out var value))       
            Console.WriteLine(value);       
        else
            Console.WriteLine( "Can't parse to int value..." );
    }
}
{% endcodeblock %}   

<br/>


及其運行的結果：

{% img /images/posts/DeclarationExpressions/1.png %}

<br/>


最後一提，該語法具備過多的彈性，過於濫用會造成程式碼可讀性下降，請小心服用。  
