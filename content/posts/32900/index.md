---
title: "[C#][Linq]Linq to Wikipedia"
slug: "[CSharp][Linq]Linq to Wikipedia"
date: "2011-08-11 01:20:08"
description: "[C#][Linq]Linq to Wikipedia"
tags: [CSharp,Linq]
---
Linq to Wikipedia元件提供開發人員使用Linq去查詢Wiki的功能，具備兩種查詢模式，一種是OpenSearch、一種是Keyword Search。

搜尋後所能提供的Wiki資訊大概就是標題、描述、頁面網址、關鍵字等等，有興趣的可將CodePlex上的專案下載下來運行看看，甚至是查閱一下WikipediaKeywordSearchResult與WikipediaOpenSearchResult這兩個類別的成員變數，就可以知道這個元件能提供我們做到甚麼程度了。

在開發時我們必須先將LinqToWikipedia.dll原件加入參考。

並加入LinqToWikipedia命名空間。

接著建立WikipediaContext物件實體，建立時可依需要帶入Proxy。WikipediaContext物件實體建立後透過OpenSearch或是KeywordSearch屬性下去做Linq的查詢動作即可。
private IQueryable OpenSearch(string keyWord)
{
return from item in (new WikipediaContext()).OpenSearch
where item.Keyword == keyWord
select item;
}

private IQueryableKeyWordSearch(string keyWord)
{
return from item in (new WikipediaContext()).KeywordSearch
where item.Keyword == keyWord
select item;
}

若一切都正常的話應該會看到類似如下的查詢回傳值。

若查詢出現錯誤碼為403的問題，可參閱Error 403 Forbidden from Mediawiki API，因為這問題已被修正，所以簡單的說若是你還有碰到該問題，解決的辦法就是將下載下來的Linq to Wikipedia專案開起來後重建，改用新建出來的dll應該就可以了。

## Link

Linq to Wikipedia