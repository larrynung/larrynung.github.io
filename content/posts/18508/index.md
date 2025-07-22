---
title: "[.NET Resource]Zeta Resource Editor 好用的資源檔編輯工具"
date: "2010-10-21 11:21:42"
description: "[.NET Resource]Zeta Resource Editor 好用的資源檔編輯工具"
tags: [.NET Resource]
---

在製作.NET多語系應用程式時，常常會發生可能改一改後有個語系的資源檔忘了修改，或是多語系資源不知道該怎麼翻譯，這時我們就必須要資源檔編輯工具來輔助我們實作多語系應用程式，Zeta Resource Editor就是這樣的一個輔助工具，具備多個語系資源同時編輯、翻譯等功能。

## 資源載入
  
在使用上Zeta Resource Editor提供了可直接開啟單一資源檔編輯的模式，與設定資源編輯專案來編輯的模式。以開啟單一資源檔編輯的模式來看，可直接在工具列上點選[Start]→[Open resourec files]按鈕。

在彈出的開啟對話框中選取所要編輯的資源檔

選取完畢程式中間區域就會開出資源檔的內容供使用者編輯

若是用設定資源編輯專案來編輯的話，則需點選工具列上方的[Start]→[Create new project]按鈕。

在彈出的[Create new project]對話框中設定專案名稱與專案存放位置

設定完畢後可在主視窗左半邊的[Project files]視窗看到剛加入的專案節點

接著用滑鼠點選工具列上方的[File groups and tags]→[Add file group to project]按鈕

或是透過專案節點滑鼠右鍵快顯選單中的[Add file group to project]選單選項

在彈出的開啟對話框中選取所要編輯的資源檔

所選取的資源檔節點就會出現在專案節點的下方

## 資源編輯
  
在做資源檔的編輯動作時，可直接透過滑鼠雙擊上方的Name去作更名、雙擊值的部分去改變資源值、或透過下方的Details View區塊去作修改，修改後再按下[Update in grid]更新回上方表格。

此外也可以利用上方的工具列來作資源項目的加入、更名、與刪除。

## 快速翻譯
  
可透過[Extras]→[Quick translate]點選開啟快速翻譯功能，可協助使用者作資源的翻譯。

使用上依序設定來源語言、轉換的目標語言、與所要轉換的字串，按下Translate按鈕翻譯，下方Translated text區就會顯示出翻譯的結果。

## 建立它語系資源
  
要建立它語系資源，可點選工具列上方的[Create new files]按鈕

在彈出的[Create multiple new files]對話框中，我們可以設定新的語系資源檔所要參考的資源語系、新的資源是哪種語系、是否要複製資源內容、是否自動翻譯資源內容...等，再按下[OK]按鈕。

指定的語系資源就會被建立在資源專案中

## 多語資源同時顯示編輯
  
使用資源編輯專案模式時，若有多語支援同時顯示編輯的需求，可點選工具列上方的[Start]→[Configure language columns]按鈕

在彈出的設定對話框中，依個人需求選取顯示所有語言或是顯示指定的語言，按下[OK]按鈕。

再用滑鼠雙擊點選主視窗左半邊[Project files]視窗的專案節點

主視窗右半邊就會帶出資源編輯畫面供使用者瀏覽與編輯

## Link
     Zeta Resource Editor