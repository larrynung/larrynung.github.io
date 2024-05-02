---
title: "[VB.NET]使用TabControlEx控制項快速抽換表單介面與實現精靈介面"
date: "2013-11-06 12:00:00"
description: "[VB.NET]使用TabControlEx控制項快速抽換表單介面與實現精靈介面"
---

<p>
	這篇要介紹的是如何抽換表單介面與實現精靈介面，順便介紹自己試寫的TabControlEx控制項，雖說是TabControl的加強版控制項，但其實也只比傳統的TabControl控制項多一個ShowPageOnly屬性。</p>
<p>
	 </p>
<h2>
	抽換表單介面</h2>
<p>
	舉個例子來說，假設今天需要撰寫個可以替換頁面的程式，當按下Button1時程式右側會切到對應畫面(如下圖)。</p>
<p>
	<img alt="image" border="0" height="223" src="\images\posts\53aa999f-0ec0-4de3-9ab2-db0b9de16504\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="387" /></p>
<p>
	 </p>
<p>
	當按下Button2時則顯示另一個畫面。</p>
<p>
	<img alt="image" border="0" height="223" src="\images\posts\53aa999f-0ec0-4de3-9ab2-db0b9de16504\image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="387" /></p>
<p>
	 </p>
<p>
	在以往，這樣的程式是需要在程式內部存放各頁面物件的參考(可搭配使用使用者控制項)，並依使用者動作抽換頁面。這樣的方法不僅在設計介面無法所見即所得，撰寫上也十分的不便。</p>
<p>
	程式碼範例如下：</p>
<div style="width: 661px; height: 276px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">Dim</span> tabs() <span class="kwrd">As</span> Control = <span class="kwrd">New</span> Control() {<span class="kwrd">New</span> DataGridView, <span class="kwrd">New</span> MonthCalendar}</pre>
		<pre>
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button1_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button1.Click</pre>
		<pre class="alt">
		RemoveTabs()</pre>
		<pre>
		tabs(0).Parent = <span class="kwrd">Me</span>.SplitContainer1.Panel2</pre>
		<pre class="alt">
		<span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>
		<pre>
		 </pre>
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button2_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button2.Click</pre>
		<pre>
		RemoveTabs()</pre>
		<pre class="alt">
		tabs(1).Parent = <span class="kwrd">Me</span>.SplitContainer1.Panel2</pre>
		<pre>
		<span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>
		<pre class="alt">
		 </pre>
		<pre>
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> RemoveTabs()</pre>
		<pre class="alt">
		<span class="kwrd">For</span> <span class="kwrd">Each</span> c <span class="kwrd">As</span> Control <span class="kwrd">In</span> tabs</pre>
		<pre>
		c.Parent = <span class="kwrd">Nothing</span></pre>
		<pre class="alt">
		<span class="kwrd">Next</span></pre>
		<pre>
		<span class="kwrd">End</span> Sub</pre>
	</div>
</div>
<p>
	 </p>
<p>
	而若是使用TabControlEx的話，在設計上就跟使用一般的TabControl一樣。</p>
<p>
	<img alt="image" border="0" height="263" src="\images\posts\53aa999f-0ec0-4de3-9ab2-db0b9de16504\image_thumb_2.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="414" /></p>
<p>
	 </p>
<p>
	表單設完後，變更ShowPageOnly屬性為True，TabControl上方的分頁標籤就會消失。</p>
<p>
	<img alt="image" border="0" height="232" src="\images\posts\53aa999f-0ec0-4de3-9ab2-db0b9de16504\image_thumb_3.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="605" /></p>
<p>
	 </p>
<p>
	在表單切換上也是跟TabControl一樣，用SelectedIndex之類的屬性或方法就可以了。</p>
<div style="width: 659px; height: 137px; overflow: auto">
	<div class="csharpcode">
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button1_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button1.Click</pre>
		<pre>
		<span class="kwrd">Me</span>.TabControlEx1.SelectedIndex = 0</pre>
		<pre class="alt">
		<span class="kwrd">End</span> <span class="kwrd">Sub</span></pre>
		<pre>
		 </pre>
		<pre class="alt">
		<span class="kwrd">Private</span> <span class="kwrd">Sub</span> Button2_Click(<span class="kwrd">ByVal</span> sender <span class="kwrd">As</span> System.<span class="kwrd">Object</span>, <span class="kwrd">ByVal</span> e <span class="kwrd">As</span> System.EventArgs) <span class="kwrd">Handles</span> Button2.Click</pre>
		<pre>
		<span class="kwrd">Me</span>.TabControlEx1.SelectedIndex = 1</pre>
		<pre class="alt">
		<span class="kwrd">End</span> Sub</pre>
	</div>
</div>
<p>
	 </p>
<p>
	TabControlEx實作的概念很簡單，其實只是把當前TabControl頁面上的控制項，全部移到蓋在TabControl上的Panel，達到無分頁標籤的假象而已。</p>
<p>
	 </p>
<h2>
	精靈介面</h2>
<p>
	了解了TabControlEx的新增的唯一功能後 ，有感覺的人應該可以想到其它的應用，在此順便介紹一種另外的應用。就是其實它也可以做到精靈介面，只需少少幾個步驟：</p>
<p>
	<strong>Step1.在各分頁加入精靈介面的背景與元件</strong></p>
<p>
	<img alt="image" border="0" height="438" src="\images\posts\53aa999f-0ec0-4de3-9ab2-db0b9de16504\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="626" /></p>
<p>
	<img alt="image" border="0" height="442" src="\images\posts\53aa999f-0ec0-4de3-9ab2-db0b9de16504\image_thumb_1.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="627" /></p>
<p>
	<strong>Step2.加上切換頁面的程式碼</strong></p>
<p>
	只需透過SelectedIndex之類的屬性或方法就可以了。</p>
<p>
	<strong>Step3.把ShowPageOnly屬性設為False</strong></p>
<p>
	<img alt="image" border="0" height="439" src="\images\posts\53aa999f-0ec0-4de3-9ab2-db0b9de16504\image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="906" /></p>
<p>
	 </p>
<h2>
	注意事項</h2>
<p>
	雖然上述例子都是用屬性框直接把ShowPageOnly直接設為True，但在使用上建議在Form.Load事件用程式碼改屬性值，因為控制項仍有小Bug。</p>
<p>
	 </p>
<h2>
	Download</h2>
<p>
	TabControlEx.zip</p>
