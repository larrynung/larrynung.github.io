---
title: "[VB.NET]實做Spy++的拖曳箭靶"
date: "2010-04-22 12:32:19"
description: "[VB.NET]實做Spy++的拖曳箭靶"
tags: [VB.NET]
---

相信有做過開發的大家，對於Spy++這套軟體一定都不陌生，應該也都知道在Spy++中有個可以拖曳的箭靶，透過這個可拖曳的箭靶，使用者可以很快速的指定要監看的視窗。今天這篇就是稍微紀錄一下如何實作這個拖曳箭靶。

![image_thumb.png](/images/posts/14736/image_thumb.png)

實作的概念很簡單，只要準備兩張圖片、一張滑鼠游標。兩張圖片分別為：

<table border="1" cellpadding="2" cellspacing="0" width="459"><tbody> <tr> <td valign="top" width="44"><a href="http://files.dotblogs.com.tw/larrynung/1004/VB.NETSpy_14E47/image_6.png"><img alt="image" border="0" height="32" src="/images/posts/14736/image_thumb_2.png" style="border-right-width: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" title="image" width="35"/></a> </td> <td valign="top" width="413">含箭靶的視窗圖示，用來顯示箭靶尚未被拖曳的狀態。</td> </tr> <tr> <td valign="top" width="44"><a href="http://files.dotblogs.com.tw/larrynung/1004/VB.NETSpy_14E47/image_8.png"><img alt="image" border="0" height="32" src="/images/posts/14736/image_thumb_3.png" style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" width="35"/></a> </td> <td valign="top" width="413">不含箭靶的視窗圖示，用來顯示箭靶已被拖曳出的狀態。</td> </tr> </tbody></table>

滑鼠游標則是準備一個像箭靶的游標。

![image_thumb_4.png](/images/posts/14736/image_thumb_4.png)

接著在滑鼠按下時把圖片換為不含箭靶的視窗圖示，並將滑鼠游標替換成箭靶的樣子。而當滑鼠釋放時，再把圖片換回含箭靶的視窗圖示，Spy++的拖曳箭靶就完成了。

在實作上我們可以在開個使用者控制項專案，加入準備好的兩張圖片至資源中。

![image_thumb_7.png](/images/posts/14736/image_thumb_7.png)

再來把準備好的滑鼠游標加入至專案中。

![image_thumb_6.png](/images/posts/14736/image_thumb_6.png)

接著在使用者控制項上放個PictureBox，載入含有箭靶的視窗圖示。設定PictureBox的SizeMode屬性為AutoSize，UserControl的AutoSize屬性為True。

![image_thumb_5.png](/images/posts/14736/image_thumb_5.png)

在PictureBox.MouseDown事件中，把圖片替換為不含箭靶的視窗圖示，並替換當前游標。

```vb
PictureBox1.Image = My.Resources.SPYXX1
Cursor.Current = New Cursor(Me.GetType, "arrow.cur")
```

在PictureBox.MouseUp事件中，把圖片再替換回含箭靶的視窗圖示。

```vb
PictureBox1.Image = My.Resources.SPYXX
```

將該控制項放置表單，即可看到如下運行效果：

![image_thumb_8.png](/images/posts/14736/image_thumb_8.png)

![image_thumb_9.png](/images/posts/14736/image_thumb_9.png)
