---
title: "[網樂通改機][sh4twbox]如何使用shpkg去做套件的安裝與管理"
date: "2013-11-06 12:00:00"
description: "[網樂通改機][sh4twbox]如何使用shpkg去做套件的安裝與管理"
---

這邊筆者以安裝nano為例做個示範，稍微紀錄一下如何使用shpkg去做套件的安裝與管理，。

首先我們要先連到網樂通，並呼叫命令"shpkg -Q"查詢我們已經安裝好的套件有哪些。因為筆者還能用vi做些編輯動作，所以已經移除類似功能的nano，故這邊呼叫命令"shpkg -Q"所查詢出來的套件列表中，看不到有nano套件在裡面。

![image_thumb.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb.png)

確定nano沒有安裝後，我們要看一下有沒有現成的套件可以安裝，不過因為系統內的套件列表要是太舊的話，很有可能會導致找不到我們想要的套件。所以這邊要先確定我們系統內的套件列表是新的，可呼叫命令"shpkg -Sy"更新套件列表。不過因為筆者已經在不久前更新過了，所以更新列表的動作會被取消。

![image_thumb_1.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_1.png)

這邊若是跟筆者一樣才更新過的，但是想要強制更新的話，我們也可以呼叫命令"shpkg -Syy"去強制他更新。

![image_thumb_2.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_2.png)

確定套件列表是新的後，可以呼叫命令"shpkg -Sl"看看套件列表內有什麼套件可以使用。

![image_thumb_3.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_3.png)

![image_thumb_4.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_4.png)

sh4twbox內建的套件列表起碼有9000多個，所以這邊會跑很久，若要中斷可按Ctrl+C。套件過多這樣查閱列表著時也沒什麼意義，也看不出到底多了什麼東西，而且有些套件其實已經不被維護了，倒不如呼叫命令"shpkg -Sl sh4twbox"查閱有哪些sh4twbox提供的套件可以使用比較實際，畢竟目前是有很多好心的網友持續的在做更新。

![image_thumb_5.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_5.png)

這邊筆者以安裝nano為例，所以呼叫"shpkg -Ss nano"，再次確認系統中的套件列表有那些nano套件可供安裝。以筆者目前的版本來說，可找到sh4twbox與fedora9提供的nano套件。

![image_thumb_6.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_6.png)

安裝前若是有疑慮，可以呼叫命令"shpkg -St nano"，查閱看看nano這個套件會動到那些檔案。

![image_thumb_7.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_7.png)

![image_thumb_8.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_8.png)

接著輸入命令"shpkg -S nano"就可以將nano套件安裝上去，安裝結束會看到像下圖這樣會顯示nano安裝成功的訊息。

![image_thumb_9.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_9.png)

安裝的動作完成後，可以呼叫命令"shpkg -E"檢查看看有沒有漏裝的東西。如果像下圖這樣看到告知"No packages require to install"，表示沒有相依的套件漏裝，理論上應該是已經安裝成功了。

![image_thumb_10.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_10.png)

這時我們再次呼叫一開始介紹的命令"shpkg -Q"查詢已安裝的套件，可以發現這時候nano已經被列在其中。

![image_thumb_11.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_11.png)

實際的呼叫nano去嘗試編輯檔案看看。

![image_thumb_12.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_12.png)

安裝的nano套件也確實運行良好。

![image_thumb_13.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_13.png)

不過如同筆者一開始說的，nano跟vi功能類似，筆者可以用vi取代，故這邊筆者再次呼叫命令"shpkg - R nano"將nano套件自系統中移除。

![image_thumb_14.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_14.png)

![image_thumb_15.png](/images/posts/ed59d238-a56e-4420-91bd-ab505410bfdf/image_thumb_15.png)
