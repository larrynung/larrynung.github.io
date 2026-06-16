---
title: "[Performance][VB.NET]If V.S IIf"
date: "2009-03-10 09:00:26"
description: "前陣子去書局翻書，看到一本寫的不錯的VB.NET入門書，很適合初學者學習使用，作者是施威明工作室。稍微翻了一下，雖是簡單的入門書，但書中仍是有些我沒注意到的東西，像是這篇提到的If函式。開始用VB.NET到現在也已經一年多了，一直以為If就只能當陳述式用，看了書上描述才知道原來也有類似IIf的用法。"
tags: [VB.NET,Performance]
---

前陣子去書局翻書，看到一本寫的不錯的VB.NET入門書，很適合初學者學習使用，作者是施威明工作室。稍微翻了一下，雖是簡單的入門書，但書中仍是有些我沒注意到的東西，像是這篇提到的If函式。開始用VB.NET到現在也已經一年多了，一直以為If就只能當陳述式用，看了書上描述才知道原來也有類似IIf的用法。

但若是If跟IIf功用完全一樣的話，又為何要有兩道函式呢？書上做了些許的描述，主要的差異是If的效率會比IIf好，也就是會比較快。

其用法與說明簡列如下：

<table border="0" cellpadding="2" cellspacing="0" width="852"><tbody> <tr> <td valign="top" width="394"><img alt="image" border="0" height="60" src="/images/posts/7424/image_thumb_4.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="518"/> <a href="http://files.dotblogs.com.tw/larrynung/0903/VB.NETIfV.SIIF_12A5D/image_2.png"><img alt="image" border="0" height="60" src="/images/posts/7424/image_thumb.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="389"/></a></td> <td valign="top" width="456"><a href="http://files.dotblogs.com.tw/larrynung/0903/VB.NETIfV.SIIF_12A5D/image_4.png"><img alt="image" border="0" height="50" src="/images/posts/7424/image_thumb_1.png" style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" width="450"/></a></td> </tr> </tbody></table>

基本上If三個參數的多載函式用法幾乎跟IIf一樣，硬要說有啥不同的話，大概只有兩點，第一點差異就是If的後兩個參數需能互相擴展轉換(也許說成相同型態會更為恰當，這邊採用Visual Studio說明的說法)，所以像下圖的寫法就會跑出錯誤。

![image_thumb_5.png](/images/posts/7424/image_thumb_5.png)

而IIf無此限制，因此像下圖這樣寫法就無錯誤出現。

![image_thumb_6.png](/images/posts/7424/image_thumb_6.png)

第二點差異就是If前面需有變數去接收函式回傳值，若前面無變數去接收回傳值，Visual Studio會將它視為是If陳述式，因此會出現如下錯誤：

![image_thumb_7.png](/images/posts/7424/image_thumb_7.png)

同樣的IIf無此限制，因此不會出現錯誤，最多只能算是沒啥意義的寫法。

![image_thumb_9.png](/images/posts/7424/image_thumb_9.png)

接著我們順便來看一下If兩個參數的多載函式的用法，簡單來說該函式的用法就是當第一個參數不為Nothing，該函式的回傳值就為第一個參數，反之若第一個參數為Nothing，該函式的回傳值就為第二個參數。看個簡單的範例，假設今天我們宣告了一個TextBox如下：

```
Dim tbx As TextBox = Nothing
```

若是這樣宣告，則當我們要使用該TextBox時會需要去判斷TextBox是否是Nothing，若是，我們會去New出TextBox物件，我們寫的Code可能會長的像下面這樣：

```
If tbx Is Nothing Then tbx = New TextBox
```

若此時運用If函式的話，寫法大概如下：

```
tbx = If(tbx, New TextBox)
```

了解了用法以後，我們當然不能錯過比較兩者之間速度上的差異，畢竟這是兩者最大的不同點。為了測試我們撰寫如下的測試程式：

```
Private Sub TestIfAndIIf(ByVal loopCount As Integer)
    Dim sw As New Stopwatch
    Dim o As Object

    Console.WriteLine("Test If")
    sw.Start()
    For i As Integer = 1 To loopCount
        o = If(True, True, False)
    Next
    Console.WriteLine("花費時間: " & sw.ElapsedMilliseconds)
    sw.Reset()

    Console.WriteLine("Test IIf")
    sw.Start()
    For i As Integer = 1 To loopCount
        o = IIf(True, True, False)
    Next
    Console.WriteLine("花費時間: " & sw.ElapsedMilliseconds)
End Sub
```

測試結果如下：

<table border="1" cellpadding="2" cellspacing="0" width="400"><tbody>
<tr>
<td valign="top" width="133">loopCount</td>
<td valign="top" width="133">If</td>
<td valign="top" width="133">IIf</td>
</tr>
<tr>
<td valign="top" width="133">10000</td>
<td valign="top" width="133">0 ms</td>
<td valign="top" width="133">0 ms</td>
</tr>
<tr>
<td valign="top" width="133">100000</td>
<td valign="top" width="133">1 ms</td>
<td valign="top" width="133">3 ms</td>
</tr>
<tr>
<td valign="top" width="133">1000000</td>
<td valign="top" width="133">10 ms</td>
<td valign="top" width="133">32 ms</td>
</tr>
<tr>
<td valign="top" width="133">10000000</td>
<td valign="top" width="133">101 ms</td>
<td valign="top" width="133">326 ms</td>
</tr>
</tbody></table>

統計一下測試數據

![image_thumb.png](/images/posts/7424/image_thumb.png)

可以清楚的看出兩者間速度的比約為 1:3，不過這是當使用很多次的情況之下，在使用次數小於100000次的情況下，其間速度的差異幾乎可忽略不計。
