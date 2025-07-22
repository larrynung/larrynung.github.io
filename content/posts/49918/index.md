---
title: "[Visual Studio]使用MSBuild的平行建置功能加速Visual Studio的建置"
date: "2011-11-02 01:04:58"
description: "[Visual Studio]使用MSBuild的平行建置功能加速Visual Studio的建置"
tags: [Visual Studio]
---

筆者在[Visual Studio]使用VSSpeedster加速Visual Studio建置這篇介紹到可以使用VSSpeedster外掛啟用平行建置，加速Visual Studio的建置，文中有帶出該外掛元件背後是透過MSBuild來達到平行建置的效果。那麼是否可以不安裝這類的外掛而直接透過整合MSBuild來平行建置呢？答案是肯定的，開發人員可開啟Visual Studio IDE，點選[Tools/External Tools...]選單選項，帶出External Tools設定對話框。    

External Tools設定對話框彈出後，按下右側的[Add]按鈕，填入自己設定的Title，Command部分設定MSBuild.exe的位置(可在 [作業系統安裝路徑]\Microsoft.NET\Framework 下找到)，參數的部分若是Release版的設定/m $(SolutionFileName) /v:m /property:Configuration=Release，是Debug版的話設定/m $(SolutionFileName) /v:m即可，至於Initial directory部分設定為$(SolutionDir)，特別注意下方的[Use Output window]選像要勾選，這樣建置的資訊才會導到輸出視窗。
                       Debug        Release                  Arguments        /m $(SolutionFileName) /v:m /property:Configuration=Release        /m $(SolutionFileName) /v:m                  Initial directory        $(SolutionDir)        $(SolutionDir)          

設定好後，若有需要可以透過剛剛加入的外部工具選單選像去執行平行建置，也可以把它加到工具列按鈕使用。

## Link
     Hack: Parallel MSBuilds from within the Visual Studio IDE