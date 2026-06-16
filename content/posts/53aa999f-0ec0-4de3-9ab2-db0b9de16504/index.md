---
title: "[VB.NET]使用TabControlEx控制項快速抽換表單介面與實現精靈介面"
date: "2013-11-06 12:00:00"
description: "這篇要介紹的是如何抽換表單介面與實現精靈介面，順便介紹自己試寫的TabControlEx控制項，雖說是TabControl的加強版控制項，但其實也只比傳統的TabControl控制項多一個ShowPageOnly屬性。"
---

這篇要介紹的是如何抽換表單介面與實現精靈介面，順便介紹自己試寫的TabControlEx控制項，雖說是TabControl的加強版控制項，但其實也只比傳統的TabControl控制項多一個ShowPageOnly屬性。

## 抽換表單介面

舉個例子來說，假設今天需要撰寫個可以替換頁面的程式，當按下Button1時程式右側會切到對應畫面(如下圖)。

![image_thumb.png](/images/posts/53aa999f-0ec0-4de3-9ab2-db0b9de16504/image_thumb.png)

當按下Button2時則顯示另一個畫面。

![image_thumb_1.png](/images/posts/53aa999f-0ec0-4de3-9ab2-db0b9de16504/image_thumb_1.png)

在以往，這樣的程式是需要在程式內部存放各頁面物件的參考(可搭配使用使用者控制項)，並依使用者動作抽換頁面。這樣的方法不僅在設計介面無法所見即所得，撰寫上也十分的不便。

程式碼範例如下：

```
Dim tabs() As Control = New Control() {New DataGridView, New MonthCalendar}
Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
RemoveTabs()
tabs(0).Parent = Me.SplitContainer1.Panel2
End Sub

Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
RemoveTabs()
tabs(1).Parent = Me.SplitContainer1.Panel2
End Sub

Private Sub RemoveTabs()
For Each c As Control In tabs
c.Parent = Nothing
Next
End Sub
```

而若是使用TabControlEx的話，在設計上就跟使用一般的TabControl一樣。

![image_thumb_2.png](/images/posts/53aa999f-0ec0-4de3-9ab2-db0b9de16504/image_thumb_2.png)

表單設完後，變更ShowPageOnly屬性為True，TabControl上方的分頁標籤就會消失。

![image_thumb_3.png](/images/posts/53aa999f-0ec0-4de3-9ab2-db0b9de16504/image_thumb_3.png)

在表單切換上也是跟TabControl一樣，用SelectedIndex之類的屬性或方法就可以了。

```
Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
Me.TabControlEx1.SelectedIndex = 0
End Sub

Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
Me.TabControlEx1.SelectedIndex = 1
End Sub
```

TabControlEx實作的概念很簡單，其實只是把當前TabControl頁面上的控制項，全部移到蓋在TabControl上的Panel，達到無分頁標籤的假象而已。

## 精靈介面

了解了TabControlEx的新增的唯一功能後 ，有感覺的人應該可以想到其它的應用，在此順便介紹一種另外的應用。就是其實它也可以做到精靈介面，只需少少幾個步驟：

**Step1.在各分頁加入精靈介面的背景與元件**

![image_thumb.png](/images/posts/53aa999f-0ec0-4de3-9ab2-db0b9de16504/image_thumb.png)

![image_thumb_1.png](/images/posts/53aa999f-0ec0-4de3-9ab2-db0b9de16504/image_thumb_1.png)

**Step2.加上切換頁面的程式碼**

只需透過SelectedIndex之類的屬性或方法就可以了。

**Step3.把ShowPageOnly屬性設為False**

![image_thumb_3.png](/images/posts/53aa999f-0ec0-4de3-9ab2-db0b9de16504/image_thumb_3.png)

## 注意事項

雖然上述例子都是用屬性框直接把ShowPageOnly直接設為True，但在使用上建議在Form.Load事件用程式碼改屬性值，因為控制項仍有小Bug。

## Download

TabControlEx.zip
