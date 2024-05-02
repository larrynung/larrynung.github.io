---
title: "Tkinter's pack geometry manager"
date: "2013-11-06 12:00:00"
description: "Tkinter's pack geometry manager"
tags: [Python]
---

<p>
	Tkinter在做版面配置有三種方式，pack是其中一種。</p>
<p>
	 </p>
<p>
	使用pack來做版面配置，可以設定元件的內邊界、外邊界、是否塞滿、以及要停駐在哪邊。如果不做任何的停駐設定，預設元件是由上往下堆放。以其他程式語言來說，pack這種版面配置方式有點像是Dock與Stack兩種版面配置容器的結合。</p>
<p>
	 </p>
<p>
	在使用時若直接呼叫pack方法，元件會由上到下堆放，元件的大小設定多大就是多大，不會隨著視窗大小變動。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f9c0695f-beb3-4e8c-900d-b369aa11493d" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
...
lbl = Label(form, text="pack test1", bg="red")
lbl.pack()

lbl = Label(form, text="pack test2", bg="yellow")
lbl.pack()

lbl = Label(form, text="pack test3", bg="blue")
lbl.pack()
...</pre>
</div>
<p>
	 </p>
<p>
	<img alt="image" border="0" height="106" src="\images\posts\9567980f-44b2-4322-851e-93c0223a0e47\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="148" /></p>
<p>
	 </p>
<p>
	若是叫用pack方法時帶入fill的值，則元件會依照帶入的值去做塞滿。像是帶入X則元件的寬度會塞滿容器，帶入Y則元件的高度會塞滿容器，帶入BOTH則元件的寬度與高度都會塞滿容器(expand記得要設，不然元件可能不會隨容器放大)。</p>
<p>
	 </p>
<p>
	這邊也可以帶入side的值去指定元件要停駐在上(TOP)、下(BOTTOM)、左(LEFT)、右(RIGHT)。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:d10406f1-683b-4285-a4a1-1a758f90b006" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
...
lbl = Label(form, text="fill test1", bg="red")
lbl.pack(fill=X)

lbl = Label(form, text="fill test2", bg="yellow")
lbl.pack(side=LEFT, fill=Y)

lbl = Label(form, text="fill test2", bg="blue")
lbl.pack(fill=BOTH, expand=1)
...</pre>
</div>
<p>
	 </p>
<p>
	<img alt="image" border="0" height="85" src="\images\posts\9567980f-44b2-4322-851e-93c0223a0e47\image_thumb_3.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="148" /></a> <a href="http://files.dotblogs.com.tw/larrynung/1308/Tkinterspacklayoutmanager_A7F8/image_10.png"><img alt="image" border="0" height="218" src="\images\posts\9567980f-44b2-4322-851e-93c0223a0e47\image_thumb_4.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="335" /></p>
<p>
	 </p>
<p>
	如果要設定元件的內外邊界，我們可以在呼叫pack時帶入padx、pady、ipadx、ipady這幾的設定值，padx、pady是外邊界(相當於我們一般所說的margin)，ipadx、ipady是內邊界(相當於我們一般所說的padding)。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:3a031e48-344a-45c1-a8f3-f1098249abb4" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
...
lbl = Label(form, text="pad test", bg="green")
lbl.pack(fill=X, padx=5, pady=5)

lbl = Label(form, text="ipad test", bg="blue")
lbl.pack(fill=X, ipadx=5, ipady=5)
...</pre>
</div>
<p>
	 </p>
<p>
	<img alt="image" border="0" height="105" src="\images\posts\9567980f-44b2-4322-851e-93c0223a0e47\image_thumb_5.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="148" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Layout Managers / Geometry Manager</li>
</ul>
