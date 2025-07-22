---
title: "[C#]如何取得Process的Owner"
slug: "[CSharp]如何取得Process的Owner"
date: "2013-11-06 12:00:00"
description: "[C#]如何取得Process的Owner"
tags: [CSharp]
---筆者最近在做的專案與自己在玩的東西都需要去取出Process的Owner來做些顯示或是判斷，這邊所謂的Owner就是工作管理員中我們所看到的User Name。

這樣的資訊，我們無法透過BCL內建的System.Diagnostics.Process直接取得。而是需要透過WMI取出Win32_Process。
...
var query = "Select * From Win32_Process Where ProcessGetOwner", argList));
if (returnVal == 0)
{
var owner = string.Join(@"\", argList.Reverse().ToArray());
...
}
...

這邊筆者將比較完整的處理整理成函式：

public static string GetProcessOwner(Process process)
{
var query = "Select * From Win32_Process Where ProcessProcess not exists!");

var argList = new string[2];
int returnVal = Convert.ToInt32(processObj.InvokeMethod("GetOwner", argList));
if (returnVal == 0)
{
return string.Join(@"\", argList.Reverse().ToArray());
}

return null;
}

使用時帶入Process就可以取得對應的Owner。

static void Main(string[] args)
{
Console.WriteLine(GetProcessOwner(Process.GetCurrentProcess()));
}

若要更方便點，也可以將其整理成擴充方法使用。

public static class ProcessExtension
{
public static string GetProcessOwner(this Process process)
{
var query = "Select * From Win32_Process Where ProcessProcess not exists!");

var argList = new string[2];
int returnVal = Convert.ToInt32(processObj.InvokeMethod("GetOwner", argList));
if (returnVal == 0)
{
return string.Join(@"\", argList.Reverse().ToArray());
}

return null;
}
}

## Link

Win32_Process class (Windows)