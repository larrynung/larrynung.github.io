---
title: "[C#]How to Detect Item Add, Insert, and Remove in a ListBox"
slug: "csharp-how-to-detect-item-add-insert-and-remove-in-a-listbox"
aliases: ["/posts/csharplistbox如何偵測item的新增插入與刪除/"]
date: "2013-11-06 12:00:00"
description: "有時候我們使用ListBox元件會想要針對Item的新增、插入、與刪除做些反應，可能像是有個Item插入時我們會想把游標移到最下面之類的。但內建的ListBox並未將這樣的訊息開放出來，所以我們無法直接的去做這樣的處理，必須要自行去接收視窗訊息才行。"
tags: [CSharp]
---

有時候我們使用ListBox元件會想要針對Item的新增、插入、與刪除做些反應，可能像是有個Item插入時我們會想把游標移到最下面之類的。但內建的ListBox並未將這樣的訊息開放出來，所以我們無法直接的去做這樣的處理，必須要自行去接收視窗訊息才行。

我們可以建立個控制項，繼承自ListBox，並視需要來接收想要處理的視窗訊息。像是想要偵測Item新增的話我們可以偵測LB_ADDSTRING、想要偵測Item插入的話可以偵測LB_INSERTSTRING、想要偵測Item刪除的話可以偵測LB_DELETESTRING。

```csharp
private const int LB_ADDSTRING = 0x180;
private const int LB_INSERTSTRING = 0x181;
private const int LB_DELETESTRING = 0x182;
```

偵測時需覆寫WndProc方法，並在方法內判斷Msg是否是我們所感興趣的訊息。有的訊息會內含較為詳細的資訊，像是Item的索引與值，若有需要可從wparam與lparam中擷取。

```csharp
protected override void WndProc(ref Message m)
{
	var itemIndex = 0;
	var itemValue = string.Empty;

	switch (m.Msg)
	{
		case LB_ADDSTRING:
			itemValue = Marshal.PtrToStringUni(m.LParam);
			OnItemAdded(EventArgs.Empty);
			break;
		case LB_INSERTSTRING:
			itemIndex = (int)m.WParam;
			itemValue = Marshal.PtrToStringUni(m.LParam);
			OnItemInserted(EventArgs.Empty);
			break;
		case LB_DELETESTRING:
			itemIndex = (int)m.WParam;
			OnItemDeleted(EventArgs.Empty);
			break;
		default:
			break;
	}
	base.WndProc(ref m);
}
```

這邊附上較為完整的測試範例：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication4
{
	public partial class Form1 : Form
	{
		class ListBoxEx : ListBox
		{
			#region Const
			private const int LB_ADDSTRING = 0x180;
			private const int LB_INSERTSTRING = 0x181;
			private const int LB_DELETESTRING = 0x182;
			#endregion

			#region Event
			public event EventHandler ItemAdded;
			public event EventHandler ItemInserted;
			public event EventHandler ItemDeleted;
			#endregion

			#region Protected Method
			protected void OnItemAdded(EventArgs e)
			{
				if (ItemAdded == null)
					return;
				ItemAdded(this, e);
			}

			protected void OnItemInserted(EventArgs e)
			{
				if (ItemInserted == null)
					return;
				ItemInserted(this, e);
			}

			protected void OnItemDeleted(EventArgs e)
			{
				if (ItemDeleted == null)
					return;
				ItemDeleted(this, e);
			}

			protected override void WndProc(ref Message m)
			{
				var itemIndex = 0;
				var itemValue = string.Empty;

				switch (m.Msg)
				{
					case LB_ADDSTRING:
						itemValue = Marshal.PtrToStringUni(m.LParam);
						OnItemAdded(EventArgs.Empty);
						break;
					case LB_INSERTSTRING:
						itemIndex = (int)m.WParam;
						itemValue = Marshal.PtrToStringUni(m.LParam);
						OnItemInserted(EventArgs.Empty);
						break;
					case LB_DELETESTRING:
						itemIndex = (int)m.WParam;
						OnItemDeleted(EventArgs.Empty);
						break;
					default:
						break;
				}
				base.WndProc(ref m);
			}
			#endregion
		}

		#region Var
		private ListBoxEx _listBox;
		#endregion

		#region Private Property
		private ListBoxEx m_ListBox
		{
			get
			{
				return _listBox ?? (_listBox = new ListBoxEx()
				{
					Dock = DockStyle.Fill
				});
			}
		}
		#endregion

		#region Constructor
		public Form1()
		{
			InitializeComponent();

			m_ListBox.ItemAdded += m_ListBox_ItemAdded;
			m_ListBox.ItemDeleted += m_ListBox_ItemDeleted;
			m_ListBox.ItemInserted += m_ListBox_ItemInserted;

			this.panel1.Controls.Add(m_ListBox);
		}
		#endregion

		#region Event Process
		private void button1_Click(object sender, EventArgs e)
		{
			m_ListBox.Items.Add(Guid.NewGuid().ToString());
		}

		private void button2_Click(object sender, EventArgs e)
		{
			var index = m_ListBox.SelectedIndex >= 0 ? m_ListBox.SelectedIndex : 0;
			m_ListBox.Items.Insert(index, Guid.NewGuid().ToString());
		}

		private void button3_Click(object sender, EventArgs e)
		{
			if (m_ListBox.SelectedIndex == -1)
				return;
			m_ListBox.Items.RemoveAt(m_ListBox.SelectedIndex);
		}

		void m_ListBox_ItemInserted(object sender, EventArgs e)
		{
			lbxLog.Items.Add("Item inserted");
		}

		void m_ListBox_ItemDeleted(object sender, EventArgs e)
		{
			lbxLog.Items.Add("Item deleted");
		}

		void m_ListBox_ItemAdded(object sender, EventArgs e)
		{
			lbxLog.Items.Add("Item added");
		}
		#endregion
	}
}
```

運行後的結果如下，新增、插入、與刪除都能夠即時的偵測。

![image_thumb.png](/images/posts/d519bf98-9092-4f48-99da-a49329ae6e5e/image_thumb.png)

## Link

* How to detect if items are added to a ListBox (or CheckedListBox) control
* LB_ADDSTRING message (Windows)
* LB_DELETESTRING message (Windows)
* LB_INSERTSTRING message (Windows)
