---
title: "[C#]如何取得Process的Owner"
slug: "[CSharp]如何取得Process的Owner"
date: "2013-11-06 12:00:00"
description: "筆者最近在做的專案與自己在玩的東西都需要去取出Process的Owner來做些顯示或是判斷，這邊所謂的Owner就是工作管理員中我們所看到的User Name。 這樣的資訊，我們無法透過BCL內建的System.Diagnostics.Process直接取得。"
tags: [CSharp]
---

筆者最近在做的專案與自己在玩的東西都需要去取出Process的Owner來做些顯示或是判斷，這邊所謂的Owner就是工作管理員中我們所看到的User Name。

![image_thumb_1.png](/images/posts/8887e4bc-7255-4477-a9e6-317869f27561/image_thumb_1.png)

這樣的資訊，我們無法透過BCL內建的System.Diagnostics.Process直接取得。而是需要透過WMI取出Win32_Process。

```csharp
...
var query = "Select * From Win32_Process Where ProcessID = " + process.Id;
var searcher = new ManagementObjectSearcher(query);
var processObj = searcher.Get().OfType<ManagementObject>().FirstOrDefault();
...
```

取得Win32_Process後，對其呼叫GetOwner取得對應的Owner就可以了。

![image_thumb_2.png](/images/posts/8887e4bc-7255-4477-a9e6-317869f27561/image_thumb_2.png)

像是下面這樣：

```csharp
...
var argList = new string[2];
int returnVal = Convert.ToInt32(processObj.InvokeMethod("GetOwner", argList));
if (returnVal == 0)
{
	var owner = string.Join(@"\", argList.Reverse().ToArray());
	...
}
...
```

這邊筆者將比較完整的處理整理成函式：

```csharp
public static string GetProcessOwner(Process process)
{
	var query = "Select * From Win32_Process Where ProcessID = " + process.Id;
	var searcher = new ManagementObjectSearcher(query);
	var processObj = searcher.Get().OfType<ManagementObject>().FirstOrDefault();

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
```

使用時帶入Process就可以取得對應的Owner。

```csharp
static void Main(string[] args)
{
	Console.WriteLine(GetProcessOwner(Process.GetCurrentProcess()));
}
```

![image_thumb.png](/images/posts/8887e4bc-7255-4477-a9e6-317869f27561/image_thumb.png)

若要更方便點，也可以將其整理成擴充方法使用。

```csharp
public static class ProcessExtension
{
	public static string GetProcessOwner(this Process process)
	{
		var query = "Select * From Win32_Process Where ProcessID = " + process.Id;
		var searcher = new ManagementObjectSearcher(query);
		var processObj = searcher.Get().OfType<ManagementObject>().FirstOrDefault();

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
}
```

## Link

* Win32_Process class (Windows)
