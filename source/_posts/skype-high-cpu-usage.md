---
layout: post
title: "Skype - High CPU usage"
date: 2014-01-08 23:29:00
comments: true
categories: Skype
keywords: Skype, CPU
description: "Skype - High CPU usage"
---

最近在筆者工作的電腦上，一直以來都運作良好的 Skype 突然開始狂吃 CPU 。查閱了一下資料，這段時間發現很多人也都碰到這個問題，不過同樣的現象卻未在同事的電腦上出現，感覺是要滿足特定的條件才會發生。  

<!--More-->


像這邊筆者的電腦就吃了 25% 左右，筆者的電腦是四核心，相當於一整顆 CPU 被吃掉了。  

{% img /images/posts/SkypeCPUHigh/1.png %}


當這樣的問題發生時，電腦上的預設瀏覽器多半是設定為 Chrome 。而解決這問題的方法也就是將預設瀏覽器設為 IE ，或是設為其它瀏覽器。  

{% img /images/posts/SkypeCPUHigh/2.png %}


修改完預設瀏覽器後， 將 Skype 重開，沒意外的話就會看到 CPU 使用率恢復正常的狀態。  

{% img /images/posts/SkypeCPUHigh/3.png %}


另外還有一種解法就是改安裝舊版的 Skype ，然後將自動更新功能關閉，避免它更新到有問題的版本。  

目前造成該問題的原因還不明確，同樣的版本同樣的預設瀏覽器設定也不一定能重現，在官方尚未修正好前暫時也只能先這樣避開問題。  


Link
----
* [【問題】Skype之CPU使用量迷思](http://forum.gamer.com.tw/C.php?bsn=60030&snA=328960)
* [Getting extremely high CPU usage?](http://community.skype.com/t5/Windows-desktop-client/Getting-extremely-high-CPU-usage/td-p/1914583/page/3)
* [SKYPE 讓cpu使用率過高](http://7club.ithome.com.tw/article/10038479/1)
* [[問題]開啟Skype電腦變LAG](http://vas.skype.pchome.com.tw/forum/board.action?method=gotoPostViewPage&boardId=2&topicId=10156)
