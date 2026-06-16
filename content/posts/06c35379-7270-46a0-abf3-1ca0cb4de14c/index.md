---
title: "[C#][Extension Method]Get directory size"
slug: "csharp-extension-method-get-directory-size"
aliases: ["/posts/csharpextension-methodget-directory-size/"]
date: "2013-11-06 12:00:00"
description: "使用.NET程式要取得指定目錄的大小，沒辦法像取得檔案大小一樣的簡單，沒有現成的屬性可以取用，必須要遶點路去達到這樣的功能。像是MSDN中的Directory 類別這篇，裡面範例有一道叫做DirSize的Function就是在做這件事情。"
tags: [CSharp]
---

使用.NET程式要取得指定目錄的大小，沒辦法像取得檔案大小一樣的簡單，沒有現成的屬性可以取用，必須要遶點路去達到這樣的功能。像是MSDN中的Directory 類別這篇，裡面範例有一道叫做DirSize的Function就是在做這件事情。

```csharp
public static long DirSize(DirectoryInfo d)
{
    long Size = 0;
    // Add file sizes.
    FileInfo[] fis = d.GetFiles();
    foreach (FileInfo fi in fis)
    {
        Size += fi.Length;
    }
    // Add subdirectory sizes.
    DirectoryInfo[] dis = d.GetDirectories();
    foreach (DirectoryInfo di in dis)
    {
        Size += DirSize(di);
    }
    return(Size);
}
```

可以看到這道Function就只是利用遞回去將目錄裡面所有的檔案大小加起來，除了醜了點外，並沒有什麼特別難的處理。這邊也可以不需要利用遞迴，改用Directory.GetFiles搭配Linq去取得目錄大小，效果是一樣的。

```csharp
static long GetDirSize(string path)
{
	return (from item in Directory.GetFiles(path, "*.*", SearchOption.AllDirectories)
				select new FileInfo(item).Length).Sum();
}
```

除了去計算目錄內的檔案總大小外，我們也可以直接取得目錄的大小。使用前需先將Microsoft  Scripting  Runtime Com組件加入參考。

![image6_thumb.png](/images/posts/06c35379-7270-46a0-abf3-1ca0cb4de14c/image6_thumb.png)

建立出Sctipting.FileSystemObjectClass物件後，呼叫GetFolder成員方法並帶入指定的目錄，該函式會回傳回Folder物件，透過Folder.Size就可以取得目錄的大小。

```csharp
static long GetFolderSize(string folder)
{
	return long.Parse((new Scripting.FileSystemObjectClass()).GetFolder(folder).Size.ToString());
}
```

這邊強力榔頭大有在如何取得資料夾容量大小這篇討論中提供用反射來做的方法，可以不用將參考加入就直接使用。

```csharp
static long GetFolderSize(string folder)
{
	Type tp = Type.GetTypeFromProgID("Scripting.FileSystemObject");
	object fso = Activator.CreateInstance(tp);
	object fd = tp.InvokeMember("GetFolder", BindingFlags.InvokeMethod, null, fso, new object[] { folder });
	long ret = Convert.ToInt64(tp.InvokeMember("Size", BindingFlags.GetProperty, null, fd, null));
	Marshal.ReleaseComObject(fso);
	return ret;
}
```

在.NET取得目錄大小的方法主要大概就是這幾種，以筆者來說，以簡單乾淨來說筆者是喜歡Linq加總的寫法，但是加總的做法總是感覺比較慢，直覺能直接透過系統去讀取目錄大小是最快，但又不想加入額外的參考，對於用反射來做又有點又臭又長，到底哪種方法比較好呢?這邊筆者做了一個簡單的測試，測試的程式如下：

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Diagnostics;

namespace ConsoleApplication8
{
	class Program
	{
		static void Main(string[] args)
		{
			GetFolderSize(@"C:\Program Files");
			GetDirSize(@"C:\Program Files");
			DirSize(new DirectoryInfo(@"C:\Program Files"));

			var sw = Stopwatch.StartNew();
			Console.WriteLine(GetFolderSize(@"C:\Program Files"));
			Console.WriteLine(sw.ElapsedMilliseconds);

			sw.Stop();
			sw.Reset();
			sw.Start();

			Console.WriteLine(GetDirSize(@"C:\Program Files"));
			Console.WriteLine(sw.ElapsedMilliseconds);

			sw.Stop();
			sw.Reset();
			sw.Start();

			Console.WriteLine(DirSize(new DirectoryInfo(@"C:\Program Files")));
			Console.WriteLine(sw.ElapsedMilliseconds);
		}

		static long GetDirSize(string path)
		{
			return (from item in Directory.GetFiles(path, "*.*", SearchOption.AllDirectories)
					select new FileInfo(item).Length).Sum();
		}

		static long GetFolderSize(string folder) // 取得資料夾大小
		{
			return long.Parse((new Scripting.FileSystemObjectClass()).GetFolder(folder).Size.ToString());
		}

		public static long DirSize(DirectoryInfo d)
		{
			long Size = 0;
			// Add file sizes.
			FileInfo[] fis = d.GetFiles();
			foreach (FileInfo fi in fis)
			{
				Size += fi.Length;
			}
			// Add subdirectory sizes.
			DirectoryInfo[] dis = d.GetDirectories();
			foreach (DirectoryInfo di in dis)
			{
				Size += DirSize(di);
			}
			return (Size);
		}
	}
}
```

經過測試很顯然的直接加總的方法是比較慢的，而且慢了好幾倍。

![image_thumb_4.png](/images/posts/06c35379-7270-46a0-abf3-1ca0cb4de14c/image_thumb_4.png)

既然測試結果指出直接去跟系統要是最快的方法，所以還是必須去面對上面又臭又長的反射，好在.NET 3.5以後有擴充方法可以用，索性就把它包成DirectoryInfo的擴充方法吧。

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Reflection;
using System.Runtime.InteropServices;

public static class DirectoryInfoExtension
{
	public static long GetSize(this DirectoryInfo dirInfo)
	{
		Type tp = Type.GetTypeFromProgID("Scripting.FileSystemObject");
		object fso = Activator.CreateInstance(tp);
		object fd = tp.InvokeMember("GetFolder", BindingFlags.InvokeMethod, null, fso, new object[] { dirInfo.FullName });
		long ret = Convert.ToInt64(tp.InvokeMember("Size", BindingFlags.GetProperty, null, fd, null));
		Marshal.ReleaseComObject(fso);
		return ret;
	}
}
```

## Link

* C# Get Directory Size
* Directory 類別
* 如何取得資料夾容量大小
* 在c#中直接取得目錄大小的方法
