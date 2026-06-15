---
title: "[VB.NET]增加圖片亮度"
date: "2009-06-04 09:00:07"
description: "[VB.NET]增加圖片亮度"
tags: [VB.NET]
---

## Introduction

本篇的主旨在於介紹如何增加圖片的亮度。主要的作法就是把圖片上的每個像素的RGB值都增加相同的數值，當數值加完後超過255將以255替換。

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
    ''' Handles the Click event of the btnLoad control.
    ''' </summary>
    ''' <param name="sender">The source of the event.</param>
    ''' <param name="e">The <see cref="System.EventArgs" /> instance containing the event data.</param>
    ''' <remarks></remarks>
    Private Sub btnLoad_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnLoad.Click
        If OpenFileDialog1.ShowDialog = Windows.Forms.DialogResult.OK Then
            Me.PictureBox1.Image = New Bitmap(OpenFileDialog1.FileName)
        End If
    End Sub

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/6/2
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    ''' Brights the bitmap.
    ''' </summary>
    ''' <param name="bmp">The BMP.</param>
    ''' <param name="brighValue">The brigh value.</param>
    ''' <remarks></remarks>
    Private Function BrightBitmap(ByVal bmp As Bitmap, ByVal brighValue As Integer) As Bitmap
        For x As Integer = 0 To bmp.Width - 1
            For y As Integer = 0 To bmp.Height - 1
                Dim color As Color = bmp.GetPixel(x, y)
                Dim r As Integer = If(color.R + brighValue > 255, 255, color.R + brighValue)
                Dim g As Integer = If(color.G + brighValue > 255, 255, color.G + brighValue)
                Dim b As Integer = If(color.B + brighValue > 255, 255, color.B + brighValue)
                bmp.SetPixel(x, y, color.FromArgb(r, g, b))
            Next
        Next
        Return bmp
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/6/3
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    ''' Handles the Click event of the btnBright control.
    ''' </summary>
    ''' <param name="sender">The source of the event.</param>
    ''' <param name="e">The <see cref="System.EventArgs" /> instance containing the event data.</param>
    ''' <remarks></remarks>
    Private Sub btnBright_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnBright.Click
        PictureBox1.Image = BrightBitmap(DirectCast(PictureBox1.Image, Bitmap), TrackBar1.Value)
    End Sub
End Class
```

執行結果：

![image_thumb.png](/images/posts/8667/image_thumb.png) ![image_thumb_1.png](/images/posts/8667/image_thumb_1.png)
