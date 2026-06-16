---
title: "Run guestbook sample Google App Engine Launcher built-in"
date: "2013-11-06 12:00:00"
tags: [Google App Engine]
description: "Google App Engine Launcher內建有幾個範例，在剛入門時可以跑起來玩玩。 以內建的留言版範例來說，我們可在Google App Engine Launcher開啟後，"
---

Google App Engine Launcher內建有幾個範例，在剛入門時可以跑起來玩玩。

以內建的留言版範例來說，我們可在Google App Engine Launcher開啟後，透過滑鼠點擊選取[Help/Demos/Python/guestbook]選單選項

![Image(35)_thumb.png](/images/posts/71275b5d-add1-4e6b-b4fc-c754d34112bd/Image%2835%29_thumb.png)

點選後會彈出對話框提示該範例程式會存放到我的文件下，點選確定按鈕繼續。

![Image(36)_thumb.png](/images/posts/71275b5d-add1-4e6b-b4fc-c754d34112bd/Image%2836%29_thumb.png)

回到Google App Engine Launcher主頁面後，下方的清單中會多出剛加入的guestbook項目。

![image_thumb_3.png](/images/posts/71275b5d-add1-4e6b-b4fc-c754d34112bd/image_thumb_3.png)

用檔案總管看一下剛剛下載的位置，可以看到Google App Engine Application最重要的app.yaml以及python程式主檔都會放在裡面。

![Image(41)_thumb.png](/images/posts/71275b5d-add1-4e6b-b4fc-c754d34112bd/Image%2841%29_thumb.png)

而這個程式也很簡單，分了MainPage與GurestBook兩個類別，MainPage負責畫面的呈現，會先將所有的留言從資料庫中撈出呈現，在去呈現發表留言所需要的表單，而GurestBook這邊則是負責留言的動作，兩個類別分別由router導到不同的位置。有興趣後續可以私下打開python主檔來仔細研究程式是如何撰寫的。

![image_thumb.png](/images/posts/71275b5d-add1-4e6b-b4fc-c754d34112bd/image_thumb.png)

回到主題，在這邊我們只是要稍微的把玩一下內建的範例，所以接著請參閱Run application with Google App Engine Launcher這篇將Application運行起來 ，可以看到運行起來就是很精簡的留言板程式，也確實可以讓我們進行留言的動作。

![Image(39)_thumb.png](/images/posts/71275b5d-add1-4e6b-b4fc-c754d34112bd/Image%2839%29_thumb.png)

![Image(40)_thumb.png](/images/posts/71275b5d-add1-4e6b-b4fc-c754d34112bd/Image%2840%29_thumb.png)
