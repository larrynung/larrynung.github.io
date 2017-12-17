---
title: "LiteDB - Create and open DB"
date: 2017-12-17 06:54:27
tags: [LiteDB]
---

LiteDB 使用上跟一般資料庫一樣需要先建立資料庫操作物件，帶入指定的資料庫檔案位置建立出 LiteDatabase 物件實體即可。  

<!-- More -->

```C#
…
using (var db = new LiteDatabase(dbFile)) 
{
  ... 
}
```

<br/>

 
LiteDatabase 物件實體建立後，即可針對 LiteDatabase 物件實體進行資料庫的操作，資料庫的連線 LiteDB 會幫我們開啟，不需自行開啟。若指定的資料庫檔案位置不存在資料庫檔案，LiteDB 會自動建立指定的資料庫檔案。  

<br/>


除了檔案形式的資料庫外，LiteDB 也允許我們使用記憶體形式的資料庫，只要建立 MemoryStream 帶入建立 LiteDatabase 的物件實體即可。  

```C#
…
using (var ms = new MemoryStream(buffer))
using (var db = new LiteDatabase(ms)) 
{
  ... 
} 
```

<br/>


這樣資料庫就會存在於記憶體中。在需要存放些資料在記憶體中的某些情境下，就可以評估使用 In-Memory 的 LiteDB。  
