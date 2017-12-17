---
title: LiteDB - Insert data
date: 2017-12-17 22:53:59
tags: [LiteDB]
---

要將資料塞入 LiteDB，需先將 LiteDB 開啟，取得 Collection，然後用 Collection.Insert 將資料塞入。  

<!-- More -->

```C#
…
using (var db = new LiteDatabase(dbFile)) 
{ 
  var collection = db.GetCollection<T>(collectionName); 

  var collectionItem = new T();
  collection.Insert(collectionItem); 
} 
```

<br/>


Collection.Insert 允許塞入單筆或是多筆資料，若要塞入多筆資料，調用 Collection.Insert 時帶入資料的集合即可。  

<br/>


除了 Collection.Insert，要塞入多筆資料也可以使用 Collection.InsertBulk，調用 Collection.InsertBulk 並帶入資料的集合與批次的大小，資料就會依指定的批次大小批次塞入。  

```C#
…
using (var db = new LiteDatabase(dbFile)) 
{ 
  var collection = db.GetCollection<T>(collectionName); 

  collection.InsertBulk(data, batchSize); 
} 
```
