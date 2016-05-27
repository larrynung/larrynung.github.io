---
layout: post
title: "Dos - Execute multiple commands in a single line"
date: 2014-09-03 21:35:00
comments: true
categories: [Dos]
keywords: "Dos"
description: "Dos - Execute multiple commands in a single line"
---

要將多行 Dos 命令寫在同一行，依據不同的使用情境，有著不同的寫法。  

<!-- More -->

<br/>

像是要在運行 Command A 完後接著運行 Command B，可以用 `&` 串接。  

    Command A & Command B


要在運行 Command A 後接著運行 Command B，並將 Command A 的運行輸出導到 Command B 的輸入，可以用 `|` 串接。   

    Command A | Command B


要在運行 Command A 後，判別 ErrorLevel 為 0 才繼續運行 Command B 的話，可以用 `&& ` 串接。  

    Command A && Command B


要在運行 Command A 後，判別 ErrorLevel 不為 0 才繼續運行 Command B 的話，可以用 `||` 串接。

    Command A || Command B


Link
----
* [dos - How to execute multiple commands in a single line - Stack Overflow](http://stackoverflow.com/questions/13719174/how-to-execute-multiple-commands-in-a-single-line)
