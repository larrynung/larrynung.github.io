---
title: "[VB.NET]使用Win32 API擷取滑鼠游標位置的顏色"
date: "2010-05-26 10:50:32"
description: "[VB.NET]使用Win32 API擷取滑鼠游標位置的顏色"
tags: [VB.NET]
---

<p>要使用Win32 API擷取滑鼠游標位置的顏色，主要可分為三個步驟：</p>  <ol>   <li>呼叫GetDC API取得畫布</li>    <li>呼叫GetPixel API取得畫布上指定位置的像素</li>    <li>呼叫ReleaseDC API釋放畫布</li> </ol>  <p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\15454\image_thumb_1.png" width="422" height="80" /></p>  <p> </p>  <p>使用上可以直接透過下面整理過的函式：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:9d1b17d6-90e4-4b45-9f3d-898b9c39c846" class="wlWriterSmartContent"><pre name="code" class="vb">    &lt;DllImport("User32.dll", EntryPoint:="GetDC", _
     CallingConvention:=CallingConvention.StdCall, _
     CharSet:=CharSet.Auto, exactspelling:=True)&gt; _
    Public Shared Function GetDC(ByVal hwnd As IntPtr) As IntPtr
    End Function
    Public Declare Function GetPixel Lib "gdi32" Alias "GetPixel" (ByVal hdc As IntPtr, ByVal X As Int32, ByVal Y As Int32) As Int32
    &lt;DllImport("user32.dll")&gt; _
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
    End Function</pre></div>

<p> </p>

<p>簡易範例如下：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:fc8b05a5-165a-4f43-923a-f2a9092f4357" class="wlWriterSmartContent"><pre name="code" class="vb">Imports System.Runtime.InteropServices

Public Class Form1
    &lt;DllImport("User32.dll", EntryPoint:="GetDC", _
     CallingConvention:=CallingConvention.StdCall, _
     CharSet:=CharSet.Auto, exactspelling:=True)&gt; _
    Public Shared Function GetDC(ByVal hwnd As IntPtr) As IntPtr
    End Function
    Public Declare Function GetPixel Lib "gdi32" Alias "GetPixel" (ByVal hdc As IntPtr, ByVal X As Int32, ByVal Y As Int32) As Int32
    &lt;DllImport("user32.dll")&gt; _
   Private Shared Function ReleaseDC(ByVal hWnd As IntPtr, ByVal hDC As IntPtr) As Integer
    End Function

    Private Sub Timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        Dim x As Integer
        Dim y As Integer
        Dim p As Point = Cursor.Position
        x = p.X
        y = p.Y
        Me.Text = "位置: x:" &amp; x &amp; ", y:" &amp; y
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

End Class</pre></div>

<p> </p>

<p>運行結果：</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\15454\image_thumb.png" width="427" height="173" /></p>

<p> </p>

<h2>Download</h2>

<p>ColorPicker.zip</p>
