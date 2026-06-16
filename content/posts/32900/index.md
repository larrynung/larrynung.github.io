---
title: "[C#][Linq]Linq to Wikipedia"
slug: "csharp-linq-linq-to-wikipedia"
aliases: ["/posts/csharplinqlinq-to-wikipedia/"]
date: "2011-08-11 01:20:08"
description: "Linq to Wikipedia元件提供開發人員使用Linq去查詢Wiki的功能，具備兩種查詢模式，一種是OpenSearch、一種是Keyword Search。"
tags: [CSharp,Linq]
---

Linq to Wikipedia元件提供開發人員使用Linq去查詢Wiki的功能，具備兩種查詢模式，一種是OpenSearch、一種是Keyword Search。

![image_thumb.png](/images/posts/32900/image_thumb.png)

搜尋後所能提供的Wiki資訊大概就是標題、描述、頁面網址、關鍵字等等，有興趣的可將CodePlex上的專案下載下來運行看看，甚至是查閱一下WikipediaKeywordSearchResult與WikipediaOpenSearchResult這兩個類別的成員變數，就可以知道這個元件能提供我們做到甚麼程度了。

![image_thumb_5.png](/images/posts/32900/image_thumb_5.png)

在開發時我們必須先將LinqToWikipedia.dll原件加入參考。

![image_thumb_2.png](/images/posts/32900/image_thumb_2.png)

並加入LinqToWikipedia命名空間。

![image_thumb_1.png](/images/posts/32900/image_thumb_1.png)

接著建立WikipediaContext物件實體，建立時可依需要帶入Proxy。WikipediaContext物件實體建立後透過OpenSearch或是KeywordSearch屬性下去做Linq的查詢動作即可。

```csharp
private IQueryable<WikipediaOpenSearchResult> OpenSearch(string keyWord)
{
    return from item in (new WikipediaContext()).OpenSearch
           where item.Keyword == keyWord
           select item;
}

private IQueryable<WikipediaKeywordSearchResult>KeyWordSearch(string keyWord)
{
    return from item in (new WikipediaContext()).KeywordSearch
           where item.Keyword == keyWord
           select item;
}
```

若一切都正常的話應該會看到類似如下的查詢回傳值。

![image_thumb_4.png](/images/posts/32900/image_thumb_4.png)

![image_thumb_3.png](/images/posts/32900/image_thumb_3.png)

若查詢出現錯誤碼為403的問題，可參閱Error 403 Forbidden from Mediawiki API，因為這問題已被修正，所以簡單的說若是你還有碰到該問題，解決的辦法就是將下載下來的[Linq to Wikipedia專案開起來後重建，改用新建出來的dll應該就可以了。](http://linqtowikipedia.codeplex.com/)

## Link

* Linq to Wikipedia
