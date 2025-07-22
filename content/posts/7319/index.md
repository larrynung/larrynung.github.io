---
title: "[C#][VB.NET]使用AxMediaPlayer撥放多媒體"
slug: "[CSharp][VB.NET]使用AxMediaPlayer撥放多媒體"
date: "2009-02-28 03:41:58"
description: "[C#][VB.NET]使用AxMediaPlayer撥放多媒體"
tags: [CSharp,VB.NET]
---

## 加入工具箱
Step1.工具箱=>滑鼠右鍵=>選擇項目 
 
Step2.切換至『COM 元件』頁籤並按下瀏覽鍵。 
 
Step3.找到Windows\System32下的msdxm.ocx檔後按下開啟鍵。 
 
Step4.會看到多了一個Windows Media Player的Com元件，此時勾選並按下確定鍵。 
 
Step5.會發現工具箱多了個Windows Media Player的控制項

## 使用AxMediaPlayer撥放多媒體
Step1.加入Windows Media Player控制項到設計表單，可看到如下的畫面。 
 
Step2.依序加入控制項使介面如下圖所示。 
 
Step3.撰寫控制項初始設定程式碼
此處是設定控制項的初始值，像是音量的最大值、最小值與目前的音量，值得注意的是AxMediaPlayer控制項的音量大小好像介於-10000~0之間，另外若不設定AutoStart = False則開啟檔案完程式就會自動撥放開啟的多媒體檔。

VB.NET

C#

Step4.撰寫開啟程式碼
AxMediaPlayer控制項的開啟可以直接設定FileName，亦可以使用Open函式。這邊除了開啟檔案外也需順道設定撥放位置的最大值與最小值。

VB.NET

C#

Step5.撰寫撥放程式碼
撰寫這部份功能程式碼只需呼叫AxMediaPlayer.Play()即可。

VB.NET

C#

Step6.撰寫停止程式碼
這邊需注意的是，AxMediaPlayer控制項的Stop函式雖然會停止撥放，但是停止後撥放位置仍維持在原位，因此當又按下撥放時，該控制項會從上次位置繼續撥放，有點類似暫停的功能(跟暫停的差異在於它會按下控制項上的Stop按鈕)，因此這邊須自行把撥放位置設回起始點。

VB.NET

C#

Step7.撰寫暫停撥放程式碼
撰寫這部份功能程式碼只需呼叫AxMediaPlayer.Pause()即可。

VB.NET

C#

Step8.撰寫音量控制程式碼
這部份功能程式碼只需對AxMediaPlayer.Volume做屬性值的變更即可。

VB.NET

C#

 Step9.撰寫撥放位置控制程式碼
這部份功能程式碼只需對AxMediaPlayer.CurrentPosition做屬性值的變更即可。

VB.NET

C#

## Download

使用AxMediaPlayer撥放多媒體.zip

## 參考連結
藍色小鋪 - media 播放設定問題如何使用 Visual Basic.NET 或 Visual Basic 2005 中播放音訊檔案