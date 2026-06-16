---
title: "[網樂通改機][sh4twbox]安裝並啟動samba，讓網樂通可透過網芳連接"
date: "2013-11-06 12:00:00"
description: "網樂通改機成功後，若想要透過網芳連進去，我們可以為網樂通加掛samba server。這篇稍微紀錄一下要怎樣才能透過sh4twbox為網樂通加掛samba server。"
---

網樂通改機成功後，若想要透過網芳連進去，我們可以為網樂通加掛samba server。這篇稍微紀錄一下要怎樣才能透過sh4twbox為網樂通加掛samba server。

首先我們必須連進網樂通，並參閱[網樂通改機][sh4twbox]如何使用shpkg去做套件的安裝與管理這篇，或是直接呼叫命令"shpkg -S samba"，將samba套件安裝起來。

![image_thumb_4.png](/images/posts/38da4593-edf6-45ff-ad4e-58a4877f1d1c/image_thumb_4.png)

安裝成功後呼叫"/etc/init.d/samba start"將服務啟動，啟動成功會像下圖一樣告知"Starting samba:ok"。

![image_thumb_5.png](/images/posts/38da4593-edf6-45ff-ad4e-58a4877f1d1c/image_thumb_5.png)

接著呼叫命令"/usr/local/bin/smbpasswd -a"去做網芳密碼的設定。

![image_thumb_6.png](/images/posts/38da4593-edf6-45ff-ad4e-58a4877f1d1c/image_thumb_6.png)

到了這邊安裝與設定都完成了，實際的進行網芳的連線測試，按下Win+R帶出執行對話框，像下面這樣輸入網樂通的網址：

![image_thumb_9.png](/images/posts/38da4593-edf6-45ff-ad4e-58a4877f1d1c/image_thumb_9.png)

可以看到密碼的詢問，帳號的部分帶入root，密碼部分則帶入上面自行設定的密碼。

![image_thumb_8.png](/images/posts/38da4593-edf6-45ff-ad4e-58a4877f1d1c/image_thumb_8.png)

通過驗證後就可以看到網樂通裡面的資料。

![image_thumb_7.png](/images/posts/38da4593-edf6-45ff-ad4e-58a4877f1d1c/image_thumb_7.png)

最後這邊要再提醒一下，像上面這樣啟動沒問題後，若是希望每次網樂通通電就可以使用這樣的功能，我們必須要參閱[網樂通改機]網樂通運行時自動啟動指定的服務這篇，將要啟動的命令寫在/etc/rc.local裡面。

![image_thumb_11.png](/images/posts/38da4593-edf6-45ff-ad4e-58a4877f1d1c/image_thumb_11.png)
