---
title: "[.NET Concept]例外處理使用時機"
date: "2009-04-04 07:01:01"
description: "[.NET Concept]例外處理使用時機"
tags: [.NET Concept]
---

<p>
	<img alt="image" border="0" height="203" src="\images\posts\7854\image_thumb_4.png" style="border-top-width: 0px; border-left-width: 0px; border-bottom-width: 0px; border-right-width: 0px" width="553" /></p>
<p>
	看到網友Bill叔寫了一連串的Try Catch的探討，這邊我也大概的整理一下我對例外處理使用時機的認知。</p>
<p>
	 </p>
<p>
	我常會看到很多我覺得不適當的例外處理寫法，大概可列出下面幾種：</p>
<ul>
	<li>
		<strong>例外處理只為了秀出Exception本來包含的訊息，完全不改成自己格式就直接秀出</strong></li>
</ul>
<p>
	像下面這種寫法秀出的資訊少到完全看不出問題點，且可能讓程式在不正常的條件下繼續執行。這樣的寫法倒不如不要使用例外處理直接讓.NET程式預設的例外視窗彈出，資訊還較為豐富，不然就是自行客制處理例外訊息的對話框，讓例外訊息對話框變成自己想要的樣子。而且通常例外所提供的訊息並不適合給使用者看，一來對於使用者並不友善，二來也多半沒有做多語的支援。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c80d45be-e5a0-4c1e-a78e-c200364807eb" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px">
	<pre class="vb" name="code">
Try
     ...
Catch ex As Exception
     MsgBox(ex.Message)
End Try</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<ul>
	<li>
		<strong>例外處理後又讓例外外擴</strong></li>
</ul>
<p>
	像下面這種寫法其實倒不如不要寫例外處理，例外本身就會外擴。除非攔截例外是為了做些記錄或是處理，不然不建議攔截後外擴，大家應該都知道例外處理攔截到例外的Overhead是很大的，若是一個例外發生後被攔截後外擴，連續發生了好幾次，不難推測這個Overhead會變成本來的好幾倍。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:438b236a-e7a1-49c9-b526-683589ab3832" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px">
	<pre class="vb" name="code">
Try
     ...
Catch ex As Exception
     throw ex
End Try</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	若是需要在例外處理中攔截例外做些處理後再外擴，也該改用throw去取代throw ex，這樣速度會比較快，也不會去變更到呼叫堆疊。</p>
<p>
	 </p>
<ul>
	<li>
		<strong>例外處理只為了吞掉例外</strong></li>
</ul>
<p>
	最糟的寫法是直接用例外處理來吞掉例外，當然有時候這樣的情況會無法避免，但起碼要知道自己在做甚麼，並盡可能的避免，畢竟這樣的處理方式不夠嚴謹，且例外處理的耗費是很重的，若頻繁執行到這個區塊，效能會大幅的降低。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2c648439-b3e4-4d09-9c2b-0574f40522b8" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px">
	<pre class="vb" name="code">
Try      
    ...
Catch ex As Exception
End Try</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	其實就我個人而言，我在程式中是很少使用Try Catch的，因為使用了Try Catch的話，在Debug時若程式當掉，Visual Studio會自動把程式跳到Catch的位置上(目前我電腦上連Catch都不會停，完全感覺不出例外發生)，而若無法從Catch參數的資訊抓到問題點的話。自己還需要再重新Debug一次，從Try的位置一步一步的追到問題點。</p>
<p>
	 </p>
<p>
	若不使用Try Catch的話，則當程式當掉時，Visual Studio會自動跳到出問題的程式那行，抓到問題的速度其實還比較快。</p>
<p>
	<img alt="image" border="0" height="281" src="\images\posts\7854\image_thumb.png" style="border-top-width: 0px; border-left-width: 0px; border-bottom-width: 0px; border-right-width: 0px" width="741" /></p>
<p>
	 </p>
<p>
	對於例外處理的使用時機，通常我是會看說這段程式是否可能會有例外發生，該例外的彈出是否是合理的。若例外的彈出合理且該例外的彈出需要秀出對應的訊息告知使用者，此時我就會使用Try Catch。會這樣做是因為我覺得例外有兩種，一種是給User看的例外、一種是給開發員看的例外。</p>
<p>
	 </p>
<p>
	給開發員看的例外主要是告知開發人員程式的寫法有誤，這類的例外本來就不該在執行階段發生，而是應該在開發時處理掉。那麼可能有人會問要是忘了處理乾淨呢？沒關係，例外發生時程式會彈出預設的例外視窗，讓程式員可以很快的把這錯誤給修正掉。</p>
<p>
	<img alt="image" border="0" height="333" src="\images\posts\7854\image_thumb_3.png" style="border-top-width: 0px; border-left-width: 0px; border-bottom-width: 0px; border-right-width: 0px" width="443" /></p>
<p>
	 </p>
<p>
	而給User看的例外則應該要能在執行階段依照例外給予不同的指示訊息，幫助使用者排除問題。這類型的例外我才會做例外處理。</p>
<p>
	<img alt="image" border="0" height="407" src="\images\posts\7854\image_thumb_5.png" style="border-top-width: 0px; border-left-width: 0px; border-bottom-width: 0px; border-right-width: 0px" width="662" /></p>
