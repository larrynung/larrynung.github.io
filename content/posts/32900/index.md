---
title: "[C#][Linq]Linq to Wikipedia"
date: "2011-08-11 01:20:08"
description: "[C#][Linq]Linq to Wikipedia"
tags: [CSharp,Linq]
---

<p>Linq to Wikipedia</a>元件提供開發人員使用Linq去查詢Wiki的功能，具備兩種查詢模式，一種是OpenSearch、一種是Keyword Search。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1108/CLinqLinqtoWikipedia_BBDD/image_2.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\32900\image_thumb.png" width="554" height="484" /></a> </p>  <p> </p>  <p>搜尋後所能提供的Wiki資訊大概就是標題、描述、頁面網址、關鍵字等等，有興趣的可將CodePlex上的專案下載下來運行看看，甚至是查閱一下WikipediaKeywordSearchResult與WikipediaOpenSearchResult這兩個類別的成員變數，就可以知道這個元件能提供我們做到甚麼程度了。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1108/CLinqLinqtoWikipedia_BBDD/image_12.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\32900\image_thumb_5.png" width="644" height="375" /></a> </p>  <p> </p>  <p>在開發時我們必須先將LinqToWikipedia.dll原件加入參考。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1108/CLinqLinqtoWikipedia_BBDD/image_6.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\32900\image_thumb_2.png" width="303" height="200" /></a> </p>  <p> </p>  <p>並加入LinqToWikipedia命名空間。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1108/CLinqLinqtoWikipedia_BBDD/image_4.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\32900\image_thumb_1.png" width="246" height="65" /> </p>  <p> </p>  <p>接著建立WikipediaContext物件實體，建立時可依需要帶入Proxy。WikipediaContext物件實體建立後透過OpenSearch或是KeywordSearch屬性下去做Linq的查詢動作即可。</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:d9d0ae49-3a61-4d7e-8f54-1088556dd420" class="wlWriterSmartContent"><pre name="code" class="c#">        private IQueryable&lt;WikipediaOpenSearchResult&gt; OpenSearch(string keyWord)
        {
            return from item in (new WikipediaContext()).OpenSearch
                   where item.Keyword == keyWord
                   select item;
        }

        private IQueryable&lt;WikipediaKeywordSearchResult&gt;KeyWordSearch(string keyWord)
        {
            return from item in (new WikipediaContext()).KeywordSearch
                   where item.Keyword == keyWord
                   select item;
        }</pre></div>

<p> </p>

<p>若一切都正常的話應該會看到類似如下的查詢回傳值。</p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\32900\image_thumb_4.png" width="644" height="460" /> </p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts\32900\image_thumb_3.png" width="644" height="460" /> </p>

<p> </p>

<p>若查詢出現錯誤碼為403的問題，可參閱Error 403 Forbidden from Mediawiki API</a>，因為這問題已被修正，所以簡單的說若是你還有碰到該問題，解決的辦法就是將下載下來的<a href="http://linqtowikipedia.codeplex.com/" target="_blank">Linq to Wikipedia專案開起來後重建，改用新建出來的dll應該就可以了。</p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Linq to Wikipedia</li>
</ul>
