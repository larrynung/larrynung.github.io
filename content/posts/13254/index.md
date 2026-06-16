---
title: "[VB.NET]取得Gif動畫圖檔內含的圖片"
date: "2010-01-24 12:31:09"
description: "要取得Gif動畫圖檔內含的圖片，必須要了解的有Bitmap.FrameDimensionsList、FrameDimension Class、Bitmap.GetFrameCount、與Bitmap.SelectActiveFrame。"
tags: [VB.NET]
---

要取得Gif動畫圖檔內含的圖片，必須要了解的有Bitmap.FrameDimensionsList、FrameDimension Class、Bitmap.GetFrameCount、與Bitmap.SelectActiveFrame。

實作上要先把Bitmap.FrameDimensionsList中第一個索引元素帶入FrameDimension建構函式，去建構FrameDimension物件。Bitmap.GetFrameCount帶入FrameDimension物件以取得動畫圖檔內含的圖片個數。再用Bitmap.SelectActiveFrame帶入FrameDimension物件與圖片索引設定當前圖片。像是：

```vb
Private Function GetGifFrames(ByVal gifBmp As Bitmap) As Bitmap()
    Dim imgFrmDim As Imaging.FrameDimension = New Imaging.FrameDimension(gifBmp.FrameDimensionsList(0))
    Dim gifFrames(gifBmp.GetFrameCount(imgFrmDim) - 1) As Bitmap
    For photoIdx As Integer = 0 To gifFrames.Count - 1
        gifBmp.SelectActiveFrame(imgFrmDim, photoIdx)
        gifFrames(photoIdx) = New Bitmap(gifBmp)
    Next
    Return gifFrames
End Function
```

範例介面

![image_thumb.png](/images/posts/13254/image_thumb.png)

範例程式

```vb
Public Class Form1

    Private Sub btnFileBrowser_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnFileBrowser.Click
        If Me.OpenFileDialog1.ShowDialog = Windows.Forms.DialogResult.OK Then
            Me.tbxGifFile.Text = Me.OpenFileDialog1.FileName
            SplitGifFrame(New Bitmap(Me.tbxGifFile.Text))
        End If
    End Sub

    Private Sub SplitGifFrame(ByVal gifBmp As Bitmap)
        Me.flpGifFrames.Controls.Clear()
        Dim gifFrames() As Bitmap = GetGifFrames(gifBmp)
        flpGifFrames.SuspendLayout()
        For Each frame As Bitmap In gifFrames
            flpGifFrames.Controls.Add(New PictureBox With {.Image = frame})
        Next
        flpGifFrames.ResumeLayout()
        Me.tsslStatus.Text = My.Computer.FileSystem.GetName(Me.tbxGifFile.Text) & " 內含 " & gifFrames.Count.ToString & " 個圖片"
    End Sub

    Private Function GetGifFrames(ByVal gifBmp As Bitmap) As Bitmap()
        Dim imgFrmDim As Imaging.FrameDimension = New Imaging.FrameDimension(gifBmp.FrameDimensionsList(0))
        Dim gifFrames(gifBmp.GetFrameCount(imgFrmDim) - 1) As Bitmap
        For photoIdx As Integer = 0 To gifFrames.Count - 1
            gifBmp.SelectActiveFrame(imgFrmDim, photoIdx)
            gifFrames(photoIdx) = New Bitmap(gifBmp)
        Next
        Return gifFrames
    End Function
End Class
```

運行結果

![image_thumb_1.png](/images/posts/13254/image_thumb_1.png)
