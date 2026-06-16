---
title: "[VB.NET]用.NET實作檔案總管"
date: "2009-07-03 12:01:31"
description: "要用.NET實作檔案總管的功能，相信應該都難不倒大家。但我也相信應該很多人都是一次取得所有電腦內的檔案與目錄清單，一次的把清單給塞到介面上。如果你不是習慣這樣寫的人，那恭喜您可以跳過這篇了。如果恰巧你就是這樣寫的，請耐著性子往下看吧。"
tags: [VB.NET]
---

要用.NET實作檔案總管的功能，相信應該都難不倒大家。但我也相信應該很多人都是一次取得所有電腦內的檔案與目錄清單，一次的把清單給塞到介面上。如果你不是習慣這樣寫的人，那恭喜您可以跳過這篇了。如果恰巧你就是這樣寫的，請耐著性子往下看吧。

要實作檔案總管功能又要兼顧效率，我們在寫作時勢必不能一次把所有檔案目錄清單給塞到介面。取而代之的是，我們可以只塞下一層的目錄與檔案。範例程式碼如下：

```
Imports System.IO

Public Class Form1

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        InitTreeView()
    End Sub

    Private Sub InitTreeView()
        Dim node As TreeNode
        TreeView1.BeginUpdate()
        For Each driver As DriveInfo In DriveInfo.GetDrives()
            node = TreeView1.Nodes.Add(driver.Name)
            If driver.IsReady Then
                AddDirectorys(node)
                AddFiles(node)
                node.Tag = True
            End If
        Next
        TreeView1.EndUpdate()
    End Sub

    Private Sub AddDirectorys(ByVal node As TreeNode)
        If CBool(node.Tag) = True Then
            Return
        End If

        Try
            TreeView1.BeginUpdate()
            For Each dir As String In Directory.GetDirectories(node.FullPath)
                node.Nodes.Add(dir.Substring(dir.LastIndexOf("\") + 1))
            Next
        Catch ex As Exception
        Finally
            TreeView1.EndUpdate()
        End Try

    End Sub

    Private Sub AddFiles(ByVal node As TreeNode)
        If CBool(node.Tag) = True Then
            Return
        End If

        Try
            TreeView1.BeginUpdate()
            For Each file As String In Directory.GetFiles(node.FullPath)
                node.Nodes.Add(My.Computer.FileSystem.GetName(file))
            Next
        Catch ex As Exception
        Finally
            TreeView1.EndUpdate()
        End Try
    End Sub

    Private Sub TreeView1_BeforeExpand(ByVal sender As System.Object, ByVal e As System.Windows.Forms.TreeViewCancelEventArgs) Handles TreeView1.BeforeExpand
        For Each node As TreeNode In e.Node.Nodes
            AddDirectorys(node)
        Next
        AddFiles(e.Node)
        e.Node.Tag = True
    End Sub
End Class
```

執行畫面

![image_thumb.png](/images/posts/9095/image_thumb.png) ![image_thumb_1.png](/images/posts/9095/image_thumb_1.png)
