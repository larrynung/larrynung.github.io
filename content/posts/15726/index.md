---
title: "[VB.NET]從剪貼簿貼上至TextBox時的注意事項"
date: "2010-06-08 10:29:01"
description: "撰寫從剪貼簿貼上的程式有兩種方式，一種是利用Clipboard.GetText去取得剪貼簿內的文字後，自行處理塞值的動作，像是下面這樣： 另一種則是透過SendKeys.Send模擬鍵盤按下Ctrl+V，像是下面這樣： 這兩種方式都可以達到從剪貼簿貼上的效果，"
tags: [VB.NET]
---

撰寫從剪貼簿貼上的程式有兩種方式，一種是利用Clipboard.GetText去取得剪貼簿內的文字後，自行處理塞值的動作，像是下面這樣：

```vb
TextBox1.Text = Clipboard.GetText
```

另一種則是透過SendKeys.Send模擬鍵盤按下Ctrl+V，像是下面這樣：

```vb
TextBox1.Clear()
TextBox1.Focus()
SendKeys.Send("^V")
```

這兩種方式都可以達到從剪貼簿貼上的效果，但是若程式中的TextBox有加設MaxLength的話，則建議採用SendKeys.Send的方法，因為若用Clipboard.GetText取得字串後自行塞入，貼上的字串長度是會可以超過MaxLength的設定的。MaxLength並沒有擋直接用程式塞字串的長度，只會檔住鍵盤直接Key In，或是貼上的字串。

這邊來看段範例，首先在Form.Load設定一下MaxLength長度為100，剪貼簿內的資料長度為200。

```vb
TextBox1.MaxLength = 100
Clipboard.SetText(New String("A"c, 200))
```

實際執行比較兩種方法，就可以看出這種現象。

![image_thumb_2.png](/images/posts/15726/image_thumb_2.png) ![image_thumb_3.png](/images/posts/15726/image_thumb_3.png)

若想用Clipboard.GetText塞值，就必須自行處理：

```vb
Dim msg As String = Clipboard.GetText
If msg.Length > TextBox1.MaxLength Then
    msg = msg.Substring(0, TextBox1.MaxLength)
End If
TextBox1.Text = msg
```
