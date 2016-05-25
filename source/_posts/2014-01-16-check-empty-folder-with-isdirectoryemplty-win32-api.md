---
layout: post
title: "Check empty folder with IsDirectoryEmplty Win32 API"
date: 2014-01-16 23:08:00
comments: true
categories: [CSharp, Win32 API]
keywords: "Win32,API,IsDirectoryEmplty,.NET,C#"
description: "Check empty folder with IsDirectoryEmplty Win32 API"
---

在判斷目錄是否為空這邊，.NET 4.0 以前，很多人都會很直覺的去使用 Directory.GetFiles 、Directory.GetDirectories 、或 Directory.GetFileSystemEntries 方法，用個數判斷是否為空。  

<!-- More -->

{% codeblock lang:c# %}
public bool IsDirectoryEmplty(string directory)
{
	//return !Directory.GetFiles(directory).Any() && !Directory.GetDirectories(directory).Any();
	return !Directory.GetFileSystemEntries(directory).Any();
}
{% endcodeblock %}

<br/>

用這樣的方式處理，必須等待所有檔案都找出來後回傳才能進行空目錄的判斷，效能十分的低落。  

在 .NET 4.0 後可改用 Directory.EnumerateFiles 、Directory.EnumerateDirectories 、或 Directory.EnumerateFileSystemEntries 替代。  

{% codeblock lang:c# %}
public bool IsDirectoryEmplty(string directory)
{
        //return !Directory.EnumerateFiles(directory).Any() && !Directory.EnumerateDirectories(directory).Any();
        return !Directory.EnumerateFileSystemEntries(directory).Any();
}
{% endcodeblock %}

<br/>

相較於 .NET 4.0 以前的處理方式，檔案變成找到就立刻回傳，因此我們找到一個檔案就可以將搜尋的動作中斷，效能問題獲得了改善。  
雖然效能的問題解決了，不過像這樣的處理方式會受限於 .NET Framework 的版本，不是一個比較通用的解法。而且空目錄判斷這樣的動作其實跟前面提到的取得目錄大小一樣，用 Win32 API 去跟 OS 問多半是最快的方式。  

以這邊來說，我們可以將之改用 IsDirectoryEmplty API 去處理。

{% codeblock lang:c# %}
[ DllImport("Shlwapi.dll" , EntryPoint = "PathIsDirectoryEmpty")]
[ return: MarshalAs (UnmanagedType.Bool)]
public static extern bool IsDirectoryEmplty([MarshalAs (UnmanagedType.LPStr)] string directory);
{% endcodeblock %}

<br/>

使用起來會像下面這樣：

{% codeblock lang:c# %}
using System.Text;
using System.Threading.Tasks;


namespace ConsoleApplication23
{
    class Program
    {
        [ DllImport("Shlwapi.dll" , EntryPoint = "PathIsDirectoryEmpty")]
        [ return: MarshalAs (UnmanagedType.Bool)]
        public static extern bool IsDirectoryEmplty([MarshalAs (UnmanagedType.LPStr)] string directory);


        static void Main(string[] args)
        {
            var sw = Stopwatch .StartNew();
            Console.WriteLine(IsDirectoryEmplty(@"C:\Program Files (x86)"));
            Console.WriteLine(sw.ElapsedMilliseconds);
        }
    }   
}
{% endcodeblock %}

<br/>

可以看到這邊判斷 Program Files 目錄也只要 1 ms 。   

{% img /images/posts/IsDirectoryEmplty/1.png %}
