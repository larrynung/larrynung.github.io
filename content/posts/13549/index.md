---
title: "[VB.NET]Get All Nodes Under a TreeView or TreeNode"
slug: "vbnet-get-all-nodes-under-a-treeview-or-treenode"
aliases: ["/posts/13549/"]
date: "2010-02-09 09:39:37"
description: "[VB.NET]取得TreeView或TreeNode下的所有節點"
tags: [VB.NET]
---

```
若要取得TreeView或TreeNode下的所有節點，可以透過遞迴的方式把所有節點給找出來。像是下面這樣：
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

使用上把TreeView或是TreeNode當作參數帶入即可，也可以整理成擴充方法使用：
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
#End Region

#Region "Public Method"
    <Extension()> _
    Public Function GetAllNodes(ByVal tree As TreeView) As TreeNode()
        Return GetAllTreeNodes(tree)
    End Function

    <Extension()> _
    Public Function GetAllNodes(ByVal node As TreeNode) As TreeNode()
        Return GetAllTreeNodes(node)
    End Function
#End Region

End Module
```
