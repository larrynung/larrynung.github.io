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

    LiteDB: default - 5000 records
    ==============================
    Insert         :  4999 ms -     1000 records/second
    Bulk           :   236 ms -    21184 records/second
    Update         :  3674 ms -     1361 records/second
    CreateIndex    :   176 ms -    28321 records/second
    Query          :   204 ms -    24467 records/second
    Delete         :   157 ms -    31722 records/second
    Drop           :    17 ms -   289513 records/second
    FileLength     :  7580 kb
    
    LiteDB: encrypted - 5000 records
    ================================
    Insert         :  5690 ms -      879 records/second
    Bulk           :   280 ms -    17820 records/second
    Update         :  3784 ms -     1321 records/second
    CreateIndex    :   174 ms -    28669 records/second
    Query          :   208 ms -    24037 records/second
    Delete         :   207 ms -    24078 records/second
    Drop           :    56 ms -    87898 records/second
    FileLength     :  7576 kb
    
    LiteDB: exclusive no journal - 5000 records
    ===========================================
    Insert         :  4839 ms -     1033 records/second
    Bulk           :   219 ms -    22775 records/second
    Update         :  3242 ms -     1542 records/second
    CreateIndex    :   176 ms -    28379 records/second
    Query          :    93 ms -    53243 records/second
    Delete         :   140 ms -    35574 records/second
    Drop           :    14 ms -   334283 records/second
    FileLength     :  7572 kb
    
    SQLite: default - 5000 records
    ==============================
    Insert         : 46379 ms -      108 records/second
    Bulk           :   122 ms -    40827 records/second
    Update         : 47470 ms -      105 records/second
    CreateIndex    :    13 ms -   367266 records/second
    Query          :   457 ms -    10933 records/second
    Delete         :    11 ms -   441583 records/second
    Drop           :    11 ms -   454141 records/second
    FileLength     :  3824 kb
    
    SQLite: encrypted - 5000 records
    ================================
    Insert         : 49296 ms -      101 records/second
    Bulk           :   122 ms -    40851 records/second
    Update         : 48490 ms -      103 records/second
    CreateIndex    :    36 ms -   136413 records/second
    Query          :   463 ms -    10798 records/second
    Delete         :    13 ms -   357189 records/second
    Drop           :    25 ms -   199642 records/second
    FileLength     :  3856 kb
    
    SQLite: no journal - 5000 records
    =================================
    Insert         :  4107 ms -     1217 records/second
    Bulk           :   106 ms -    47121 records/second
    Update         :  4101 ms -     1219 records/second
    CreateIndex    :     8 ms -   592916 records/second
    Query          :   468 ms -    10680 records/second
    Delete         :     3 ms -  1578981 records/second
    Drop           :     3 ms -  1574952 records/second
    FileLength     :  3824 kb
    
<br/>


{% asset_img 2.png %}

<br/>


Link
----
* [LiteDB :: A .NET embedded NoSQL database](http://www.litedb.org/)
* [GitHub - mbdavid/LiteDB-Perf: A simple INSERT/BULK compare between SQLite and LiteDB v3](https://github.com/mbdavid/LiteDB-Perf)
