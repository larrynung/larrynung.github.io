---
title: "[VB.NET]Notes on String Handling for Enum Types"
slug: "vbnet-notes-on-string-handling-for-enum-types"
aliases: ["/posts/10348/"]
date: "2009-09-01 09:00:33"
description: "不知道大家是否有發現，列舉型別在做字串處理時，會因寫法不同而有所差異。 舉個例子來看，假設我們寫了一個SexType的列舉 並做了如下的字串處理： 後面未加ToString()的在編譯後會先被轉型成Int後才轉型為String。"
tags: [VB.NET]
---

不知道大家是否有發現，列舉型別在做字串處理時，會因寫法不同而有所差異。

舉個例子來看，假設我們寫了一個SexType的列舉

```vb
Enum SexType As Integer
     Boy
     Girl
 End Enum
```

並做了如下的字串處理：

```vb
Dim sex As SexType = SexType.Boy
Console.WriteLine("Sex: " & sex.ToString & " (" & sex & ")")
```

後面未加ToString()的在編譯後會先被轉型成Int後才轉型為String。![image_thumb_2.png](/images/posts/10348/image_thumb_2.png)

運行結果
![image_thumb_1.png](/images/posts/10348/image_thumb_1.png)

若換個寫法

```vb
Dim sex As SexType = SexType.Boy
Console.WriteLine(String.Format("Sex: {0} ({1})", sex, CInt(sex)))
```

運行後結果跟上面的一樣，因此我們可發現透過String.Format來處理，列舉型別就不會先轉為int再轉為String。

再做個實驗看看，當我們把列舉值直接秀出

```vb
Dim sex As SexType = SexType.Boy
Console.WriteLine(sex)
```

編譯後程式還是會先被轉換成Int
![image_thumb_4.png](/images/posts/10348/image_thumb_4.png)

運行結果
![image_thumb_3.png](/images/posts/10348/image_thumb_3.png)

若是先把列舉值塞到Object型別再顯示

```vb
Dim sex As SexType = SexType.Boy
Dim sexObj As Object = sex
Console.WriteLine(sexObj)
```

運行結果
![image_thumb_5.png](/images/posts/10348/image_thumb_5.png)

由以上實驗可以看出，當把列舉值直接當字串顯示時，會先轉成Int後再顯示。但當把列舉值塞到Object顯示，則會直接顯示而不會先轉成Int。

完整範例

```vb
Module Module1
    Enum SexType As Integer
        Boy
        Girl
    End Enum

    Sub Main()
        Dim msg As String
        Dim sex As SexType = SexType.Boy
        msg = "Sex: " & sex.ToString & " (" & sex & ")"
        Console.WriteLine(msg)

        msg = String.Format("Sex: {0} ({1})", sex, CInt(sex))
        Console.WriteLine(msg)
    End Sub
End Module
```

執行結果
![image_thumb.png](/images/posts/10348/image_thumb.png)
