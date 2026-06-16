---
title: "AppHarbor - .NET Cloud Platform as a Service"
date: "2013-11-06 12:00:00"
description: "AppHarbor是一支援.NET的雲端平台服務，它提供了雲端的Repository讓開發人員能將專案放置於雲端，也能直接整合現有的Online Repository Solution (e.x.GitHub)， 進行雲端建置以及單元測試。"
---

AppHarbor是一支援.NET的雲端平台服務，它提供了雲端的Repository讓開發人員能將專案放置於雲端，也能直接整合現有的Online Repository Solution (e.x.GitHub)， 進行雲端建置以及單元測試。簡單的說，AppHarbor就是Online Repository + Online CI Server，不過不只那麼單純，它還提供了一些彈性，像是可以支援Add-ons之類的。

![ScreenClip(23)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2823%29_thumb.png)

要使用AppHarbor首先我們要進行Sign Up。

![ScreenClip(10)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2810%29_thumb.png)

Sign Up後到信箱收取驗證信件，點選連結完成驗證的動作。驗證完登入，我們可以看到類似像下面這樣的畫面，左側是專案列表，提供基本的排序功能，不過因為此時我們還沒放置任何專案，所以這邊會空盪盪的。至於右側這邊則是是用來新增專案的，這邊筆者實際的建立個TestProject示範一下。

![ScreenClip(12)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2812%29_thumb.png)

專案建立後，瀏覽器會導到像下面這樣的專案頁面，左側有許多的設定項目，比較重要的就是Setting以及下方的兩個按鈕，右側這邊則是一些教學的連結以及add-on連結。

![Image(12)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/Image%2812%29_thumb.png)

這邊筆者先示範怎樣將專案放置於AppHarbor。先按下左側下方的REPOSITORY URL按鈕，該專案對應的Repository會複製於剪貼簿中。

![Image(13)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/Image%2813%29_thumb.png)

開啟Git shell將Repository整個clone下來。

![ScreenClip(15)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2815%29_thumb.png)

抓下來後放置個簡單的C#專案進去

![ScreenClip(16)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2816%29_thumb.png)

再將本地的修改推回雲端

![ScreenClip(17)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2817%29_thumb.png)

重新整理對應的AppHarbor專案頁面，可以看到AppHarbor已經偵測到變動且開始建置。建置完，專案的首頁會出現建置的結果，可清楚的一眼看出建置成功或失敗。

![image_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/image_thumb.png)

點選建置的結果，可進一步查閱建置的細部狀態，像是建置出來的檔案、建置的log、與單元測試。也可以在這邊將建置好的檔案下載下來。

![image_thumb_1.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/image_thumb_1.png)

下載下來的檔案用解壓縮軟體開啟，可以看到建置的組件以及建置的log都放置在裡面。

![image_thumb_2.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/image_thumb_2.png)

若是發生建置錯誤，可進一步點選後方的Show Log連結。

![ScreenClip(27)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2827%29_thumb.png)

有更為詳細的建置資訊供開發人員排除錯誤。

![ScreenClip(28)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2828%29_thumb.png)

這邊可能有人注意到了，在這個例子中，我們在把Commit推到AppHarbor時，AppHarbor就自動進行了建置的動作。但是我們在做版本控制時，通常會有多個分支並行，並不是所有的分支都要進行建置，通常只有主分支會想要建置，這時我們可以進入設定頁面設定Tracking branch。若是只是拿AppHarbor來充當Private Repository，設定這邊也可以把建置的功能給關閉。

![ScreenClip(29)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2829%29_thumb.png)

接著示範一下怎樣用AppHarbor連結現有的Online Repository，這邊筆者以Codeplex為例。首先按下專案頁面左側下方的BUILD URL按鈕，該專案對應的建置用位置會複製於剪貼簿中。

![ScreenClip(32)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2832%29_thumb.png)

開啟筆者的LevelUp Serializer Codeplex專案，點選右上方的Edit Project Summary & Details連結，

![ScreenClip(30)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2830%29_thumb.png)

捲到下方會看到WEB SITE DEPLOYMENT設定，勾選Enable AppHarbor deployment support.選項，並在下方的BUILD URL中貼上我們剛剛在AppHarbor複製的網址。

![ScreenClip(31)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2831%29_thumb.png)

設定完後存檔，進行程式的編修。當雲端的Repository有Commit進來時，AppHarbor會自動開始進行建置，建置的結果一樣會列在專案的首頁，跟直接將專案放置在AppHarbor沒什麼太大的差異。

![ScreenClip(37)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2837%29_thumb.png)

一樣也可以看到建置的細部狀態，不過這邊比較要提一下，因為筆者的這個CodePlex專案有寫點單元測試，所以可以在建置的細部狀態這邊看到建置時花了10.77秒在運行單元測試，39個單元測試都運行通過。

![ScreenClip(33)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2833%29_thumb.png)

若要看單元測試的運行狀況，可點選下方的View test hierarchy連結，找到想要查閱的單元測試。

![ScreenClip(35)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2835%29_thumb.png)

可以看到該單元測試的測試狀態、測試時間、以及輸出結果。

![ScreenClip(36)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2836%29_thumb.png)

最後這邊要特別提一下，雖然AppHarbor看起來很美好，但就筆者使用起來他有些限制存在。像是他建置是會把方案檔內所有的專案建置，所以當我們加進一個ModelingProject進行程式的架構規劃。

![ScreenClip(24)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2824%29_thumb.png)

當Commit推上AppHarbor後

![ScreenClip(25)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2825%29_thumb.png)

就會發現他建置錯誤了。

![ScreenClip(26)_thumb.png](/images/posts/e20ad3db-39bd-448c-9032-269ca1dc67e2/ScreenClip%2826%29_thumb.png)

類似的問題很多，像是開發一個Visual Studio Extension，我們需要加裝SDK，但SDK無法上到AppHarbor一樣會建置錯誤。
