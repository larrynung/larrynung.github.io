---
title: "[C#]如何取得Process的Owner"
date: "2013-11-06 12:00:00"
description: "[C#]如何取得Process的Owner"
tags: [CSharp]
---

<p>筆者最近在做的專案與自己在玩的東西都需要去取出Process的Owner來做些顯示或是判斷，這邊所謂的Owner就是工作管理員中我們所看到的User Name。</p>  <p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\8887e4bc-7255-4477-a9e6-317869f27561\image_thumb_1.png" width="644" height="436" /> </p>  <p> </p>  <p>這樣的資訊，我們無法透過BCL內建的System.Diagnostics.Process直接取得。而是需要透過WMI取出Win32_Process。</p>  <div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:a55d6839-caf7-4b77-a440-a0ffa88c3ab8" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">...
var query = "Select * From Win32_Process Where ProcessID = " + process.Id;
var searcher = new ManagementObjectSearcher(query);
var processObj = searcher.Get().OfType&lt;ManagementObject&gt;().FirstOrDefault();
...</pre></div>

<p> </p>

<p>取得Win32_Process後，對其呼叫GetOwner取得對應的Owner就可以了。</p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\8887e4bc-7255-4477-a9e6-317869f27561\image_thumb_2.png" width="644" height="300" /> </p>

<p> </p>

<p>像是下面這樣：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:553235cf-174b-44c3-96f8-65e2c18df091" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">...
var argList = new string[2];
int returnVal = Convert.ToInt32(processObj.InvokeMethod("GetOwner", argList));
if (returnVal == 0)
{
	var owner = string.Join(@"\", argList.Reverse().ToArray());
	...
}
...</pre></div>

<p> </p>

<p>這邊筆者將比較完整的處理整理成函式：</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:20668ccf-9ba1-4873-9cf3-5c07b0d9ad06" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">		public static string GetProcessOwner(Process process)
		{
			var query = "Select * From Win32_Process Where ProcessID = " + process.Id;
			var searcher = new ManagementObjectSearcher(query);
			var processObj = searcher.Get().OfType&lt;ManagementObject&gt;().FirstOrDefault();

			if (processObj == null)
				throw new ArgumentException("Process not exists!");

			var argList = new string[2];
			int returnVal = Convert.ToInt32(processObj.InvokeMethod("GetOwner", argList));
			if (returnVal == 0)
			{
				return string.Join(@"\", argList.Reverse().ToArray());
			}

			return null;
		}</pre></div>

<p> </p>

<p>使用時帶入Process就可以取得對應的Owner。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ffbd3156-cf1e-4593-bf1b-cc3081d383ba" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">		static void Main(string[] args)
		{
			Console.WriteLine(GetProcessOwner(Process.GetCurrentProcess()));
		}</pre></div>

<p> </p>

<p><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts\8887e4bc-7255-4477-a9e6-317869f27561\image_thumb.png" width="441" height="192" /> </p>

<p> </p>

<p>若要更方便點，也可以將其整理成擴充方法使用。</p>

<div id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:d105616e-4bc3-4346-937f-050d2d4c7fba" class="wlWriterSmartContent" style="float: none; padding-bottom: 0px; padding-top: 0px; padding-left: 0px; margin: 0px; display: inline; padding-right: 0px"><pre name="code" class="c#">public static class ProcessExtension
{
	public static string GetProcessOwner(this Process process)
	{
		var query = "Select * From Win32_Process Where ProcessID = " + process.Id;
		var searcher = new ManagementObjectSearcher(query);
		var processObj = searcher.Get().OfType&lt;ManagementObject&gt;().FirstOrDefault();

		if (processObj == null)
			throw new ArgumentException("Process not exists!");

		var argList = new string[2];
		int returnVal = Convert.ToInt32(processObj.InvokeMethod("GetOwner", argList));
		if (returnVal == 0)
		{
			return string.Join(@"\", argList.Reverse().ToArray());
		}

		return null;
	}
}</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>Win32_Process class (Windows)</li>
</ul>
