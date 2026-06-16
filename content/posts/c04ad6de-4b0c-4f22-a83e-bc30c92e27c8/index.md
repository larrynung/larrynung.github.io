---
title: ".NET 4.0 New Feature - Stopwatch.Restart"
date: "2013-11-06 12:00:00"
description: "在.NET 4.0以前使用Stopwatch來測量時間，若是想延用同一個Stopwatch物件來作量測的動作，我們會先呼叫Reset方法將測量的時間歸零，接著再呼叫Start方法重新啟動Stopwatch進行量測的動作，"
---

在.NET 4.0以前使用Stopwatch來測量時間，若是想延用同一個Stopwatch物件來作量測的動作，我們會先呼叫Reset方法將測量的時間歸零，接著再呼叫Start方法重新啟動Stopwatch進行量測的動作，就想下面這樣：

```vb
Dim sw As Stopwatch = Stopwatch.StartNew
sw.Start()
...
sw.Reset()
sw.Start()
...
```

而.NET 4.0在Stopwatch類別新增了Restart方法，可將計數的時間歸零後重新測量，因此像以往那樣的程式我們就可以如下撰寫：

```vb
Dim sw As Stopwatch = Stopwatch.StartNew
sw.Start()
...
sw.Restart()
...
```

## Link

* Stopwatch.Restart 方法
