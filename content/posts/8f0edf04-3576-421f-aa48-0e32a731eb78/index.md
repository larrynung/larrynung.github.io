---
title: "Push to different remote repository by git"
date: "2013-11-06 12:00:00"
description: "Push to different remote repository by git"
tags: [Git]
---

筆者這一兩年接觸了很多不同的Source Hosting Solution，像是GitHub、CodePlex、與Bitbuck。在要開放Source Code時，因為技術背景的關係筆者總是會優先傾向使用CodePlex去做Source Hosting，雖然CodePlex已經很好用了，但只放在那邊總是有些遺憾，若是能將程式碼同時發佈到GitHub不僅能再多一份備份，也能讓更多的人接觸到這份程式碼，進而對其給些建議、指教、甚至是多了從GitHub發Pull Request的管道，能讓這份程式變得更加的完善。

所以這篇稍稍紀錄一下要怎樣將程式碼發佈至不同的remote repository。

筆者以現有的CodePlex專案為例，將它上一份到GitHub。首先到GitHub創建對應的repository。

![image_thumb_1.png](/images/posts/8f0edf04-3576-421f-aa48-0e32a731eb78/image_thumb_1.png)

![image_thumb.png](/images/posts/8f0edf04-3576-421f-aa48-0e32a731eb78/image_thumb.png)

將repository的git位置記錄下來。

![image_thumb_2.png](/images/posts/8f0edf04-3576-421f-aa48-0e32a731eb78/image_thumb_2.png)

切到Git shell呼叫命令"git remote -v"查看目前專案對應到哪些remote repository，像是筆者這個因為是CodePlex的專案，所以origin指到的是CodePlex那邊的專案git位置。

![image_thumb_3.png](/images/posts/8f0edf04-3576-421f-aa48-0e32a731eb78/image_thumb_3.png)

這邊呼叫命令"git remote rename origin codeplex"將origin改名為codeplex，再次呼叫命令"git remote -v"查閱，我們可以看到本來的origin已經被我們改名為codeplex。

![image_thumb_4.png](/images/posts/8f0edf04-3576-421f-aa48-0e32a731eb78/image_thumb_4.png)

接著呼叫命令"git remote add github [git repository uri]"，這邊的[git repository uri]就是我們上面GitHub那邊顯示的git位置。再次呼叫命令"git remote -v"，我們可以看到這邊會多了github。

![image_thumb_5.png](/images/posts/8f0edf04-3576-421f-aa48-0e32a731eb78/image_thumb_5.png)

實際要上Code到GitHub時，我們只要呼叫命令"git push github [branch name]"就可以了。

![image_thumb_6.png](/images/posts/8f0edf04-3576-421f-aa48-0e32a731eb78/image_thumb_6.png)

上完Code到GitHub查驗，沒意外的話會像下面這樣，Source Code、Comments、跟Tag那些資訊都被帶上去了。

![image_thumb_7.png](/images/posts/8f0edf04-3576-421f-aa48-0e32a731eb78/image_thumb_7.png)

若要將Code上一份到本來的CodePlex，這邊也是用一樣的方式來處理。

![image_thumb_8.png](/images/posts/8f0edf04-3576-421f-aa48-0e32a731eb78/image_thumb_8.png)
