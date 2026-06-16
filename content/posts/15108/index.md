---
title: "[VB.NET]Fix the MDI Child Form List Not Updating in Real Time"
slug: "vbnet-fix-the-mdi-child-form-list-not-updating-in-real-time"
aliases: ["/posts/15108/"]
date: "2010-05-09 11:09:12"
description: "在做MDI程式時，若有使用到MDI子表單清單的功能，需特別留意當子表單標題被更動時，MDI子表單清單不會即時的更新。 而是要將子視窗切換該子表單清單才會更新。 若要修正這個問題，可在WindowsMenu.DropDownOpening事件，呼叫ActivateMdiChild保護方法，"
tags: [VB.NET]
---

在做MDI程式時，若有使用到MDI子表單清單的功能，需特別留意當子表單標題被更動時，MDI子表單清單不會即時的更新。

![image_thumb.png](/images/posts/15108/image_thumb.png)

![image_thumb_1.png](/images/posts/15108/image_thumb_1.png)

而是要將子視窗切換該子表單清單才會更新。

![image_thumb_3.png](/images/posts/15108/image_thumb_3.png)

若要修正這個問題，可在WindowsMenu.DropDownOpening事件，呼叫ActivateMdiChild保護方法，像是下面這樣：

```vb
Private Sub WindowsMenu_DropDownOpening(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles WindowsMenu.DropDownOpening
    Dim childForm As Form = ActiveMdiChild
    ActivateMdiChild(Nothing)
    ActivateMdiChild(childForm )
End Sub
```
