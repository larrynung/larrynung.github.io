---
title: "[C#][VB.NET]反轉圖片顏色"
slug: "[CSharp][VB.NET]反轉圖片顏色"
date: "2009-06-03 09:01:55"
description: "[C#][VB.NET]反轉圖片顏色"
tags: [VB.NET,CSharp]
---

## Introduction

本篇的主旨在於介紹如何反轉圖片的顏色。欲把圖片顏色反轉，我們只需把圖片上的每個像素的RGB值設為其與255的差值即可。

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
            Me.PictureBox1.Image = GetInvertBitmap(OpenFileDialog1.FileName)
        End If
    End Sub

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/6/2
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    ''' Gets the invert bitmap.
    ''' </summary>
    ''' <param name="file">The file.</param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Private Function GetInvertBitmap(ByVal file As String) As Bitmap
        Dim bmp As Bitmap = New Bitmap(file)
        For x As Integer = 0 To bmp.Width - 1
            For y As Integer = 0 To bmp.Height - 1
                Dim color As Color = bmp.GetPixel(x, y)
                bmp.SetPixel(x, y, color.FromArgb(255 - color.R, 255 - color.G, 255 - color.B))
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
                pictureBox1.Image = GetInvertBitmap(openFileDialog1.FileName);
            }
        }

        //***************************************************************************
        //Author: Larry Nung
        //Date: 2009/6/2
        //Purpose:
        //Memo:
        //***************************************************************************
        /// <summary>
        /// Gets the invert bitmap.
        /// </summary>
        /// <param name="file">The file.</param>
        /// <returns></returns>
        private Bitmap GetInvertBitmap(string file)
        {
            Bitmap bmp = new Bitmap(file);
            for (int x = 0; x < bmp.Width; x++)
            {
                for (int y = 0; y < bmp.Height; y++)
                {
                    Color color = bmp.GetPixel(x, y);
                    bmp.SetPixel(x, y, Color.FromArgb(255 - color.R, 255 - color.G, 255 - color.B));
                }
            }
            return bmp;
        }
    }
}
```

執行結果：

![image_thumb.png](/images/posts/8652/image_thumb.png)
