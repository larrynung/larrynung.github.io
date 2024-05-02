---
title: "[C#]C# 4.0 具名參數 (Named Parameters)"
date: "2009-07-30 09:05:43"
description: "[C#]C# 4.0 具名參數 (Named Parameters)"
tags: [CSharp]
---

<h2>Introduction</h2>  <p>具名參數是C# 4.0的特色之一，可搭配選擇性參數使用，主要功能是讓使用者可在呼叫函數時指定傳入的值要帶入哪個參數。    <br /> </p>  <h2>Support</h2>  <ul>   <li>C# 4.0  or latter      <br /> </li> </ul>  <h2>使用方式</h2>  <p>當我們想指定傳入的值要帶入的參數時，我們可以透過":"關鍵字來使用具名參數。</p>  <p>舉個例子來說，當我們有道函式其函式原型如下：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:daf181e4-b8ff-459d-9200-f527aee7499d" class="wlWriterSmartContent">   <pre class="c#:nocontrols" name="code">public Person(string name, SexType sex = SexType.Boy, int year = 18)</pre>
</div>

<p>若只想輸入名字與年紀，我們可以像這樣寫：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:92e80619-f4e1-43c6-a2b4-f01abddea138" class="wlWriterSmartContent">
  <pre class="c#:nocontrols" name="code">Person larry = new Person("Larry", year:29);</pre>
</div>

<p> </p>

<p> </p>

<p>或是</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9189268e-21e8-4af8-9451-4f54c690b9a1" class="wlWriterSmartContent">
  <pre class="c#:nocontrols" name="code">Person larry = new Person(name:"Larry", year:29);</pre>
</div>

<p>也可以不照順序輸入參數</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e1172c32-ca02-4bd8-9f49-93f84f7a8aaa" class="wlWriterSmartContent">
  <pre class="c:nocontrols" name="code">Person larry = new Person(year:29, name:"Larry");</pre>
</div>

<blockquote>
  <p>在VB.NET 8.0中也有提供對應的用法，使用的關鍵字為":="。</p>
</blockquote>

<h4> </h4>

<h2>Video</h2>

<p>下面列出一些網路上的示範影片，有興趣的可以順便看一下。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:5737277B-5D6D-4f48-ABFC-DD9C333F4C5D:8161eba9-0ffd-4874-b5f2-eb45e269fe4c" class="wlWriterEditableSmartContent"><div id="985fdc2e-f478-45b7-ab55-ba6b62707c01" style="margin: 0px; padding: 0px; display: inline;"><div><img src="\images\posts\9732ideo3329c488da15.jpg" style="border-style: none" galleryimg="no" onload="var downlevelDiv = document.getElementById('985fdc2e-f478-45b7-ab55-ba6b62707c01'); downlevelDiv.innerHTML = &quot;&lt;div&gt;&lt;object width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;param name=\&quot;movie\&quot; value=\&quot;http://www.youtube.com/v/vDHIPeLaREQ&amp;hl=en\&quot;&gt;&lt;\/param&gt;&lt;embed src=\&quot;http://www.youtube.com/v/vDHIPeLaREQ&amp;hl=en\&quot; type=\&quot;application/x-shockwave-flash\&quot; width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;\/embed&gt;&lt;\/object&gt;&lt;\/div&gt;&quot;;" alt="" /></div></div></div>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:5737277B-5D6D-4f48-ABFC-DD9C333F4C5D:6bfbd5b4-593d-43eb-814c-d5e7f5543f98" class="wlWriterEditableSmartContent"><div id="df438a79-81e3-4b8f-8182-5c99a6a1330e" style="margin: 0px; padding: 0px; display: inline;"><div><img src="\images\posts\9732ideo7e6ac25a3a9d.jpg" style="border-style: none" galleryimg="no" onload="var downlevelDiv = document.getElementById('df438a79-81e3-4b8f-8182-5c99a6a1330e'); downlevelDiv.innerHTML = &quot;&lt;div&gt;&lt;object width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;param name=\&quot;movie\&quot; value=\&quot;http://www.youtube.com/v/8RN14Rgrw5w&amp;hl=en\&quot;&gt;&lt;\/param&gt;&lt;embed src=\&quot;http://www.youtube.com/v/8RN14Rgrw5w&amp;hl=en\&quot; type=\&quot;application/x-shockwave-flash\&quot; width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;\/embed&gt;&lt;\/object&gt;&lt;\/div&gt;&quot;;" alt="" /></div></div></div>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:5737277B-5D6D-4f48-ABFC-DD9C333F4C5D:7b4beedb-7133-46fb-b832-6f6d4fcae3e4" class="wlWriterEditableSmartContent"><div id="c6e7f0a8-44a1-4267-bcc2-26b3c459997e" style="margin: 0px; padding: 0px; display: inline;"><div><img src="\images\posts\9732ideoaade64e08bd3.jpg" style="border-style: none" galleryimg="no" onload="var downlevelDiv = document.getElementById('c6e7f0a8-44a1-4267-bcc2-26b3c459997e'); downlevelDiv.innerHTML = &quot;&lt;div&gt;&lt;object width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;param name=\&quot;movie\&quot; value=\&quot;http://www.youtube.com/v/rSekCQIDDbE&amp;hl=en\&quot;&gt;&lt;\/param&gt;&lt;embed src=\&quot;http://www.youtube.com/v/rSekCQIDDbE&amp;hl=en\&quot; type=\&quot;application/x-shockwave-flash\&quot; width=\&quot;425\&quot; height=\&quot;355\&quot;&gt;&lt;\/embed&gt;&lt;\/object&gt;&lt;\/div&gt;&quot;;" alt="" /></div></div></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>C# 4.0 新特性：動態型別、選用參數、具名參數</li>

  <li>C# 4.0 Named Parameters for better code quality</li>

  <li>New Features in C# 4.0</li>

  <li>C# 4.0's New Features Explained</li>
</ul>
