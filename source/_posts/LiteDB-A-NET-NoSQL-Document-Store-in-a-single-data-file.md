---
title: LiteDB - A .NET NoSQL Document Store in a single data file
date: 2017-12-15 23:19:17
tags: LiteDB
---

LiteDB 是一用 C# 寫的 .NET NoSQL 免費開源資料庫。  

<!-- More -->

{% asset_img 1.png %}

<br/>


具備有以下特點：

- Lightweight
- Fast
- Thread safe
- Process safe
- Portable UWP and Xamarin iOS/Android
- ACID transaction
- Recovery data in writing failure (journal mode)
- Map your POCO class to BsonDocument
- Fluent API for custom mapping
- Cross collections references (DbRef)
- Store files and stream data (like GridFS in MongoDB)
- LINQ support
- FREE for everyone - including commercial use
- Shell command line
- Datafile encryption using DES (AES) cryptography

<br/>


LiteDB 有點像是 MongoDB 與 SQLite 的混合體，操作與使用上跟 MongoDB 相似，但又跟 SQLite 一樣是 Standalone 的資料庫，不像 MongoDB 需要架設服務，只需引用 250 KB 左右的組件即可直接使用。    

<br/>


因為跟 SQLite 一樣是 Sandalone 的資料庫，所以適用的情境跟 SQLite 類似，適用於行動裝置的應用程式、小型的桌面應用程式、小型的網頁應用程式...等。  

<br/>


這邊作者也拿 SQLite 與 LiteDB 做了些效能的比較，可做為資料庫方案決定的參考依據。   

{% asset_img 2.png %}

<br/>


Link
----
* [LiteDB :: A .NET embedded NoSQL database](http://www.litedb.org/)
* [GitHub - mbdavid/LiteDB-Perf: A simple INSERT/BULK compare between SQLite and LiteDB v3](https://github.com/mbdavid/LiteDB-Perf)
