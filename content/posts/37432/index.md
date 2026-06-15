---
title: "[Visual Studio]Visual Studio 2011 Preview New Feature - Find and Replace control improvements"
date: "2011-09-23 01:28:52"
description: "[Visual Studio]Visual Studio 2011 Preview New Feature - Find and Replace control improvements"
tags: [Visual Studio]
---

Visual Studio 2011 Preview在搜尋與取代功能上也做了些小小的改進，也是自Productivity Power Tools修改過來的功能。在Visual Studio 2011 Preview中按下『Ctrl + F』搜尋或是按下『CTRL + H』取代，即會發現現在的呈現方式已不如以往。以往會彈出搜尋/取代的對話框，現在則是在編輯區右上方以小框呈現，節少了顯示的空間在使用上卻更為便利。

![image_thumb.png](/images/posts/37432/image_thumb.png)

一般的搜尋只要透過在搜尋框中鍵入關鍵字按下『Enter』即可，要做不同方向的搜尋也可以，後方箭頭下拉後可以選取，或是直接透過『F3』或『Shift + F3』來決定搜尋的方向。

![image_thumb_2.png](/images/posts/37432/image_thumb_2.png)

按下『Shift + F3』往前搜尋時箭頭的方向會改變，可從箭頭知道是往前還往後搜尋。但這邊筆者覺得不習慣的是，當箭頭改變為向前時，若是改用『Enter』去繼續搜尋，竟然還是往後搜尋，有點令人混淆。

![image_thumb_3.png](/images/posts/37432/image_thumb_3.png)

用關鍵字下去搜尋不到內容時，搜尋框會變紅色的邊框，用以提示該關鍵字無法搜尋到東西。

![image_thumb_1.png](/images/posts/37432/image_thumb_1.png)

在搜尋途中若是有看到更適合的關鍵字，想切換關鍵字下去搜尋時，透過『Ctrl + F3』可以快速的幫您完成這樣的動作。像是下面我本來用sql當關鍵字搜尋，搜尋的途中覺得搜尋出來的資料太多，我比較關注的應該是m_MySelConn的話，可用滑鼠在m_MySelConn上連點選取，並按下『Ctrl + F3』熱鍵。

![image_thumb_8.png](/images/posts/37432/image_thumb_8.png)

Visual Studio會幫我們替換關鍵字，改用新選取的字串當作關鍵字下去做搜尋的動作。

![image_thumb_9.png](/images/posts/37432/image_thumb_9.png)

若搜尋時想要直接套用之前搜尋過的關鍵字，或做些搜尋時細部的調整，像是要使用正規表示式、比對時大小寫要一樣等等，可用滑鼠點選搜尋框後方的下拉圖示，或是當焦點停留在搜尋框時透過熱鍵『Alt + Down』觸發下拉清單調整(做取代時亦同)。

![image_thumb_4.png](/images/posts/37432/image_thumb_4.png)

也可以在點選『Find In Files...』連結，改叫出原先我們熟悉的對話框來做搜尋。

![image_thumb_5.png](/images/posts/37432/image_thumb_5.png)

取代的動作操作也類似，可透過搜尋框左上方的摺疊圖式切換，或是按下『Ctrl + H』叫出，使用上大同小異，這邊稍稍帶出不做贅述。

![image_thumb_6.png](/images/posts/37432/image_thumb_6.png)

## Link

* [Visual Studio 11 Developer Preview: Find & Replace](http://blogs.msdn.com/b/visualstudio/archive/2011/09/22/find-amp-replace-in-visual-studio-11-developer-preview.aspx)
