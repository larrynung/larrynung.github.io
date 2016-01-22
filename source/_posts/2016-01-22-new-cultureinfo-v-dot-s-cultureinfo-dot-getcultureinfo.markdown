---
layout: post
title: "new CultureInfo v.s CultureInfo.GetCultureInfo"
date: 2016-01-22 05:31
comments: true
categories: 
keywords: "CultureInfo"
description: "new CultureInfo v.s CultureInfo.GetCultureInfo"
---

要取得 CultureInfo 通常有兩種做法，一個是透見建構子構建 ，一個則是透過 CultureInfo.GetCultureInfo 去取得。  

<!-- More -->

<br/>


透過建構子建立會產生新的物件，若頻繁的調用會對 GC 造成不必要的負擔。若改調用 CultureInfo.GetCultureInfo，會從快取中拿取，不會頻繁的建構，效能上也會比較好。  

<br/>


這邊筆者實際做個簡單的測試：  

{% codeblock lang:c# %}
using System;
using System.Globalization;
using System.Diagnostics;

public class Program
{
    public static void Main()
    {
        var count = 10000000;
        Console.WriteLine( "new CultureInfo: {0} ms" , DoTest(count, () =>
        {
            var cultureInfo = new CultureInfo("en-GB" );
        }).ToString());

        Console.WriteLine( "CultureInfo.GetCultureInfo: {0} ms" , DoTest(count, () =>
        {
            var cultureInfo = CultureInfo.GetCultureInfo("en-GB" );
        }).ToString());
    }

    static long DoTest(int count, Action action)
    {
        var sw = Stopwatch.StartNew();
        for ( int i = 0; i < count; ++i)
        {
            action();
        }

        return sw.ElapsedMilliseconds;
    }
}
{% endcodeblock %}

<br/>


可以看到 CultureInfo.GetCultureInfo 有著較佳的效能。  

{% img /images/posts/CultureInfoTest/1.png %}

<br/>


最後這邊附上實驗的數據。  

{% img /images/posts/CultureInfoTest/2.png %}
