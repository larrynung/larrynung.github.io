---
title: "[C#]使用ShowCaret amp; HideCaret控制元件上的插入符號"
slug: "[CSharp]使用ShowCaret amp; HideCaret控制元件上的插入符號"
date: "2013-11-06 12:00:00"
description: "[C#]使用ShowCaret &amp; HideCaret控制元件上的插入符號"
tags: [CSharp]
---

<p>有時候我們會有需要能精確的控制元件是否顯示插入符號，這時可以使用ShowCaret與HideCaret兩個Win32 API來達成這個目的，這兩個API的宣告方式如下：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:13ec442e-30c4-4569-a7fd-3936a18eab64" class="wlWriterSmartContent"><pre name="code" class="c#">		[DllImport("user32.dll")]
		static extern bool ShowCaret(IntPtr hWnd);

		[DllImport("user32.dll")]
		static extern bool HideCaret(IntPtr hWnd);</pre></div>

<p> </p>

<p>使用上只要帶入元件的handle就可以了，像是想要控制TextBox的插入符號，可以像下面這樣撰寫：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:29493a42-b4c7-40b2-98c4-4a0e2408d0f5" class="wlWriterSmartContent"><pre name="code" class="c#">...
ShowCaret(textBox1.Handle);
...
HideCaret(textBox1.Handle);
...</pre></div>

<p> </p>

<p>最後這邊附上比較完整的使用範例：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:83f1e1f6-5cab-4d13-b442-6a6504153227" class="wlWriterSmartContent"><pre name="code" class="c#">using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace WindowsFormsApplication22
{
	public partial class Form1 : Form
	{
		[DllImport("user32.dll")]
		static extern bool ShowCaret(IntPtr hWnd);

		[DllImport("user32.dll")]
		static extern bool HideCaret(IntPtr hWnd);

		public Form1()
		{
			InitializeComponent();
		}

		private void timer1_Tick(object sender, EventArgs e)
		{
			if (rbtnShowCaret.Checked)
			{
				ShowCaret(textBox1.Handle);
			}
			else
			{
				HideCaret(textBox1.Handle);
			}
		}
	}
}</pre></div>

<p> </p>

<p>運行的畫面像下面這樣，可以分別選取Show caret與Hide caret兩個選項，並在上方的TextBox點選，讓TextBox取得焦點，仔細觀察插入符號在這兩種狀況下的運行狀況，應該可以發現在選取Hide caret時插入符號一下就會消失，而在選取Show caret時就跟一般的使用無異。</p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts92cdeb-069f-4f5b-a9cc-3fad64e5bba8\image_thumb.png" width="304" height="117" /> </p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>HideCaret function</li>

  <li>ShowCaret function</li>
</ul>
