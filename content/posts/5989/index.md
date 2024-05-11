---
title: "[C#][VB.NET]自製桌面小玩意"
slug: "[CSharp][VB.NET]自製桌面小玩意"
date: "2008-11-15 01:28:44"
description: "[C#][VB.NET]自製桌面小玩意"
tags: [VB.NET, CSharp]
---

<h2>Abstract</h2><ul><li>Introduction</li><li>自製桌面小玩意</li><li>Conclusion</li></ul><p> </p><h2>Introduction</h2><p>本篇將由一個簡單的小範例，試範如何利用.NET自製類似widget的桌面小玩意。</p><p> </p><h2>自製桌面小玩意</h2><p>Step1.首先，打開一個Window Form專案。</p><p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="644" height="448" src="\images\posts\5989\image_thumb.png" /></a></p><p> </p><p>Step2.設定其表單的FormBorderStyle屬性值為None，你會發現設完後其表單的標題列與視窗本來的邊框都不見了。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_4.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="644" height="448" src="\images\posts\5989\image_thumb_1.png" /></a></p><p> </p><p>Step3.在表單中放入PictureBox，用以顯示桌面小玩意的外觀圖片。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_8.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="644" height="446" src="\images\posts\5989\image_thumb_3.png" /></a></p><p> </p><p>Step4.設定PictureBox的影象內容為桌面小玩意的外觀圖片。把調整大小模式設為AutoSize，並啟動停駐父容器。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_16.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="644" height="446" src="\images\posts\5989\image_thumb_7.png" /></a> </p><p> </p><p>Step5.將表單的AutoSize屬性設為True，並把AutoSizeMode設為GrowAndShrink。讓表單大小可以自動隨著圖片大小變化。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_18.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="644" height="446" src="\images\posts\5989\image_thumb_8.png" /></a></p><p> </p><p>Step6.將表單的TransparencyKey設為Control，這樣可以去掉桌面小玩意外圍多餘的部份。以下圖為例，我們可以藉由設定該屬性去去掉彎彎旁邊的顏色。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_20.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="644" height="446" src="\images\posts\5989\image_thumb_9.png" /></a></p><p> </p><p>Step7.把Form.ShowInTaskBar設為False。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_26.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="644" height="446" src="\images\posts\5989\image_thumb_12.png" /></a></p><p> </p><p>Step8.在表單中放入ContextMenuStript，並予以設定其選單的選項。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_22.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="644" height="446" src="\images\posts\5989\image_thumb_10.png" /></a></p><p> </p><p> </p><p>Step9.把表單的ContextMenuStrip屬性設為上一步設好的ContextMenuStrip。</p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_24.png"><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" width="644" height="446" src="\images\posts\5989\image_thumb_11.png" /></p><p> </p><p>Step10.加入ContextMenuStrip選項按下時對應的程式碼</p><p>VB.NET</p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:38a2770f-9b00-40d5-b3c7-6b1b5dbbcda1" class="wlWriterSmartContent"><pre class="vb" name="code">
Private Sub ExitToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ExitToolStripMenuItem.Click
        Me.Close()
