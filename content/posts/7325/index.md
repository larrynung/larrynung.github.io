---
title: "[C#][VB.NET]使用AxWindowsMediaPlayer撥放多媒體"
slug: "[CSharp][VB.NET]使用AxWindowsMediaPlayer撥放多媒體"
date: "2009-03-01 02:09:40"
description: "[C#][VB.NET]使用AxWindowsMediaPlayer撥放多媒體"
tags: [VB.NET,CSharp]
---

## 加入工具箱


Step1.工具箱=>滑鼠右鍵=>選擇項目

Step2.切換至『COM 元件』頁籤=>勾選Windows Media Player=>確定

Step3.會發現工具箱多了個Windows Media Player的控制項

## 使用AxWindowsMediaPlayer撥放多媒體


Step1.加入Windows Media Player控制項到設計表單，可看到如下的畫面。

Step2.依序加入控制項使介面如下圖所示。

Step3.撰寫控制項初始設定程式碼

此處是設定控制項的初始值，像是音量的最大值、最小值、目前的音量、與啟動Timer(用來偵測檔案總長度用)，值得注意的是AxWindowsMediaPlayer控制項的音量大小介於0~100之間，另外若不設定AutoStart = False則開啟檔案完程式就會自動撥放開啟的多媒體檔。

VB.NET

C#

Step4.撰寫開啟程式碼

AxWindowsMediaPlayer控制項是去設定AxWindowsMediaPlayer.URL屬性值來達到多媒體檔案開啟的功能。

VB.NET

C#

Step5.撰寫撥放程式碼

這部份功能程式碼只需呼叫AxWindowsMediaPlayer.Ctlcontrols.play()即可。

VB.NET

C#

Step6.撰寫停止程式碼

這部份功能程式碼只需呼叫AxWindowsMediaPlayer.Ctlcontrols.stop()即可。

VB.NET

C#

Step7.撰寫暫停撥放程式碼

這部份功能程式碼只需呼叫AxWindowsMediaPlayer.Ctlcontrols.pause()即可。

VB.NET

C#

Step8.撰寫音量控制程式碼

這部份功能程式碼只需對AxWindowsMediaPlayer.settings.volume做屬性值的變更即可。

VB.NET 

C#

Step9.撰寫撥放位置控制程式碼

除需對AxWindowsMediaPlayer.Ctlcontrols.currentPosioion做屬性值的變更外，尚需利用AxWindowsMediaPlayer.currentMedia.duration去設定最大影片長度。

VB.NET

C#

## Download


使用AxWindowsMediaPlayer撥放多媒體.zip

## 參考連結


MSDN Library - AxWindowsMediaPlayer Object (VB and C#)

黑色幽默 - AxWindowsMediaPlayer媒体文件主要方法属性