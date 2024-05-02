---
title: "[VB.NET].NET多語系程式(一)"
date: "2009-04-24 12:32:11"
description: "[VB.NET].NET多語系程式(一)"
tags: [VB.NET]
---

<h2>
	<img alt="image" border="0" height="179" src="\images\posts\8158\image_thumb_16.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="561" /></h2>
<h2>
	範例說明</h2>
<p>
	本篇將介紹.NET多語系程式的寫法 ，下面會利用最簡單方便且正統的方法也就是資源檔來達到多語系的功能。</p>
<p>
	 </p>
<h2>
	學習目標</h2>
<ul>
	<li>
		.NET多語程式撰寫</li>
	<li>
		資源檔的使用與操作</li>
	<li>
		CultureInfo類別的使用</li>
	<li>
		語系的切換</li>
</ul>
<p>
	 </p>
<h2>
	操作步驟</h2>
<h3>
	介面上的多語</h3>
<p>
	<strong>Step1.將表單的Localizable屬性設為True</strong></p>
<p>
	<img alt="image" border="0" height="24" src="\images\posts\8158\image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="244" /></p>
<p>
	 </p>
<p>
	<strong>Step2.切換表單的Language屬性為欲使用的語系</strong></p>
<p>
	<img alt="image" border="0" height="23" src="\images\posts\8158\image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="244" /></p>
<p>
	設完後會在分頁標籤上看到目前設定的語系</p>
<p>
	<img alt="image" border="0" height="25" src="\images\posts\8158\image_thumb_4.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="244" /></p>
<p>
	 </p>
<p>
	<strong>Step3.設定介面上欲顯示的字樣並適當的調整版面</strong></p>
<p>
	<img alt="image" border="0" height="23" src="\images\posts\8158\image_thumb_2.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="244" /></p>
<p>
	<img alt="image" border="0" height="108" src="\images\posts\8158\image_thumb_3.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="206" /></p>
<p>
	 </p>
<p>
	到此，用資源檔做的多語系程式就完成了。</p>
<p>
	我們可以到檔案總管看一下，可看到Visual Studio自己幫我們產生了對應的資源檔。</p>
<p>
	<img alt="image" border="0" height="170" src="\images\posts\8158\image_thumb_5.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="244" /></p>
<p>
	因此，在實作介面上的多語時，我們並不需自己手動加入資源檔。</p>
<p>
	<img alt="image" border="0" height="395" src="\images\posts\8158\image_thumb_9.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="687" /></p>
<p>
	 </p>
<h3>
	訊息的多語</h3>
<p>
	上面的範例帶出了介面上支援多語的寫法，但卻不適用於訊息上，若要在訊息上也支援多語。請依下列步驟：</p>
<p>
	<strong>Step1.加入資源檔</strong></p>
<p>
	資源檔依照 "資源檔名.文化特性.resx" 格式命名，如 "Resources.zh-tw.resx"。</p>
<p>
	<img alt="image" border="0" height="395" src="\images\posts\8158\image_thumb_9.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="687" /></p>
<p>
	 </p>
<p>
	<strong>Step2.設定資源檔內的訊息內容</strong></p>
<p>
	在資源檔上連點兩下</p>
<p>
	<img alt="image" border="0" height="205" src="\images\posts\8158\image_thumb_12.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="283" /></p>
<p>
	設定對應的語系字串</p>
<p>
	<img alt="image" border="0" height="141" src="\images\posts\8158\image_thumb_11.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="424" /></p>
<p>
	<img alt="image" border="0" height="133" src="\images\posts\8158\image_thumb_13.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="388" /></p>
<p>
	 </p>
<p>
	<strong>Step3.使用資源檔內的訊息內容</strong></p>
<p>
	這邊只要透過My.Resources去取出資源檔內的值即可，內部OR Mapping轉換都幫你做好好，可以用強型別的方式直接取用，能避免掉許多不必要的低級錯誤。</p>
<div class="csharpcode">
	<pre class="alt">
MsgBox(My.Resources.Resource1.String1)</pre>
</div>
<div class="csharpcode">
	 </div>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[

.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	 </p>
<p>
	其實個人習慣是命名為 "Resources.文化特性.resx"，因為專案裡已偷放了一個Resources.resx資源檔，因此只需加入非預設語系的資源檔即可。</p>
<p>
	<img alt="image" border="0" height="207" src="\images\posts\8158\image_thumb_14.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="277" /></p>
<p>
	 </p>
<p>
	在使用上也會變得較為簡短</p>
<div class="csharpcode">
	<pre class="alt">
MsgBox(My.Resources.String1)</pre>
</div>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[

.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	 </p>
<h2>
	切換語系</h2>
<p>
	依上面步驟操作完後，其實已具多語支援能力。當程式開啟時，會自動依照當前語系去顯示介面畫面。因此我們開啟時應該是顯示中文而不是本來的英文。若要自己切換語系可利用Threading.Thread.CurrentThread.CurrentUICulture。</p>
<div class="csharpcode">
	<pre class="alt">
Threading.Thread.CurrentThread.CurrentUICulture = New CultureInfo(<span class="str">"en"</span>)</pre>
</div>
<p>
	值得注意的是，這樣的寫法是不會影響已開啟的視窗的。只有後來開啟的視窗會被切換語系。</p>
<p>
	那是否已開啟的視窗就無法切換了呢？那倒也不是。可以透過使用ResourceManager.GetString去取得對應的字串，把取出的字串再設到介面上即可。但是這也不是很好的方法，個人傾向使用ComponentResourceManager配合遞迴去把介面上的字串換成對應語系的字串。有興趣的可以參考Form.Designer.vb檔的程式碼。</p>
<p>
	<img alt="image" border="0" height="200" src="\images\posts\8158\image_thumb_7.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="281" /></p>
<p>
	 </p>
<p>
	</p><style type="text/css"><![CDATA[

.csharpcode, .csharpcode pre
{
	font-size: small;
	color: black;
	font-family: consolas, "Courier New", courier, monospace;
	background-color: #ffffff;
	/*white-space: pre;*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt 
{
	background-color: #f4f4f4;
	width: 100%;
	margin: 0em;
}
.csharpcode .lnum { color: #606060; }]]></style>

<p>
	<img alt="image" border="0" height="269" src="\images\posts\8158\image_thumb_8.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="440" /></p>
<p>
	 </p>
<h2>
	注意事項</h2>
<p>
	在用多國語言資源檔時，建議最後在弄其它語系的設定。因為當我們設定多語系時，Visual Studio會自動幫我們產生資源檔，且內含預設的設定值。若太早讓Visual Studi產生資源檔，則預設的設定值將只有少少的幾個，後面的設定值都需手動的設定，且每個語系的資源檔都要設定。</p>
<p>
	<img alt="image" border="0" height="376" src="\images\posts\8158\image_thumb_17.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="770" /></p>
