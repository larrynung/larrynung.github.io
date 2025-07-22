---
title: "[VS 2010]Start Page Customization"
date: "2010-01-16 02:58:43"
description: "[VS 2010]Start Page Customization"
tags: [Visual Studio]
---## Introduction

Visual Studio在啟動時，預設會自動載入起始頁面。預設的起始頁面上會放一些微軟覺得常用與實用的功能，像是歡迎訊息、回報問題.‧‧‧等功能。方便使用者快速的使用這些功能。

但這些功能畢竟是由微軟所訂定，不可能符合所有使用者的需求。對於進階的操作者或是不同需求的使用者來說，這些預設的功能可能就不太適用。好在VS 2010利用WPF技術，為我們提供了客制化起始頁面的功能。透過客制化起始頁面，使用者都能擁有適合自己又便於使用的起始頁面。

## 客制化起始頁面的操作步驟

客制化起始頁面主要可分為如下三個操作步驟：
Step1.點選[Tools\Options…]開啟Options視窗，切換到Startup並下拉設定Customize Start Page。
 
Step2.拷貝"%ProgramFiles%\Microsoft Visual Studio 10.0\Common7\IDE\StartPages\"下的StartPage.xaml與StartPage.csproj檔案到"我的文件\Visual Studio 10\StartPages"下。
 
Step3.開啟複製的專案檔(.csproj)並編輯存檔。
開啟複製的專案檔後，開啟專案中的StartPage.xaml檔，我們可以看到如下編輯畫面：

透過設計介面或是Xaml編輯畫面修改起始頁面畫面，存檔後起始頁面就會跟著變動。

## Video

這是網友放在網路上的相關教學影片，可順便參考看看。

## Link
Visual Studio 2010 Beta 1 Start Page Customization Customizing Start Page in Visual Studio 2010 Customize your Start Page in Visual Studio 2010