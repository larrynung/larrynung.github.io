---
title: "安裝stlinux23-sh4-microperl套件，讓網樂通具備運行Perl的能力"
date: "2013-11-06 12:00:00"
description: "網樂通改機成功後，若想要讓網樂通可以支援運行Perl的能力，我們可以為網樂通加掛stlinux23-sh4-microperl套件。這篇稍微紀錄一下要怎樣才能透過sh4twbox為網樂通加掛stlinux23-sh4-microperl套件。"
---

網樂通改機成功後，若想要讓網樂通可以支援運行Perl的能力，我們可以為網樂通加掛stlinux23-sh4-microperl套件。這篇稍微紀錄一下要怎樣才能透過sh4twbox為網樂通加掛stlinux23-sh4-microperl套件。

首先我們必須連進網樂通，並參閱[網樂通改機][sh4twbox]如何使用shpkg去做套件的安裝與管理這篇，或是直接呼叫命令"shpkg -S stlinux23-sh4-microperl"，將Perl套件安裝起來。

![image_thumb.png](/images/posts/20920693-f416-448d-af66-f994c5eb1ee9/image_thumb.png)

安裝完成後記得要呼叫命令shpkg -E檢查是否有相依的套件需要安裝。

![image_thumb_6.png](/images/posts/20920693-f416-448d-af66-f994c5eb1ee9/image_thumb_6.png)

這邊應該會找到需要安裝的相依套件，會提示我們要按下Enter安裝相依的套件，直接按下Enter繼續即可。

![image_thumb_2.png](/images/posts/20920693-f416-448d-af66-f994c5eb1ee9/image_thumb_2.png)

相依的套件也安裝完後，若是整個流程都沒有什麼意外的話，套件就算正常的安裝上去了。

![image_thumb_3.png](/images/posts/20920693-f416-448d-af66-f994c5eb1ee9/image_thumb_3.png)

實際呼叫命令microperl --help看看是否perl的運行環境都已經安裝妥當，沒意外的話應該可像下圖一樣看到指令參數的說明。

![image_thumb_4.png](/images/posts/20920693-f416-448d-af66-f994c5eb1ee9/image_thumb_4.png)

這邊我們也可以帶入參數-e實際的運行一行perl看看是否可以正確運行。

![image_thumb_5.png](/images/posts/20920693-f416-448d-af66-f994c5eb1ee9/image_thumb_5.png)
