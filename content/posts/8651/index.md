---
title: "[C#][VB.NET]彩色圖片轉為黑白圖片"
slug: "[CSharp][VB.NET]彩色圖片轉為黑白圖片"
date: "2009-06-03 09:01:40"
description: "Introduction 本篇的主旨在於介紹如何把圖片轉為黑白照片。欲把彩色圖片轉為黑白圖片，我們可以把圖片上的每個像素都設為灰階值。灰階值的取得可套用下面公式。 灰階值 = (R+G+B)/3 範例程式 VB.NET C# 執行結果："
tags: [CSharp,VB.NET]
---

## Introduction

本篇的主旨在於介紹如何把圖片轉為黑白照片。欲把彩色圖片轉為黑白圖片，我們可以把圖片上的每個像素都設為灰階值。灰階值的取得可套用下面公式。

**灰階值 = (R+G+B)/3**

## 範例程式

VB.NET

```
'|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'Author: Larry Nung
'Date: 2009/6/2
'File:
'Memo:
'|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
''' <summary>
'''
''' </summary>
''' <remarks></remarks>
Public Class Form1

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/6/2
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    ''' Handles the Click event of the Button1 control.
    ''' </summary>
    ''' <param name="sender">The source of the event.</param>
    ''' <param name="e">The <see cref="System.EventArgs" /> instance containing the event data.</param>
    ''' <remarks></remarks>
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        If OpenFileDialog1.ShowDialog = Windows.Forms.DialogResult.OK Then
            Me.PictureBox1.Image = GetGrayBitmap(OpenFileDialog1.FileName)
        End If
    End Sub

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/6/2
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    ''' Gets the gray image.
    ''' </summary>
    ''' <param name="file">The file.</param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Private Function GetGrayBitmap(ByVal file As String) As Bitmap
        Dim bmp As Bitmap = New Bitmap(file)
        For x As Integer = 0 To bmp.Width - 1
            For y As Integer = 0 To bmp.Height - 1
                Dim color As Color = bmp.GetPixel(x, y)
                Dim gray As Integer = (CInt(color.R) + CInt(color.G) + CInt(color.B)) \ 3
                bmp.SetPixel(x, y, color.FromArgb(gray, gray, gray))
            Next
        Next
        Return bmp
    End Function

End Class
```

C#

```
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

    //|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    //Author: Larry Nung
    //Date: 2009/6/2
    //File:
    //Memo:
    //|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    /// <summary>
    ///
    /// </summary>
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //***************************************************************************
        //Author: Larry Nung
        //Date: 2009/6/2
        //Purpose:
        //Memo:
        //***************************************************************************
        /// <summary>
        /// Handles the Click event of the button1 control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="System.EventArgs"/> instance containing the event data.</param>
        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                pictureBox1.Image = GetGrayBitmap(openFileDialog1.FileName);
            }
        }

        //***************************************************************************
        //Author: Larry Nung
        //Date: 2009/6/2
        //Purpose:
        //Memo:
        //***************************************************************************
        /// <summary>
        /// Gets the gray bitmap.
        /// </summary>
        /// <param name="file">The file.</param>
        /// <returns></returns>
        private Bitmap GetGrayBitmap(string file)
        {
            Bitmap bmp = new Bitmap(file);
            for (int x=0; x < bmp.Width; x++)
            {
                for (int y=0; y < bmp.Height; y++)
                {
                    Color color = bmp.GetPixel(x, y);
                    int gray = (color.R + color.G + color.B) / 3;
                    bmp.SetPixel(x, y, Color.FromArgb(gray, gray, gray));
                }
            }
            return bmp;
        }
    }
}
```

執行結果：

![image_thumb.png](/images/posts/8651/image_thumb.png)
