---
title: "如何更新在Visual Studio Gallery上所發佈的元件"
date: "2013-11-06 12:00:00"
description: "如何更新在Visual Studio Gallery上所發佈的元件"
---

筆者之前在如何上傳Visual Studio Extension至Visual Studio Gallery這篇稍微介紹了一下怎樣發佈元件到Visual Studio Gallery，發佈後元件若是後續有在持續更新，總是會要更新發佈在Visual Studio Gallery的元件。所以這邊稍微紀錄一下怎樣更新發佈的元件。  

要更新發佈的元件，首先必需先登入CodePlex，登入後進到元件專案的首頁，點選元件專案首頁會上方的編輯連結進到元件專案的編輯畫面。

在第二步上傳字樣的後面有個變更的連結，點選下去。

選取新版的元件檔將之上傳。

新版本的元件上傳後會跟一開始我們放上專案時一樣去解析vsix內的manifest資訊，並自動將這些資訊的帶入到表單中，這邊我們確定像是版號之類的資訊都帶入正確就可以儲存離開了。

儲存離開會回到元件專案首頁，這邊的資訊也會變成是新版本的，這樣就完成了元件更新的動作。
          
最後當然還是要回到Visual Studio確認一下是否真的已經完成元件更新的動作，而這樣的操作對於Visual Studio內建的更新機制來說是否又可以正常的運作。所以這邊我們開啟Visual Studio的Extensions and Updates對話框，將對話框切換至Updates頁面，可以看到元件會有剛剛更換上去的版本可以替換，按下Update按鈕也確實可以進行更新的動作。