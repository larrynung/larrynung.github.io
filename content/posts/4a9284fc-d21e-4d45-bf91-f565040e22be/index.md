---
title: "[C#]使用Mutex實現單一程式執行個體的注意事項"
slug: "csharp-使用mutex實現單一程式執行個體的注意事項"
aliases: ["/posts/csharp使用mutex實現單一程式執行個體的注意事項/"]
date: "2013-11-06 12:00:00"
description: "相信大家都知道在.NET程式中若要實現單一程式執行個體，一般來說有幾種方法，像是去判斷是否已經有開啟的Process是相同的程式、用Mutex與Semaphore之類的技術來判斷是否程式正在開啟。"
tags: [CSharp]
---

相信大家都知道在.NET程式中若要實現單一程式執行個體，一般來說有幾種方法，像是去判斷是否已經有開啟的Process是相同的程式、用Mutex與Semaphore之類的技術來判斷是否程式正在開啟。但是很多網路上的文章都忽略了在用Mutex實現單一程式執行個體時，其實會有些必須要注意的地方，導致於在實際運用上沒有發揮到該有的效果。

以一個簡單的例子來看，一般我們在網路上常看到的使用方式大概就像下面的程式碼片段類似，建構Mutex時就會回傳該Mutex是否已經存在，利用該回傳值來決定程式應該繼續開啟還是關閉。

```c
using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using System.Threading;

namespace WindowsFormsApplication10
{
	static class Program
	{
		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main()
		{
			Application.EnableVisualStyles();
			Application.SetCompatibleTextRenderingDefault(false);

			Boolean bCreatedNew;

			//Create a new mutex using specific mutex name
			Mutex m = new Mutex(false, "myUniqueName", out bCreatedNew);

			if (bCreatedNew)
				Application.Run(new Form1());
		}
	}
}
```

這樣的程式到底有什麼樣的問題呢？有興趣的可以試著建置Release的程式看看，其實這樣的程式在某些情況下會在Release模式下失效，Debug的運作卻是正常的，若試不出來的可以再加上個GC.Collect試試，會更容易重現。

```csharp
...
Boolean bCreatedNew;

//Create a new mutex using specific mutex name
Mutex m = new Mutex(false, "myUniqueName", out bCreatedNew);

GC.Collect();

if (bCreatedNew)
	Application.Run(new Form1());
...
```

之所以會有這樣的問題，是因為Mutex在Release模式下被GC給回收了，而Debug模式下因為便於開發人員除錯，據說有將GC的周期給拉長，所以不容易重現。那這樣的問題要怎麼樣解決呢？這邊筆者有整理了幾種方法。

一個方法就是把Mutex給拉出來成為類別成員。

```csharp
...
static Mutex m;

/// <summary>
/// The main entry point for the application.
/// </summary>
[STAThread]
static void Main()
{
	Application.EnableVisualStyles();
	Application.SetCompatibleTextRenderingDefault(false);

	Boolean bCreatedNew;

	//Create a new mutex using specific mutex name
	m = new Mutex(false, "myUniqueName", out bCreatedNew);
	GC.Collect();

	if (bCreatedNew)
		Application.Run(new Form1());
}
...
```

另一個方法就是讓Mutex不要被GC回收掉，像是在程式最後明確呼叫Dispose，讓GC知道該Mutex仍在使用。

```csharp
...
Boolean bCreatedNew;

//Create a new mutex using specific mutex name
Mutex m = new Mutex(false, "myUniqueName", out bCreatedNew);

GC.Collect();

if (bCreatedNew)
	Application.Run(new Form1());

m.Dispose();
...
```

也可以用using或是try...finally之類的語法將Mutex給hold住。

```csharp
...
Boolean bCreatedNew;

//Create a new mutex using specific mutex name
using (Mutex m = new Mutex(false, "myUniqueName", out bCreatedNew))
{
	GC.Collect();

	if (bCreatedNew)
		Application.Run(new Form1());
}
...
```

或是把Mutex的用法寫的比較正規一點，加上WaitOne與ReleaseMutex去明確控制Mutex的作用範圍。

```csharp
...
Boolean bCreatedNew;

//Create a new mutex using specific mutex name
Mutex m = new Mutex(false, "myUniqueName", out bCreatedNew);

m.WaitOne();
GC.Collect();

if (bCreatedNew)
	Application.Run(new Form1());

m.ReleaseMutex();
...
```

## Link

* C#,利用Mutex實現應用程式的單實例運行
* [C#] 避免重複開啟應用程式
* [C#/VB.net] 一次只執行一個WinForm視窗程式
* 如何避免相同的 ConsoleApp 或 WinForm 同時間重複執行
* [C#.NET][VB.NET][VB6] 如何禁止程式重覆執行 / System.Threading.Mutex & Semaphore
* 单实例程序 互斥进程 Mutex Debug VS Release 运行不一样
* Mutex is different in debug model and release model?
* Mutex实现单实例，你真的搞懂了吗？来看看吧。
