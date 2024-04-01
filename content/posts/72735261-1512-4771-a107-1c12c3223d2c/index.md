---
title: "[C#]如何偵測特定檔案是否為Lock狀態"
date: "2013-11-06 12:00:00"
description: "[C#]如何偵測特定檔案是否為Lock狀態"
tags: [CSharp]
---

<p>
	要怎樣才能有效的偵測出檔案是被Lock住，這樣的問題在程式開發時開發人員常常會碰到，筆者看到多半的解法都是試圖去開開看檔案，當檔案無法開啟時就視為檔案被Lock住。這樣的做法雖不算錯，但總是不太精確，因為很多情況都有可能造成開檔錯誤，不見得都能很單純的這樣做判斷。</p>
<p>
	 </p>
<p>
	比較正確的做法應該是嘗試開啟檔案，若開啟檔案時發生例外，將發生的IOException例外攔截後透過Mashal.GetHRForException方法取得HRESULT，然後將HRESULT再跟65535做and運算取得對應的error code，若是error code為32或33則表示檔案被Lock住，反之則否。</p>
<p>
	 </p>
<p>
	之所以要這樣判斷是因為HRESULT的格式定義是像下面這樣子，前面16個bit為error code，所以我們取得的HRESULT必須要跟65535去做and運算，這樣才能取出error code的部分。</p>
<p>
	<img alt="image" border="0" height="82" src="\images\posts\72735261-1512-4771-a107-1c12c3223d2c\image_thumb.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="644" /></p>
<p>
	 </p>
<p>
	而取出error code後之所以要判斷32與33這兩個值，則是因為它們分別是ERROR_SHARING_VIOLATION與ERROR_LOCK_VIOLATION這兩個錯誤碼，看一下MSDN的定義相信就不難理解。</p>
<p>
	<img alt="image" border="0" height="179" src="\images\posts\72735261-1512-4771-a107-1c12c3223d2c\image_thumb_1.png" style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" width="612" /></p>
<p>
	 </p>
<p>
	因此整個偵測檔案是否被Lock的程式碼撰寫起來就會像下面這樣：</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:94d83d12-c4a5-4fda-8b2b-c5cdedaecb5c" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px">
	<pre class="c#" name="code">
		public static bool IsFileLocked(string file)
		{
			try
			{
				using (File.Open(file, FileMode.Open, FileAccess.Write, FileShare.None))
				{
					return false;
				}
			}
			catch (IOException exception)
			{
				var errorCode = Marshal.GetHRForException(exception) &amp; 65535;
				return errorCode == 32 || errorCode == 33;
			}
			catch (Exception)
			{
				return false;
			}
		}</pre>
</div>
<p>
	 </p>
<h2>
	Link</h2>
<ul>
	<li>
		System Error Codes (0-499) (Windows)</li>
	<li>
		C++零食：HRESULT 與Windows Error Codes 不是一回事</li>
	<li>
		How to check For File Lock in C#?</li>
	<li>
		2.1 HRESULT</li>
</ul>
