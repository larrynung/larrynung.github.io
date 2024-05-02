---
title: "Tkinter.TK"
date: "2013-11-06 12:00:00"
description: "Tkinter.TK"
tags: [Python]
---

<p>
	前面筆者在Hello, Tkinter這篇簡單的示範了一下最基本的Tkinter程式要如何撰寫。這邊進一步紀錄一下如何透過Tkinter.TK類別去設定與控制我們的程式視窗。</p>
<p>
	 </p>
<p>
	在設定前記得要先將Tkinter package import進來，import進來後宣告，我們才可以進行設定的動作。</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:95fac225-aa18-47a6-a3c1-2e88671ff0e0" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
from Tkinter import *
form = Tk()</pre>
</div>
<p>
	 </p>
<p>
	要設定視窗上的標題，可以叫用TK.title方法，帶入視窗標題所要顯示的字串。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0dd8fe5e-6ae6-45e9-91bc-c46ed8ffbbd6" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.title("Tkinter.TK Demo")</pre>
</div>
<p>
	 </p>
<p>
	要設定視窗標題前的小圖示，可叫用TK.iconbitmap方法，帶入視窗標題前要顯示的小圖示檔案位置。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f9cde87a-e2ce-43e3-abf3-849d437bc86c" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.iconbitmap('Icon.ico')</pre>
</div>
<p>
	 </p>
<p>
	要設定視窗的背景顏色，可叫用TK.configure方法，帶入視窗的背景顏色。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:d06e47f0-55fa-4910-863e-9fa8d4ecbf3b" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.configure(background='black')
form.configure(background='#888888')</pre>
</div>
<p>
	 </p>
<p>
	要設定視窗是否可以縮放，可以叫用TK.resizable方法。第一個帶入的參數是用來指定寬度大小是否可供縮放調整、第二個則是用來指定高度大小是否可供縮放調整。</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0649f631-2c44-405b-bb89-ae34abba1ea8" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.resizable(False, False)</pre>
</div>
<p>
	 </p>
<p>
	要設定視窗啟動時的大小與位置，可以叫用TK.geometry方法，帶入特定的格式字串(寬x長+左位移+右位移)。像是"300x200+10+10"就是在(10,10)這個位置建立大小的視窗。這邊若有需要也可以只指定視窗大小，或是視窗的位置，像是"300x200"與"+10+10"。</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:34d6cdef-2851-4319-8a90-3f3a9e22c191" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.geometry("300x200+10+10")</pre>
</div>
<p>
	 </p>
<p>
	要設定視窗最小的縮放大小，可以叫用TK.minsize方法，帶入視窗最小可接受的寬度與高度。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2167f978-35f3-4e68-9e04-f6f178e8ab91" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.minsize(300, 200)</pre>
</div>
<p>
	 </p>
<p>
	要設定視窗最大的縮放大小，可以叫用TK.maxsize方法，帶入視窗最大可接受的寬度與高度。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:03860dc2-ca44-471c-91cb-bb47c00b1ecb" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.maxsize(600, 400)</pre>
</div>
<p>
	 </p>
<p>
	要將視窗變成ToolWindow Style，可以呼叫TK.attributes("-toolwindow", 1)。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:b79fc627-7167-4f25-837e-c940b9f96791" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.attributes("-toolwindow", 1) </pre>
</div>
<p>
	 </p>
<p>
	要將視窗設為置頂視窗，可以呼叫TK.attributes("-topmost", 1)。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:77a0d5a1-c209-4f78-b339-d5d5ce705620" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.attributes("-topmost", 1) </pre>
</div>
<p>
	 </p>
<p>
	要在啟動時最大化，可以呼叫TK.state("zoomed")。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:403a9e2e-853e-4299-bb77-aa8690891ef5" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.state("zoomed")</pre>
</div>
<p>
	 </p>
<p>
	要最小化可以呼叫TK.iconify方法。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:8937a449-5966-4e09-bd9a-9971a0ad7475" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.iconify()</pre>
</div>
<p>
	 </p>
<p>
	要還原最小化可以呼叫TK.deiconify方法。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:32ea7430-01ee-4550-8931-06344965ef28" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
form.deiconify()</pre>
</div>
<p>
	 </p>
<p>
	最後實際來看個完整的使用範例：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f06ded55-6039-4899-9d66-6c84ef1a9126" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
from Tkinter import *

form = Tk()

form.title("Tkinter.TK Demo")
form.geometry("300x200+10+10")
form.iconbitmap('Icon.ico')
#form.resizable(False, False)
form.minsize(300, 200)
form.maxsize(600, 400)
#form.attributes("-toolwindow", 1) 
form.attributes("-topmost", 1) 
#form.state("zoomed")
#form.iconify()
#form.deiconify()
form.configure(background='black')

form.mainloop()</pre>
</div>
<p>
	 </p>
<p>
	運行起來會像下面這樣：</p>
<p>
	<img alt="image" border="0" height="243" src="\images\posts\8a8276ec-0f3a-4999-8ed5-74cfc8b050c4\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="320" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Toplevel Window Methods</li>
</ul>
