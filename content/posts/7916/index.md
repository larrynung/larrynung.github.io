---
title: "[WPF]Windows Form程式使用WPF控制項"
date: "2009-04-08 12:34:45"
description: "[WPF]Windows Form程式使用WPF控制項"
tags: [WPF]
---

在Windows Form程式中若欲使用WPF，我們可以很簡單的透過ElementHost控制項來達成。

## 
	步驟

	操作步驟如下：

	Step1.加入WPF控制項到方案

	Step2.加入ElementHost控制項到表單

	Step3.建置專案

	Step4.設定ElementHost控制項的裝載內容為Step1中加的WPF控制項

	可以直接透過控制項的智慧標籤來設定。

	或是透過ElementHost控制項的Child屬性設定。

	設定完後即可看到效果。