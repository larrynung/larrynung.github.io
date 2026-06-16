---
title: "[Visual Studio]Process Pro Extension v1.0"
date: "2013-11-06 12:00:00"
tags: [Visual Studio]
description: "不知道您是不是有同樣的經驗，有時候開發的專案需要開啟多個Process，除錯時常常視窗就在旁邊卻要從眾多Process中找到並attach上去，除錯結束時常常要從眾多Process中一一確認是否都被關掉了，明明就有地表最強大的開發工具，卻要開啟工作管理員去輔助做些確認，"
---

不知道您是不是有同樣的經驗，有時候開發的專案需要開啟多個Process，除錯時常常視窗就在旁邊卻要從眾多Process中找到並attach上去，除錯結束時常常要從眾多Process中一一確認是否都被關掉了，明明就有地表最強大的開發工具，卻要開啟工作管理員去輔助做些確認，而且也無法一眼望出這些Process到底吃了多少的資源。筆者常常在開發上常碰到類似這樣的困擾，因此順手將以前寫的小工具Process Manager做些強化並整合至Visual Studio，順便練練怎樣撰寫Visual Studio Extension。這邊姑且就將它叫做[Process Pro Extension](http://visualstudiogallery.msdn.microsoft.com/4e58c006-8aac-4b63-b858-f8467ccb444e)，有興趣的可以至[Visual Studio Gallery下載並安裝。](http://visualstudiogallery.msdn.microsoft.com/4e58c006-8aac-4b63-b858-f8467ccb444e)

![image_thumb_2.png](/images/posts/6af94d32-364a-48e2-aace-9f633a8056b1/image_thumb_2.png)

或是透過Extension Manager安裝也可以。

![image_thumb_1.png](/images/posts/6af94d32-364a-48e2-aace-9f633a8056b1/image_thumb_1.png)

安裝完後可在[VIEW/Other Windows]下多了一個[Process Pro]的選單選項，點選可開啟Process Pro tool window。

![2013-03-13_084431_thumb.jpg](/images/posts/6af94d32-364a-48e2-aace-9f633a8056b1/2013-03-13_084431_thumb.jpg)

開啟後就可以看到像下面這樣的tool window，應該看看就會用了，這邊就不贅述。

![2013-03-13_003714_thumb.jpg](/images/posts/6af94d32-364a-48e2-aace-9f633a8056b1/2013-03-13_003714_thumb.jpg)

## Link

* Process Pro extension - Visual Studio Gallery
* Process Pro Extension - CodePlex
