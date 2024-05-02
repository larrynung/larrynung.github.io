---
title: "[HTML]HTML5 New Feature - x-webkit-speech"
date: "2013-11-06 12:00:00"
description: "[HTML]HTML5 New Feature - x-webkit-speech"
---

<p>
	HTML5的Input tag新提供x-webkit-speech語法，目前只能在Chrome 11以後的瀏覽器上使用，能讓我們將語音輸入的功能很簡單的帶到我們的網站中。最簡易的運用方式是像下面這樣將x-webkit-speech加在input tag後方就可以了。</p>
<script src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\5703874.js?file=gistfile1.html"></script>
<p>
	 </p>
<p>
	運行起來後我們可以在輸入框後方看到麥克風的圖示。</p>
<p>
	<img alt="image" border="0" height="132" src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="203" /></p>
<p>
	 </p>
<p>
	點選麥克風的圖示即可啟動語音輸入功能。</p>
<p>
	<img alt="image" border="0" height="212" src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\image_thumb_1.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="288" /></p>
<p>
	<img alt="image" border="0" height="136" src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\image_thumb_2.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="201" /></p>
<p>
	 </p>
<p>
	若有需要這邊我們可以再進一步透過lang指定語音輸入所要使用的語系，像是帶入lang= "zh-CN"的話，語音輸入所識別出來的文字就會變成簡體字。</p>
<script src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\5703874.js?file=gistfile2.html"></script>
<p>
	 </p>
<p>
	<img alt="image" border="0" height="147" src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\image_thumb_5.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="279" /></p>
<p>
	 </p>
<p>
	此外我們也可以透過onwebkitspeechchange去為語音輸入時加些對應的動作。</p>
<script src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\5703874.js?file=gistfile3.html"></script>
<p>
	 </p>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\image_thumb_4.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="602" /></p>
<p>
	 </p>
<p>
	x-webkit-speech使用上就是那麼簡單，但是最後這邊還是要再提一下，x-webkit-speech語法並不是所有瀏覽器都可以支援的，因此我們在使用上必須針對與法是否支援做些檢查，有需要的話檢查的動作可參閱下面的簡易範例。</p>
<script src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\5703874.js?file=gistfile4.html"></script>
<p>
	<img alt="image" border="0" height="484" src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	若有在用點部落的，我們也可以用這個語法來加強點部落的搜尋功能，只要在網站管理頁面的Custom HTML/Script區域將textSearch的element啟用webkitSpeech功能就可以了。</p>
<p>
	<img alt="image" border="0" height="419" src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\image_thumb_6.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
<p>
	 </p>
<p>
	是不是很簡單呢？</p>
<p>
	<img alt="image" border="0" height="76" src="\images\posts\4c7c9536-cf32-4c67-b33c-911f15226dff\image_thumb_7.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="309" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		x-webkit-speech 語音輸入功能</li>
	<li>
		Google語音識別||x-webkit-speech–HTML5實現聲音錄製功能的方法</li>
	<li>
		How to Use HTML5 Speech Input Fields</li>
	<li>
		x-webkit-speech input and textareas</li>
	<li>
		Collect Speech Input with HTML5 on Google Chrome</li>
</ul>
