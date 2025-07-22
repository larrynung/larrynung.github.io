---
title: "[Visual Studio]追蹤點(Tracepoint)的使用"
date: "2009-11-04 08:38:52"
description: "[Visual Studio]追蹤點(Tracepoint)的使用"
tags: [Visual Studio]
---

## 追蹤點的設定與使用
  
追蹤點在使用上跟中斷點一樣簡單。在一般的情況下，欲設定追蹤點，我們只需在欲追蹤的地方按下滑鼠右建，點選Breakpoint，接者再點下Insert Tracepoint即可。

若是在欲設定中斷點的地方，已經有設定了中斷點。設定的追蹤點的方式就會變為要透過[When Hit…]功能來叫起視窗設定。

當做完上述動作後。如下圖，追蹤點的設定視窗即會彈出。

透過彈出的設定視窗，我們可以設定我們想要追蹤的訊息。除了內建的$ADDRESS、$CALLER、$CALLSTACK、$FUNCTION、$PID、$PNAME、$TID、與$TNAME等系統資訊可供顯示外。若想要顯示的是程式中的變數或是運算，我們可以也透過"{"與"}"把想要顯示的資訊包住，來追蹤我們想看的資訊。像是： 

設定完後，可看到追蹤點在編輯環境中是用菱形來表示。
               
除錯時，我們可以透過輸出視窗、或是即時運算視窗，查看我們所設定欲追蹤的資訊。

## 同時使用中斷點與追蹤點
  
若要同時使用中斷點與追蹤點的功能，只需注意需勾選[Print a message] ，並取消勾選[Continue execution]即可。

## 設定追蹤點觸發條件
  
Visual Studio內建有三種觸發條件可供設定。若要設定追蹤點的觸發條件，我們可以在追蹤點上按滑鼠右鍵，選取預設定的項目選單來做設定。

選取[Condition…]選單選項。

選取後，會彈出如下[Breakpoint Condition]設定視窗。可透過該視窗設定觸發的條件。

設定完後追蹤點的菱形圖示會外加個加號在上面。

選取[Hit Count…]選單選項，會彈出如下[Breakpoint Hit Count]設定視窗。可透過該視窗設定第幾次進入時才觸發。 

選取[Filter…]選單選項，會彈出如下[Breakpoint Filter]設定視窗。可透過該視窗設定哪個Process、哪個機器名稱、哪個執行緒才觸發。 

## 檢視追蹤點設定值
  
要檢視追蹤點的設定值，我們可以把滑鼠移至追蹤點的上方。此時會顯示出如下浮動視窗，透過該浮動視窗，我們可以檢視目前的設定。

## 設定訊息顯示視窗
  
追蹤點的訊息可以顯示在Ouput或是Immediate視窗。可以透過[Tools]→[Options…]叫出[Options]設定視窗，並勾選[Debugging]→[Redirect all Output Window text to the Immediate Window]來把訊息導到Immediate視窗、或是取消勾選把訊息留在輸出視窗。

## Link
     Visual Studio 2005除錯功能概覽(1) (N050103601)    [ASP.NET]Visual Studio的BreakPoint與TracePoint功能