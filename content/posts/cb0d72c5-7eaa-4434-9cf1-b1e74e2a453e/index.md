---
title: "[Visual Studio]The User Control Test Container"
slug: "visual-studio-the-user-control-test-container"
aliases: ["/posts/cb0d72c5-7eaa-4434-9cf1-b1e74e2a453e/"]
date: "2013-11-06 12:00:00"
tags: [Visual Studio]
description: "Introduction 使用者控制項測試容器(User Control Test Container)是VS2005加入的功能，能為開發者提供簡易的控制項測試方式。開發者藉此功能能在不建立表單、不把控制項拖曳到表單的狀況下，對使用者控制項做初步的測試。"
---

## Introduction

使用者控制項測試容器(User Control Test Container)是VS2005加入的功能，能為開發者提供簡易的控制項測試方式。開發者藉此功能能在不建立表單、不把控制項拖曳到表單的狀況下，對使用者控制項做初步的測試。

## User Control Test Container

![image_thumb_1.png](/images/posts/cb0d72c5-7eaa-4434-9cf1-b1e74e2a453e/image_thumb_1.png)

在User Control Test Container叫起後，開發者可直接選取想要測試的控制項，並在控制項預覽區操作測試。細部設定可在屬性編輯區作修改，預覽區會對屬性的修改作即時的變化。

## Invoke User Control Test Container

要使用User Control Test Container上有兩種方式：

1. 從自身專案叫用
2. 從另一個專案叫用

若要從自身專案叫用，我們可以建立一個Windows Form Control Library專案，撰寫控制項後，按下F5。User Control Test Container就會被叫起，並載入自身專案所建立的組件。

而若要從另一個專案叫用，一樣我們必須做上面的動作。不同的是，在User Control Test Container被叫起後，我們需按下Load按鈕，選取其他專案所產生的組件，按下確定後即可選取其組件內含的控制項。

![image_thumb_4.png](/images/posts/cb0d72c5-7eaa-4434-9cf1-b1e74e2a453e/image_thumb_4.png)

這兩種叫用方式，說穿了只是Load功能的應用罷了。而依個人的使用經驗來看，要叫用User Control Test Container主要是要滿足下列兩個條件：

1. 應用程式類型為類別庫類型
2. 起始動作為起始專案

![image_thumb_2.png](/images/posts/cb0d72c5-7eaa-4434-9cf1-b1e74e2a453e/image_thumb_2.png)

![image_thumb_3.png](/images/posts/cb0d72c5-7eaa-4434-9cf1-b1e74e2a453e/image_thumb_3.png)

只要滿足上述兩個條件，按下F5，User Control Test Container應該就會被叫用了。

## Link

* [How to: Test the Run-Time Behavior of a UserControl](http://msdn.microsoft.com/en-us/library/ms171738.aspx)
* [HOW TO：測試 UserControl 的執行階段行為](http://msdn.microsoft.com/zh-tw/library/ms171738(VS.80).aspx)
