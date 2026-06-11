---
title: "[VB.NET]取得TreeView或TreeNode下的樹葉節點"
date: "2010-02-09 09:45:26"
description: "[VB.NET]取得TreeView或TreeNode下的樹葉節點"
tags: [VB.NET]
---

若要取得TreeView或TreeNode下的樹葉節點，我們可以先找出所有的節點後，再去挑出Nodes.Count為0的節點：
```
Private Function GetAllLeafNodes(ByVal treeOrNode As Object) As TreeNode()
Return (From tn In GetAllNodes(treeOrNode) Where tn.Nodes.Count = 0 Select tn).ToArray
End Function

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
```
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

Private Function GetAllLeafTreeNodes(ByVal treeOrNode As Object) As TreeNode()
Return (From tn In GetAllTreeNodes(treeOrNode) Where tn.Nodes.Count = 0 Select tn).ToArray
End Function
#End Region

#Region "Public Method"
_
Public Function GetAllLeafNodes(ByVal tree As TreeView) As TreeNode()
Return GetAllLeafTreeNodes(tree)
End Function

_
Public Function GetAllLeafNodes(ByVal node As TreeNode) As TreeNode()
Return GetAllLeafTreeNodes(node)
End Function
#End Region

End Module
```