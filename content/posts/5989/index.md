---
title: "[C#][VB.NET]自製桌面小玩意"
slug: "[CSharp][VB.NET]自製桌面小玩意"
date: "2008-11-15 01:28:44"
description: "[C#][VB.NET]自製桌面小玩意"
tags: [VB.NET, CSharp]
---

## Abstract
Introduction自製桌面小玩意Conclusion

## Introduction

本篇將由一個簡單的小範例，試範如何利用.NET自製類似widget的桌面小玩意。

## 自製桌面小玩意

Step1.首先，打開一個Window Form專案。

Step2.設定其表單的FormBorderStyle屬性值為None，你會發現設完後其表單的標題列與視窗本來的邊框都不見了。

Step3.在表單中放入PictureBox，用以顯示桌面小玩意的外觀圖片。

Step4.設定PictureBox的影象內容為桌面小玩意的外觀圖片。把調整大小模式設為AutoSize，並啟動停駐父容器。

Step5.將表單的AutoSize屬性設為True，並把AutoSizeMode設為GrowAndShrink。讓表單大小可以自動隨著圖片大小變化。

Step6.將表單的TransparencyKey設為Control，這樣可以去掉桌面小玩意外圍多餘的部份。以下圖為例，我們可以藉由設定該屬性去去掉彎彎旁邊的顏色。

Step7.把Form.ShowInTaskBar設為False。

Step8.在表單中放入ContextMenuStript，並予以設定其選單的選項。

Step9.把表單的ContextMenuStrip屬性設為上一步設好的ContextMenuStrip。

Step10.加入ContextMenuStrip選項按下時對應的程式碼

VB.NET

Private Sub ExitToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ExitToolStripMenuItem.Click
        Me.Close()
End Sub

C#

private void ExitToolStripMenuItem_Click(object sender, System.EventArgs e)
{
    this.Close();
}

Step11.加入托曳桌面小玩意的程式碼

VB.NET

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

C#

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
  
}  

Step12.完成

完整範例如下:

VB.NET

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

C#

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

## Conclusion

這篇以一個簡單的小範例試範了如何利用.NET自製類似widget的桌面小玩意。雖然是簡單的概念，但是卻十分的實用。像是桌曆、桌面量尺、電子寵物...等，都是可以利用此概念來寫出來的。全看自我的想像力。有興趣的可以試著擴充此範例，像是加上滑鼠移上去或按下時彎彎會換動作、或是讓彎彎在電腦上跑來跑去..等。