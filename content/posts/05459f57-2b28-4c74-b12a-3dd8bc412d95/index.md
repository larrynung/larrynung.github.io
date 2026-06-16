---
title: "[網樂通改機]讓網樂通突破限制，使用256MB的記憶體"
date: "2013-11-06 12:00:00"
description: "網樂通內建256MB的記憶體，但是預設只用了128MB。要突破這個限制，我們必需下載uboot再次刷機更新。 這邊可至sh4twbox下載uboot。 再下載Win32 disk imager將uboot寫到USB碟。"
---

網樂通內建256MB的記憶體，但是預設只用了128MB。要突破這個限制，我們必需下載uboot再次刷機更新。

這邊可至sh4twbox下載uboot。

![image_thumb.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image_thumb.png)

![image3_thumb.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image3_thumb.png)

再下載Win32 disk imager將uboot寫到USB碟。需將下載的uboot先行解開，解開後會看到附檔名為dd的檔，這檔案需透過[Win32 disk imager將它寫到usb中。](http://sourceforge.net/projects/win32diskimager/)

![image6_thumb.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image6_thumb.png)

要寫入時記得Select a disk image對話框的副檔名需選*.*，這樣才看的到我們欲寫的資料。

![image9_thumb.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image9_thumb.png)

選取好後按下write進行寫入。

![image18_thumb.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image18_thumb.png)

![image12_thumb.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image12_thumb.png)

![image15_thumb.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image15_thumb.png)

![image21_thumb.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image21_thumb.png)

寫入後usb會無法透過windows進行瀏覽，甚至是會提示要格式化磁碟機，這是正常的現象，忽略它就好。

![image_thumb_9.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image_thumb_9.png)

將準備好的USB插入斷電的網樂通，一邊用戳著reset按鈕一邊通電，通電後會看到網樂通前端的燈會短閃個三下後長亮，完成更新的動作。

這邊注意在更新時網樂通不需要接到螢幕，因為螢幕畫面跟一開始刷sh4twbox一樣，會一直是網樂通的logo，所以看螢幕也沒有用，照著上面操作就好。

更新完uboot後再次連進網樂通，呼叫命令free，可以看到此時網樂通已經突破128MB的限制，可以用到256MB的記憶體空間。

![image_thumb_8.png](/images/posts/05459f57-2b28-4c74-b12a-3dd8bc412d95/image_thumb_8.png)
