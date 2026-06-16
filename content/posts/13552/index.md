---
title: "[VB.NET]Reorder Nodes Under a TreeView or TreeNode"
slug: "vbnet-reorder-nodes-under-a-treeview-or-treenode"
aliases: ["/posts/13552/"]
date: "2010-02-09 10:10:25"
description: "整理一下網友問題。據網友開的需求，希望將本來長成像下面這樣的節點： 整理成像下面這個樣子： 這樣的需求我們可以先找出所有節點，找出後用巢狀迴圈去合併具有相同的FullPath的節點： 使用上把TreeView或是TreeNode當作參數帶入即可，也可以整理成擴充方法使用："
tags: [VB.NET]
---

整理一下網友問題。據網友開的需求，希望將本來長成像下面這樣的節點：
 ![image_thumb.png](/images/posts/13552/image_thumb.png)

整理成像下面這個樣子：
![image_thumb_1.png](/images/posts/13552/image_thumb_1.png)

這樣的需求我們可以先找出所有節點，找出後用巢狀迴圈去合併具有相同的FullPath的節點：

```vb
Private Sub AdjustTreeNodes(ByVal tree As TreeView)
    Dim allNodes() As TreeNode = GetAllNodes(tree)
    Dim node1, node2 As TreeNode
    Try
        tree.SuspendLayout()
        tree.BeginUpdate()
        For idx1 As Integer = allNodes.Count - 1 To 0 Step -1
            For idx2 As Integer = idx1 - 1 To 0 Step -1
                node1 = allNodes(idx1)
                node2 = allNodes(idx2)
                If node1.TreeView IsNot Nothing AndAlso node2.TreeView IsNot Nothing AndAlso node1.FullPath = node2.FullPath Then
                    Dim childNodes(node1.Nodes.Count - 1) As TreeNode
                    node1.Nodes.CopyTo(childNodes, 0)
                    node1.Remove()
                    node2.Nodes.AddRange(childNodes)
                End If
            Next
        Next
    Finally
        tree.EndUpdate()
        tree.ResumeLayout()
    End Try
End Sub

Private Function GetAllNodes(ByVal treeOrNode As Object) As TreeNode()
    If Not TypeOf treeOrNode Is TreeNode AndAlso Not TypeOf treeOrNode Is TreeView Then
        Throw New ArgumentException("Error param type!!")
    End If

    Dim nodes As New List(Of TreeNode)
    If TypeOf treeOrNode Is TreeNode Then
        nodes.Add(treeOrNode)
    End If
    For Each tn As TreeNode In treeOrNode.Nodes
        nodes.AddRange(GetAllNodes(tn))
    Next
    Return nodes.ToArray
End Function
```

使用上把TreeView或是TreeNode當作參數帶入即可，也可以整理成擴充方法使用：

```vb
Imports System.Runtime.CompilerServices

Public Module TreeViewExtension

#Region "Private Method"
    Private Function GetAllTreeNodes(ByVal treeOrNode As Object) As TreeNode()
        If Not TypeOf treeOrNode Is TreeNode AndAlso Not TypeOf treeOrNode Is TreeView Then
            Throw New ArgumentException("Error param type!!")
        End If

        Dim nodes As New List(Of TreeNode)
        If TypeOf treeOrNode Is TreeNode Then
            nodes.Add(treeOrNode)
        End If
        For Each tn As TreeNode In treeOrNode.Nodes
            nodes.AddRange(GetAllTreeNodes(tn))
        Next
        Return nodes.ToArray
    End Function

    Private Sub AdjustAllTreeNodes(ByVal treeOrNode As Object)
        Dim allNodes() As TreeNode = GetAllTreeNodes(treeOrNode)
        Dim node1, node2 As TreeNode
        For idx1 As Integer = allNodes.Count - 1 To 0 Step -1
            For idx2 As Integer = idx1 - 1 To 0 Step -1
                node1 = allNodes(idx1)
                node2 = allNodes(idx2)
                If node1.TreeView IsNot Nothing AndAlso node2.TreeView IsNot Nothing AndAlso node1.FullPath = node2.FullPath Then
                    Dim childNodes(node1.Nodes.Count - 1) As TreeNode
                    node1.Nodes.CopyTo(childNodes, 0)
                    node1.Remove()
                    node2.Nodes.AddRange(childNodes)
                End If
            Next
        Next
    End Sub
#End Region

#Region "Public Method"
    <Extension()> _
    Public Sub AdjustAllNodes(ByVal tree As TreeView)
        AdjustAllTreeNodes(tree)
    End Sub

    <Extension()> _
    Public Sub AdjustAllNodes(ByVal node As TreeNode)
        AdjustAllTreeNodes(node)
    End Sub
#End Region

End Module
```
