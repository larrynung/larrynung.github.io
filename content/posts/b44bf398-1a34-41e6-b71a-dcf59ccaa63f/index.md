---
title: "GAE's Memcache"
date: "2013-11-06 12:00:00"
description: "GAE's Memcache"
---
Memcache 是高效能、分散式的記憶體物件快取系統。存放在Memcache內的資料若一段時間不訪問，或是可供快取的空間用完時，快取的內容即會過時。

首先需先將google.appengine.ext.db import進來。

from google.appengine.api import memcache

要將資料存放到Memcache時，可以呼叫memcache.set方法，帶入資料的Key、Value、以及Timeout的時間 (Timeout的時間可以省略，若要指定需注意到這邊是以秒為單位)。

memcache.set(key, value, timeout)

要將資料從Memcache讀出，可以呼叫memcache.get方法，帶入所要取出的資料鍵值。若有對應的資料存放在Memcache則會將值回傳，若無則會回傳None。

value = memcache.get(key)

if value:
#Data still cached
...
else:
#Data without cached
...

除了單一值的存取外，Memcache也支援多值的存取。使用上會像下面這樣：

memcache.set_multi({key1: value1, key2: value2})
values = memcache.get_multi([key1, key2])
value1 = values[key1]
value2 = values[key2]

存放改呼叫memcache.set_multi方法，用Dictionary帶入多筆Key/Value配對進去。取出資料則是改呼叫memcache.get_multi方法，用陣列帶入多筆鍵值。

實際看個簡單的例子：

from google.appengine.api import memcache
import webapp2

class MainHandler(webapp2.RequestHandler):
def get(self):
memcache.set("name", "LevelUp")

value = memcache.get("name")

self.response.write(value + "
")

memcache.set_multi({"name": "LevelUp", "url": "httlp://www.dotblogs.com.tw/larrynung"})
values = memcache.get_multi(["name", "url"])

self.response.write(values["name"] + "
")
self.response.write(values["url"] + "
")

application = webapp2.WSGIApplication([
('/', MainHandler)
])

運行起來會像下面這樣：

再進一步將筆者GAE's Python Datastore API這篇的範例套用Memcache，讓用GQL讀取出的資料可以存放在Memcache中，可以像下面這樣撰寫：

####

from google.appengine.api import memcache
from google.appengine.ext import db
import webapp2
import uuid

class Article(db.Model):
content = db.TextProperty()

class Blog(db.Model):
url = db.LinkProperty(required=True)
articleIDs = db.StringListProperty()

class MainHandler(webapp2.RequestHandler):
def get(self):
self.response.write("")

blogs = db.GqlQuery("select * from Blog Limit 1")

if not blogs or blogs.count() == 0:
blog = Blog(, url="http://www.dotblogs.com.tw/larrynung")

article
Article(, content="hello world").put()

blog.articleIDs = [articleID]

blog.put()
self.response.write("Blog data saved...

")
self.redirect("/")
return

blog = memcache.get("blog")
if blog:
self.response.write("Cached blog data...

")
else:
self.response.write("Blog data loading...

")

blog = Blog.gql("Limit 1")[0]

self.response.write("Save blog data to memcache...

")

memcache.set("blog", blog, 5)

self.response.write(blog.name + "
")
self.response.write(blog.url + "
")

for articleID in blog.articleIDs:
article = Article.gql("where articleID)[0]
self.response.write(article.name + "")
self.response.write(article.content + "")
self.response.write("
")

self.response.write("")

application = webapp2.WSGIApplication([
('/', MainHandler)
])

第一次運行就會將資料讀出後存放進Memcache。

再次運行就會改由Memcache中讀取。

##
Link

Using Memcache