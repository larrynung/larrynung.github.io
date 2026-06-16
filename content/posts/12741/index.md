---
title: "[Performance]Set Form's Position"
date: "2009-12-30 10:56:13"
description: "今天看網路文章時，注意到指定表單位置的方法。一般來說我們碰到這個問題，可以直接建立一個Point，並指派給Form.Location。或是直接指派Form.Top與Form.Left兩個表單屬性。很無聊的我又測了一下兩者的效能差異。"
tags: [Performance]
---

今天看網路文章時，注意到指定表單位置的方法。一般來說我們碰到這個問題，可以直接建立一個Point，並指派給Form.Location。或是直接指派Form.Top與Form.Left兩個表單屬性。很無聊的我又測了一下兩者的效能差異。

測試UI如下：

![image_thumb.png](/images/posts/12741/image_thumb.png)

測試程式碼如下：

```vb
Public Class Form1

    Dim _f As New Form
    Private Sub btnSetByPoint_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSetByPoint.Click
        _f.Show()
        Dim sw As Stopwatch = Stopwatch.StartNew
        For i As Integer = 0 To NumericUpDown1.Value
            _f.Location = New Point(10, 10)
        Next
        sw.Stop()
        _f.Hide()
        MsgBox("SetByPoint: " & sw.ElapsedMilliseconds.ToString)
    End Sub

    Private Sub btnSetByProperty_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSetByProperty.Click
        _f.Show()
        Dim sw As Stopwatch = Stopwatch.StartNew
        For i As Integer = 0 To NumericUpDown1.Value
            _f.Top = 10
            _f.Left = 10
        Next
        sw.Stop()
        _f.Hide()
        MsgBox("SetByProperty: " & sw.ElapsedMilliseconds.ToString)
    End Sub

End Class
```

測試結果如下：

當測試次數為10000時

![image_thumb_10.png](/images/posts/12741/image_thumb_10.png) ![image_thumb_11.png](/images/posts/12741/image_thumb_11.png)

當測試次數為100000時

![image_thumb_14.png](/images/posts/12741/image_thumb_14.png) ![image_thumb_13.png](/images/posts/12741/image_thumb_13.png)

當測試次數為1000000時

![image_thumb_15.png](/images/posts/12741/image_thumb_15.png) ![image_thumb_16.png](/images/posts/12741/image_thumb_16.png)

當測試次數為10000000時

![image_thumb_17.png](/images/posts/12741/image_thumb_17.png) ![image_thumb_18.png](/images/posts/12741/image_thumb_18.png)

統計一下測試結果

![image_thumb_1.png](/images/posts/12741/image_thumb_1.png)

依以上的測試，我們可以看到直接指定Location會比透過屬性設定表單位置來得有效率。
