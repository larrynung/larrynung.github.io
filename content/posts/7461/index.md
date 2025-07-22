---
title: "[Performance][VB.NET].NET空字串判斷徹底研究"
date: "2009-03-13 08:49:01"
description: "[Performance][VB.NET].NET空字串判斷徹底研究"
tags: [Performance,VB.NET]
---

.NET下的空字串判斷整體來說大概可分為下列幾種方法：
用 is Nothing 判斷。e.x. If str Is Nothing用 = Nothing 判斷(類別中只有字串可以用 = Nothing 來判斷)。e.x. If str = Nothing用 = "" 判斷。e.x. If str = ""用 = String.Empty 判斷。e.x. If str = String.Empty用 Is String.Empty 判斷。e.x. If str Is String.Empty用 String.IsNullOrEmpty(str) 判斷。e.x. If String.IsNullOrEmpty(str)用 String.Length = 0 判斷。e.x. If str.Length = 0

上述所列出的空字串判斷方法，其所跑出的效果不盡相同，為了看出其差異性，這邊撰寫了簡單的測試程式如下：

執行結果如下圖所示：

由上圖可知， "" 與 String.Empty 結果是一樣的。比較有趣的是，當字串值是""與String.Empty時， str is Nothing 是不會成立的，但是 str = Nothing 卻會成立。而當字串參考是 Nothing 時，str is string.Empty 不成立、 str = string.Empty 成立。這是因為當使用=運算子判斷時，Nothing 、 "" 與 String.Empty 是被視為一樣的，才會造成此有趣的現象。

接著我們來比較一下空字串判斷的執行速度，同樣的我們須撰寫如下測試程式：

執行結果如下：

從上圖可看出幾個現象
用String.IsNullOrEmpty同時判斷Nothing與空字串會比只判斷是否為 Nothing 或為空還慢當字串不為 Nothing 時要判斷字串是否為空的話，用Is String.Empty去判斷最快(文件上通常是說String.Length = 0最快)

接著再看個實驗來看當同時判斷Nothing與空字串的情況，測試程式如下：

執行結果如下：
 可以看出 String.IsNullOrEmpty 函式的效能與自行混用 str Is Nothing 與 Is String.Empty 判斷方法來達到相同目的的效能差不多。
經過以上三個實驗，對於字串為空的判斷相信已有相當的了解，若能清楚分辨其功用與使用的時機，多少都能增進程式的效能。像是使用上若只需判斷Nothing或為空的話，應避免誤用會同時判斷的方法(如下例)，就可以避免不必要的OverHead。