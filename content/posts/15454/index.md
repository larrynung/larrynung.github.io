---
title: "[VB.NET]使用Win32 API擷取滑鼠游標位置的顏色"
date: "2010-05-26 10:50:32"
description: "要使用Win32 API擷取滑鼠游標位置的顏色，主要可分為三個步驟： 呼叫GetDC API取得畫布 呼叫GetPixel API取得畫布上指定位置的像素 呼叫ReleaseDC API釋放畫布 使用上可以直接透過下面整理過的函式： 簡易範例如下： 運行結果： Download…"
tags: [VB.NET]
---

要使用Win32 API擷取滑鼠游標位置的顏色，主要可分為三個步驟：

1. 呼叫GetDC API取得畫布
2. 呼叫GetPixel API取得畫布上指定位置的像素
3. 呼叫ReleaseDC API釋放畫布

![image_thumb_1.png](/images/posts/15454/image_thumb_1.png)

使用上可以直接透過下面整理過的函式：

```vb
 <DllImport("User32.dll", EntryPoint:="GetDC", _
  CallingConvention:=CallingConvention.StdCall, _
  CharSet:=CharSet.Auto, exactspelling:=True)> _
 Public Shared Function GetDC(ByVal hwnd As IntPtr) As IntPtr
 End Function
 Public Declare Function GetPixel Lib "gdi32" Alias "GetPixel" (ByVal hdc As IntPtr, ByVal X As Int32, ByVal Y As Int32) As Int32
 <DllImport("user32.dll")> _
Private Shared Function ReleaseDC(ByVal hWnd As IntPtr, ByVal hDC As IntPtr) As Integer
 End Function

 Private Function GetColor() As Color
     Return GetColor(Cursor.Position)
 End Function

 Private Function GetColor(ByVal point As Point) As Color
     Return GetColor(point.X, point.Y)
 End Function

 Private Function GetColor(ByVal x As Integer, ByVal y As Integer) As Color
     Dim hdc As IntPtr
     hdc = GetDC(IntPtr.Zero)   '取該Handle值的DC
     GetColor = ColorTranslator.FromWin32(GetPixel(hdc, x, y))
     ReleaseDC(IntPtr.Zero, hdc)  '將DC 釋放
 End Function
```

簡易範例如下：

```vb
Imports System.Runtime.InteropServices

Public Class Form1
    <DllImport("User32.dll", EntryPoint:="GetDC", _
     CallingConvention:=CallingConvention.StdCall, _
     CharSet:=CharSet.Auto, exactspelling:=True)> _
    Public Shared Function GetDC(ByVal hwnd As IntPtr) As IntPtr
    End Function
    Public Declare Function GetPixel Lib "gdi32" Alias "GetPixel" (ByVal hdc As IntPtr, ByVal X As Int32, ByVal Y As Int32) As Int32
    <DllImport("user32.dll")> _
   Private Shared Function ReleaseDC(ByVal hWnd As IntPtr, ByVal hDC As IntPtr) As Integer
    End Function

    Private Sub Timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        Dim x As Integer
        Dim y As Integer
        Dim p As Point = Cursor.Position
        x = p.X
        y = p.Y
        Me.Text = "位置: x:" & x & ", y:" & y
        lblColor.BackColor = GetColor()
        lblWin32ColorCode.Text = ColorTranslator.ToWin32(lblColor.BackColor)
        lblHtmlColorCode.Text = ColorTranslator.ToHtml(lblColor.BackColor)
        lblOLEColorCode.Text = ColorTranslator.ToOle(lblColor.BackColor)
        lblColorInfo.Text = lblColor.BackColor.ToString
    End Sub

    Private Function GetColor() As Color
        Return GetColor(Cursor.Position)
    End Function

    Private Function GetColor(ByVal point As Point) As Color
        Return GetColor(point.X, point.Y)
    End Function

    Private Function GetColor(ByVal x As Integer, ByVal y As Integer) As Color
        Dim hdc As IntPtr
        hdc = GetDC(IntPtr.Zero)   '取該Handle值的DC
        GetColor = ColorTranslator.FromWin32(GetPixel(hdc, x, y))
        ReleaseDC(IntPtr.Zero, hdc)  '將DC 釋放
    End Function

End Class
```

運行結果：

![image_thumb.png](/images/posts/15454/image_thumb.png)

## Download

ColorPicker.zip
