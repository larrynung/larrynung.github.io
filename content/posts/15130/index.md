---
title: "[VB.NET]將集合類別繫結至DataGridView並使其具備新增功能"
date: "2010-05-10 10:55:23"
description: "若直接把集合類別繫結至DataGridView。 就算DataGridView有設定AllowUserToAddRows，DataGridView也是無法做新增的動作。"
tags: [VB.NET]
---

若直接把集合類別繫結至DataGridView。

```vb
Public Class Form1

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
End Class
```

就算DataGridView有設定AllowUserToAddRows，DataGridView也是無法做新增的動作。

![image_thumb.png](/images/posts/15130/image_thumb.png)

要解決這樣的問題，可以把集合類別設至BindingSource，把AllowNew屬性設起來，再把BindingSource給繫到DataGridView就可以了。

```vb
Public Class Form1

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        Dim lst As New List(Of Person)
        lst.Add(New Person With {.Name = "Larry"})
        Dim binding As New BindingSource
        binding.DataSource = lst
        binding.AllowNew = True
        DataGridView1.DataSource = Binding
    End Sub

End Class
```

![image_thumb_1.png](/images/posts/15130/image_thumb_1.png)
