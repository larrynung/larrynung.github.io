---
title: "[Library]利用CodeDom序列化Control、表單等複雜物件"
date: "2009-07-13 12:47:54"
description: "最近很少發文，除了雜事纏身外，主要是在玩序列化與擴充方法。有玩過序列化的人相信都知道對於表單、Control等複雜的物件，我們並無法很直接的把它給序列化成檔案存起來。也很多人在論壇上問過類似的問題。"
tags: [Library]
---

最近很少發文，除了雜事纏身外，主要是在玩序列化與擴充方法。有玩過序列化的人相信都知道對於表單、Control等複雜的物件，我們並無法很直接的把它給序列化成檔案存起來。也很多人在論壇上問過類似的問題。像是：

1. MSDN-請問有沒有可能將Form物件序列化到硬碟儲存？
2. [程式設計俱樂部-請問如何動態儲存form](http://www.programmer-club.com.tw/showsametitleN/csharp/11142.html)

剛好最近在網路上看到對岸有人利用CodeDom寫好了現成的函式庫，抓下來試驗後確實可以Work，拿來儲存或複製控制項都還不錯，只可惜美中不足的是好像只能做二進制的序列化。有興趣的可以玩玩看。

[如何序列化Control等复杂类型对象](http://www.cnblogs.com/kevinshan/archive/2008/05/27/1208565.html)

![image_thumb_2.png](/images/posts/9453/image_thumb_2.png)

[How the sequence of Control, and other types of complex objects](http://www.googlemother.com/wpblogs/2008/05/27/howthesequenceofcontrolandothertypesofcomplexobjects/)

![image_thumb_1.png](/images/posts/9453/image_thumb_1.png)
