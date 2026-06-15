---
title: "[VB.NET]ErrorProvider"
date: "2009-06-15 11:12:09"
description: "[VB.NET]ErrorProvider"
tags: [VB.NET]
---

## Introduction

ErrorProvider為Visual Studio所內建的控制項，主要功能是用以顯示錯誤訊息，提示錯誤發生。

## 重要成員

**屬性**

![image_thumb.png](/images/posts/8828/image_thumb.png)

**方法**

![image_thumb_1.png](/images/posts/8828/image_thumb_1.png)

其中BlinkStyle所用到的ErrorBlinkStyle列舉型別如下：

![image_thumb_2.png](/images/posts/8828/image_thumb_2.png)

## 使用ErrorProvider

ErrorProvider是個很簡單的控制項，基本上只需要了解SetError的用法即可。

讓我們先看一下MSDN的用法

![image_thumb_3.png](/images/posts/8828/image_thumb_3.png)

![image_thumb_4.png](/images/posts/8828/image_thumb_4.png)

MSDN上已把用法寫的很明顯了，就是傳入兩個參數，一個是有錯誤的控制項、一個就是錯誤的描述字串，在此就不再贅述。讓我們直接來看範例。

假設今天我要做一個只能輸入數字的介面

![image_thumb_5.png](/images/posts/8828/image_thumb_5.png)

當使用者輸入的值不為數字時，介面將提示使用者鍵入數字。

![image_thumb_7.png](/images/posts/8828/image_thumb_7.png)

在程式編寫時只需在Validated事件內用ErrorProvider.SetError設定錯誤訊息即可。

```
Public Class Form1

    Private Sub TextBox1_Validated(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox3.Validated, TextBox2.Validated, TextBox1.Validated
        Dim ctrl As Control = DirectCast(sender, Control)
        ErrorProvider1.SetError(ctrl, If(IsNumeric(ctrl.Text), "", "此欄位只接受數字"))
    End Sub
End Class
```

程式流程如下：

![image_thumb_8.png](/images/posts/8828/image_thumb_8.png)

## ErrorProvider的運用

除了上面介紹的正規使用方式外。有時我們在撰寫介面時，我們會希望當介面上的資料有任意錯誤發生，則不讓使用者關閉、或是彈出確認視窗。通常一般的作法可能會透過Flag另外去記錄資訊，藉此判別是否有錯誤的資料。其實透過ErrorProvider我們可以很容易很方便的達到這需求。

程式碼如下：

```
Public Class Form1

    Private Sub TextBox1_Validated(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox3.Validated, TextBox2.Validated, TextBox1.Validated
        Dim ctrl As Control = DirectCast(sender, Control)
        ErrorProvider1.SetError(ctrl, If(IsNumeric(ctrl.Text), "", "此欄位只接受數字"))
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        If IsError() Then
            If MsgBox("部分設定有誤") = MsgBoxResult.Ok Then
                Return
            End If
        End If
        Me.Close()
    End Sub

    Private Function IsError() As Boolean
        For Each ctrl As Control In Controls
            If ErrorProvider1.GetError(ctrl).Length > 0 Then
                Return True
            End If
        Next
        Return False
    End Function
End Class
```

執行畫面

![image_thumb_10.png](/images/posts/8828/image_thumb_10.png)
