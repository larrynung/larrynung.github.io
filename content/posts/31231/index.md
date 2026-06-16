---
title: "[C#][Linq]BLinq - Linq To Bing"
slug: "[CSharp][Linq]BLinq - Linq To Bing"
date: "2011-07-06 11:21:50"
description: "BLinq元件能讓我們使用Linq語法去查詢Bing搜尋引擎上的網頁與圖片。 使用上十分的簡單，先將BLinq的元件下載下來，開啟方案檔編譯，將其編譯後的BLinq組件加入參考，接著建立BingContext物件，建立時需帶入App ID，"
tags: [Linq, CSharp]
---

BLinq元件能讓我們使用Linq語法去查詢Bing搜尋引擎上的網頁與圖片。

使用上十分的簡單，先將BLinq的元件下載下來，開啟方案檔編譯，將其編譯後的BLinq組件加入參考，接著建立BingContext物件，建立時需帶入App ID，若無App ID則請先至[Bing Develop Center申請。](http://www.bing.com/developers/)

```csharp
//Created BingContext With Bing App ID
BingContext m_Bing = new BingContext("1234567890");
```

建立完BingContext物件後，查詢的動作也很簡單，若是要搜尋網頁，則對BingContext.Pages去做查詢的動作，若是搜尋圖片的話，則對BingContext.Images去做搜尋。另外就是一個回傳的是PageSearchResult型態的資料，一個回傳的是ImageSearchResult，除此之外兩者並無太大的差異。

```csharp
private IEnumerable<PageSearchResult> SearchPages(string keyWord)
{
    return from item in m_Bing.Pages
           where item.Query == keyWord
           select item;
}

private IEnumerable<ImageSearchResult> SearchImages(string keyWord)
{
    return from item in m_Bing.Images
           where item.Query == keyWord
           select item;
}
```

這邊以LinqPad試範一下搜尋符合Level Up關鍵字的網頁與圖片。

![image_thumb.png](/images/posts/31231/image_thumb.png)

![image_thumb_1.png](/images/posts/31231/image_thumb_1.png)

## Download

* BLinq.zip

## Link

* LINQ To Bing Search Engine - Get Bing Search Results via LINQ
* BLinq - Linq to Bing Search APIs
