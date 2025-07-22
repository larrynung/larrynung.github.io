---
title: "[Visual Studio]Visual Studio 2010 New Feature - DataTips"
date: "2010-03-15 06:08:11"
description: "[Visual Studio]Visual Studio 2010 New Feature - DataTips"
tags: [Visual Studio]
---

VS2010在DataTips上也做了些改進，像是允許我們把DataTips給釘在相關的程式上、或是匯入匯出DataTips等。

## Pin DataTips
  
要把DataTips給釘在程式相關的程式中，我們可以在除錯運行被中斷的狀態，把滑鼠移到要觀看的變數上面，然後在浮現的DataTips後方，點選圖釘圖示。

或是直接在程式碼的變數上按右鍵，點選[Pin To Source]。

DataTips釘住後，可以看到程式碼前方會出現圖釘圖示，後方的DataTips會用浮動的狀態持續的顯示。

重複上述動作，我們可以在同一行程式加入多個DataTips浮動框 。

此外，我們也可以在已開啟的DataTips浮動框上，按下滑鼠右鍵，點選[Add Expression]。

輸入要加入的DataTips Expression，就可以把多個DataTips加到同一個DataTips浮動框。

若是不小心在錯誤的位置釘上了DataTips，可以直接用滑鼠拖曳著上下移動，DataTips浮動框會隨著拖曳變更釘住的位置。

在除錯狀態停止後，DataTips浮動框會消失不見，前方的圖釘圖示仍會持續顯示。當把滑鼠游標移至前方的圖釘圖示，DataTips浮動框會浮現出來，順帶會顯示上次除錯的狀態。

## Set DataTips Comment
  
若是有要注意或要提示的事宜想要標註，VS2010也允許我們為DataTips加入對應的註解，只要把滑鼠移至DataTips浮動框上方，在浮現出來的控制列上，選取最下方的按鈕把Comments展開。

在展開的Comments欄位中，鍵入DataTips對應的註解即可。

若後來覺得DataTips註解礙眼，也可以透過點選同樣的控制列按鈕，把DataTips註解摺疊隱藏。

## Arrange DataTips
  
VS2010的DataTips也支援排列的功能，若某行的DataTips被擺放的很凌亂，影響到程式的閱讀，我們可以透過VS2010的DataTips排列功能，做自動的排列整理。

只要在程式碼前方的圖釘圖示按下滑鼠右鍵，在彈出的快顯選單中，點選Arrange。

該行的DataTips就會被自動排列整理。

## UnPin DataTips
  
DataTips在VS2010除了可以釘在相關的程式碼外，也可以不跟程式碼綁住，而是像便利貼一樣隨處擺放。只要把滑鼠移至釘住的DataTips浮動框，選取中間的控制列按鈕，把DataTips浮動框的圖釘給拔起。

DataTips浮動框就會變得像是便利貼一樣，就像是一個Memo，而與程式無直接對應的關係。

## Clear DataTips
  
可以增加DataTips，自然也可以移除不用的DataTips。在DataTips的移除上，可以一次移除全部，也可以只移除特定的DataTips。

在移除全部上，我們可以透過滑鼠點選[Debug]→[Clear All DataTips]，把專案中所有的DataTips給移除。

或是透過滑鼠點選[Debug]→[Clear All DataTips Pinned to Form1.cs]，把檔案中所有的DataTips給移除。

而在移除指定的DataTips上，可在除錯運行的狀態下，透過DataTips浮動框工具列上的Close按鈕。

或是在程式碼前方的圖釘圖示上按下滑鼠右鍵，點選Clear，來清除指定的DataTips。

##  
  
## Import/Export DataTips
  
DataTips也支援匯出與匯入的動作。若要匯出DataTips，可透過滑鼠點選[Debug]→[Export DataTips…]，把專案中的DataTips給匯出成Xml檔。

匯入時，可透過滑鼠點選[Debug]→[Import DataTips…]，把之前匯出的Xml檔給匯入進來。

值得注意的是，DataTips的匯入與匯出動作看起來跟BreakPoint的處理一樣，只看檔名與行數，因此使用上必須確保檔案是一致的，不然可能會造成DataTips的位置不正確的情況，或是造成錯誤的發生。

## Link
     [VS2010 Online]在VS2010中的筆記本 – DataTips 以及 BreakPoint 新功能介紹     PIN A DATATIP TO SOURCE – VSTIPDEBUG0005     CLEARING YOUR DATATIPS – VSTIPDEBUG0014     IMPORT AND EXPORT DATATIPS     DATATIP VALUE FROM THE LAST DEBUG SESSION     ADDING COMMENTS TO A DATATIP – VSTIPDEBUG0007     CREATE A FLOATING DATATIP -- VSTIPDEBUG0006