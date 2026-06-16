---
title: "[網樂通改機]網樂通硬改，用高效的USB碟替換內建的8G Dom"
date: "2013-11-06 12:00:00"
tags: [網樂通]
description: "網樂通內建的8G Dom效率不好，因此筆者在用 sh4twbox 軟改完了還是將它稍微硬改了一下，改用較為高效的USB替換。 這邊筆者準備了一條一樣是8G的USB隨身碟，因為筆者沒在抓BT，網樂通暫時也只是用來熟悉Linux用的，所以替換的目的主要還是做個硬改的嚐試，"
---

網樂通內建的8G Dom效率不好，因此筆者在用 sh4twbox 軟改完了還是將它稍微硬改了一下，改用較為高效的USB替換。

這邊筆者準備了一條一樣是8G的USB隨身碟，因為筆者沒在抓BT，網樂通暫時也只是用來熟悉Linux用的，所以替換的目的主要還是做個硬改的嚐試，以及要改善本來的8G Dom效率低落的問題。所以筆者是用手邊現有的8G USB隨身碟，沒改用更大容量的USB隨身碟。

因為筆者不想燒一片Live CD，所以不使用再生龍下去複製隨身碟，改用Linux內建的dd來做這個動作，故這邊直接將準備好要用來替換的USB插到網樂通的後面，

![IMAG0844_thumb.jpg](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/IMAG0844_thumb.jpg)

然後用telnet連進網樂通(不要用SSH~可能會找不到命令)，呼叫命令fdisk -l ，我們可以看到磁碟分割區的狀態，這邊筆者插在外面的USB對應到的就是/dev/sdb。

![image_thumb_4.png](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/image_thumb_4.png)

確定USB有找到也確定了分割區後，呼叫命令 dd if=/dev/sda of=/dev/sdb bs= 1048576將系統複製到準備好的USB中。bs的大小可依需求下去調整，不帶bs的話整個動作會要很久才能完成。

![image_thumb_7.png](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/image_thumb_7.png)

dd時我們預設會看不到處理的進度，若想要讓處理進度顯示出來，我們可以再開啟個telnet，一樣連進網樂通，呼叫命令watch -n 5 killall -USR1 dd。

![image_thumb_6.png](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/image_thumb_6.png)

本來在處理dd命令的視窗就會開始顯示處理進度，會明確的告知目前處理了多少容量。

![image_thumb_8.png](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/image_thumb_8.png)

![image_thumb_9.png](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/image_thumb_9.png)

系統複製好後，接著我們將網樂通背後四個腳的軟墊拔起，鬆開螺絲將網樂通拆解。

![IMAG0830_thumb.jpg](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/IMAG0830_thumb.jpg)

拆解後裡面大概長這個樣子 。

![IMAG0832_thumb.jpg](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/IMAG0832_thumb.jpg)

將內建的8G Dom螺絲鬆開後小心的拔起

![IMAG0833_thumb.jpg](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/IMAG0833_thumb.jpg)

拔起的8G Dom可焊上USB公頭充當USB，這邊筆者不想要那麼慢又脆弱的USB，故筆者只將90°USB公頭插上8G Dom的杜邦接頭保存起來充當系統的備份。

**![IMAG0835_thumb.jpg](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/IMAG0835_thumb.jpg)**

網樂通主機版上本來接8G Dom的杜邦接頭焊上180°USB母頭，讓後續好再次抽換系統碟。這邊注意到這邊的杜邦接頭靠近機身中間的是5v的接腳，靠近兩旁機身的是接地接腳，焊接時得特別注意。若是不會的，只要注意焊起來的USB母頭裡面的那一槓要靠近下方就可以了。**![IMAG0839_thumb.jpg](/images/posts/b14e4611-6b8d-4cf9-a3e9-32bc15406b65/IMAG0839_thumb.jpg)**

若是沒意外的話改插上我們複製好的USB隨身碟後開機就可以用了。若是開機後機身前方的燈號一直狂閃，那可能就是系統沒有複製好，需要再進行確認。
