---
title: "[Visual Studio]Visual Studio 2010 Pro Power Tools"
date: "2010-06-14 12:21:58"
description: "[Visual Studio]Visual Studio 2010 Pro Power Tools"
tags: [Visual Studio]
---

Visual Studio 2010 Pro Power Tools在2010年6月釋出，該擴充元件提供許多好用的功能，改善許多在Visual Studio 2010令人不便的設計，可加速程式員在Visual Studio 2010中的開發。

![image_thumb_1.png](/images/posts/15862/image_thumb_1.png)

## Visual Studio 2010 Pro Power Tools

欲安裝Visual Studio 2010 Pro Power Tools，我們可以透過工具列上的Extension Manager按鈕。

![image_thumb_2.png](/images/posts/15862/image_thumb_2.png)

或是透過[Tools]→[Extension Manager…]選單選項叫起Extension Manager對話框。

![image_thumb_3.png](/images/posts/15862/image_thumb_3.png)

在Extension Manager對話框中，選取OnLine Gallery，在右上搜尋框輸入Power關鍵字，點選Visual Studio 2010 Pro Power Tools安裝。

![image_thumb.png](/images/posts/15862/image_thumb.png)

安裝完後重新啟動，即可啟用該擴充套件的功能，下面就讓我們來看一下該擴充套件的功能。

### Fix Mixed Tabs

Fix Mixed Tabs功能可以自動判別程式中的縮排使用的是Tab還是Space，會在上方導覽列的下方出現修正的提示。

![image_thumb_5.png](/images/posts/15862/image_thumb_5.png)

### Extension Update

Extension Update功能會自動在啟動時偵測是否已安裝的擴充元件有新的更新檔，若發現新的更新，系統會在右下彈出氣泡對話框提示。

![image_thumb_7.png](/images/posts/15862/image_thumb_7.png)

### Add Reference Dialog

Add Reference對話框在安裝完該擴充套件後，使用上整個介面會被替換，新的Add Reference對話框提供了搜尋與排序的功能，讓加入組件參考更為快速方便。不過美中不足的是，這部份的修改把VS 2010的修改給換掉了，開啟速度上會比VS 2010還要慢。

![image_thumb_4.png](/images/posts/15862/image_thumb_4.png)

### Highlight Current Line

在以往使用Visual Studio，若是在非選取程式碼的狀態，常常會找不太到目前的游標位置。此時多半會上下左右移動看看游標，以找尋到游標所在位置。在安裝了該擴充套件後，在非選取程式碼的狀態下，當前游標位置所在的那行會被標示出來，減少不必要的時間浪費。

![image_thumb_6.png](/images/posts/15862/image_thumb_6.png)

### Triple Click

若要選取整行程式，在以往我們需要用滑鼠拖曳選取。現在透過該擴充套件的輔助，我們只需在該行上點選三次即可輕鬆選取整行程式。

### Document Tab Well

Document Tab Well功能是針對Tab分頁所做的改進，使用上可在Tab分頁旁的空白區域按下滑鼠右鍵，點選[Customize…]。

![image21_thumb.png](/images/posts/15862/image21_thumb.png)

或是透過 [Tools]->[Options]開啟Options對話框，選取[Environment]->[Document Tab Well]切換至Tab設定頁面。

![image24_thumb.png](/images/posts/15862/image24_thumb.png)

在Tab設定頁面中提供許多設定，像是上方Preset可以選取一些現有的設定值，可直接設定VS2008、VS2010等樣式。下方則是可設定捲軸、垂直Tab頁面、顯示關閉按鈕、Tab頁面的排序、是否顯示Icon、與設定Tab顏色等等。

大部分的設定都很簡單，玩玩就會了，比較複雜一點的是Tab變色功能，這邊簡單示範一下。首先視需求設定Color tabs by project與Color tabs by regular expressions。

![image51_thumb.png](/images/posts/15862/image51_thumb.png)

在切至Document Tab Well下方的Color Coding節點，設定對應的顏色即可。值得注意的是，這邊的顏色是依專案或是RegEx來區別的，不同的專案檔案可給予不同的顏色，甚至可依照Regex的比對給予顏色。

![image48_thumb.png](/images/posts/15862/image48_thumb.png)

![image54_thumb.png](/images/posts/15862/image54_thumb.png)

### Ctrl + Click Go To Definition

Ctrl + Click Go To Definition功能提供快速移至定義的方法，在以往我們要移至定義，可透過滑鼠右鍵點選Go To Definition，或是透過按下F12按鈕直接移至定義。而Ctrl + Click Go To Definition功能允許我們透過按住Ctrl按鈕，並點選滑鼠左鍵快速的移至定義。

### Align Assignments

Align Assignments功能提供我們把程式中塞值的部分排的比較整齊，只要按下Ctrl+Alt+]，本來凌亂的程式就會被排列整齊。

![image27_thumb.png](/images/posts/15862/image27_thumb.png)![image30_thumb.png](/images/posts/15862/image30_thumb.png)

值得注意的是，該功能會跟Ignore spaces in declaration statements功能互衝，因此在使用上必須點選[Tools]->[Options]開啟Options對話框，點選[Text Editor]->[C#]->[Formatting]->[Spacing]，取消勾選Ignore spaces in declaration statements功能。

![image33_thumb.png](/images/posts/15862/image33_thumb.png)

### Move Line Up/Down Commands

以往要複製搬動程式碼位置，通常我們必須選取後按住滑鼠左鍵拖曳至所要放置的位置，或是透過減下貼上，若使用該擴充套件的Move Line Up/Downe功能，我們只需要按住Alt按鍵，並按下上或下按鍵把程式搬移。該功能支援多行與單行程式的搬移，單行程式可不用選取，多行程式則必須先行選取。

![image60_thumb.png](/images/posts/15862/image60_thumb.png)

![image63_thumb.png](/images/posts/15862/image63_thumb.png)

### Alignment Helpers

以往在瀏覽程式時，若程式碼很多，順著開下來常常頭昏眼花，看到後來不集中精神都分不出哪個在區塊內。Alignment Helpers的出現解決了這樣的問題，該功能提供程式碼瀏覽上的視覺輔助線，讓瀏覽程式變得較不費力。

使用上只要在要加入視覺輔助線的位置，按下滑鼠右鍵，點選Add guideline選項。

![image_thumb_12.png](/images/posts/15862/image_thumb_12.png)

視覺輔助線就會出現在指定的位置。

![image_thumb_13.png](/images/posts/15862/image_thumb_13.png)

若要移除視覺輔助線，一樣的我們必須把游標移至視覺輔助線所在的位置，按下滑鼠右鍵，點選Remove guideline選項，視覺輔助線就會被移除。

![image_thumb_14.png](/images/posts/15862/image_thumb_14.png)

### Colorized Parameter Help

Colorized Parameter Help功能改進了Visual Studio 2010的參數提示框，參數提示框會從黑白的變為彩色的，在瀏覽上會更為清楚。

![image_thumb_15.png](/images/posts/15862/image_thumb_15.png)

## Link

* [Visual Studio 2010 Pro Power Tools](http://charlesbc.blogspot.com/2010/06/visual-studio-2010-pro-power-tools.html)
* [Announcing: VS2010 Productivity Power Tools and Modeling Feature Packs](http://blogs.msdn.com/b/jasonz/)
* [Visual Studio 2010 Pro Power Tools Released Today](http://blogs.msdn.com/b/lisa/archive/2010/06/08/visual-studio-2010-pro-power-tools-released-today.aspx)
