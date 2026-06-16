---
title: "[NetTV Mod][sh4twbox]Install and Start dropbear to Connect to the NetTV Box via SSH"
slug: "nettv-mod-sh4twbox-install-and-start-dropbear-to-connect-to-the-nettv-box-via-ssh"
aliases: ["/posts/290823e0-38b8-4ed3-affb-d3a399e083e1/"]
date: "2013-11-06 12:00:00"
tags: [網樂通]
description: "網樂通改機成功後，一開始我們只能透過telnet連進去，這種方式比較不安全，若需要更為安全的連接方式，我們可以為網樂通加掛dropbear server，讓網樂通支援SSH連接。這篇稍微紀錄一下要怎樣才能透過sh4twbox為網樂通加掛dropbear server。"
---

網樂通改機成功後，一開始我們只能透過telnet連進去，這種方式比較不安全，若需要更為安全的連接方式，我們可以為網樂通加掛dropbear server，讓網樂通支援SSH連接。這篇稍微紀錄一下要怎樣才能透過sh4twbox為網樂通加掛dropbear server。

首先我們必須連進網樂通，並參閱[網樂通改機][sh4twbox]如何使用shpkg去做套件的安裝與管理這篇，或是直接呼叫命令"shpkg -S dropbear"，將dropbear套件安裝起來。

![image_thumb_2.png](/images/posts/290823e0-38b8-4ed3-affb-d3a399e083e1/image_thumb_2.png)

安裝成功後呼叫"/etc/init.d/dropbear start"將服務啟動，啟動成功會像下圖一樣告知"Starting dropbear:"。

![image_thumb_3.png](/images/posts/290823e0-38b8-4ed3-affb-d3a399e083e1/image_thumb_3.png)

到了這邊服務已經安裝完成並啟用，實際的用PuTTY進行SSH連線測試，可以像下面這樣帶入網樂通的網址後按下Open進行連接：

![image_thumb_4.png](/images/posts/290823e0-38b8-4ed3-affb-d3a399e083e1/image_thumb_4.png)

輸入網樂通的帳號密碼，沒意外的話應該可以像下面這樣正常的連接。

![image_thumb_5.png](/images/posts/290823e0-38b8-4ed3-affb-d3a399e083e1/image_thumb_5.png)

最後這邊要再提醒一下，像上面這樣啟動沒問題後，若是希望每次網樂通通電就可以使用這樣的功能，我們必須要參閱[網樂通改機]網樂通運行時自動啟動指定的服務這篇，將要啟動的命令寫在/etc/rc.local裡面。

![image_thumb_11.png](/images/posts/290823e0-38b8-4ed3-affb-d3a399e083e1/image_thumb_11.png)
