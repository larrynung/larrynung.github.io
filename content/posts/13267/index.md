---
title: "[VB.NET]為控制項加上顯示載入動畫的機制"
date: "2010-01-24 09:56:23"
description: "最近有個需求是當程式在做複雜的運算時，需要告知使用者程式仍然運作，而若用彈出單一Loading對話框的方式又不太適用，因此會想跟網頁一樣能在控制項上外加載入動畫。 在找不到更好的解法前，這邊我先考慮用擴充方法來實作這樣的需求功能。主要是利用擴充方法啟動控制項的載入畫面，啟動多執行緒去更新載入動畫。"
tags: [VB.NET]
---

最近有個需求是當程式在做複雜的運算時，需要告知使用者程式仍然運作，而若用彈出單一Loading對話框的方式又不太適用，因此會想跟網頁一樣能在控制項上外加載入動畫。

在找不到更好的解法前，這邊我先考慮用擴充方法來實作這樣的需求功能。主要是利用擴充方法啟動控制項的載入畫面，啟動多執行緒去更新載入動畫。程式碼如下：

```vb
#Region "Imports"
Imports System.Runtime.CompilerServices
Imports System.Collections.Specialized
Imports System.Windows.Forms
Imports System.Drawing
Imports System.Threading
Imports System.Drawing.Imaging

#End Region

Public Module ControlLoadingExtension

#Region "Class"
    Class LoadingInfo
        Private _loaddingBmp As Image
        Private _loaddingBmpActiveFrameIdx As Integer
        Private _loaddingBmpDimension As FrameDimension
        Private _loaddingBmpFrameCount As Integer
        Private _displayLocation As Point

        Property LoaddingBmp As Image
            Get
                Return _loaddingBmp
            End Get
            Set(ByVal value As Image)
                If _loaddingBmp IsNot value Then
                    _loaddingBmp = value
                    LoaddingBmpDimension = New FrameDimension(value.FrameDimensionsList(0))
                    LoaddingBmpFrameCount = value.GetFrameCount(LoaddingBmpDimension)
                    LoaddingBmpActiveFrameIdx = 0
                End If
            End Set
        End Property

        Property LoaddingBmpActiveFrameIdx As Integer
            Get
                Return _loaddingBmpActiveFrameIdx
            End Get
            Set(ByVal value As Integer)
                _loaddingBmpActiveFrameIdx = value
                LoaddingBmp.SelectActiveFrame(LoaddingBmpDimension, value)
            End Set
        End Property

        Property LoaddingBmpDimension As FrameDimension
            Get
                Return _loaddingBmpDimension
            End Get
            Private Set(ByVal value As FrameDimension)
                _loaddingBmpDimension = value
            End Set
        End Property

        Property LoaddingBmpFrameCount As Integer
            Get
                Return _loaddingBmpFrameCount
            End Get
            Private Set(ByVal value As Integer)
                _loaddingBmpFrameCount = value
            End Set
        End Property

        Property DisplayLocation As Point
            Get
                Return _displayLocation
            End Get
            Set(ByVal value As Point)
                _displayLocation = value
            End Set
        End Property
    End Class
#End Region

#Region "Var"
    Private _loadingStatePool As HybridDictionary
    Private _updateThread As Thread
#End Region

#Region "Private Property"
    Private ReadOnly Property m_LoadingStatePool() As HybridDictionary
        Get
            If _loadingStatePool Is Nothing Then
                _loadingStatePool = New HybridDictionary
            End If
            Return _loadingStatePool
        End Get
    End Property

    Private Property m_UpdateThread As Thread
        Get
            If _updateThread Is Nothing Then
                _updateThread = New Thread(AddressOf ThreadingUpdatePhoto) With {.IsBackground = True}
            End If
            Return _updateThread
        End Get
        Set(ByVal value As Thread)
            _updateThread = value
        End Set
    End Property
#End Region

#Region "Private Method"
    Private Sub InvalidLoaddingBmp(ByVal ctrl As Control)
        Dim info As LoadingInfo = DirectCast(m_LoadingStatePool(ctrl), LoadingInfo)
        ctrl.Invalidate(New Rectangle(info.DisplayLocation, info.LoaddingBmp.Size))
    End Sub

    Private Sub BindingControlEvent(ByVal ctrl As Control)
        UnBindingControlEvent(ctrl)
        AddHandler ctrl.Paint, AddressOf Control_Paint
        AddHandler ctrl.HandleDestroyed, AddressOf Control_HandleDestroyed
        AddHandler ctrl.Resize, AddressOf Control_Resize
    End Sub

    Private Sub UnBindingControlEvent(ByVal ctrl As Control)
        RemoveHandler ctrl.Paint, AddressOf Control_Paint
        RemoveHandler ctrl.HandleDestroyed, AddressOf Control_HandleDestroyed
        RemoveHandler ctrl.Resize, AddressOf Control_Resize
    End Sub

    Private Function GetDisplayLocation(ByVal ctrl As Control) As Point
        Dim info As LoadingInfo = DirectCast(m_LoadingStatePool(ctrl), LoadingInfo)
        Dim bmp As Bitmap = info.LoaddingBmp
        Return New Point(ctrl.Width \ 2 - bmp.Width \ 2, ctrl.Height \ 2 - bmp.Height \ 2)
    End Function

    Private Sub AdjustDisplayLocation(ByVal ctrl As Control)
        Dim info As LoadingInfo = DirectCast(m_LoadingStatePool(ctrl), LoadingInfo)
        Dim bmp As Bitmap = info.LoaddingBmp
        info.DisplayLocation = GetDisplayLocation(ctrl)
    End Sub

    Private Sub PaintGraphic(ByVal g As Graphics, ByVal ctrl As Control)
        Dim info As LoadingInfo = DirectCast(m_LoadingStatePool(ctrl), LoadingInfo)
        Dim bmp As Bitmap = info.LoaddingBmp
        info.LoaddingBmpActiveFrameIdx = (info.LoaddingBmpActiveFrameIdx + 1) Mod info.LoaddingBmpFrameCount
        g.DrawImage(bmp, info.DisplayLocation)
    End Sub

    Private Sub ThreadingUpdatePhoto()
        While True
            For idx As Integer = m_LoadingStatePool.Count - 1 To 0 Step -1
                InvalidLoaddingBmp(DirectCast(m_LoadingStatePool.Keys(idx), Control))
            Next
            Thread.Sleep(100)
        End While
    End Sub
#End Region

#Region "Public Method"
    <Extension()> _
    Function IsLoadingState(ByVal ctrl As Control) As Boolean
        Return m_LoadingStatePool.Contains(ctrl)
    End Function

    <Extension()> _
    Sub ActiveLoadingState(ByVal ctrl As Control, ByVal loaddingBmp As Image)
        If loaddingBmp Is Nothing Then
            Throw New ArgumentNullException("loaddingBmp")
        End If
        DeActiveLoadingState(ctrl)
        m_LoadingStatePool.Add(ctrl, New LoadingInfo() With {.LoaddingBmp = loaddingBmp})
        AdjustDisplayLocation(ctrl)
        BindingControlEvent(ctrl)
        If m_LoadingStatePool.Count = 1 Then
            m_UpdateThread.Start()
        End If
    End Sub

    <Extension()> _
    Sub DeActiveLoadingState(ByVal ctrl As Control)
        If IsLoadingState(ctrl) Then
            UnBindingControlEvent(ctrl)
            m_LoadingStatePool.Remove(ctrl)
            ctrl.Invalidate()
        End If
        If m_LoadingStatePool.Count = 0 Then
            Try
                m_UpdateThread.Abort()
            Catch ex As Exception
            Finally
                m_UpdateThread = Nothing
            End Try
        End If
    End Sub
#End Region

#Region "Event Process"
    Private Sub Control_Paint(ByVal sender As Object, ByVal e As PaintEventArgs)
        PaintGraphic(e.Graphics, DirectCast(sender, Control))
    End Sub

    Private Sub Control_HandleDestroyed(ByVal sender As Object, ByVal e As EventArgs)
        DeActiveLoadingState(DirectCast(sender, Control))
    End Sub

    Private Sub Control_Resize(ByVal sender As Object, ByVal e As EventArgs)
        AdjustDisplayLocation(DirectCast(sender, Control))
    End Sub
#End Region
End Module
```

範例介面如下：
![image9_thumb.png](/images/posts/13267/image9_thumb.png)

範例程式碼如下：

```vb
Public Class Form1
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        For Each c As Control In Me.Controls
            c.ActiveLoadingState(My.Resources.ajax_loader__1_)
        Next
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        For Each c As Control In Me.Controls
            c.DeActiveLoadingState()
        Next
    End Sub
End Class
```

運行結果如下：

![image12_thumb.png](/images/posts/13267/image12_thumb.png)
