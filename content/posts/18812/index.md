---
title: "[VB.NET]用Extension Method移除控制項"
date: "2010-11-05 12:50:17"
description: "今天在撰寫程式時想把某個控制項移除，移了半天都沒效果，仔細查看了一下，原來是我的控制項並不在我以為的元件上面，但又懶的去找尋控制項所在的元件，故改用Control.Parent去找尋父元件來做移除，這邊將其整理為擴充方法： 使用上直接呼叫Control.Remove()就可以了。"
tags: [VB.NET]
---

今天在撰寫程式時想把某個控制項移除，移了半天都沒效果，仔細查看了一下，原來是我的控制項並不在我以為的元件上面，但又懶的去找尋控制項所在的元件，故改用Control.Parent去找尋父元件來做移除，這邊將其整理為擴充方法：

```vb
Imports System.Runtime.CompilerServices
Imports System.Windows.Forms

Public Module ControlExtension

#Region "Public Method"
    <Extension()> _
    Public Sub Remove(ByVal ctrl As Control)
        Dim parent As Control = ctrl.Parent
        If parent Is Nothing Then
            Return
        End If
        parent.Controls.Remove(ctrl)
    End Sub
#End Region

End Module
```

使用上直接呼叫Control.Remove()就可以了。
