---
title: "GAE's Memcache"
date: "2013-11-06 12:00:00"
description: "GAE's Memcache"
---

<p>
	Memcache 是高效能、分散式的記憶體物件快取系統。存放在Memcache內的資料若一段時間不訪問，或是可供快取的空間用完時，快取的內容即會過時。</p>
<p>
	 </p>
<p>
	首先需先將google.appengine.ext.db import進來。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0901961e-28f5-4d60-b587-a533a8516416" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
from google.appengine.api import memcache</pre>
</div>
<p>
	 </p>
<p>
	要將資料存放到Memcache時，可以呼叫memcache.set方法，帶入資料的Key、Value、以及Timeout的時間 (Timeout的時間可以省略，若要指定需注意到這邊是以秒為單位)。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6b914f9b-197b-43d3-b733-f10e32f8665a" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
memcache.set(key, value, timeout)</pre>
</div>
<p>
	 </p>
<p>
	要將資料從Memcache讀出，可以呼叫memcache.get方法，帶入所要取出的資料鍵值。若有對應的資料存放在Memcache則會將值回傳，若無則會回傳None。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:33e493ee-71a3-4d2c-ab1b-2b01387eea6b" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
value = memcache.get(key)

if value:
	#Data still cached
	...
else:
	#Data without cached
	...</pre>
</div>
<p>
	 </p>
<p>
	除了單一值的存取外，Memcache也支援多值的存取。使用上會像下面這樣：</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:7d31a0cb-9475-4e11-b412-4f303f922e3c" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
memcache.set_multi({key1: value1, key2: value2})
values = memcache.get_multi([key1, key2])
value1 = values[key1]
value2 = values[key2]

</pre>
</div>
<p>
	 </p>
<p>
	存放改呼叫memcache.set_multi方法，用Dictionary帶入多筆Key/Value配對進去。取出資料則是改呼叫memcache.get_multi方法，用陣列帶入多筆鍵值。</p>
<p>
	 </p>
<p>
	實際看個簡單的例子：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9f2e1881-c85a-4895-a4d0-24734b53d31e" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
from google.appengine.api import memcache
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        memcache.set("name", "LevelUp")

        value = memcache.get("name")

        self.response.write(value + "&lt;br/&gt;")

        memcache.set_multi({"name": "LevelUp", "url": "httlp://www.dotblogs.com.tw/larrynung"})
        values = memcache.get_multi(["name", "url"])

        self.response.write(values["name"] + "&lt;br/&gt;")
        self.response.write(values["url"] + "&lt;br/&gt;")

application = webapp2.WSGIApplication([
	('/', MainHandler)
	])</pre>
</div>
<p>
	 </p>
<p>
	運行起來會像下面這樣：</p>
<p>
	<img alt="image" border="0" height="154" src="\images\posts44bf398-1a34-41e6-b71a-dcf59ccaa63f\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="327" /></p>
<p>
	 </p>
<p>
	再進一步將筆者GAE's Python Datastore API這篇的範例套用Memcache，讓用GQL讀取出的資料可以存放在Memcache中，可以像下面這樣撰寫：</p>
<h4>
	 </h4>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c45d7ea1-87f2-4c17-8f66-e0a675f5000b" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
from google.appengine.api import memcache
from google.appengine.ext import db
import webapp2
import uuid

class Article(db.Model):
    id = db.StringProperty(required=True)
    name = db.StringProperty()
    content = db.TextProperty()

class Blog(db.Model):
    id = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    url = db.LinkProperty(required=True)
    articleIDs = db.StringListProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("&lt;html&gt;&lt;body&gt;")

        blogs = db.GqlQuery("select * from Blog Limit 1")

        if not blogs or blogs.count() == 0:
            blog = Blog(id=str(uuid.uuid1()), name="LevelUp", url="http://www.dotblogs.com.tw/larrynung")

            articleID = str(uuid.uuid1())
            Article(id=articleID, name="hello", content="hello world").put()

            blog.articleIDs = [articleID]

            blog.put()
            self.response.write("Blog data saved...&lt;br/&gt;&lt;br/&gt;")
            self.redirect("/")
            return
        
        blog = memcache.get("blog")
        if blog:
            self.response.write("Cached blog data...&lt;br/&gt;&lt;br/&gt;")
        else:
            self.response.write("Blog data loading...&lt;br/&gt;&lt;br/&gt;")

            blog = Blog.gql("Limit 1")[0]

            self.response.write("Save blog data to memcache...&lt;br/&gt;&lt;br/&gt;")

            memcache.set("blog", blog, 5)

        self.response.write(blog.name + "&lt;br/&gt;")
        self.response.write(blog.url + "&lt;br/&gt;")

        for articleID in blog.articleIDs:
            article = Article.gql("where id = :1", articleID)[0]
            self.response.write(article.name + "&lt;/br&gt;")
            self.response.write(article.content + "&lt;/br&gt;")
            self.response.write("&lt;br/&gt;")


        self.response.write("&lt;/body&gt;&lt;/html&gt;")

application = webapp2.WSGIApplication([
	('/', MainHandler)
	])</pre>
</div>
<p>
	 </p>
<p>
	第一次運行就會將資料讀出後存放進Memcache。</p>
<p>
	<img alt="image" border="0" height="222" src="\images\posts44bf398-1a34-41e6-b71a-dcf59ccaa63f\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="361" /></p>
<p>
	 </p>
<p>
	再次運行就會改由Memcache中讀取。</p>
<p>
	<img alt="image" border="0" height="187" src="\images\posts44bf398-1a34-41e6-b71a-dcf59ccaa63f\image_thumb_2.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="334" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Using Memcache</li>
</ul>
