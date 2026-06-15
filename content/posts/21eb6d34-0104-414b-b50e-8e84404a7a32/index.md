---
title: "Visual Studio 2013 Preview New Feature - Enhanced Code Analysis Window"
date: "2013-11-06 12:00:00"
description: "Visual Studio 2013 Preview New Feature - Enhanced Code Analysis Window"
---

以前我們在使用Visual Studio的Code Analysis功能進行程式碼的分析時，分析出來的結果會照著程式檔名進行排序。這樣的呈現方式可能不是使用者所預期的，也不具彈性，假設今天想要針對某一個分析規則進行處理，可能就必需使用過濾功能，或是整個分析結果要掃過一遍。而在分類上這邊也只有所有結果、警告、錯誤這三種分類，以筆者來說還真的不知道何時要用這些分類(因為程式碼分析出來的應該都是警告，如果錯誤編譯時就會知道)，不像FoxCop那樣清楚，所以如果要針對特定類型的規則(像是效能相關的規則)下去處理也不太容易。

![Image(16)_thumb.png](/images/posts/21eb6d34-0104-414b-b50e-8e84404a7a32/Image(16)_thumb.png)

在Visual Studio 2013 Preview這問題獲得了改善，Code Analysis視窗開始支援排序功能。可以用規則ID、規則名稱 、檔案路徑、檔案名稱、行號、以及分類下去排序。

![Image(19)_thumb.png](/images/posts/21eb6d34-0104-414b-b50e-8e84404a7a32/Image(19)_thumb.png)

另外在分類這邊也已經可以看到跟FoxCop一樣清楚。

![Image(18)_thumb.png](/images/posts/21eb6d34-0104-414b-b50e-8e84404a7a32/Image(18)_thumb.png)
