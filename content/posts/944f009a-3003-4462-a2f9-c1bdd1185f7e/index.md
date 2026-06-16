---
title: "Online Json format and validate tool"
date: "2013-11-06 12:00:00"
tags: [Web]
description: "這陣子在撰寫社群服務的程式，解析了很多社群服務API所吐回的格式，多半這些服務吐回的資訊都是Xml的，或是可選用Xml與Json，我都盡可能的選用慣用的Xml以避開處理Json。"
---

這陣子在撰寫社群服務的程式，解析了很多社群服務API所吐回的格式，多半這些服務吐回的資訊都是Xml的，或是可選用Xml與Json，我都盡可能的選用慣用的Xml以避開處理Json。

不過逃了半天終究還是有要面對的一天，最近將Facebook認證部份重寫時發現，資料是以Json型態存放在網址內，就算不願意還是得將資料解析。雖然解析的處理不會太麻煩，但看到一串未經格式化的Json資料實在很令人頭大，因此找了一下格式化的工具，讓解析的過程能更加順利。

下面摘錄一下這類型的線上工具:

JSONLint

JSONLint提供簡單的介面格式化並驗證JSON，使用上只要將JSON資料貼到上方編輯區，並按下Validate按鈕就可以了。按下按鈕後上方編輯區的內容會被格式化，下方Results會顯示所帶入的資料格式是否正確。

![image_thumb_6.png](/images/posts/944f009a-3003-4462-a2f9-c1bdd1185f7e/image_thumb_6.png)

JSON Formatter & Validator

JSON Formatter & Validator是目前看起來最好的，提供格式化與驗證功能，一樣在上方編輯區貼入JSON資料，或是直接只訂JSON資料所在的網址，按下Process按扭下方Results區就會顯示格式化後的資料與格式驗證的結果，這網站好的是除了會保留之前的紀錄，還會在右上方附上了複製之類的便捷按鈕。

![image_thumb_1.png](/images/posts/944f009a-3003-4462-a2f9-c1bdd1185f7e/image_thumb_1.png)

JSON format

JSON Format是我最先找到的線上工具，但也是最難用的，它也同樣的提供了格式化與驗證的功能，但在格式化方面它也做得過火了，格式化的同時會很雞婆的將資料的順序給排序，如果解析的處理方式會跟資料順序有關聯的話，會被他的好心排序給困擾住。在使用上跟上面的都大同小異，這邊就不再多做無謂的介紹。

![image_thumb_5.png](/images/posts/944f009a-3003-4462-a2f9-c1bdd1185f7e/image_thumb_5.png)

![image_thumb_4.png](/images/posts/944f009a-3003-4462-a2f9-c1bdd1185f7e/image_thumb_4.png)

## Link

* [Other]Online JSON Formatter
* JSONLint
* JSON Formatter & Validator
* JSON format