End Sub</pre></div><p>C#</p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:21a766c0-8ef5-41b4-ac0e-e8ecd082c1ea" class="wlWriterSmartContent"><pre class="c#" name="code">
private void ExitToolStripMenuItem_Click(object sender, System.EventArgs e)
{
    this.Close();
}
</pre></div><p> </p><p>Step11.加入托曳桌面小玩意的程式碼</p><p>VB.NET</p><p> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:932cdc26-f7fa-48fc-ad67-735adcb9a8f0" class="wlWriterSmartContent"><pre class="vb" name="code">
  Private Sub PictureBox1_MouseDown(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles PictureBox1.MouseDown
        '紀錄滑鼠點選時的視窗位置與滑鼠點選位置  
        nOldWndLeft = Me.Left
        nOldWndTop = Me.Top
        nClickX = e.X
        nClickY = e.Y
    End Sub

    Private Sub PictureBox1_MouseMove(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles PictureBox1.MouseMove
        If PictureBox1.Capture = True Then      '如果滑鼠按著拖曳  
            '設定新的視窗位置  
            Me.Top = e.Y + nOldWndTop - nClickY
            Me.Left = e.X + nOldWndLeft - nClickX
            '更新紀錄的視窗位置  
            nOldWndLeft = Me.Left
            nOldWndTop = Me.Top
        End If
    End Sub</pre></div><p> </p><p>C#</p><p> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f0c57834-e54e-4456-896a-5ebc58634d32" class="wlWriterSmartContent"><pre class="c#" name="code">
private void PictureBox1_MouseDown(object sender, MouseEventArgs e)  
{  
    //紀錄滑鼠點選時的視窗位置與滑鼠點選位置  
    nOldWndLeft = this.Left;  
    nOldWndTop = this.Top;  
    nClickX = e.X;  
    nClickY = e.Y;  
}  
  
private void PictureBox1_MouseMove(object sender, MouseEventArgs e)  
{  
    if (pnlTitleBar.Capture == true)        //如果滑鼠按著拖曳  
    {  
        //'設定新的視窗位置  
        this.Top = e.Y + nOldWndTop - nClickY;  
        this.Left = e.X + nOldWndLeft - nClickX;  
        //更新紀錄的視窗位置  
        nOldWndLeft = this.Left;  
        nOldWndTop = this.Top;  
    }  
  
}  </pre></div><p> </p><p> </p><p>Step12.完成</p><p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="244" height="64" src="\images\posts\5989\image_thumb_2.png" /></a></p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_28.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="200" height="71" src="\images\posts\5989\image_thumb_5.png" /></a></p><p><a href="http://files.dotblogs.com.tw/larrynung/0811/682dd121ff78_1181/image_14.png"><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="244" height="62" src="\images\posts\5989\image_thumb_4.png" /></p><p> </p><p>完整範例如下:</p><p>VB.NET</p><p> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ce2cd745-b780-4cea-a98c-dcbb95d9e48c" class="wlWriterSmartContent"><pre class="vb" name="code">
Public Class Form1
    Dim nOldWndLeft As Integer
    Dim nOldWndTop As Integer
    Dim nClickX As Integer
    Dim nClickY As Integer

    Private Sub ExitToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ExitToolStripMenuItem.Click
        Me.Close()
    End Sub


    Private Sub PictureBox1_MouseDown(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles PictureBox1.MouseDown
        '紀錄滑鼠點選時的視窗位置與滑鼠點選位置  
        nOldWndLeft = Me.Left
        nOldWndTop = Me.Top
        nClickX = e.X
        nClickY = e.Y
    End Sub

    Private Sub PictureBox1_MouseMove(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles PictureBox1.MouseMove
        If PictureBox1.Capture = True Then      '如果滑鼠按著拖曳  
            '設定新的視窗位置  
            Me.Top = e.Y + nOldWndTop - nClickY
            Me.Left = e.X + nOldWndLeft - nClickX
            '更新紀錄的視窗位置  
            nOldWndLeft = Me.Left
            nOldWndTop = Me.Top
        End If
    End Sub
End Class
</pre></div><p> </p><p>C#</p><p> </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:1bd8b462-bc62-4452-8c9e-21990bb81e88" class="wlWriterSmartContent"><pre class="c#" name="code">
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        int nOldWndLeft;
        int nOldWndTop;
        int nClickX;
        int nClickY;  
  
        public Form1()
        {
            InitializeComponent();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {          
            //紀錄滑鼠點選時的視窗位置與滑鼠點選位置  
            nOldWndLeft = this.Left;
            nOldWndTop = this.Top;
            nClickX = e.X;
            nClickY = e.Y;  

        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (pictureBox1.Capture == true)        //如果滑鼠按著拖曳  
            {
                //'設定新的視窗位置  
                this.Top = e.Y + nOldWndTop - nClickY;
                this.Left = e.X + nOldWndLeft - nClickX;
                //更新紀錄的視窗位置  
                nOldWndLeft = this.Left;
                nOldWndTop = this.Top;
            }  
        }
     
    }
}
</pre></div><p> </p><p> </p><h2>Conclusion</h2><p>這篇以一個簡單的小範例試範了如何利用.NET自製類似widget的桌面小玩意。雖然是簡單的概念，但是卻十分的實用。像是桌曆、桌面量尺、電子寵物...等，都是可以利用此概念來寫出來的。全看自我的想像力。有興趣的可以試著擴充此範例，像是加上滑鼠移上去或按下時彎彎會換動作、或是讓彎彎在電腦上跑來跑去..等。</p>
