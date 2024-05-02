---
title: "[VB.NET]取得TreeView或TreeNode下的所有節點"
date: "2010-02-09 09:39:37"
description: "[VB.NET]取得TreeView或TreeNode下的所有節點"
tags: [VB.NET]
---

<pre>若要取得TreeView或TreeNode下的所有節點，可以透過遞迴的方式把所有節點給找出來。像是下面這樣：<br /><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:94b16595-8ff8-4a35-b389-85925bef270a" class="wlWriterEditableSmartContent"><pre name="code" class="vb:nocontrols">    Private Function GetAllNodes(ByVal treeOrNode As Object) As TreeNode()
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
    End Function</pre></div></pre>

<pre> </pre>

<pre>使用上把TreeView或是TreeNode當作參數帶入即可，也可以整理成擴充方法使用：<br /><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:feae1230-0751-4a87-9fb5-f5065a401e9c" class="wlWriterEditableSmartContent"><pre name="code" class="vb:nocontrols">Imports System.Runtime.CompilerServices

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
    &lt;Extension()&gt; _
    Public Function GetAllNodes(ByVal tree As TreeView) As TreeNode()
        Return GetAllTreeNodes(tree)
    End Function

    &lt;Extension()&gt; _
    Public Function GetAllNodes(ByVal node As TreeNode) As TreeNode()
        Return GetAllTreeNodes(node)
    End Function
#End Region

End Module</pre></div></pre>
