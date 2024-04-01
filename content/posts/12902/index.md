---
title: "[Performance][C#]絕對值的取得"
date: "2010-01-07 10:50:16"
description: "[Performance][C#]絕對值的取得"
tags: [CSharp,Performance]
---

<p>絕對值的取得大概有兩種方法，一種是利用.NET Framework內建的Math.Abs函式；一種則是自行判斷是否為負，若為負則把它變正。稍微比較了一下兩者的速度差異，記錄如下。</p>  <p> </p>  <p>測試介面    <br /><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\12902\image_thumb_1.png" width="253" height="204" /> </p>  <p> </p>  <p>測試程式碼    <br /></p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9c67f7f1-bf11-4681-856f-7691a1ad9cea" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">using System;
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
            return value &lt; 0 ? -value : value;
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
            for (int idx = 0; idx &lt; count; ++idx)
                ABS1(value);
            sw.Stop();
            textBox1.AppendText("ABS1: " + sw.ElapsedMilliseconds + Environment.NewLine);
            sw.Reset();
            sw.Start();
            for (int idx = 0; idx &lt; count; ++idx)
                ABS2(value);
            sw.Stop();
            textBox1.AppendText("ABS2: " + sw.ElapsedMilliseconds + Environment.NewLine);
            textBox1.AppendText(new string('=', 10) + Environment.NewLine);
        } 
    }
}
</pre></div>

<p />

<p> </p>

<p>測試結果</p>

<table border="1" cellspacing="0" cellpadding="2" width="400"><tbody>
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

<p> </p>

<p>實驗數據圖 
  <br /><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\12902\image_thumb_2.png" width="487" height="295" /> </p>

<p> </p>

<p>本來還十分不解為何會有這樣的情形，經網友提醒才注意到原來是因為少判斷了臨界值所導致。</p>

<p>再簡單的試驗一下，若使用checked來檢查，仍會稍微快一點。 
  <br /></p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:cbd7ab44-b1d3-46cf-a330-87b0a8bca832" class="wlWriterEditableSmartContent"><pre name="code" class="c#:nocontrols">using System;
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
            for (int idx = 0; idx &lt; count; ++idx) 
               absValue= ABS1(value); 
            sw.Stop(); 
            Console.WriteLine(sw.ElapsedMilliseconds); 
            sw.Reset(); 
            sw.Start(); 
            for (int idx = 0; idx &lt; count; ++idx)
                absValue=ABS2(value); 
            sw.Stop(); 
            Console.WriteLine(sw.ElapsedMilliseconds);             

        } 

        static int ABS1(int value)
        {
            checked
            {
                return value &lt; 0 ? -value : value;
            }            
        } 
        static int ABS2(int value) 
        { 
            return Math.Abs(value); 
        } 

    }
}
</pre></div>

<p />

<p> </p>

<p>運行1000000000次的結果如下：</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\12902\image_thumb.png" width="409" height="191" /> </p>

<p> </p>

<p>而若是自行用if判斷臨界值，經我測試是會變得比較慢。</p>

<p> </p>

<p>經過測試，我們可以發現當不判斷臨界值時提升的效能會較為明顯，可在不會有臨界值問題的狀況下使用。像是[C#]RNGCryptoServiceProvider亂數產生器這篇下面所提的保哥的範例，使用了4個Byte來產生亂數並轉換成整數。這種情況下就不會有臨界值問題，可考慮自行撰寫程式以省略臨界值判斷。</p>
