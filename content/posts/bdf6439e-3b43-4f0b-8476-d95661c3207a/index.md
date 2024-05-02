---
title: "GAE's Python Datastore API"
date: "2013-11-06 12:00:00"
description: "GAE's Python Datastore API"
---

<p>
	GAE提供了一組Datastore API，可以讓我們將資料存在雲端，這邊一樣以Python為例簡單的紀錄一下。</p>
<p>
	 </p>
<p>
	首先將google.appengine.ext.db import進來。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:1d19eb69-d179-4c31-bdcd-c5acf78c7e2f" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
from google.appengine.ext import db</pre>
</div>
<p>
	 </p>
<p>
	接著必須設定我們要儲存的Model類別。</p>
<p>
	 </p>
<p>
	宣告繼承自db.model的類別，並在裡面宣告需要的Property (類似資料庫的欄位，Property的型態可參閱類型和 Property 類別這篇)就可以了。</p>
<p>
	 </p>
<p>
	以下面這程式碼片段為例：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:128cd68a-d968-40b2-aff8-24786da0d16e" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
class Article(db.Model):
    id = db.StringProperty(required=True)
    name = db.StringProperty()
    content = db.TextProperty()

class Blog(db.Model):
    id = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    url = db.LinkProperty(required=True)
    articleIDs = db.StringListProperty()</pre>
</div>
<p>
	 </p>
<p>
	這邊筆者建立了一個名為Article的Model，裡面有id、name、以及content這幾個Property。id可用來識別article，為必要的參數，存放的資料為string型態；name是文章的標題，存放的資料一樣是string型態；content則是文章的內文，因為文章的內文可能很長， 所以這邊用text型態 (可超越500字)。</p>
<p>
	 </p>
<p>
	另外一個Model是Blog，裡面有id、name、url、以及articleIDs這幾個Property，id與name跟Article Model的大同小異，url是blog的網址，為必要的參數，存放的資料為link型態；articleIDs是部落格的文章ID清單，存放的資料為string list型態。</p>
<p>
	 </p>
<p>
	Model類別建立好，當我們要儲存資料時只要建立出Model的物件實體，填入對應的資料後呼叫put方法就可以了。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2ab39a61-d7e8-40bb-8186-7d421758c801" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
            ...
            blog = Blog(id=str(uuid.uuid1()), name="LevelUp", url="http://www.dotblogs.com.tw/larrynung")

            articleID = str(uuid.uuid1())
            Article(id=articleID, name="hello", content="hello world").put()

            blog.articleIDs = [articleID]

            blog.put()
            ...</pre>
</div>
<p>
	 </p>
<p>
	資料的取出這邊我們可以透過db.GqlQuery帶入GQL語法 (類似SQL語法，詳細的語法可參閱GQL Reference這篇)去做。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9bac86ae-b4b3-48a1-80af-7adf5331ecc8" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
...
blog = db.GqlQuery("select * from Blog Limit 1")[0]
...</pre>
</div>
<p>
	 </p>
<p>
	或是直接呼叫Model的gql方法也可以。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:bbf43ba5-5230-4513-bf05-178dc9b54610" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
...
blog = Blog.gql("Limit 1")[0]
...</pre>
</div>
<p>
	 </p>
<p>
	最後這邊實際來看個完整的範例程式：</p>
<p><script src="\images\postsdf6439e-3b43-4f0b-8476-d95661c3207a\6131131.js"></script>
	 </p>
<p>
	這範例程式會先嘗試用GQL去讀取Blog資料，若是已經有Blog的資料則將它呈現在畫面上。若是還沒有Blog的資料，則會建立預設的資料並存入，存入後將頁面重新導回做呈現。</p>
<p>
	 </p>
<p>
	所以運行起來應該會像下面這樣：</p>
<p>
	<img alt="image" border="0" height="216" src="\images\postsdf6439e-3b43-4f0b-8476-d95661c3207a\image_thumb_3.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="327" /></p>
<p>
	 </p>
<p>
	最後一提，在試驗Datastore API時，我們可能會在試驗的同時存了過多不正確的資訊進去，若想每次都是在乾淨的狀況下進行測試，這邊可以開啟Google App Engine Launcher，點擊[Edit/Application Settings...]選單選項。</p>
<p>
	<img alt="image" border="0" height="273" src="\images\postsdf6439e-3b43-4f0b-8476-d95661c3207a\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="392" /></p>
<p>
	 </p>
<p>
	在Application Settings設定對話框中，將Extra Command Ling Flags設為--clear_datastore=yes。</p>
<p>
	<img alt="image" border="0" height="384" src="\images\postsdf6439e-3b43-4f0b-8476-d95661c3207a\image_thumb_2.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="566" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Python 的資料模型</li>
	<li>
		GQL Reference</li>
	<li>
		Property 類別</li>
	<li>
		類型和 Property 類別</li>
</ul>
