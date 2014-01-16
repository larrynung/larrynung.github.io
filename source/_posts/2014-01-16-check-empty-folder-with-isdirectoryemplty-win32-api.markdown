---
layout: post
title: "Check empty folder with IsDirectoryEmplty Win32 API"
date: 2014-01-16 23:08
comments: true
categories: [CSharp, Win32 API]
keywords: "Win32,API,IsDirectoryEmplty,.NET,C#"
description: "Check empty folder with IsDirectoryEmplty Win32 API"
---

在判斷目錄是否為空這邊，很多人都會很直覺的去使用 Directory.GetFiles 、Directory.GetDirectories 、或 Directory.GetFileSystemEntries 方法，用個數判斷是否為空。  

<!-- More -->

{% codeblock lang:c# %}
public bool IsDirectoryEmplty(string directory)
{
	//return !Directory.GetFiles(directory).Any() && !Directory.GetDirectories(directory).Any();
	return !Directory.GetFileSystemEntries(directory).Any();
}
{% endcodeblock %}

<br/>

在 .NET 4.0 後可能就會改用 Directory.EnumerateFiles 、Directory.EnumerateDirectories 、或 Directory.EnumerateFileSystemEntries 替代。  

{% codeblock lang:c# %}
public bool IsDirectoryEmplty(string directory)
{
        //return !Directory.EnumerateFiles(directory).Any() && !Directory.EnumerateDirectories(directory).Any();
        return !Directory.EnumerateFileSystemEntries(directory).Any();
}
{% endcodeblock %}

<br/>

不過這種處理其實跟前面提到的取得目錄大小一樣，用 Win32 API 去跟 OS 問多半是最快的方式。  

以這邊來說，我們就可以將之改用 IsDirectoryEmplty API 去處理。

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
