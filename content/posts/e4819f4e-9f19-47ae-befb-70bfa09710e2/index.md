---
title: "How to customize .NET 4.0's System.Runtime.Caching.ChangeMonitor"
date: "2013-11-06 12:00:00"
description: "How to customize .NET 4.0's System.Runtime.Caching.ChangeMonitor"
tags: [CSharp]
---

筆者很久以前寫過一篇.NET 4.0 New Feature - System.Runtime.Caching，稍稍的簡單介紹了一下.NET 4.0新加入的快取框架。基本上的操作只要參閱那篇應該都不成問題，但是該快取框架內建只提供HostFileChangeMonitor與SqlChangeMonitor兩個ChangeMonitor的實作，我們要快取的資料不可能永遠在磁碟與SQL DB這兩個快取介質內，有時候我們可能會要自己串些Restful API抓取資料並做快取，或是是要套些比較複雜的檢查規則，這時我們就必須善用該快取框架易於擴充的特點，客制自己的ChangeMonitor。

要客制自己的ChangeMonitor不難，大概只有五個流程步驟：

依序是：

Create a class that Inherited ChangeMonitor

Implement UniqueId property and Dispose method

Init in constructor

Invoke InitializationComplete method after init

Invoke OnChanged method when content must update

簡單的說就是要建立一個類別繼承至ChangeMonitor，並覆寫它的Uniqueid屬性與Dispose方法，接著在建構子這邊做些初始的動作，初始完呼叫InitializationComplete方法告知初始動作完成，最後在偵測到資料變動時呼叫OnChanged方法就可以了。

這邊可參閱MSDN ChangeMonitor Class 這篇的Notes to Inheritors這段，裡面有提到很多實作的眉眉角角需要注意。

實際的來看個例子加深印象，筆者在這邊簡單的實做了一個ClipboardChangeMonitor，期望Cache的內容能在剪貼簿資料發生變動時失效。

using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Caching;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CustomChangeMonitorDemo
{
public class ClipboardChangeMonitor : ChangeMonitor
{
#region Var
private string _clipboardText;
private Timer _timer;
private string _uniqueID; 
#endregion

#region Private Property
private string m_ClipboardText
{
get { return _clipboardText ?? string.Empty; }
set 
{
if (_clipboardText == value)
return;

_clipboardText = value;
OnChanged(value);
}
}

private System.Windows.Forms.Timer m_Timer 
{
get
{
return _timer ?? (_timer = new System.Windows.Forms.Timer());
}
} 
#endregion

#region Public Property
public override string UniqueId
{
            get { return _uniqueID ?? (_uniqueID = Guid.NewGuid().ToString()); }
} 
#endregion

#region Constructor
public ClipboardChangeMonitor()
{
m_Timer.Interval = 1000;
m_Timer.Tick += m_Timer_Tick;
m_Timer.Start();

_clipboardText = Clipboard.GetText();

InitializationComplete();
}
#endregion

#region Protected Method
protected override void Dispose(bool disposing)
{
} 
#endregion

#region Event Process
void m_Timer_Tick(object sender, EventArgs e)
{
m_ClipboardText = Clipboard.GetText();
}  
#endregion
}
}

整個實作非常的簡單，只是在建構子這邊擷取剪貼簿的內容與設定Timer，然後叫用InitializationComplete，後面就只是定時的去看剪貼簿是否有所更動。Uniqueid屬性這邊筆者也只是簡單的傳回一個識別用的GUID，而Dispose方法因為該類別沒什麼非託管的資源，這邊就姑且讓它是空的。

這邊寫個簡單的Console程式測試一下：

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.Caching;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CustomChangeMonitorDemo
{
class Program
{
[STAThread]
static void Main(string[] args)
{
FileContentProvider textFile = new FileContentProvider();
Stopwatch sw = new Stopwatch();
while (true)
{
sw.Reset();
sw.Start();
Console.WriteLine(textFile.Content);
sw.Stop();
Console.WriteLine("Elapsed Time: {0} ms", sw.ElapsedMilliseconds);
Console.WriteLine(new string('=', 50));
Console.ReadLine();
Application.DoEvents();
}
}
}

public class FileContentProvider
{
public String Content
{
get
{
const string CACHE_KEY = "Content";
string content = m_Cache[CACHE_KEY] as string;
if (content == null)
{
CacheItemPolicy policy = new CacheItemPolicy();
//policy.SlidingExpiration = TimeSpan.FromMilliseconds(1500);

var changeMonitor = new ClipboardChangeMonitor();

policy.ChangeMonitors.Add(changeMonitor);

content = Guid.NewGuid().ToString();
Thread.Sleep(1000);
m_Cache.Set(CACHE_KEY, content, policy);
}
return content;
}
}

private ObjectCache _cache;
private ObjectCache m_Cache
{
get
{
if (_cache == null)
_cache = MemoryCache.Default;
return _cache;
}
}
}
}

運行起來會像下面這樣，不論怎麼按Enter更新，Cache的GUID都是一樣的。

但是一經選取複製。

ClipboardChangeMonitor就會偵測到剪貼簿有變動，Cache的資料就會過期進而更新，因此複製完後按下Enter更新，這邊會重新抓取新的Guid。

若有需要可至CustomChangeMonitorDemo下載完整的程式範例。

## Link


CustomChangeMonitorDemo