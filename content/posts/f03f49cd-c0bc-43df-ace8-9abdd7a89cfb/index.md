---
title: "[C#]使用FindFirstFile、FindNextFile API實做EnumerateFiles"
slug: "[CSharp]使用FindFirstFile、FindNextFile API實做EnumerateFiles"
date: "2013-11-06 12:00:00"
description: "[C#]使用FindFirstFile、FindNextFile API實做EnumerateFiles"
tags: [CSharp]
---

<p>.NET 4.0開始Directory類別新增了EnumerateFiles函式，該函式能提供較有效率的方式找尋檔案，不會等到整個搜尋動作完成才回傳。在.NET 4.0以前我們則可以用FindFirstFile、FindNextFile這幾個API來達到類似的效果。</p>  <p> </p>  <p>實做起來就像下面這樣，有需要的自行取用：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:cd2cbbeb-7d05-4934-9db3-914ccaefcdd8" class="wlWriterSmartContent"><pre name="code" class="c#">		private static readonly IntPtr INVALID_HANDLE_VALUE = new IntPtr(-1); 

		[DllImport("kernel32.dll", CharSet = System.Runtime.InteropServices.CharSet.Auto, SetLastError = true)]
		private static extern IntPtr FindFirstFile(string pFileName, ref  WIN32_FIND_DATA pFindFileData);

		[DllImport("kernel32.dll", CharSet = System.Runtime.InteropServices.CharSet.Auto, SetLastError = true)]
		private static extern bool FindNextFile(IntPtr hndFindFile, ref  WIN32_FIND_DATA lpFindFileData);  

		[DllImport( "kernel32.dll" , SetLastError =  true )]  
		private  static  extern  bool  FindClose(IntPtr hndFindFile);     

		[Serializable, StructLayout(LayoutKind.Sequential, CharSet = CharSet.Auto), BestFitMapping(false)]
		internal struct WIN32_FIND_DATA
		{
			public FileAttributes dwFileAttributes;
			public uint ftCreationTime_dwLowDateTime;
			public uint ftCreationTime_dwHighDateTime;
			public uint ftLastAccessTime_dwLowDateTime;
			public uint ftLastAccessTime_dwHighDateTime;
			public uint ftLastWriteTime_dwLowDateTime;
			public uint ftLastWriteTime_dwHighDateTime;
			public uint nFileSizeHigh;
			public uint nFileSizeLow;
			public int dwReserved0;
			public int dwReserved1;
			[MarshalAs(UnmanagedType.ByValTStr, SizeConst = 260)]
			public string cFileName;
			[MarshalAs(UnmanagedType.ByValTStr, SizeConst = 14)]
			public string cAlternateFileName;
		}

		public IEnumerable&lt;string&gt; EnumerateFiles(string path, string searchPattern = "*.*", SearchOption searchOption = SearchOption.AllDirectories)
		{
			IntPtr hFind = INVALID_HANDLE_VALUE;
			WIN32_FIND_DATA FindFileData = default(WIN32_FIND_DATA);

			hFind = FindFirstFile(Path.Combine(path, searchPattern), ref  FindFileData);
			if (hFind != INVALID_HANDLE_VALUE)
			{
				do
				{
					if (FindFileData.cFileName.Equals(@".") || FindFileData.cFileName.Equals(@".."))
						continue;

					if (searchOption == SearchOption.AllDirectories &amp;&amp; ((FindFileData.dwFileAttributes &amp; FileAttributes.Directory) == FileAttributes.Directory))
					{
						foreach (var file in EnumerateFiles(Path.Combine(path, FindFileData.cFileName)))
							yield return file;
					}
					else
					{
						yield return Path.Combine(path, FindFileData.cFileName);
					}
				}
				while (FindNextFile(hFind, ref  FindFileData));
			}
			FindClose(hFind);
		}</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>c#調用api(FindFirstFile,FindNextFile)高效遍歷目錄文件 </li>

  <li>In C#, Use Win32 API to Enumerate File and Directory Quickly </li>
</ul>
