---
title: "[C#]The Thread That Raises Process.Exited Is Affected by the Process.SynchronizingObject Property"
slug: "csharp-the-thread-that-raises-process-exited-is-affected-by-the-process-synchronizingobject-property"
aliases: ["/posts/csharpprocess.exited事件觸發的執行緒會受process.synchronizingobject屬性設定的影響/"]
date: "2013-11-06 12:00:00"
description: "最近在用Process時才發現自己對於Process類別實在不是很熟，本來以為在主執行緒將Process叫起來後關閉，Process.Exited事件會被導回主執行緒去觸發，後來才發現並不是那麼一回事，這邊以一個簡單的範例來看： 程式啟動時會順帶開啟計算機程式，並秀出主執行緒ID。"
tags: [CSharp]
---

最近在用Process時才發現自己對於Process類別實在不是很熟，本來以為在主執行緒將Process叫起來後關閉，Process.Exited事件會被導回主執行緒去觸發，後來才發現並不是那麼一回事，這邊以一個簡單的範例來看：

```csharp
using System;
using System.Diagnostics;
using System.Threading;
using System.Windows.Forms;

namespace WindowsFormsApplication13
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void Form1_Load(object sender, EventArgs e)
		{
			var process = Process.Start("calc.exe");
			process.EnableRaisingEvents = true;
			process.Exited += new EventHandler(process_Exited);
			textBox1.Text = "Main Thread ID:" + Thread.CurrentThread.ManagedThreadId.ToString();
			Console.Read();
		}

		void process_Exited(object sender, EventArgs e)
		{
			MessageBox.Show("Process Thread ID:" + Thread.CurrentThread.ManagedThreadId.ToString());
		}
	}
}
```

程式啟動時會順帶開啟計算機程式，並秀出主執行緒ID。

![image_thumb_2.png](/images/posts/960b6dbe-fdb8-4c05-ac13-265716515704/image_thumb_2.png)

關閉計算機程式時會顯示出所在的執行緒ID，從下圖可以看出執行緒ID並不一樣，Process.Exited被帶到另外個執行緒了。

![image_thumb_3.png](/images/posts/960b6dbe-fdb8-4c05-ac13-265716515704/image_thumb_3.png)

後來詢問網友才發現原來Process.Exited事件觸發的執行緒會受Process.SynchronizingObject屬性設定的影響，這在MSDN中的Process.Exited 事件也有稍稍提到。

![image_thumb_5.png](/images/posts/960b6dbe-fdb8-4c05-ac13-265716515704/image_thumb_5.png)

MSDN把這個細節寫在Process.SynchronizingObject 屬性那邊。

![image_thumb_6.png](/images/posts/960b6dbe-fdb8-4c05-ac13-265716515704/image_thumb_6.png)

裡面也有提到說如果是透過工具列將Process元件加入使用的話，Visual Studio會幫你自動設定SynchornizingObject屬性。

![image_thumb_7.png](/images/posts/960b6dbe-fdb8-4c05-ac13-265716515704/image_thumb_7.png)

這邊試著加入SynchornizingObject屬性設定後再跑一次。

```csharp
using System;
using System.Diagnostics;
using System.Threading;
using System.Windows.Forms;

namespace WindowsFormsApplication13
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void Form1_Load(object sender, EventArgs e)
		{
			var process = Process.Start("calc.exe");
			process.EnableRaisingEvents = true;
			process.Exited += new EventHandler(process_Exited);
			process.SynchronizingObject = this;
			textBox1.Text = "Main Thread ID:" + Thread.CurrentThread.ManagedThreadId.ToString();
			Console.Read();
		}

		void process_Exited(object sender, EventArgs e)
		{
			MessageBox.Show("Process Thread ID:" + Thread.CurrentThread.ManagedThreadId.ToString());
		}
	}
}
```

Process.Exited觸發的動作就會被帶回到主執行緒。

![image_thumb_4.png](/images/posts/960b6dbe-fdb8-4c05-ac13-265716515704/image_thumb_4.png)

這邊筆者還是有點Confuse，基本上Process離開時多半人預想都是回到主執行緒，而多半在使用時也都是帶入表單讓它帶回主執行緒，甚至透過工具列使用Process元件也是自動設定讓它帶回主執行緒，那做這樣的設計實在有些奇怪，也許是因為實作上有些限制而採取這樣的設計吧。

## Link

* Process.SynchronizingObject 屬性
* Process.Exited 事件
