---
title: "[C#]偵測系統Power狀態的改變以及是否進入Sleep mode"
slug: "[CSharp]偵測系統Power狀態的改變以及是否進入Sleep mode"
date: "2013-11-06 12:00:00"
description: "[C#]偵測系統Power狀態的改變以及是否進入Sleep mode"
tags: [CSharp]
---

筆者之前在[C#]使用GetSystemPowerStatus API查看目前電源使用狀態與[[C#][VB.NET]使用SystemInformation.PowerStatus查看目前電源使用狀態](http://www.dotblogs.com.tw/larrynung/archive/2009/09/29/10817.aspx)這兩篇文章中介紹過了如何偵測電源使用狀態，當時年紀小是用Timer定時去Pooling更新狀態，這樣作法是不好的，應該避免使用Pooling，改用系統主動通知的方式下去更新。

要讓系統主動通知電源狀態變更，我們可以很簡單的繫結SystemEvents.PowerModeChanged事件，透過事件處理常式回傳的參數我們可以很容易的判斷出是目前系統是發生了怎樣的電源狀態改變。電源狀態的對應值可參閱[PowerModes 列舉型別](http://msdn.microsoft.com/zh-tw/library/microsoft.win32.powermodes.aspx)。

![image3_thumb.png](/images/posts/02d6b98e-748c-442a-8f77-2d468419a3de/image3_thumb.png)

這邊來看個簡單的範例：

```csharp
using System;
using System.Windows.Forms;
using Microsoft.Win32;

namespace WindowsFormsApplication15
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void Form1_Load(object sender, EventArgs e)
		{
			SystemEvents.PowerModeChanged += new PowerModeChangedEventHandler(SystemEvents_PowerModeChanged);
		}

		void SystemEvents_PowerModeChanged(object sender, PowerModeChangedEventArgs e)
		{
			textBox1.Text += e.Mode.ToString() + Environment.NewLine;
		}
	}
}
```

這邊將程式運行起來，拔掉筆電的電源線再插上，系統會告知我們目前為StatusChange狀態，表示從充電狀態與電池模式之間的切換。若是將電腦切換至睡眠模式，系統會告知我們目前為Suspend狀態。再將電腦從睡眠模式中喚醒，則會收到Resume的狀態變更。

![image_thumb.png](/images/posts/02d6b98e-748c-442a-8f77-2d468419a3de/image_thumb.png)

除了透過.NET BCL內建的SystemEvents外，我們也可以直接攔截系統發送的訊息。當電源狀態改變時，作業系統會發送WM_POWERBROADCAST (0x218)給所有的程式，我們可以直接攔截該訊息，找出wParam所代表的狀態改變為何就可以了。(wParam的定義可參閱WM_POWERBROADCAST message文章中的對照表)

![image6_thumb.png](/images/posts/02d6b98e-748c-442a-8f77-2d468419a3de/image6_thumb.png)

![image9_thumb.png](/images/posts/02d6b98e-748c-442a-8f77-2d468419a3de/image9_thumb.png)

這邊一樣附上個簡單的使用範例：

```csharp
using System;
using System.Windows.Forms;

namespace WindowsFormsApplication15
{
	public partial class Form1 : Form
	{
		private const int WM_POWERBROADCAST = 0x218;
		private const int PBT_APMSUSPEND = 0x4;
		private const int PBT_APMRESUMESUSPEND = 0x7;
		private const int PBT_APMRESUMEAUTOMATIC = 0x12;
		public Form1()
		{
			InitializeComponent();
		}

		protected override void WndProc(ref Message m)
		{
			if(m.Msg == WM_POWERBROADCAST)
			{
				switch ((int)m.WParam)
				{
					case PBT_APMSUSPEND:
						textBox1.Text += "PBT_APMSUSPEND" + Environment.NewLine;
						break;
					case PBT_APMRESUMEAUTOMATIC:
						textBox1.Text += "PBT_APMRESUMEAUTOMATIC" + Environment.NewLine;
						break;
					case PBT_APMRESUMESUSPEND:
						textBox1.Text += "PBT_APMRESUMESUSPEND" + Environment.NewLine;
						break;
				}
			}
			base.WndProc(ref m);
		}
	}
}
```

![image12_thumb.png](/images/posts/02d6b98e-748c-442a-8f77-2d468419a3de/image12_thumb.png)

## Link

* SystemEvents 類別
* SystemEvents.PowerModeChanged 事件
* PowerModeChangedEventArgs 類別
* PowerModes 列舉型別
* WM_POWERBROADCAST message
