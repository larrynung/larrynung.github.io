---
title: "[VB.NET]Merge MDI ToolStrip"
date: "2010-10-14 10:14:46"
description: "[VB.NET]Merge MDI ToolStrip"
tags: [VB.NET]
---

有時候在MDI架構下，我們會有需要將子視窗與父視窗工具列或是選單合併的需求。在選單的合併上，MDI架構提供了很簡易的合併方法，只要調整MergeAction與MergeIndex，在切換子視窗時就會自動幫您合併選單。但在工具列的合併上就比較麻煩點，除了一樣要調整MergeAction與MergeIndex外。

我們還需處理MDIChildActivate事件的動作，透過ToolStripManager.RevertMerge把工具列先前的合併狀態給還原，並透過ToolStripManager.Merge將當前子視窗的工具列與父視窗工具列合併。

這邊看個簡單的例子，為方便起見這邊定義了一個IChildForm介面，用以開出子視窗的工具列，便於做工具列的合併動作。

Public Interface IChildForm

    ReadOnly Property MainToolStrip() As ToolStrip

End Interface

子視窗實做IChildForm介面，把子視窗的工具列開出。

Public Class Form1
    Implements IChildForm

    Public ReadOnly Property MainToolStrip() As System.Windows.Forms.ToolStrip Implements IChildForm.MainToolStrip
        Get
            Return ToolStrip1
        End Get
    End Property
End Class

在父視窗中處理MDIChildActivate事件，將工具列合併。

Public Class MDIParent1
    Protected Overrides Sub OnMdiChildActivate(ByVal e As System.EventArgs)
        MyBase.OnMdiChildActivate(e)
        ToolStripManager.RevertMerge(ToolStrip)
        Dim childForm As IChildForm = CType(ActiveMdiChild, IChildForm)
        If childForm IsNot Nothing Then
            ToolStripManager.Merge(childForm.MainToolStrip, ToolStrip)
        End If
    End Sub
End Class

## Download

MergeMDIToolStrip.zip