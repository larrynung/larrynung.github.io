---
title: "[VB.NET]將集合類別繫結至DataGridView並使其具備新增功能"
date: "2010-05-10 10:55:23"
description: "[VB.NET]將集合類別繫結至DataGridView並使其具備新增功能"
tags: [VB.NET]
---

<p>若直接把集合類別繫結至DataGridView。</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ccdff7c6-1001-4db7-bf40-85f4c3e44254" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Public Class Form1

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim lst As New List(Of Person)
        lst.Add(New Person With {.Name = "Larry"})
        DataGridView1.DataSource = lst
    End Sub

End Class

Class Person
    Dim _name As String
    Property Name() As String
        Get
            Return _name
        End Get
        Set(ByVal value As String)
            _name = value
        End Set
    End Property
End Class</pre></div>

<p> </p>

<p>就算DataGridView有設定AllowUserToAddRows，DataGridView也是無法做新增的動作。</p>

<p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" src="\images\posts\15130\image_thumb.png" width="304" height="304" /> </p>

<p> </p>

<p>要解決這樣的問題，可以把集合類別設至BindingSource，把AllowNew屬性設起來，再把BindingSource給繫到DataGridView就可以了。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:565d988f-0d2a-42a2-9d9b-4574af030d56" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Public Class Form1

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        Dim lst As New List(Of Person)
        lst.Add(New Person With {.Name = "Larry"})
        Dim binding As New BindingSource
        binding.DataSource = lst
        binding.AllowNew = True
        DataGridView1.DataSource = Binding
    End Sub

End Class</pre></div>

<p><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" src="\images\posts\15130\image_thumb_1.png" width="304" height="304" /></p>
