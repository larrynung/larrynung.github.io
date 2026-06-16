---
title: "[C#]如何使用TraceListener實作類似Visual Studio的輸出視窗"
slug: "csharp-如何使用tracelistener實作類似visual-studio的輸出視窗"
aliases: ["/posts/csharp如何使用tracelistener實作類似visual-studio的輸出視窗/"]
date: "2013-11-06 12:00:00"
description: "前陣子花了點時間在為開發中的產品加強除錯的功能，想要讓開發上發生的問題能直接在產品上就一目而然的看到，而不用另行開啟DebugView或是Log來看。簡單地說想要為產品加上類似是Visual Studio的輸出視窗，或者是DebugView類似的功能，"
tags: [CSharp]
---

前陣子花了點時間在為開發中的產品加強除錯的功能，想要讓開發上發生的問題能直接在產品上就一目而然的看到，而不用另行開啟DebugView或是Log來看。簡單地說想要為產品加上類似是Visual Studio的輸出視窗，或者是DebugView類似的功能，能夠很即時的偵測並顯示出系統發出的Debug或是Trace訊息。為了達到這個需求，筆者用內建的TraceListener簡單的試做了一下，這篇隨手紀錄一下。

要達到類似DebugView的效果，代表著我們必須要能擷取到Debug.WriteLine或是Trace.WriteLine的訊息，為此我們必須要建立一個TraceListener，繼承自DefaultTraceListener，並覆寫它的WriteLine方法。在覆寫的WriteLine方法中我們可以將收到的訊息做些處理，像是把它顯示到ListBox之類的。

```csharp
public class ListBoxLogTraceListener : DefaultTraceListener
{
	private ListBox m_ListBox { get; set; }

	/// <summary>
	/// Initializes a new instance of the <see cref="ListBoxLogTraceListener"/> class.
	/// </summary>
	/// <param name="listBox">The list box.</param>
	public ListBoxLogTraceListener(ListBox listBox)
	{
		m_ListBox = listBox;
	}

	/// <summary>
	/// Writes the output to the OutputDebugString function and to the <see cref="M:System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String)"/> method, followed by a carriage return and line feed (\r\n).
	/// </summary>
	/// <param name="message">The message to write to OutputDebugString and <see cref="M:System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String)"/>.</param>
	/// <PermissionSet>
	/// 	<IPermission class="System.Security.Permissions.FileIOPermission, mscorlib, Version=2.0.3600.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" version="1" Unrestricted="true"/>
	/// 	<IPermission class="System.Security.Permissions.SecurityPermission, mscorlib, Version=2.0.3600.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" version="1" Flags="ControlEvidence"/>
	/// </PermissionSet>
	public override void WriteLine(string message)
	{
		if (!m_ListBox.Visible)
			return;

		if (m_ListBox.InvokeRequired)
		{
			m_ListBox.BeginInvoke(new MethodInvoker(
				   delegate { WriteLine(message); }
				   ));
			return;
		}

		m_ListBox.Items.Add(string.Format("{0}\t{1}", DateTime.Now, message));
	}
}
```

TraceListener類別撰寫完畢，可以透過Debug.Listeners.Add或是Trace.Listeners.Add將撰寫的TraceListener類別加入，當我們程式中有用到Debug.WriteLine或是Trace.WriteLine時就會連帶觸發我們撰寫的TraceListener，藉此滿足我們想要達到的效果。

```csharp
...
//Debug.Listeners.Add(new ListBoxLogTraceListener(listBox1));
Trace.Listeners.Add(new ListBoxLogTraceListener(listBox1));
...
Debug.WriteLine("Debug msg...");
...
Trace.WriteLine("Trace msg...");
...
```

這邊附上較為完整的測試範例：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication6
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
			//Debug.Listeners.Add(new ListBoxLogTraceListener(listBox1));
			Trace.Listeners.Add(new ListBoxLogTraceListener(listBox1));
		}

		private void button1_Click(object sender, EventArgs e)
		{
			Debug.WriteLine("Debug msg...");
		}

		private void button2_Click(object sender, EventArgs e)
		{
			Trace.WriteLine("Trace msg...");
		}
	}

	public class ListBoxLogTraceListener : DefaultTraceListener
	{
		private ListBox m_ListBox { get; set; }

		/// <summary>
		/// Initializes a new instance of the <see cref="ListBoxLogTraceListener"/> class.
		/// </summary>
		/// <param name="listBox">The list box.</param>
		public ListBoxLogTraceListener(ListBox listBox)
		{
			m_ListBox = listBox;
		}

		/// <summary>
		/// Writes the output to the OutputDebugString function and to the <see cref="M:System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String)"/> method, followed by a carriage return and line feed (\r\n).
		/// </summary>
		/// <param name="message">The message to write to OutputDebugString and <see cref="M:System.Diagnostics.Debugger.Log(System.Int32,System.String,System.String)"/>.</param>
		/// <PermissionSet>
		/// 	<IPermission class="System.Security.Permissions.FileIOPermission, mscorlib, Version=2.0.3600.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" version="1" Unrestricted="true"/>
		/// 	<IPermission class="System.Security.Permissions.SecurityPermission, mscorlib, Version=2.0.3600.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" version="1" Flags="ControlEvidence"/>
		/// </PermissionSet>
		public override void WriteLine(string message)
		{
			if (!m_ListBox.Visible)
				return;

			if (m_ListBox.InvokeRequired)
			{
				m_ListBox.BeginInvoke(new MethodInvoker(
					   delegate { WriteLine(message); }
					   ));
				return;
			}

			m_ListBox.Items.Add(string.Format("{0}\t{1}", DateTime.Now, message));
		}
	}
}
```

運行起來我們可以看到它能偵測並顯示系統發出的Debug或是Trace訊息，在產品的除錯上會方便許多。

![image_thumb.png](/images/posts/58014e43-9fa3-45fc-a5b0-defa3e5fb3e7/image_thumb.png)
