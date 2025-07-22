---
title: "[C#][VB.NET]自定義.NET WindowForm表單介面"
slug: "[CSharp][VB.NET]自定義.NET WindowForm表單介面"
date: "2008-11-11 11:09:17"
description: "[C#][VB.NET]自定義.NET WindowForm表單介面"
tags: [CSharp,VB.NET]
---

## Abstract
Introduction自定義WindowForm表單介面Conclusion

## Introduction

本篇將由一個簡單的小範例，試範如何實現自定義的WindowForm表單介面。

## 自定義WindowForm表單介面

Step1.首先，打開一個Window Form專案。

Step2.設定其表單的FormBorderStyle屬性值為None，你會發現設完後其表單的標題列與視窗本來的邊框都不見了。

Step3.設定表單的BackgroundImage屬性，將其屬性值設定為自定義的介面圖片。設定完後表單會變成自定義的介面，記得要把表單的大小調整的跟圖片一樣。這邊若自定義的介面是非矩形的介面，則須利用Form.TransparencyKey屬性把介面多餘的部份變為透明。

Step4.為了後面方便做到自定表單標題列的拖曳動作。我們在表單中加入一個Panel控制項，並使其Dock在最上面，且剛好覆蓋標題列。

Step5.將剛放入的Panel的BackColor設為Transparent，設定完後Panel將會變成透明的，使用者無法用肉眼察覺此Panel的存在。

Step6.針對標題列上Panel的MouseDown事件與MouseMove事件加入處理表單拖曳的程式碼，實現自定表單標題列的拖曳機制。

VB.NET

    Private Sub pnlTitleBar_MouseDown(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles pnlTitleBar.MouseDown
       '紀錄滑鼠點選時的視窗位置與滑鼠點選位置
        nOldWndLeft = Me.Left
        nOldWndTop = Me.Top
        nClickX = e.X
        nClickY = e.Y
    End Sub

    Private Sub pnlTitleBar_MouseMove(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles pnlTitleBar.MouseMove
        If pnlTitleBar.Capture = True Then		'如果滑鼠按著拖曳
            '設定新的視窗位置
            Me.Top = e.Y + nOldWndTop - nClickY
            Me.Left = e.X + nOldWndLeft - nClickX
           '更新紀錄的視窗位置
            nOldWndLeft = Me.Left
            nOldWndTop = Me.Top
        End If
    End Sub

C#

        private void pnlTitleBar_MouseDown(object sender, MouseEventArgs e)
        {
            //紀錄滑鼠點選時的視窗位置與滑鼠點選位置
            nOldWndLeft = this.Left;
            nOldWndTop = this.Top;
            nClickX = e.X;
            nClickY = e.Y;
        }

        private void pnlTitleBar_MouseMove(object sender, MouseEventArgs e)
        {
            if (pnlTitleBar.Capture == true)		//如果滑鼠按著拖曳
            {
                //'設定新的視窗位置
                this.Top = e.Y + nOldWndTop - nClickY;
                this.Left = e.X + nOldWndLeft - nClickX;
                //更新紀錄的視窗位置
                nOldWndLeft = this.Left;
                nOldWndTop = this.Top;
            }

        }

Step7.在標題列放入兩個PictureBox，並將其外觀設定的跟標題列的按鈕一樣。

Step8.加入實作標題列按鈕的程式碼。

VB.NET

    Private Sub pbxMinBtn_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles pbxMinBtn.Click
        Me.WindowState = FormWindowState.Minimized		'標題列縮小按鈕被按下=>縮小視窗
    End Sub

    Private Sub pbxCloseBtn_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles pbxCloseBtn.Click
        Me.Close()		'標題列關閉按鈕被按下=>關閉視窗
    End Sub

C#

        private void pbxMinBtn_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;		//標題列縮小按鈕被按下=>縮小視窗
        }

        private void pbxCloseBtn_Click(object sender, EventArgs e)
        {
            this.Close();		//標題列關閉按鈕被按下=>關閉視窗
        }

Step9.完成

完整範例如下:

VB.NET

Public Class Form1

    Dim nOldWndLeft As Integer
    Dim nOldWndTop As Integer
    Dim nClickX As Integer
    Dim nClickY As Integer

    Private Sub pbxMinBtn_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles pbxMinBtn.Click
        Me.WindowState = FormWindowState.Minimized		'標題列縮小按鈕被按下=>縮小視窗
    End Sub

    Private Sub pbxCloseBtn_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles pbxCloseBtn.Click
        Me.Close()		'標題列關閉按鈕被按下=>關閉視窗
    End Sub

    Private Sub pnlTitleBar_MouseDown(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles pnlTitleBar.MouseDown
       '紀錄滑鼠點選時的視窗位置與滑鼠點選位置
        nOldWndLeft = Me.Left
        nOldWndTop = Me.Top
        nClickX = e.X
        nClickY = e.Y
    End Sub

    Private Sub pnlTitleBar_MouseMove(ByVal sender As System.Object, ByVal e As System.Windows.Forms.MouseEventArgs) Handles pnlTitleBar.MouseMove
        If pnlTitleBar.Capture = True Then		'如果滑鼠按著拖曳
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

        private void pbxMinBtn_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;		//標題列縮小按鈕被按下=>縮小視窗
        }

        private void pbxCloseBtn_Click(object sender, EventArgs e)
        {
            this.Close();		//標題列關閉按鈕被按下=>關閉視窗
        }

        private void pnlTitleBar_MouseDown(object sender, MouseEventArgs e)
        {
            //紀錄滑鼠點選時的視窗位置與滑鼠點選位置
            nOldWndLeft = this.Left;
            nOldWndTop = this.Top;
            nClickX = e.X;
            nClickY = e.Y;
        }

        private void pnlTitleBar_MouseMove(object sender, MouseEventArgs e)
        {
            if (pnlTitleBar.Capture == true)		//如果滑鼠按著拖曳
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

這篇以一個簡單的小範例試範了如何實現自定義的WindowForm表單介面。值得注意的是，該篇試範的是用簡單的矩形表單，當自定義的表單不是一般的矩形的話，則須要結合 設定.NET透明表單 與這篇的概念下去做，把介面多餘的部份變為透明的。表單介面在顯示上才不會有多餘的空白部份。