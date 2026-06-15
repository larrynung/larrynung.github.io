---
title: "[C#][Linq]LINQ To WMI"
slug: "[CSharp][Linq]LINQ To WMI"
date: "2011-07-10 10:38:05"
description: "[C#][Linq]LINQ To WMI"
tags: [CSharp,Linq]
---
Linq To WMI元件可提供我們使用Linq去查詢WMI的功能。

至Linq To WMI將檔案下載下來後，解開後會看到下面三個專案：

LinqToWmi.ClassGenerator

LinqToWmi.Core

LinqToWmi.Tests

LinqToWmi.ClassGenerator專案是用來建立使用Linq To WMI時所需要的WMI對應的類別，LinqToWmi.Core專案是整個Linq To WMI的核心，提供整個查詢的功能，而LinqToWmi.Tests則是範例專案，示範要如何使用Linq To WMI的功能。

在進行Linq To WMI查詢前，我們必須先建立WMI對應的類別，LinqToWmi.Core內並未含有任何的WMI Class，因此只將LinqToWmi.Core加入參考使用，並無法做任何的查詢動作。需使用LinqToWmi.ClassGenerator專案編譯出來的Console Cmd，產生查詢所需的WMI對應類別，LinqToWmi.ClassGenerator.Exe可使用的參數如下：

Switches:
/wmi - WMI object to create class for! (Required)
/out - Filename to create
/ns - Namespace
/provider - Language to generate the file for (IE. CSharp)

最簡單的產生方法就是帶入wmi參數指定WMI Class，並帶入out參數指定輸出的檔案，像是下面這個簡單的範例就是產生Win32_UserAccount Class對應的WMI類別，產生的檔案名稱為Win32_UserAccount.cs。

LinqToWmi.ClassGenerator.exe /wmi:Win32_UserAccount /out:Win32_UserAccount.cs

產生的類別會跟WMI Class具有相同的成員屬性。

我們可將產生的類別直接加入至專案中，將LinqToWmi.Core專案編譯出來的組件加入參考，建立WmiContext，並以WmiContext.Source當作搜尋的來源，使用Linq去查詢。

private static void QueryAccounts()
{
using (WmiContext context = new WmiContext(@"\."))
{
var query = from account in context.Source()
select account;

foreach (Win32_UserAccount account in query)
{
Console.WriteLine(account.Name);
}
}
}

下面這邊我以LinqPad簡單的帶出查閱其它WMI Class的情況。

這邊若有需要查閱其它WMI Classes或想要更進一步了解其WMI Class可用來做查詢的資訊有哪些，可至Win32 Classes查閱。

##
Link

Linq To WMI

QUERY YOUR WMI WITH EASE USING WMILINQ!

An Updated LINQ to WMI Implementation

Win32 Classes