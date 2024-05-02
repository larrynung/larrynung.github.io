---
title: ".NET 4.0 New Feature - Stopwatch.Restart"
date: "2013-11-06 12:00:00"
description: ".NET 4.0 New Feature - Stopwatch.Restart"
---

<p>在.NET 4.0以前使用Stopwatch來測量時間，若是想延用同一個Stopwatch物件來作量測的動作，我們會先呼叫Reset方法將測量的時間歸零，接著再呼叫Start方法重新啟動Stopwatch進行量測的動作，就想下面這樣：</p>  <div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:54b32177-503b-4731-ab62-a972984e1c20" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Dim sw As Stopwatch = Stopwatch.StartNew
sw.Start()
...
sw.Reset()
sw.Start()
... </pre></div>

<p> </p>

<p>而.NET 4.0在Stopwatch類別新增了Restart方法，可將計數的時間歸零後重新測量，因此像以往那樣的程式我們就可以如下撰寫：</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:abbbe3f6-036c-4329-b3d6-4bb7d91924f1" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Dim sw As Stopwatch = Stopwatch.StartNew
sw.Start()
...
sw.Restart()
...</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Stopwatch.Restart 方法</li>
</ul>
