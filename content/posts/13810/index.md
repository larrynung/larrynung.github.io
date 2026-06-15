---
title: "[VB.NET]如何自製使用者控制項測試容器(User Control Test Container)"
date: "2010-02-27 11:22:26"
description: "[VB.NET]如何自製使用者控制項測試容器(User Control Test Container)"
tags: [VB.NET]
---

前一篇[Visual Studio]使用者控制項測試容器(User Control Test Container)介紹了User Control Test Container的使用方式。雖然User Control Test Container很好用，但美中不足的是一定要開啟Visual Studio才能叫用。因此這篇介紹一下如何自己來做這樣的功能。

要做類似User Control Test Container的程式，首先我們必須要會使用.NET中的反射技術。利用反射技術把載入的組件所內含的控制項類別名稱都加到下拉清單中。像下面這樣：

```vb
m_Assembly = Assembly.LoadFrom(assemblyFile)
Try
    cbxUserControl.BeginUpdate()
    cbxUserControl.Items.Clear()
    For Each t As Type In m_Assembly.GetTypes
        If t.IsSubclassOf(GetType(Control)) AndAlso Not t.IsAbstract AndAlso Not t.IsNested Then
            cbxUserControl.Items.Add(t)
        End If
    Next
    If cbxUserControl.Items.Count > 0 Then
        cbxUserControl.SelectedIndex = 0
    End If
Finally
    cbxUserControl.EndUpdate()
End Try
```

再來就是要在選取好控制項後，利用反射技術把控制項物件給建立起來，動態的嵌到預覽區，並把物件設定到PropertyGrid。像下面這樣：

```vb
Private Sub SetPreviewControl()
    If cbxUserControl.SelectedItem IsNot Nothing Then
        SetPreviewControl(m_Assembly.CreateInstance(cbxUserControl.Text))
    End If
End Sub

Private Sub SetPreviewControl(ByVal c As Control)
    With pnlControlContainer.Controls
        .Clear()
        .Add(c)
    End With
    Me.PropertyGrid1.SelectedObject = c
End Sub
```

如此簡易的User Control Test Container就完成了。

這邊附上我寫好的範例程式，主要介面仿照User Test Container。除提供User Test Container的功能外，另加上語系切換，與預覽表單的功能。程式介面外觀如下：

![image_thumb.png](/images/posts/13810/image_thumb.png)

## Download

[User Control Test Container.zip](http://Files.Dotblogs.com.tw/larrynung/1002/2010227232727262.zip)
