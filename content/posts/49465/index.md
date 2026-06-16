---
title: "[Visual Studio]使用VSSpeedster加速Visual Studio建置"
date: "2011-11-01 09:16:05"
description: "VSSpeedster是Visual Studio的外掛元件，若開發的電腦具備多核心，安裝後能讓Visual Studio利用多核心去建置專案，減少建置所需的時間。"
tags: [Visual Studio]
---

VSSpeedster是Visual Studio的外掛元件，若開發的電腦具備多核心，安裝後能讓Visual Studio利用多核心去建置專案，減少建置所需的時間。

下載後解壓縮，將解壓縮後的檔案放置C:\Users\UserName\Documents\Visual Studio 2010\AddIns。

![image_thumb.png](/images/posts/49465/image_thumb.png)

開啟Visual Studio，點選[Tools/Add-in Manager...]選單選項，開啟Add-in Manager設定對話框。

![image6%5B1%5D_thumb.png](/images/posts/49465/image6%5B1%5D_thumb.png)

Add-in Manager設定對話框彈出後，可以看到Available Add-ins會出現VSSpeeder，將VSSpeeder勾選後按下[OK]按鈕離開Add-in Manager設定對話框。

![image4_thumb.png](/images/posts/49465/image4_thumb.png)

設定完後可在Build選單看到多了個[Parallel Build]選單選項。

![image1_thumb.png](/images/posts/49465/image1_thumb.png)

點選該選單選項可切換是否啟用平行建置，確定選單選項變為[Disable Parallel Builds] 即為啟用狀態。

![image7_thumb.png](/images/posts/49465/image7_thumb.png)

啟用平行建置後，建置時就會自動採用平行處理，建置的途中若有需要也可透過[Cancel Parallel Build]選單選項去取消平行建置。

![image13_thumb.png](/images/posts/49465/image13_thumb.png)

建置的資訊與耗費的時間可透過輸出視窗查閱，這邊可以看到其實該外掛元件背後也只是使用msbuild帶入/m參數，讓msbuild以平行處理的方式建置。

![image10_thumb.png](/images/posts/49465/image10_thumb.png)

另外提一下，在筆者的筆電安裝後會出現以下的錯誤訊息，外掛元件無法啟動，但在公司的電腦就能正常運行，在官網中也有人反映一樣的問題，該問題暫時不明原因。

![image9_thumb.png](/images/posts/49465/image9_thumb.png)

還有在筆者實驗的過程中也有發現某些專案以平行建置時，會無法產生建置後的組件，若碰到這種狀況，請採用一般的建置方式。

## Link

* [VSSpeedster - Speed up your VS 2010](http://vsspeedster.codeplex.com/)
* [VSSpeedster加速Visual Studio的建置時間](http://gogojimmy.net/?p=347)
