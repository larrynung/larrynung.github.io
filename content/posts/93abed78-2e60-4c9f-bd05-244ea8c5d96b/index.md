---
title: "網樂通刷sh4twbox自動安裝碟"
date: "2013-11-06 12:00:00"
description: "網樂通刷sh4twbox自動安裝碟"
---

網樂通的改機目前已經算很成熟了，網路上有兩三種以上的刷機方式，因為sh4twbox能啟用到250MB的記憶體，記憶體能使用比較多，另外又內建套件管理程式，可用套件多，套件也比較好安裝，所以幾經評估之下筆者最後是選用sh4twbox來做刷機。

sh4twbox刷機有分自動跟手動安裝，兩者的區別不大，只有還原磁區的差異，所以這邊當然是直接選用比較簡單的自動安裝碟來做刷機。這邊可至sh4twbox下載自動安裝碟。

![image_thumb_4.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb_4.png)

![image_thumb_3.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb_3.png)

再下載[Win32 disk imager](http://sourceforge.net/projects/win32diskimager/)將uboot寫到USB碟。需將下載的uboot先行解開，解開後會看到附檔名為dd的檔，這檔案需透過[Win32 disk imager](http://sourceforge.net/projects/win32diskimager/)將它寫到usb中。

![image9_thumb.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image9_thumb.png)

要寫入時記得Select a disk image對話框的副檔名需選*.*，這樣才看的到我們欲寫的資料。

![image_thumb.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb.png)

選取好後按下write進行寫入。

![image12_thumb.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image12_thumb.png)

![image18_thumb.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image18_thumb.png)

![image21_thumb.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image21_thumb.png)

![image24_thumb.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image24_thumb.png)

將準備好的USB插入斷電的網樂通，一邊用戳著Reset按鈕(網樂通前端的小洞，可用迴紋針按壓)一邊通電，通電後會看到網樂通前端的燈會短閃個三下後長亮，等約40秒鐘。

![2013-04-22%2015.37.06_thumb.jpg](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/2013-04-22%2015.37.06_thumb.jpg)

接著拔掉USB跟電源，將網路線插上，並再次戳著Reset按鈕通電。通電後一樣會看到網樂通前端的燈會短閃個三下後長亮，Reset按鈕放掉等約3分鐘。

這邊注意在更新時網樂通不需要接到螢幕，因為螢幕畫面會一直是網樂通的logo(有的刷機方式是會有畫面上的變化，但是sh4twbox沒有)，所以看螢幕也沒有用，照著上面操作就好。

![image_thumb_1.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb_1.png)

等待差不多3分鐘後，我們可以嘗試telnet進去。

這邊如果是將電腦設定成192.168.168.x，並用網路線直接對連網樂通跟電腦的話。

![image_thumb_6.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb_6.png)

我們可以直接在命令列模式下telnet 192.168.168.168連進網樂通。

![image_thumb_10.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb_10.png)

不過這種連接方式實在不優，不僅要動到桌機的IP，後續網樂通要安裝什麼東西時，接線方式又得換過。

所以這邊還是建議直接將網樂通接到IP分享器，讓DHCP配給IP給網樂通。線接好後我們需要確定網樂通的IP，可以看一下網樂通機盒後方，會有網樂通的MAC Address。

![image_thumb_5.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb_5.png)

連到IP分享器的網頁查閱DHCP配給的狀況，看哪個IP是對到網樂通的MAC Address。

![image_thumb_7.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb_7.png)

像這邊筆者的網樂通就是被配置到192.168.0.102，所以呼叫命令telnet 192.168.0.102，用telnet連進網樂通。

![image_thumb_11.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb_11.png)

連進網樂通後我們會看到下面這個畫面，需要我們輸入帳號密碼。sh4twbox預設的帳號是root，密碼則是twpdatwpda。

![image_thumb_9.png](/images/posts/93abed78-2e60-4c9f-bd05-244ea8c5d96b/image_thumb_9.png)

完成登入的動作後，我們就可以對網樂通進行些設定與客製。像是呼叫命令passwd去變更登入的密碼，或是安裝我們想要使用的套件。

## Link

* [sh4twbox](https://code.google.com/p/sh4twbox/)
