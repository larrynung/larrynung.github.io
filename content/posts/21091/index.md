---
title: "[Software][.NET Resource]ManagedSpy"
date: "2011-01-27 10:45:18"
description: "[Software][.NET Resource]ManagedSpy"
tags: [Software,.NET Resource]
---

相信很多開發人員都有用過Spy++這套工具，在非.NET程式我們可以透過Spy++去追到視窗的名稱、Handle...等資訊，但在.NET程式Spy++就不能用了，就算能用也不合用。因為對於.NET程式人員來說Handle等資訊已經不是他們想要關心的了，他們想關心的是介面的組成架構、屬性、與事件，ManagedSpy即為一個能提供這些資訊的輔助工具。啟動後會看到如下介面，程式會自動偵測電腦開啟的Managed程式，若要重新搜尋開啟的Managed程式，可透過上方工具列的重新整理按鈕。

若有找到的程式會在左半邊用樹狀節點顯示其組成架構，可以藉此知道界面是由哪些元件所組成，而在右側則是會顯示其選取物件的屬性。

若是左側元件過多無法判別是否為想要觀察的元件，可以在左側樹節點上方點選滑鼠右件，點選[Show Window]滑鼠右鍵快顯選單。

對應的元件就會出現短暫的藍色框框閃爍。

若有需要，你可以在執行階段透過ManagedSpy動態改變元件的屬性，並觀察其變化。

若要觀察應用程式的事件驅動是否正常，或是想了解會觸發的事件與事件觸發的順序，也可以透過上方工具列的第一個過濾按鈕設定所要觀察的事件。

並按下上方工具列的執行按鈕，開始監控.NET應用程式的事件觸發。

## Download
  ManagedSpy.exe  

## Link
     Deliver The Power Of Spy++ To Windows Forms With Our New Tool     MANAGED SPY：用我們的新工具繼續Spy++對Windows Forms的神話