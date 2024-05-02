---
title: "用Extension Method在執行階段進行控制項的拖曳"
date: "2010-06-20 10:02:40"
description: "用Extension Method在執行階段進行控制項的拖曳"
tags: [VB.NET]
---

<p>整理一下拖曳控制項用的Extension Method，簡單紀錄如下：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:06d00e8f-f639-4315-af4a-57ed6059ea24" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Imports System.Runtime.CompilerServices

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
            If _runtimeDragClickPoint &lt;&gt; value Then
                _runtimeDragClickPoint = value
            End If
        End Set
    End Property
#End Region


#Region "Public Method"
    &lt;Extension()&gt; _
    Public Sub EnableRuntimeDrag(ByVal ctrl As Control)
        DisableRuntimeDrag(ctrl)
        AddHandler ctrl.MouseDown, AddressOf ctrl_MouseDown
        AddHandler ctrl.MouseMove, AddressOf ctrl_MouseMove
        AddHandler ctrl.HandleDestroyed, AddressOf ctrl_HandleDestroyed
    End Sub


    &lt;Extension()&gt; _
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

End Module</pre></div>

<p> </p>

<p>使用上若要啟動拖曳，透過呼叫EnableRuntimeDrag就好，若要關閉拖曳，則呼叫DisableRuntimeDrag。簡單的範例程式如下：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e692bcab-fbed-4174-a89d-597f3f31335c" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Public Class Form1
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        For Each c As Control In Controls
            c.EnableRuntimeDrag()
            c.Cursor = Cursors.Hand
        Next
    End Sub
End Class
</pre></div>

<p> </p>

<p>執行後表單中的控制項就可以直接透過滑鼠拖曳。</p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\16012\image_thumb.png" width="410" height="270" /> </p>

<p><img style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" border="0" alt="image" src="\images\posts\16012\image_thumb_1.png" width="410" height="270" /></p>
