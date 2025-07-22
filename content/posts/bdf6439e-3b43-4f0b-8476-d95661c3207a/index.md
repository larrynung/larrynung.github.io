---
title: "GAE's Python Datastore API"
date: "2013-11-06 12:00:00"
description: "GAE's Python Datastore API"
---

GAE提供了一組Datastore API，可以讓我們將資料存在雲端，這邊一樣以Python為例簡單的紀錄一下。

	首先將google.appengine.ext.db import進來。

from google.appengine.ext import db

	接著必須設定我們要儲存的Model類別。

	宣告繼承自db.model的類別，並在裡面宣告需要的Property (類似資料庫的欄位，Property的型態可參閱類型和 Property 類別這篇)就可以了。

	以下面這程式碼片段為例：

class Article(db.Model):
    id = db.StringProperty(required=True)
    name = db.StringProperty()
    content = db.TextProperty()

class Blog(db.Model):
    id = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    url = db.LinkProperty(required=True)
    articleIDs = db.StringListProperty()

	這邊筆者建立了一個名為Article的Model，裡面有id、name、以及content這幾個Property。id可用來識別article，為必要的參數，存放的資料為string型態；name是文章的標題，存放的資料一樣是string型態；content則是文章的內文，因為文章的內文可能很長， 所以這邊用text型態 (可超越500字)。

	另外一個Model是Blog，裡面有id、name、url、以及articleIDs這幾個Property，id與name跟Article Model的大同小異，url是blog的網址，為必要的參數，存放的資料為link型態；articleIDs是部落格的文章ID清單，存放的資料為string list型態。

	Model類別建立好，當我們要儲存資料時只要建立出Model的物件實體，填入對應的資料後呼叫put方法就可以了。

            ...
            blog = Blog(id=str(uuid.uuid1()), name="LevelUp", url="http://www.dotblogs.com.tw/larrynung")

            articleID = str(uuid.uuid1())
            Article(id=articleID, name="hello", content="hello world").put()

            blog.articleIDs = [articleID]

            blog.put()
            ...

	資料的取出這邊我們可以透過db.GqlQuery帶入GQL語法 (類似SQL語法，詳細的語法可參閱GQL Reference這篇)去做。

...
blog = db.GqlQuery("select * from Blog Limit 1")[0]
...

	或是直接呼叫Model的gql方法也可以。

...
blog = Blog.gql("Limit 1")[0]
...

	最後這邊實際來看個完整的範例程式：

	這範例程式會先嘗試用GQL去讀取Blog資料，若是已經有Blog的資料則將它呈現在畫面上。若是還沒有Blog的資料，則會建立預設的資料並存入，存入後將頁面重新導回做呈現。

	所以運行起來應該會像下面這樣：

	最後一提，在試驗Datastore API時，我們可能會在試驗的同時存了過多不正確的資訊進去，若想每次都是在乾淨的狀況下進行測試，這邊可以開啟Google App Engine Launcher，點擊[Edit/Application Settings...]選單選項。

	在Application Settings設定對話框中，將Extra Command Ling Flags設為--clear_datastore=yes。

## 
	Link

		Python 的資料模型
	
		GQL Reference
	
		Property 類別
	
		類型和 Property 類別