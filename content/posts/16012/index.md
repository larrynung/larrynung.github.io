---
title: "Drag Controls at Runtime Using an Extension Method"
slug: "drag-controls-at-runtime-using-an-extension-method"
aliases: ["/posts/16012/"]
date: "2010-06-20 10:02:40"
description: "整理一下拖曳控制項用的Extension Method，簡單紀錄如下： 使用上若要啟動拖曳，透過呼叫EnableRuntimeDrag就好，若要關閉拖曳，則呼叫DisableRuntimeDrag。簡單的範例程式如下： 執行後表單中的控制項就可以直接透過滑鼠拖曳。"
tags: [VB.NET]
---

整理一下拖曳控制項用的Extension Method，簡單紀錄如下：

```vb
Imports System.Runtime.CompilerServices

Public Module ControlExtension

#Region "Var"
    Private _runtimeDragClickPoint As Point
#End Region

#Region "Private Property"
    Private Property m_RuntimeDragClickPoint() As Point
        Get
            Return _runtimeDragClickPoint
        End Get
        Set(ByVal value As Point)
            If _runtimeDragClickPoint <> value Then
                _runtimeDragClickPoint = value
            End If
        End Set
    End Property
#End Region

#Region "Public Method"
    <Extension()> _
    Public Sub EnableRuntimeDrag(ByVal ctrl As Control)
        DisableRuntimeDrag(ctrl)
        AddHandler ctrl.MouseDown, AddressOf ctrl_MouseDown
        AddHandler ctrl.MouseMove, AddressOf ctrl_MouseMove
        AddHandler ctrl.HandleDestroyed, AddressOf ctrl_HandleDestroyed
    End Sub

    <Extension()> _
    Public Sub DisableRuntimeDrag(ByVal ctrl As Control)
        If ctrl Is Nothing Then
            Throw New ArgumentNullException("ctrl")
        End If
        RemoveHandler ctrl.MouseDown, AddressOf ctrl_MouseDown
        RemoveHandler ctrl.MouseMove, AddressOf ctrl_MouseMove
        RemoveHandler ctrl.HandleDestroyed, AddressOf ctrl_HandleDestroyed
    End Sub
#End Region

#Region "Event Process"
    Private Sub ctrl_MouseDown(ByVal sender As Object, ByVal e As MouseEventArgs)
        m_RuntimeDragClickPoint = New Point(e.X, e.Y)
    End Sub

    Private Sub ctrl_MouseMove(ByVal sender As Object, ByVal e As MouseEventArgs)
        Dim ctrl As Control = DirectCast(sender, Control)
        If ctrl.Capture Then      '如果滑鼠按著拖曳
            '設定新的視窗位置
            ctrl.Top = e.Y + ctrl.Top - m_RuntimeDragClickPoint.Y
            ctrl.Left = e.X + ctrl.Left - m_RuntimeDragClickPoint.X
        End If
    End Sub

    Private Sub ctrl_HandleDestroyed(ByVal sender As Object, ByVal e As EventArgs)
        DisableRuntimeDrag(sender)
    End Sub
#End Region

End Module
```

使用上若要啟動拖曳，透過呼叫EnableRuntimeDrag就好，若要關閉拖曳，則呼叫DisableRuntimeDrag。簡單的範例程式如下：

```vb
Public Class Form1
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        For Each c As Control In Controls
            c.EnableRuntimeDrag()
            c.Cursor = Cursors.Hand
        Next
    End Sub
End Class
```

執行後表單中的控制項就可以直接透過滑鼠拖曳。

![image_thumb.png](/images/posts/16012/image_thumb.png)

![image_thumb_1.png](/images/posts/16012/image_thumb_1.png)
