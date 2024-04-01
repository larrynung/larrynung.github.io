---
title: "Use WebAuthenticationBroker to do single sign on (SSO) connections"
date: "2013-11-06 12:00:00"
description: "Use WebAuthenticationBroker to do single sign on (SSO) connections"
---

<p>
	在串接社群服務時，通常都需要去做OAuth認證，以前這樣的動作都必需要我們開發人員自己去串接處理，像是筆者[C#]OAuth認證開發這篇就使用OAuthBase與內建的瀏覽器元件自己去做OAuth認證。而在Windows Store apps中，內建WebAuthenticationBroker能幫我們簡化部分的處理。</p>
<p>
	 </p>
<p>
	以OAuth驗證來說，在取得Request Token兜出授權網址後，我們可以呼叫WebAuthenticationBroker.AuthenticateAsync方法，帶入WebAuthenticationOptions、授權網址、與Callback網址。</p>
<script src="\images\posts\15eda79b-7cfb-4581-87c7-0c01cb3de9f4\5453283.js"></script>
<p>
	 </p>
<p>
	運行後Windows Store apps就會出現像下面這樣制式的頁面。</p>
<p>
	 <img alt="image" border="0" height="397" src="\images\posts\15eda79b-7cfb-4581-87c7-0c01cb3de9f4\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	當我們在授權頁面完成登入與授權的動作，這邊會跳離頁面並回傳WebAuthenticationResult。我們可以由回傳的WebAuthenticationResult.ResponseStatus去取得授權的狀態，依照不同的狀態做不同的處理。若是授權成功，可以接著用WebAuthenticationResult.ResponseData取得回傳的資料，並從回傳的資料中取得後續呼叫API會需要用到的AccessToken。</p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		WebAuthenticationBroker class</li>
	<li>
		Metro Style App: 使用 WebAuthenticationBroker 做 Facebook 帳號驗證</li>
	<li>
		WinRT：WebAuthenticationBroker For OAuth認證</li>
	<li>
		Web authentication broker sample</li>
	<li>
		How web authentication broker works (Windows Store apps)</li>
</ul>
