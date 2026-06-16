---
title: "[VB.NET]Implementing the MDI Child Window List"
slug: "vbnet-implementing-the-mdi-child-window-list"
aliases: ["/posts/15508/"]
date: "2010-05-30 09:57:44"
description: "最近在撰寫MDI程式，碰到很多很麻煩的問題，尤其是在MDI子視窗清單功能的部分，個人覺得特別難處理。其中最麻煩的莫過於When close is cancelled on MDI Child Window and it is hidden, MDI parent's window never…"
tags: [VB.NET]
---

最近在撰寫MDI程式，碰到很多很麻煩的問題，尤其是在MDI子視窗清單功能的部分，個人覺得特別難處理。其中最麻煩的莫過於When close is cancelled on MDI Child Window and it is hidden, MDI parent's window never shows it again.這篇所提到的問題。

雖然MenuStrip內建的MDIWindowListItem十分好用，但要自行擋住為數眾多的問題，最後還是決定自己實作MDI子視窗清單的功能，好在實作這樣的功能並不困難，只要處理MenuItem的DropDownOpening與DropDownClosed事件即可，這邊簡單的紀錄一下：

```vb
Private Sub WindowsMenu_DropDownClosed(ByVal sender As Object, ByVal e As System.EventArgs) Handles WindowsMenu.DropDownClosed
    Dim separators() As ToolStripItem = WindowsMenu.DropDownItems.Find("MdiWindowListSeperator", False)
    If separators.Count = 0 Then
        Return
    End If
    Dim spIdx As Integer = WindowsMenu.DropDownItems.IndexOf(separators(0))
    For idx As Integer = WindowsMenu.DropDownItems.Count - 1 To spIdx Step -1
        WindowsMenu.DropDownItems.RemoveAt(idx)
    Next
End Sub

Private Sub WindowsMenu_DropDownOpening(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles WindowsMenu.DropDownOpening
    If ActiveMdiChild Is Nothing Then
        Return
    End If
    Dim sp As New ToolStripSeparator
    sp.Name = "MdiWindowListSeperator"
    WindowsMenu.DropDownItems.Add(sp)
    For Each f As Form In MdiChildren
        If Not f.Visible Then
            Continue For
        End If
        WindowsMenu.DropDownItems.Add(New ToolStripMenuItem(f.Text, Nothing, AddressOf MDIChildren_Click) With {.Checked = ActiveMdiChild Is f, .Tag = f})
    Next
End Sub

Private Sub MDIChildren_Click(ByVal sender As Object, ByVal e As EventArgs)
    DirectCast(DirectCast(sender, ToolStripMenuItem).Tag, Form).Activate()
End Sub
```

也可以只處理MenuItem的DropDownOpening事件：

```vb
Private Sub WindowToolStripMenuItem_DropDownOpening(ByVal sender As System.Object, ByVal e As System.EventArgs)
    Const seperatorKey As String = "MdiWindowListSeperator"
    Dim dropDownItems As ToolStripItemCollection = _ideForm.WindowToolStripMenuItem.DropDownItems
    If dropDownItems.ContainsKey(seperatorKey) Then
        Dim spIdx As Integer = dropDownItems.IndexOf(dropDownItems.Find(seperatorKey, False)(0))
        For idx As Integer = dropDownItems.Count - 1 To spIdx Step -1
            dropDownItems.RemoveAt(idx)
        Next
    End If

    Dim linq = From f In _ideForm.MdiChildren Where f.Visible Select f
    If linq.Count = 0 Then
        Return
    End If
    Dim sp As New ToolStripSeparator
    sp.Name = seperatorKey
    dropDownItems.Add(sp)
    For Each f As Form In linq
        dropDownItems.Add(New ToolStripMenuItem(f.Text, Nothing, AddressOf MDIChildren_Click) With {.Checked = _ideForm.ActiveMdiChild Is f, .Tag = f})
    Next
End Sub
```
