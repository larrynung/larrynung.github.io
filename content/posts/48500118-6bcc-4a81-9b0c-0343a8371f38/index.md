---
title: "Check In to Team Fundation Service"
date: "2013-11-06 12:00:00"
description: "Check In to Team Fundation Service"
---

前面Connect to Team Fundation Service這篇，大致的帶過要如何使用Visual Studio連接Team Fundation Service。這邊稍微介紹一下要怎樣才能將我們的專案程式Check In進Team Fundation Service。

	首先我們必須要開啟Options，確定Source Control Plug-In目前選取的是Visual Studio Team Fundation Server。(若是沒做這設定，Source Control Explorer會無法使用，也無法將專案加進版本控制)

	接著在方案上按下右鍵叫出滑鼠右鍵選單，點選Add Solution to Source Control這個選單選項。

	點選後會彈出個對話框詢問要放置到Team Fundation Service的哪個專案，以及要放在哪個目錄下面。這邊請視個人需求下去設定，設定完後按下OK按鈕繼續。

	透過Source Control Explorer我們可以看到選取的位置會多出我們所創建的專案。再仔細看的話可以發現前面會多帶一個"+"符號，代表這個是新增且未Check In的。

	我們先透過Team Explorer將專案先Check In上Team Fundation Service。輸入這次Check In的變動內容至Commit欄位，再按下Check In按鈕...(注意到Team Explorer這邊也可以看到這次變動的檔案有哪些，Check In前可以先進行確認，看是否都要Check In上去)

	Visual Studio會再次確認是否要將這些變動Check In上去，若是確定這邊就直接按下Yes繼續。

	Check In後Team Explorer會提示這次的動作是成功或是失敗。

	若不是網路不通或是衝突的話，這邊應該都是能正常的上到Team Fundation Service。除了透過前面提到的小小訊息列進行確認外，我們也可以透過Source Control Explorer進行確認，本來在Source Control Explorer這邊前面帶有"+"符號的項目，"+"這個符號應該會隨著Check In消失(因為本機的變動已經上去了)。

	另外我們也可以直接連至Team Fundation Service網頁，這邊看到的程式碼應該會是新的。

	changesets頁籤這邊應該也會有新的Commit紀錄。