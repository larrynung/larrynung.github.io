---
title: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (四) Contract.ForAll amp; Contract.Exists"
date: "2010-09-20 05:32:47"
description: ".NET 4.0 New Feature - 程式碼合約(Code Contracts) (四) Contract.ForAll &amp; Contract.Exists"
tags: [CSharp]
---

為了方便處理集合類型變數的合約驗證，Code Contracts貼心的提供了Contract.ForAll與Contract.Exists兩個輔助用的合約方法，可與前置條件或後置條件搭配使用。

## Contract.ForAll

Contract.ForAll合約方法可用來判斷集合內部的所有項目是否皆滿足所要驗證的條件，其運作規則如下：

-
集合內任何元素帶入運算為False=>ForAll動作停止，回傳False

-
集合內所有元素帶入運算皆為True=>回傳True

撰寫時可用Contract.ForAll方法表示，主要有下列兩個多載函式：

<img alt="clip_image001" border="0" height="125" src="\images\posts\17822