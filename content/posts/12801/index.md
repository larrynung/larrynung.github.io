---
title: "[C#]不同的Random物件給予不同的亂數種子"
slug: "[CSharp]不同的Random物件給予不同的亂數種子"
date: "2010-01-04 10:41:36"
description: "[C#]不同的Random物件給予不同的亂數種子"
tags: [CSharp]
---

<p>.NET Framework中，Random類別的建構函式有兩個。一個是不需帶參數的建構函式，使用其建構函式會使用時間相依預設種子值來初始化 Random 類別的新執行個體。其亂數種子是依系統時鐘衍生而來，解析度有限。若在極短的時間內頻繁叫用，會使得Random物件的亂數種子皆相同，因此得到完全相同的亂數組。另一個則是帶有一個參數的建構函式，可讓使用者自行帶入亂數種子。</p>  <p> </p>  <p>要讓不同的Random物件產生不同的亂數組，我們必須要做的是給予不同的Random物件不同的亂數種子。以往像這樣的需求我會這摸寫：    <br /></p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a20b1bed-d6f1-452d-bf83-8311305e71b7" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">Random r = new Random(DateTime.Now.Millisecond);</pre></div>

<p />

<p> </p>

<p>但在回應網友問題時才發現，使用這種寫法並無法有效的解決亂數重複問題。</p>

<p>後來再度嚐試MSDN的方法</p>

<p />

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:06dacf4f-c7b2-4403-b96c-58f19915ae6d" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">Random Counter = new Random(unchecked((int)(DateTime.Now.Ticks &gt;&gt; ctr)));</pre></div>

<p />

<p />

<p> </p>

<p>在極短的時間內一樣是無法有效的取得不同的亂數種子。最後想到用GUID的HashCode來當亂數種子帶入才能有效解決這問題。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:95f56efc-6e9b-4b86-a08a-0821b6908303" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">Random Counter = new Random(Guid.NewGuid().GetHashCode());</pre></div>

<p> </p>

<p>之所以能這樣寫是因為亂數種子必須要在極短的時間內帶入不同的值，而GUID剛好能有效的產生不重複的識別值，HashCode又是用來當作雜湊的Key，相同物件才會有相同的HashCode，因此GUID的HashCode剛好就能有效的產生不同的整數值作為亂數種子。Google了一下，這方法在對岸及國外都有在用，所以應該是沒有問題。</p>

<p> </p>

<p>除此之外，我們也可以自行設計其它的演算法來取得不同的亂數種子，就像這篇討論所探討的。</p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Random 建構函式 </li>

  <li>關於亂數 Random 問題 </li>

  <li>C#概念釐清，我的問題出在哪裡 ? </li>
</ul>
