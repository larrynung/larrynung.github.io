---
title: "[C#][CodePlex]LevelUp Serializer"
date: "2013-11-06 12:00:00"
description: "[C#][CodePlex]LevelUp Serializer"
tags: [CSharp]
---

<p>
	因為網路上的函式庫都不太合手，想整理個自己用的序列化函式庫已經有兩三年了，不是想做多大的函式庫，但卻也遲遲沒有毅力將這完成。直到這幾天才將寫到一半的函式庫打開來繼續撰寫、調整、測試，終於擠出了第一版本，目前已經可在CodePlex的LevelUp Serializer頁面中看到。</p>
<p>
	<img alt="image" border="0" height="429" src="\images\postsad443fe-d83e-40ac-9f64-b001e1519e59\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	以這函式庫來說大概有以下幾個特點</p>
<ol>
	<li>
		Ease of use</li>
	<li>
		Supports almost all serializer, like Binary、Xml、Soap、Json、DataContract.</li>
	<li>
		Support serialize to file、serialize to stream、deserialize from file、deserialize from stream.</li>
	<li>
		Support Xml encryption.</li>
	<li>
		Support serialize accelerate through the XML serialization assemble.</li>
</ol>
<p>
	 </p>
<p>
	簡單的說它就是使用簡單(對筆者而言)、支援大部份的序列化格式、支援序列化到檔案或是串流、從檔案或串流解序列化回物件、支援XML序列化後加密、以及會自動偵測XML序列化組件來加速等功能。</p>
<p>
	 </p>
<p>
	架構上也十分簡單，沒有什麼特別的設計。除了可以直接建出需要的Serializer來用外，也可以直接透過Serializer這個輔助類別去動作。</p>
<p>
	<img alt="2012-06-03_130715" border="0" height="389" src="\images\postsad443fe-d83e-40ac-9f64-b001e1519e59\2012-06-03_130715_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="644" /></p>
<p>
	 </p>
<p>
	使用方式就不多做說明，方案裡面的資料應該很齊全，除了類別圖外，也附有一些簡單的單元測試，看一下應該就OK了。簡單的帶一下，大概就是先取得對應的Serializer，這邊可以透過Serializer.GetSerializer取得。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e447a8d1-889d-4246-838e-fdeb8452c10f" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c" name="code">
ISerializer serializer = Serializer.GetSerializer(SerializerType.Xml);</pre>
</div>
<p>
	 </p>
<p>
	或是直接New出對應的Serializer。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:1ba0be96-34af-4ae2-a4a3-c38df73ca2ff" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
ISerializer serializer = New XmlSerializer();</pre>
</div>
<p>
	 </p>
<p>
	然後透過對應的Serializer去做序列化或解序列化的動作。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:bf39a19d-b939-4b26-bd0e-74dcfdc5a228" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
serializer.Serialize(obj, "Data.dat");
...
var deserializedObj = serializer.DeSerialize&lt;OBJECT_TYPE&gt;("Data.dat");</pre>
</div>
<p>
	 </p>
<p>
	除此之外也可以直接透過Serializer輔助類別去做序列化或解序列化。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:bdfca29c-7ecf-4465-abea-ae4fd189eabc" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
Serializer.Serialize(obj, "Data.dat", SerializerType.Xml);
...
var deSerializedObj = Serializer.DeSerialize&lt;OBJECT_TYPE&gt;("Data.dat", SerializerType.Xml);</pre>
</div>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		LevelUp Serializer</li>
</ul>
