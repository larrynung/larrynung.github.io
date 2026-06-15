---
title: "[Visual Studio]Visual Studio 2010 New Feature-Breakpoint Labeling、Searching、Import/Export"
date: "2010-03-06 09:14:36"
description: "[Visual Studio]Visual Studio 2010 New Feature-Breakpoint Labeling、Searching、Import/Export"
tags: [Visual Studio]
---

這邊記錄一下VS2010在Breakpoint功能的三項改進：

1. Breakpoint Labeling
2. Breakpoint Searching
3. Breakpoint Import/Export

目前支援的版本如下：

![image_thumb_2.png](/images/posts/13902/image_thumb_2.png)

## Breakpoint Labeling

在VS2010中新增了Breakpoint Labeling新功能，允許我們對中斷點作標記的動作。

使用上我們可以在中斷點上按滑鼠右鍵，點選[Edit Labels…]。

![image_thumb.png](/images/posts/13902/image_thumb.png)

或是在中斷點視窗中，選取中斷點後按下滑鼠右鍵，點選[Edit Labels…]。

![image_thumb_1.png](/images/posts/13902/image_thumb_1.png)

系統會帶出[Edit breakpoint labels]視窗，在其中鍵入要設定的label，按下Add按鈕後關閉。

![image_thumb_12.png](/images/posts/13902/image_thumb_12.png)

![image_thumb_13.png](/images/posts/13902/image_thumb_13.png)

在中斷點視窗中就可以看到設定的Labels。

![image_thumb_14.png](/images/posts/13902/image_thumb_14.png)

若有一次設定多個中斷點Labels的需求，可在中斷點視窗中，選取多個中斷點後，按下滑鼠右鍵，點選[Edit labels…]後，設定其Labels。

![image_thumb_15.png](/images/posts/13902/image_thumb_15.png)

## Breakpoint Searching

在VS2010中新增了Breakpoint Searching新功能，允許我們在中斷點視窗，對其中的中斷點作過濾的動作。

使用上我們可以透過中斷點視窗上方的工具列，鍵入搜尋條件後按下Enter，中斷點視窗下方則會顯示過濾完後的中斷點。

![image_thumb_4.png](/images/posts/13902/image_thumb_4.png)

![image_thumb_5.png](/images/posts/13902/image_thumb_5.png)

也可以設定搜尋的欄位，只要透過[In Column]下拉選取設定。

![image_thumb_6.png](/images/posts/13902/image_thumb_6.png)

![image_thumb_7.png](/images/posts/13902/image_thumb_7.png)

若要快速的清除搜尋條件，按下後放的叉叉即可。

## Breakpoint Import/Export

Breakpoint Import/Export允許我們對中斷點作匯入與匯出的動作。

我們可對特定斷點做匯出的動作。透過在中斷點上按滑鼠右鍵，點選[Export…]。

![image_thumb_9.png](/images/posts/13902/image_thumb_9.png)

或是透過中斷點視窗，選取其中的中斷點，在中斷點上按滑鼠右鍵，點選[Export selected…]。

![image_thumb_10.png](/images/posts/13902/image_thumb_10.png)

若要匯出多個中斷點，可在中斷點視窗中，選取多個中斷點後，按下滑鼠右鍵，點選[Export selected…]。

![image_thumb_16.png](/images/posts/13902/image_thumb_16.png)

或是使用中斷點視窗的匯出工具列按鈕，匯出所有中斷點。

![image_thumb_11.png](/images/posts/13902/image_thumb_11.png)

要匯入中斷點時，透過中斷點視窗的匯入工具列按鈕，選取要匯入的中斷點匯出檔，中斷點就會被匯入進去。

![image_thumb_17.png](/images/posts/13902/image_thumb_17.png)

中斷點的匯出檔是用XML的格式來做的，有興趣的可自行開啟查閱其內容。

值得注意的是，中斷點的匯入與匯出，最好確保在專案甚至是檔案是一樣的狀況之下。

當檔案內容不一樣時，匯入的中斷點可能會在不正確的位置。而在檔案甚至專案不一樣時，中斷點匯入後，中斷點視窗仍會顯示匯入的中斷點，但在程式編輯區左側則無顯示任何的斷點，若再連點中斷點視窗的斷點，Visual Studio會發出無法跳至中斷點的錯誤。

![image_thumb_18.png](/images/posts/13902/image_thumb_18.png)

## Link

* How to: Label Breakpoints
* How to: Import and Export Breakpoints
* How to: Search the Breakpoints List
