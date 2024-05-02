---
title: ".NET 4.0 New Feature - Enum.TryParse"
date: "2010-10-20 12:57:39"
description: ".NET 4.0 New Feature - Enum.TryParse"
tags: [VB.NET]
---

<p>.NET 4.0加入的Enum.TryParse跟Enum.Parse同樣都是用來轉換資料回列舉型別用的方法，相較於Enum.Parse，Enum.TryParse方法少觸發了無法轉換時的例外，因此可以減去省去不必要的例外處理，跟一般其它類別的TryParse一樣，可直接透過方法的回傳值判別是否成功轉換。</p>  <p> </p>  <p>Enum.TryParse具有兩個多載方法，兩個多載方法的差異只在於在轉換列舉型別物件時是否會依照大小寫的不同下去處理。</p>  <p><img style="border-top-width: 0px; border-left-width: 0px; border-bottom-width: 0px; border-right-width: 0px" height="162" alt="image" src="\images\posts\18467\image_thumb.png" width="562" border="0" /> </p>  <p> </p>  <p>在使用Enum.TryParse轉換時，可以帶入的參數有列舉型別成員之基礎值或具名常數，或以逗號 (,) 分隔之具名常數清單的字串表示或基礎值清單。這邊在MSDN上的描述比起Enum.Parse多出了基礎值清單，看起來應該是可把列舉值用逗號串起去轉換，但這邊我試不出這樣的效果。而其它的轉換都跟Enum.Parse帶入的資料是一樣的，同樣以下面這個列舉為例來看一下使用方式。</p>  <div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:b37be79a-4391-485f-a3bf-f7bbcedd3a77" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">&lt;Flags()&gt; _
Enum Colors As Integer
        None = 0
        Red = 1
        Green = 2
        Blue = 4    
End Enum</pre></div>

<p> </p>

<p>我們可以像下面這般將數值轉換回列舉</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:aaebd612-1ead-4f8e-b2dd-4ed4b9f558f4" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Dim value As String = "1"
Dim colorValue As Colors
Dim pf As Boolean
pf = [Enum].TryParse(Of Colors)(value, colorValue)</pre></div>

<p> </p>

<p>把列舉型別常數名稱轉回列舉</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:43fdf8d0-535c-4070-9581-636c9ebf82a5" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Dim value As String = "Red"
Dim colorValue As Colors
Dim pf As Boolean
pf = [Enum].TryParse(Of Colors)(value, colorValue)</pre></div>

<p> </p>

<p>或是透過逗號串起的列舉型別常數名稱轉回列舉</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9d13c41a-4995-42f0-acc7-81d98bfd4ee3" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Dim value As String = String.Join(",", New Object() {"None", "Red", "Green"})
Dim colorValue As Colors
Dim pf As Boolean
pf = [Enum].TryParse(Of Colors)(value, colorValue)</pre></div>

<p>  </p>

<h2>Link</h2>

<ul>
  <li>Enum.TryParse 方法 </li>
</ul>
