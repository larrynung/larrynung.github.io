---
layout: post
title: "Tkinter's tkColorChooser"
date: 2013-11-06 12:00:00
comments: true
tags: [Python]
description: "Tkinter's tkColorChooser"
---
<p>
	使用Tkinter中的tkColorChooser，可以為叫出顏色選取對話框。</p>
<p>
	 </p>
<p>
	使用時需先將tkColorChooser package import進來。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:5ec2be90-0681-44be-8992-e1ffb590630c" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
import tkColorChooser   </pre>
</div>
<p>
	 </p>
<p>
	Import完後就可以開始實際的撰寫程式，在此之前讓我們先來看一下tkColorChooser的函式原型：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9dfae048-1e49-4675-ad96-41ab0ee4126d" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
tkColorChooser.askcolor(color, options)</pre>
</div>
<p>
	 </p>
<p>
	因為預設選取的顏色較為常用，tkColorChooser.askcolor這邊允許我們直接將預設選取的顏色帶入。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:342b4757-d2ab-4e4d-aa80-99cd8df6f02a" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
...
print tkColorChooser.askcolor("red")
...</pre>
</div>
<p>
	 </p>
<p>
	除了預設選取的顏色外，tkColorChooser.askcolor也可以透過options參數帶入些其它的設定，像是initialcolor、parent、title。initialcolor一樣是預設選取的顏色、parent是用來指定對話框的父視窗，而title則是設定顏色選取對話框的標題列文字 (依筆者的經驗在Windows下設定並無效果)。</p>
<p>
	 </p>
<p>
	另外要注意到的是回傳值的部分，tkColorChooser.askcolor選取完顏色後對話框關閉會回傳(triple, color)這樣的Tuple。triple這部分是顏色的RGB值，color這部份則是對應的color物件。所以tkColorChooser.askcolor呼叫完所回傳的值會像下面這樣：</p>
<p>
	<img alt="image" border="0" height="59" src="\images\posts\edb1e98e-d6f7-4e4c-bb31-2c0dc2a0ce8d\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="298" /></p>
<p>
	 </p>
<p>
	最後附上筆者在測試時所用的範例：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:6037e07d-fd15-4e36-9493-83ff7446a6a2" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
import tkColorChooser   

print tkColorChooser.askcolor(title="test")
print tkColorChooser.askcolor("red")
print tkColorChooser.askcolor(initialcolor="red")</pre>
</div>
<p>
	 </p>
<p>
	在Windows下運行會出現色彩對話框...</p>
<p>
	<img alt="image" border="0" height="378" src="\images\posts\edb1e98e-d6f7-4e4c-bb31-2c0dc2a0ce8d\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="532" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		55.3. The tkColorChooser module</li>
</ul>
