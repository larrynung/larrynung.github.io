---
title: LiteDB - A .NET NoSQL Document Store in a single data file
date: 2017-12-15 23:19:17
tags: LiteDB
---

LiteDB 是一用 C# 寫的 .NET NoSQL 免費開源資料庫。  

<!-- More -->

{% asset_img 1.png %}

<br/>


有點像是 MongoDB 與 SQLite 的混合體，操作與使用上跟 MongoDB 相似，但又跟 SQLite 一樣是 Standalone 的資料庫，不像 MongoDB 需要架設服務，只需引用 250 KB 左右的組件即可直接使用。    

<br/>


該資料庫輕量且快速且具備有以下特點：  

- Portable UWP and Xamarin iOS/Android
- ACID transaction
- Recovery data in writing failure (journal mode)
- Map your POCO class to BsonDocument
- Fluent API for custom mapping
- Cross collections references (DbRef)
- Store files and stream data (like GridFS in MongoDB)
- LINQ support
- FREE for everyone - including commercial use

<br/>


Link
----
* [LiteDB :: A .NET embedded NoSQL database](http://www.litedb.org/)
