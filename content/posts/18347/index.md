---
title: "[VB.NET]Merge MDI ToolStrip"
date: "2010-10-14 10:14:46"
description: "[VB.NET]Merge MDI ToolStrip"
tags: [VB.NET]
---

<p>有時候在MDI架構下，我們會有需要將子視窗與父視窗工具列或是選單合併的需求。在選單的合併上，MDI架構提供了很簡易的合併方法，只要調整MergeAction與MergeIndex，在切換子視窗時就會自動幫您合併選單。但在工具列的合併上就比較麻煩點，除了一樣要調整MergeAction與MergeIndex外。</p><p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" width="299" height="310" src="\images\posts\18347\image_thumb.png" /></p><p> </p><p>我們還需處理MDIChildActivate事件的動作，透過ToolStripManager.RevertMerge把工具列先前的合併狀態給還原，並透過ToolStripManager.Merge將當前子視窗的工具列與父視窗工具列合併。</p><p> </p><p>這邊看個簡單的例子，為方便起見這邊定義了一個IChildForm介面，用以開出子視窗的工具列，便於做工具列的合併動作。</p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f55f1024-ee9f-4d2e-bbc8-a82cfb9c4fe9" class="wlWriterSmartContent"><pre class="vb" name="code">
Public Interface IChildForm

    ReadOnly Property MainToolStrip() As ToolStrip

End Interface</pre></div><p> </p><p>子視窗實做IChildForm介面，把子視窗的工具列開出。</p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:11e1a5a3-768d-4eb2-acc9-9b4bf976f5fd" class="wlWriterSmartContent"><pre class="vb" name="code">
Public Class Form1
    Implements IChildForm

    Public ReadOnly Property MainToolStrip() As System.Windows.Forms.ToolStrip Implements IChildForm.MainToolStrip
        Get
            Return ToolStrip1
        End Get
    End Property
End Class</pre></div><p> </p><p>在父視窗中處理MDIChildActivate事件，將工具列合併。</p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:af6d3e1e-fcf5-4b35-bb11-c692772d881a" class="wlWriterSmartContent"><pre class="vb" name="code">
Public Class MDIParent1
    Protected Overrides Sub OnMdiChildActivate(ByVal e As System.EventArgs)
        MyBase.OnMdiChildActivate(e)
        ToolStripManager.RevertMerge(ToolStrip)
        Dim childForm As IChildForm = CType(ActiveMdiChild, IChildForm)
        If childForm IsNot Nothing Then
            ToolStripManager.Merge(childForm.MainToolStrip, ToolStrip)
        End If
    End Sub
End Class</pre></div><p> </p><h2>Download</h2><p>MergeMDIToolStrip.zip</p>
