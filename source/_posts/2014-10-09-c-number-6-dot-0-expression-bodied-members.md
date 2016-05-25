---
layout: post
title: "C# 6.0 - Expression bodied members"
date: 2014-10-09 23:47:00
comments: true
categories: [C#]
keywords: "C#"
description: "C# 6.0 - Expression bodied members"
---

Expression bodied members 是預計要在 C# 6.0 釋出的新功能，目前已可在 Visual Studio 14 中透過設定將功能開啟進行體驗，只要在方案檔中加上：

<!-- More -->

    <LangVersion>experimental</LangVersion>

<br/>

當撰寫簡單的成員方法或是屬性時，Expression bodied members 能讓我們將程式碼精簡。  
<br/>


在使用上就只要將屬性或方法的宣告後面直接接上 Lambda 表示式即可。  

<br/>


像是成員屬性的處理會像下面這樣，少了本來大括弧的區塊，也少了 Get 區塊。    

{% codeblock lang:c# %}
...
public string ID => Guid.NewGuid().ToString();
...
{% endcodeblock %}


如果是成員方法處理上也類似，只是本來大括弧區塊內的內容用 Lambda 取代。  

{% codeblock lang:c# %}
...
public override string ToString() => this.Name;
...
{% endcodeblock %}


這邊可以看到用這樣的寫法可能會造成很難區別是屬性還是方法，使用上要特別注意小心，基本上差異只在於後面有沒有接小括弧區塊及方法的參數。  

<br/>


最後看個完整的範例：  

{% codeblock lang:c# %}
using System;


public class Program(string name)
{
    public string ID => Guid.NewGuid().ToString();


    public string Name { get; private set ; } = name;


    public override string ToString() => this.Name;


    public static void Main()
    {
        var p = new Program("LevelUp" );
        Console.WriteLine(p.ToString());
    }
}
{% endcodeblock %}


運行結果：  

{% img /images/posts/ExpressionBodiedMembers/1.png %}

<br/>


不免俗的反組譯看一下，其實就只是簡單的語法糖，在編譯時都已經幫我們轉成本來屬性與方法的寫法。  

{% img /images/posts/ExpressionBodiedMembers/2.png %}

