---
title: "[C#]Decode Unicode Character"
slug: "[CSharp]Decode Unicode Character"
date: "2013-11-06 12:00:00"
description: "[C#]Decode Unicode Character"
tags: [CSharp]
---

<p>
	最近偷閒玩些自己的東西，碰到要解析的資料有像是\u0026這樣的Unicode Character，必須要將之解碼才會變成我們想要的資料。這時候就卡在怎樣做解碼的動作，本來在研究的程式牠是直接將\u0026用"&amp;"取代，這真是髒到我用不下手，所以順手下去研究了一下，找到How to decode “\u0026” in a URL?這篇還不錯的範例。簡單的來說，解碼的動作就是要先取得Unicode Character的後四碼，然後將其從16進位轉換為10進位，再將其數值轉回字元就可以了。像是下面這樣：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:d1e70d1c-6d19-4897-8e9d-09cf7fbaf40a" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
		private string GetValueFromUnicodeCharacter(string unicodeCharacter)
		{
			var match = Regex.Match(unicodeCharacter, @"\u(?&lt;code&gt;\d{4})");

			if (!match.Success)
				return string.Empty;

			var code = match.Groups["code"].Value;
			int value = Convert.ToInt32(code, 16);
			return ((char)value).ToString();
		}</pre>
</div>
<p>
	 </p>
<p>
	也可以用Regex.Replace將裡面所有的Unicode Character都替換。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:15073eee-dbf1-40dd-941f-d2c3d99611f1" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
		private string DecodeUnicodeCharacter(string unicodeCharacter)
		{
			MatchEvaluator matchAction = (match) =&gt;
				{
					var code = match.Groups["code"].Value;
					int value = Convert.ToInt32(code, 16);
					return ((char)value).ToString();
				};
			return Regex.Replace(unicodeCharacter, @"\u(?&lt;code&gt;\d{4})", matchAction);
		}</pre>
</div>
<p>
	 </p>
<p>
	為什麼會這樣轉換也可以參閱ASCII表，搭配上面的程式與說明應該不難理解為什麼可以這樣處理。</p>
<p>
	<img alt="image" border="0" height="226" src="\images\posts