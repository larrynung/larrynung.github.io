---
title: "[C#]如何在程式中內嵌其它應用程式"
date: "2013-11-06 12:00:00"
description: "[C#]如何在程式中內嵌其它應用程式"
tags: [CSharp]
---

<p>
	最近筆者再嘗試實現類似Chrome的程式架構，程式由多個Process組成並協同運作，因此最先要碰到的課題就是要把別的應用程式Process給內嵌到程式內。</p>
<p>
	 </p>
<p>
	以內嵌小算盤為例，會期望程式能達到像下面這樣的效果：</p>
<p>
	<img alt="image" border="0" height="472" src="\images\posts\9848f1fb-de15-4e46-a34a-d35008280841\image_thumb_1.png" style="border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-top-width: 0px" width="440" /></p>
<p>
	 </p>
<p>
	要實現這樣的需求不難，叫出其它應用程式的Process後，待視窗出來後用SetParent API將它內嵌到我們程式的元件，再呼叫MoveWindow API將應用程式塞滿元件就可以了。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:266eb907-704a-4c5f-a378-090bd0013148" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="c#" name="code">
...
var handle = m_Process.MainWindowHandle;
			
if (HideApplicationTitleBar)
	SetWindowLong(handle, GWL_STYLE, WS_VISIBLE);

SetParent(handle, this.Handle);

MoveWindow(handle, 0, 0, this.Width, this.Height, true);
...</pre>
</div>
<p>
	 </p>
<p>
	內嵌完後比較麻煩的問題就是要怎樣讓內嵌的視窗隨著我們的程式縮放，這邊只要在我們的程式縮放時在次呼叫MoveWindow API調整就可以了。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a282a405-07a9-4dca-8cd0-aaf0198ac285" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="c#" name="code">
		void ApplicationHost_Resize(object sender, EventArgs e)
		{
			var handle = m_Process.MainWindowHandle;

			if (handle != IntPtr.Zero)
				MoveWindow(handle, 0, 0, this.Width, this.Height, true);
		}</pre>
</div>
<p>
	 </p>
<p>
	剩下的就是我們必須要在程式關閉時妥善地將內嵌的Process連帶釋放，這只要在解構子之類的地方將Process砍掉就可以了，應該沒什麼太大的問題。內嵌一個應用程式就是那麼容易。</p>
<p>
	 </p>
<p>
	這邊筆者也撰寫了一個名為ApplicationHost控制項，以便於以後重用，放在larrynung/ApplicationHostControl，有需要的就自行取用吧。</p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Hosting EXE Applications in a WinForm project</li>
	<li>
		Embedding different applications in a Win Form in .NET</li>
	<li>
		C#自定义控件：WinForm将其它应用程序窗体嵌入自己内部</li>
</ul>
