---
title: "Hubot - Create first script"
date: "2018-11-02 23:58:49"
description: "Hubot scripting 支援 Coffee script 與 Javascript，script 放置於 scripts 目錄下， 內含範本 example.coffee 可以參閱。"
tags: [Hubot]
---

Hubot scripting 支援 Coffee script 與 Javascript，script 放置於 scripts 目錄下， 內含範本 example.coffee 可以參閱。

![1.jpg](1.jpg)

![2.jpg](2.jpg)

在 scripts 目錄內建立 script 檔，像是筆者這邊就準備了一個簡單的 script，當監聽到 hello 就會回應 Hello world!。

```
module.exports = function(bot){
bot.respond(/hello/, function(res){
res.send('Hello world!');
});
}
```

![3.jpg](3.jpg)

將 Hubot 運行起來即可正常運作。

![4.jpg](4.jpg)

Link
----
* [Scripting](https://hubot.github.com/docs/scripting/)