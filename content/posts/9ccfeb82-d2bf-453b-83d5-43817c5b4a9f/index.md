---
title: "[C#]DateTime 與 ISO8601 格式字串的相互轉換"
slug: "csharp-datetime-與-iso8601-格式字串的相互轉換"
aliases: ["/posts/csharpdatetime-與-iso8601-格式字串的相互轉換/"]
date: "2013-11-06 12:00:00"
description: "要從DateTime轉換成ISO8601的格式，在.NET中我們有幾種方式，一種是直接帶入ISO8601的Format，像是： 一種是帶入s並在最後面加上\"Z\"： 最後一種是帶入o： 實際程式撰寫會像下面這樣： 運行後可以看到時間正確的轉換為ISO8601的格式：…"
tags: [CSharp]
---

要從DateTime轉換成ISO8601的格式，在.NET中我們有幾種方式，一種是直接帶入ISO8601的Format，像是：

```csharp
var ISO8601String = dt.ToString(@"yyyy-MM-dd\THH:mm:ss\Z");
```

一種是帶入s並在最後面加上"Z"：

```csharp
var ISO8601String = string.Format("{0}Z", dt.ToString("s"));
```

最後一種是帶入o：

```csharp
var ISO8601String = dt.ToString("o");
```

實際程式撰寫會像下面這樣：

```csharp
var dt = DateTime.UtcNow;
Console.WriteLine(string.Format("{0}Z", dt.ToString("s")));
Console.WriteLine(dt.ToString("o"));
Console.WriteLine(dt.ToString(@"yyyy-MM-dd\THH:mm:ss\Z"));
```

運行後可以看到時間正確的轉換為ISO8601的格式：

![image_thumb_2.png](/images/posts/9ccfeb82-d2bf-453b-83d5-43817c5b4a9f/image_thumb_2.png)

若要從ISO8601的字串格式轉換回DateTime，可以使用DateTime.TryParseExact，將ISO8601的格式帶入，像是下面筆者所整理的函式一樣：

```csharp
static DateTime? ToDateTimeFromUTCISO8601(string dateTimeString)
{
    DateTime dt;
    var sucessed = DateTime.TryParseExact(dateTimeString, new string[] { @"yyyy-MM-dd\THH:mm:ss\Z", "o" }, CultureInfo.InvariantCulture, DateTimeStyles.AssumeUniversal, out dt);

    return sucessed ? new DateTime?(dt) : null;
}
```

使用起來會像下面這樣：

```csharp
var dt = ToDateTimeFromUTCISO8601(@"2010-08-20T15:00:00Z");
var utcDT = dt.Value.ToUniversalTime();
```

```csharp
var dt = ToDateTimeFromUTCISO8601(@"2007-06-06T09:03:01.1234567+02:00");
var utcDT = dt.Value.ToUniversalTime();
```
