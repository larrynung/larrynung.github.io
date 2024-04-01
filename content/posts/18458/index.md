---
title: ".NET 4.0 New Feature - Enum.HasFlag"
date: "2010-10-19 09:43:02"
description: ".NET 4.0 New Feature - Enum.HasFlag"
tags: [VB.NET]
---

<p> 在.NET 4.0以前，若有要判斷Flag屬性修飾過的列舉是否含有特定Flag時，我們會將列舉值與Flag去做And運算，判斷做完運算後的值是否等同Flag，像是下面這樣： </p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:487bb971-4b72-4a4b-9225-1740f60c6854" class="wlWriterSmartContent"><pre name="code" class="vb">Dim hasFlag = (enumValue And flag)  =  flag </pre></div>

<p>  </p>

<p>
  </p><p />  在.NET 4.0後我們有另一個更輕鬆的選擇就是Enum.HasFlag，使用上直接帶入要判斷的Flag即可。

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:bdcd3d21-a606-47a2-a7be-e78315a1c644" class="wlWriterSmartContent"><pre name="code" class="vb">Dim hasFlag = enumValue.HasFlag(flag)</pre></div>

<p> </p>

<p>這邊來看個簡化過的MSDN使用範例來加深印象</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:79e716b8-c94d-4183-a58c-01ae49f6ff93" class="wlWriterSmartContent"><pre name="code" class="vb">&lt;Flags&gt; Public Enum DinnerItems As Integer
   None = 0
   Entree = 1
   Appetizer = 2
   Side = 4
   Dessert = 8
   Beverage = 16 
   BarBeverage = 32
End Enum

...
   Dim myOrder As DinnerItems = DinnerItems.Appetizer Or DinnerItems.Entree Or
                                DinnerItems.Beverage Or DinnerItems.Dessert
   Dim hasFlag As Boolean = myOrder.HasFlag(DinnerItems.Entree Or DinnerItems.Beverage)
...</pre></div>

<p> </p>

<p>需特別注意的是當帶入的flag 其對應值是零時，則方法會傳回 true，在設計列舉時需加留意，不要把不是代表空值的列舉值設為0。</p>

<p> </p>

<p>.NET 4.0加入的Enum.HasFlag是個簡單好用的小方法，在拿列舉做些像是Enum 的設計與應用 - 簡易權限設計這篇介紹到的權限控管，或是拿來做一些狀態上的判斷時，使用Enum.HasFlag來替換傳統的處理方法會更為方便。</p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Enum.HasFlag 方法 </li>

  <li>Enum 的設計與應用 - 簡易權限設計 </li>
</ul>
