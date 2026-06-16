---
title: "[Performance][C#]Getting the Absolute Value"
slug: "performance-csharp-getting-the-absolute-value"
aliases: ["/posts/12902/"]
date: "2010-01-07 10:50:16"
description: "絕對值的取得大概有兩種方法，一種是利用.NET Framework內建的Math.Abs函式；一種則是自行判斷是否為負，若為負則把它變正。稍微比較了一下兩者的速度差異，記錄如下。"
tags: [CSharp,Performance]
---

絕對值的取得大概有兩種方法，一種是利用.NET Framework內建的Math.Abs函式；一種則是自行判斷是否為負，若為負則把它變正。稍微比較了一下兩者的速度差異，記錄如下。

測試介面
![image_thumb_1.png](/images/posts/12902/image_thumb_1.png)

測試程式碼

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace WindowsFormsApplication35
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        static int ABS1(int value)
        {
            return value < 0 ? -value : value;
        }
        static int ABS2(int value)
        {
            return Math.Abs(value);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int count = (int)numericUpDown1.Value;
            int value = -1;
            textBox1.AppendText("Count: " + count.ToString() + Environment.NewLine);
            Stopwatch sw = Stopwatch.StartNew();
            for (int idx = 0; idx < count; ++idx)
                ABS1(value);
            sw.Stop();
            textBox1.AppendText("ABS1: " + sw.ElapsedMilliseconds + Environment.NewLine);
            sw.Reset();
            sw.Start();
            for (int idx = 0; idx < count; ++idx)
                ABS2(value);
            sw.Stop();
            textBox1.AppendText("ABS2: " + sw.ElapsedMilliseconds + Environment.NewLine);
            textBox1.AppendText(new string('=', 10) + Environment.NewLine);
        }
    }
}
```

測試結果

<table border="1" cellpadding="2" cellspacing="0" width="400"><tbody>
<tr>
<td valign="top" width="133">Count</td>
<td valign="top" width="133">ABS1</td>
<td valign="top" width="133">ABS2</td>
</tr>
<tr>
<td valign="top" width="133">10000</td>
<td valign="top" width="133">0</td>
<td valign="top" width="133">1</td>
</tr>
<tr>
<td valign="top" width="133">100000</td>
<td valign="top" width="133">2</td>
<td valign="top" width="133">2</td>
</tr>
<tr>
<td valign="top" width="133">1000000</td>
<td valign="top" width="133">22</td>
<td valign="top" width="133">29</td>
</tr>
<tr>
<td valign="top" width="133">10000000</td>
<td valign="top" width="133">221</td>
<td valign="top" width="133">296</td>
</tr>
<tr>
<td valign="top" width="133">100000000</td>
<td valign="top" width="133">1820</td>
<td valign="top" width="133">2155</td>
</tr>
</tbody></table>

實驗數據圖

![image_thumb_2.png](/images/posts/12902/image_thumb_2.png)

本來還十分不解為何會有這樣的情形，經網友提醒才注意到原來是因為少判斷了臨界值所導致。

再簡單的試驗一下，若使用checked來檢查，仍會稍微快一點。

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;

namespace ConsoleApplication31
{
    class Program
    {

        static void Main(string[] args)
        {
            int count = 1000000000;
            int value = -123;// -2147483648;
            int absValue;
            Stopwatch sw = Stopwatch.StartNew();
            for (int idx = 0; idx < count; ++idx)
               absValue= ABS1(value);
            sw.Stop();
            Console.WriteLine(sw.ElapsedMilliseconds);
            sw.Reset();
            sw.Start();
            for (int idx = 0; idx < count; ++idx)
                absValue=ABS2(value);
            sw.Stop();
            Console.WriteLine(sw.ElapsedMilliseconds);

        }

        static int ABS1(int value)
        {
            checked
            {
                return value < 0 ? -value : value;
            }
        }
        static int ABS2(int value)
        {
            return Math.Abs(value);
        }

    }
}
```

運行1000000000次的結果如下：

![image_thumb.png](/images/posts/12902/image_thumb.png)

而若是自行用if判斷臨界值，經我測試是會變得比較慢。

經過測試，我們可以發現當不判斷臨界值時提升的效能會較為明顯，可在不會有臨界值問題的狀況下使用。像是[C#]RNGCryptoServiceProvider亂數產生器這篇下面所提的保哥的範例，使用了4個Byte來產生亂數並轉換成整數。這種情況下就不會有臨界值問題，可考慮自行撰寫程式以省略臨界值判斷。
