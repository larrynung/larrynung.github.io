---
title: "[VB.NET]處理MDI子視窗清單中的殘留分隔線"
date: "2010-04-23 10:10:45"
description: "在撰寫MDI視窗程式時，要讓程式在某個選單選項上，下拉時顯示所有開起的子視窗清單，我們可以在選單控制項上設定MdiWindowListItem屬性，把該屬性指到要顯示子視窗清單的選單選項。 設完後會發現基本上已達到了顯示子視窗清單的需求，只是美中不足的在運作上會有個小瑕疵。讓我們來看一下。"
tags: [VB.NET]
---

在撰寫MDI視窗程式時，要讓程式在某個選單選項上，下拉時顯示所有開起的子視窗清單，我們可以在選單控制項上設定MdiWindowListItem屬性，把該屬性指到要顯示子視窗清單的選單選項。

![image_thumb.png](/images/posts/14779/image_thumb.png)

設完後會發現基本上已達到了顯示子視窗清單的需求，只是美中不足的在運作上會有個小瑕疵。讓我們來看一下。

這邊使用Visual Studio內建的MDI Parent樣版視窗來示範，首先打開選單選項，會看到如下圖示，由於尚未開起任何子表單，故只有基本的視窗控制功能，未含任何子視窗清單。

![image_thumb_1.png](/images/posts/14779/image_thumb_1.png)

當開啟了子視窗後，子視窗清單會接續在剛打開的打開選單選項後面。

![image_thumb_2.png](/images/posts/14779/image_thumb_2.png)

接著把所有子視窗關閉，小瑕疵就跑出來了，不知道怎摸回事，該消失不見的分隔線竟然還在。

![image_thumb_3.png](/images/posts/14779/image_thumb_3.png)

這個小瑕疵我們可以透過處理該選單選項的DropDownOpening事件，判斷最後一個選項是否是分隔線，是的話則移除，程式代碼如下：

```vb
Private Sub WindowsMenu_DropDownOpening(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles WindowsMenu.DropDownOpening
    Dim menuItem As ToolStripMenuItem = DirectCast(sender, ToolStripMenuItem)
    Dim childItems As ToolStripItemCollection = menuItem.DropDownItems
    Dim lastChildItem As ToolStripItem = childItems(childItems.Count - 1)
    If TypeOf lastChildItem Is ToolStripSeparator Then
        childItems.Remove(lastChildItem)
    End If
End Sub
```
