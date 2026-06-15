---
title: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: rvalue reference"
date: "2011-09-01 01:24:16"
description: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: rvalue reference"
tags: [Visual Studio,C++]
---

Visual studio 2010為C++的開發人員新增了rvalue reference這個C++0x的功能，主要是用來解決過多臨時變數的問題，讓開發人員可以寫出更有效率的 C++ 程式碼。

rvalue reference又稱為右值引用，是沒有名稱的臨時變數，在記憶體上沒有固定的位址，這邊可以從大家最熟悉的字串串接來看：

```c
string str1 = "123";
string str2 = "456";
string str3 = str1 + str2 + "789" + "101112";
```

以上面這個例子來說，大家都知道在自串串接時會有臨時變數的耗費，也就是在上面程式中的str1 + str2那邊會先將變數的串接完的值存在一個臨時的變數。這邊談到的概念可參閱string類別的+運算子實作。

![image_thumb.png](/images/posts/34975/image_thumb.png)

這樣的問題在運算頻繁時會更加嚴重。而若是這樣的臨時變數能讓我們引用，利用臨時變數的引用重覆去運算，可有效的改善這樣的問題，rvalue reference就是這樣的技術。

rvalue reference在使用上跟以前我們使用的lvalue reference類似，lvalue reference是用&去取得引用，而rvalue reference是用&&去取得引用。rvalue reference在Visual Studio 2010已經整入至標準函式庫內，故可直接參閱標準函式庫的做法，像是在string類別內就有用rvalue reference去實作新的+運算子。

![image_thumb_1.png](/images/posts/34975/image_thumb_1.png)

## Link

* A Brief Introduction to Rvalue References
* VC2010中的C++0x特性Part 2：右值引用
