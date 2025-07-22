---
title: "Invoke Team Build with Team Foundation Service"
date: "2013-11-06 12:00:00"
description: "Invoke Team Build with Team Foundation Service"
---

前面介紹了怎樣連結Team Foundation Service，也將我們的專案CheckIn上去了。隨著專案的行進我們總是免不了會有建置組件的需求，不論是手動觸發建置，又或者是每日例行性的建置。因此這邊筆者簡單的隨手紀錄一下要如何才能使用Team Foundation Service來建置我們的專案組件。

首先我們先點擊Team Explorer內的Builds連結，將 Team Explorer 切至Builds頁面。

點擊New Build Definition連結，開始建立一個新的建置設定。

建置的動作大概可分為六個步驟：

第一步我們要為該建置設定取一個識別用的名稱，以及該建置的描述。

第二步要設定建置的週期，是要手動觸發建置、每次上Code舅舅至、還是固定週期去做建置。

第三步決定要進行建置的專案。

第四步設定建置出來的檔案所要存放位置。

第五步設定細部的雜項設定。

像是Items to Build項目就可進一步設定建置的組件是Debug還是Release。

也可以設定建置出來的是x86組件還是Any CPU的組件。

除此之外還有其他可能會需要用到的設定，像是是否運行單元測試、以及是否啟用多核建置…等等。

第六步設定建置出來的組件要保留多少，以及進行刪除時要刪除那些。(沒什麼太大的原因需要做調整的話，這步驟可直接跳過)

設定完後按下熱鍵Ctrl + s進行存檔，Team Explore會出現剛剛我們所加入的建置設定。

建置設定設好，我們開始進行實際的建置測試。如果剛剛不是設定週期性或是自動的建置，我們可以在剛產生的建置設定上方按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中，選取Queue New Build...選單選項，主動觸發建置的動作。

這邊也可以透過Build Explorer的工具列來觸發建置的動作。

建置動作觸發後，Visual Studio會先彈出Queue Build的對話框要求使用者確認，除了觸發的建置資訊外，這邊還有建置的優先權可做調整。若沒什麼問題，可以按下Queue的按鈕將建置動作加入Queue。

  建置動作Queue起來後，Team Foundation Service有空時就會開始運行建置，建置完成我們可在Team Explorer或是Build Explorer看到建置的結果。        
 
    我們也可以至Team Foundation Service網站上查看，並將建置後的組件打包下載。