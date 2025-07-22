---
title: "[VB.NET]自定義.NET WindowForm表單介面(三)"
date: "2010-04-23 12:11:15"
description: "[VB.NET]自定義.NET WindowForm表單介面(三)"
tags: [VB.NET]
---繼之前談到的自定義WindowForm表單介面(二)，裡面提到的方法一與方法二在使用上都會有個現象，那就是在工作列上按下滑鼠右鍵，本來該彈出的快顯選單消失不見了。

![](\images\posts\14759\image_thumb.png)

其實這個問題可以透過GetWindowLong把視窗目前的Style值取出，加上系統選單與縮小的Style，再用SetWindowLong把視窗Style設起來。程式如下：
```
_
Private Shared Function GetWindowLong( _
ByVal hWnd As IntPtr, _
ByVal nIndex As Integer) As Integer
End Function

_
Private Shared Function SetWindowLong(ByVal hWnd As IntPtr, ByVal nIndex As Integer, ByVal dwNewLong As Integer) As Integer
End Function

Public Const WS_SYSMENU As Integer = &H80000
Const WS_MINIMIZEBOX As Integer = &H20000

Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
Dim winLong As Integer = GetWindowLong(New HandleRef(Me, Me.Handle), -16)
SetWindowLong(New HandleRef(Me, Me.Handle), -16, winLong Or WS_SYSMENU Or WS_MINIMIZEBOX)
End Sub
```
運行後在工作列上的圖示按滑鼠右鍵，就會發現消失的快顯選單被恢復了。

![](\images\posts\14759\image_thumb.png)