---
title: "[Performance][C#]List V.S SortedList"
date: "2009-03-27 11:51:26"
description: "[Performance][C#]List V.S SortedList"
tags: [Performance,CSharp]
---

之前有看到網路文章介紹SortedList類別，該類別使用方式類似HashTable，也是由Key跟Value所組成的字典類別，而與其它字典類別最大的差異就在於SortedList類別會自動排序。

但我實在很難想到這種Key跟Value的組合有啥排序的必要性，因為通常這種字典類別都是直接把Key帶入用以取得Value。而這種用法實在沒排序之必要性，除非要列出所有的配對資料。

而我想應該也有滿多的人是直接把SortedList當作會自動排序的List用而已吧。這篇主要就是針對"把SortedList當作會自動排序的List用"的作法來做一些比較與探討。

廢話不多說，直接看例子： 

執行後的結果如下：

統計一下測試資料

由執行的結果我們可以看出，若程式的需求非每插入一筆就要排序好資料的話，在筆數少的情況下，用SortedList來作效率會較高，筆數高的話則把資料全部插入List後再用Sort排序反而有更好的效率。若程式的需是每插入一筆就要排序好資料的話(有興趣的可把上面範例的ListTest中Sort改為用迴圈內的)，不論筆數多寡都是用SortedList來作效率最好。

      非每插入一筆就要排序好

      每插入一筆就要排序好

      筆數少

      SortedList

      SortedList

      筆數多

      List+Sort

      SortedList