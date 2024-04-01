---
title: "GAE's Users Service"
date: "2013-11-06 12:00:00"
description: "GAE's Users Service"
---

<p>
	開發GAE application時可能會有整合Google帳號的需求，這時我們可以使用Users Service。</p>
<p>
	 </p>
<p>
	首先將google.appengine.api.users import進來。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:efa9f881-9b08-4a46-90a4-7c46e0a11e25" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
from google.appengine.api import users</pre>
</div>
<p>
	 </p>
<p>
	呼叫users.get_current_user()取得當前的使用者。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:00bb8bbf-1afb-4da6-b4a1-3697c7ae131e" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
user = users.get_current_user()</pre>
</div>
<p>
	 </p>
<p>
	若是有取到當前的使用者，代表目前使用者已是登入的狀態，我們可以取得使用者資訊做些呈現 (可參閱User 類別這篇)。</p>
<p>
	 </p>
<p>
	像是呼叫nickname方法取得當前使用者的暱稱。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:026bc800-852c-42f1-bcac-2b2af1cc7e8e" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
nickName = user.nickname()</pre>
</div>
<p>
	 </p>
<p>
	呼叫email方法取得當前使用者的Email位置。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:07debd5e-fe50-469f-8a3d-180b1968758f" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
email = user.email()</pre>
</div>
<p>
	 </p>
<p>
	或者是呼叫user_id方法取得當前使用者的識別ID。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:59495033-bb13-418c-95ed-aa755cada879" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
userID = user.user_id()</pre>
</div>
<p>
	 </p>
<p>
	若需要實現登出的動作，則我們可以呼叫create_logout_url方法取得登出動作的網址，。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:56d5b7d0-15e4-4947-99da-c0038cf37a6b" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
users.create_logout_url("/")</pre>
</div>
<p>
	 </p>
<p>
	而要是使用者尚未登入，這邊我們無法取得當前的使用者，這時可以透過users.create_login_url方法取得登入的頁面位置，呼叫users.create_login_url的同時可以指定登入成功所要返回的頁面位置。</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:59beaf6a-f31b-4df5-9105-b52fa1558321" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
users.create_login_url(self.request.uri)</pre>
</div>
<p>
	 </p>
<p>
	登入的頁面位置取得後，視需求可以做些不同的處理，像是讓使用者透過點擊連結去做登入，或是直接將頁面直接導過去。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c0a3c5fc-a265-47b6-bd83-c5d95f7829b6" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
self.redirect(users.create_login_url(self.request.uri))</pre>
</div>
<p>
	 </p>
<p>
	總結下來整個Users Service的撰寫應該會是像下面這樣的處理方式：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:afd8728a-205a-49fe-8eea-9990bbd48249" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="py" name="code">
    	user = users.get_current_user()

    	if user:
    		#User Logined
    	else:
		#User Need Login =&gt; Redirect to login page
    		self.redirect(users.create_login_url(self.request.uri))</pre>
</div>
<p>
	 </p>
<p>
	最後這邊實際來看個完整的範例程式：</p>
<p><script src="\images\posts\dd434fd1-e8bf-48d5-9df8-551c2f5cd471\6130083.js"></script>
	 </p>
<p>
	 </p>
<p>
	本地運行起來可以看到像下面這樣簡易的登入畫面，按下Login按鈕繼續。</p>
<p>
	<img alt="image" border="0" height="278" src="\images\posts\dd434fd1-e8bf-48d5-9df8-551c2f5cd471\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="424" /></p>
<p>
	 </p>
<p>
	會看到登入成功後的樣子，這邊的範例是將NickName與登出功能秀出來。</p>
<p>
	<img alt="image" border="0" height="147" src="\images\posts\dd434fd1-e8bf-48d5-9df8-551c2f5cd471\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="284" /></p>
<p>
	 </p>
<p>
	本地測試時帳號怎樣輸入都會成功登入，因為只是讓我們可以很容易的在本地進行測試，不會整合Google的帳號服務，也不會進行驗證的動作。但若是實際將其佈署到Cloud上，就會與Google帳號服務整合，所以可以看到登入的畫面會改成Google帳號的登入頁面。</p>
<p>
	<img alt="image" border="0" height="212" src="\images\posts\dd434fd1-e8bf-48d5-9df8-551c2f5cd471\image_thumb_3.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	登入後的動作一樣正常運作。</p>
<p>
	<img alt="image" border="0" height="156" src="\images\posts\dd434fd1-e8bf-48d5-9df8-551c2f5cd471\image_thumb_2.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="331" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		Using the Users Service</li>
</ul>
