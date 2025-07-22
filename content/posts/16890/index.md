---
title: "[Visual Studio]為專案加入不同Visual Studio版本的方案檔"
date: "2010-07-29 10:37:09"
description: "[Visual Studio]為專案加入不同Visual Studio版本的方案檔"
tags: [Visual Studio]
---

為專案加入不同Visual Studio版本的方案檔，讓不同的方案檔對應致相同的專案檔，可以方便用各種版本的Visual Studio 開啟，只要點選愈開啟的版本方案檔，就會直接用對應版本的Visual Studio開啟。

讓我們來看個例子方便理解，假設今天有個專案是用Visual Studio 2005所編寫的，

此時若想用新版本的Visual Studio開啟，多半的做法應該是直接點方案檔開啟升級，升級後若不特別處理，舊版本的Visual Studio便無法直接開啟該專案。

  其實換個做法，我們可以把本來的方案檔改名為XXXX 2005.sln，接著複製多份方案檔，改名為XXXX 2008.sln與XXXX 2010.sln。    

然後分別把新複製的方案檔用對應的Visual Studio開啟後轉換。

轉換完畢後，該專案就會有不同版本的方案檔了，以後要用哪個版本就可以直接點選開啟。

  但這樣的做法有個缺陷，就是您的電腦中必需裝有對應的Visual Studio，而且必需是舊版本的專案才可使用，若不符合這樣的條件，可以參閱將VS2010專案以VS2008開啟這篇去做。  

簡單來說就是把方案檔給打開修改其對應的Format Version與Visual Studio的Version。

對應的版本可查閱下表：
              Visual Studio        Format Version                  Visual Studio 2003        8.00                  Visual Studio 2005        9.00                  Visual Studio 2008        10.00                  Visual Studio 2010        11.00          
 
  這邊我依此觀念寫了隻簡陋的Console小工具SolutionConverter.zip，使用上可下命令，或是直接把方案檔給托曳至Console程式圖示上方放掉即可。  

## Download
   SolutionConverter.zip  

## Link
     將VS2010專案以VS2008開啟