---
title: "[C#]平行處理網路傳輸時因連線數不足發生連線Timeout的解決方案"
slug: "[CSharp]平行處理網路傳輸時因連線數不足發生連線Timeout的解決方案"
date: "2013-11-06 12:00:00"
description: "[C#]平行處理網路傳輸時因連線數不足發生連線Timeout的解決方案"
tags: [CSharp]
---

<p>
	最近專案程式發生了一個很奇妙的BUG，專案程式在某些情況下網路傳輸會發生Timeout的現象，而且一發生就是一連串的網路傳輸都連帶Timeout。這問題很難重現，程式看起來邏輯都對，在大部分的情況下都看不到這種現象，開發團隊的電腦也沒有一台發生。後來查了一下網路文章，大膽推測是因為連線數過多造成的，可能是某些狀況下程式會同時有多個網路傳輸的連線，導致超過可容納的連線數造成等待而Timeout。</p>
<p>
	 </p>
<p>
	MSDN中的ServicePointManager.DefaultConnectionLimit 屬性這篇有提到，ServicePointManager.DefaultConnectionLimit在一般的WinForm程式中預設是2，而在ASP.NET中預設是10，而ServicePointManager.DefaultConnectionLimit這個屬性值又是HttpWebRequet.ServicePoint.ConnectionLimit的預設值，也就是說在WinForm下同時只能服務兩個連線數，超過兩個以上的連線自然就會被卡住而最後導致Timeout。</p>
<p>
	 </p>
<p>
	因此解決方法不外乎就是設定ServicePoint.ConnectionLimit的值，或是直接修改ServicePointManager.DefaultConnectionLimit，從預設值開始下手調整。這邊筆者附上完整的測試程式。</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:0eda318e-aedf-4b7a-8959-1505fe5a6a14" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net;
using System.Threading;

namespace ConsoleApplication15
{
	class Program 
	{
		public static string url = "https://www.google.com/images/srpr/logo3w.png";
		private static List&lt;WaitHandle&gt; finished = new List&lt;WaitHandle&gt;();
		public static void Main()
		{
			ServicePointManager.DefaultConnectionLimit = 200;   
			finished.Clear();
			for (var idx = 0; idx &lt; 5; ++idx )
			{
				finished.Add(new ManualResetEvent(false));
				Download(idx, url);
			}
			WaitHandle.WaitAll(finished.ToArray());
			Console.WriteLine("Done...");   
		}    

		private static void Download(int idx, string url)
		{
			var wc = new WebClient();
			wc.OpenReadCompleted += wc_OpenReadCompleted;
			wc.OpenReadAsync(new Uri(url), idx);
		}

		private static void wc_OpenReadCompleted(object sender, OpenReadCompletedEventArgs e)
		{
			Console.WriteLine(string.Format("{0}: Download Completed", e.UserState));

			var idx = (int)e.UserState;
			var manualResetEvent = finished[idx] as ManualResetEvent;

			Debug.Assert(manualResetEvent != null, "manualResetEvent != null");
			manualResetEvent.Set();
		}     
	}
}
</pre>
</div>
<p>
	 </p>
<p>
	注意到裡面有一段ServicePointManager.DefaultConnectionLimit = 200;的程式，若是把它給Mark起來，我們可以發現運行起來程式會跑兩個網路傳輸就卡住了。</p>
<p>
	<img alt="image" border="0" height="239" src="\images\posts\4da8b526-fba1-4d3d-a3e6-6c80749981f5\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="505" /></p>
<p>
	 </p>
<p>
	若是將Mark拿掉，程式就可以把所有的網路傳輸正常的跑完。</p>
<p>
	<img alt="image" border="0" height="271" src="\images\posts\4da8b526-fba1-4d3d-a3e6-6c80749981f5\image_thumb_1.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="465" /></p>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		WebClient并发下载问题</li>
	<li>
		How can I programmatically remove the 2 connection limit in WebClient</li>
	<li>
		ServicePointManager.DefaultConnectionLimit 屬性</li>
</ul>
