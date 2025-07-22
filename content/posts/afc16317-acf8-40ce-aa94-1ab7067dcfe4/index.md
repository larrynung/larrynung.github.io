---
title: "[Win8]如何在Desktop mode取得Metro mode下看到的應用程式"
date: "2013-11-06 12:00:00"
description: "[Win8]如何在Desktop mode取得Metro mode下看到的應用程式"
---

我們在Win8按下熱鍵Win + Q可已進入搜尋應用程式的畫面，在這個畫面下我們可以看到很多我們安裝的APP。

有些App是可以在Desktop mode下運作的，但卻都要進入到Metro mode去找尋，若您覺得這樣的切換很麻煩，我們可以讓Desktop mode看到這些app。我們可以在Desktop mode的桌面上按下滑鼠右鍵，點選[新增→捷徑]。

在項目位置那邊填入"%windir%\explorer.exe shell:::{4234d49b-0245-4df3-b780-3893943456e1}"。

然後為這個捷徑取個名字。

完成我們會在桌面看到剛剛我們所產生的捷徑。

滑鼠連點捷徑會開啟Applications的目錄，裡面的內容就會是我們在Metro mode下看到的app。