---
title: "[Visual Studio]Visual Studio 2011 Preview File preview's Issue"
date: "2013-11-06 12:00:00"
description: "[Visual Studio]Visual Studio 2011 Preview File preview's Issue"
---

Visual Studio 2011 Preview自釋出用到現在，感覺上大致都滿穩定的除了幾個地方用起來有點怪怪的，像是File Preview功能就有點小Issue，這邊將之整理一下，方便後續回報給微軟。

File Preview的問題主要是出在於當視窗開啟過多時，有些視窗頁籤會被Visual Studio隱藏，這時File Preview功能會記錄到錯誤的視窗狀態，導致運作上會有些異常。

這邊實際示範一次整個問題的重現步驟，首先開啟個專案檔，為其加入多個程式檔案，接著將程式編輯視窗開啟多個，讓視窗頁籤多到會被Visual Studio隱藏。然後在方案總管中點擊個未開啟過的程式檔，讓File Preview功能將該程式檔預覽出來。

![image_thumb.png](/images/posts/2605c43b-fd1e-4084-ad55-0b95710c5716/image_thumb.png)

File Preview預覽視窗出來後，點擊上方的[Promote]按鈕將預覽的程式編輯視窗開出。

![image_thumb_1.png](/images/posts/2605c43b-fd1e-4084-ad55-0b95710c5716/image_thumb_1.png)

透過這樣的步驟開啟的程式視窗就會有錯亂的現象，為了方便觀察這樣的現象，這邊將它釘選起來。

![image_thumb_2.png](/images/posts/2605c43b-fd1e-4084-ad55-0b95710c5716/image_thumb_2.png)

然後隨便點選其它已開啟的視窗，會發現剛剛透過File Preview開啟的視窗會消失，只有在取得焦點時會正確的顯示。

![image_thumb_3.png](/images/posts/2605c43b-fd1e-4084-ad55-0b95710c5716/image_thumb_3.png)

若還是察覺不出來怪怪的，也可以將其它多餘的視窗先關閉，只保留透過File Preview所開啟的視窗。

![image_thumb_4.png](/images/posts/2605c43b-fd1e-4084-ad55-0b95710c5716/image_thumb_4.png)

然後再隨便開啟一個程式視窗看看，你會發現就算視窗沒有多到要隱藏，透過File Preview功能所開啟的視窗還是隱藏起來了。

![image_thumb_5.png](/images/posts/2605c43b-fd1e-4084-ad55-0b95710c5716/image_thumb_5.png)
