---
title: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: decltype"
date: "2011-08-30 12:55:08"
description: "Visual studio 2010為C++的開發人員新增了decltype這個C++0x的功能，能根據所給的運算式決定型別，使用時只要在decltype關鍵字後面用小括號圍住要判斷的運算式，即可推斷出運算式回傳的型態，並加以進一步去做些處理。"
tags: [Visual Studio,C++]
---

Visual studio 2010為C++的開發人員新增了decltype這個C++0x的功能，能根據所給的運算式決定型別，使用時只要在decltype關鍵字後面用小括號圍住要判斷的運算式，即可推斷出運算式回傳的型態，並加以進一步去做些處理。

```c
decltype( expression )
```

像是下面這個例子就非常的簡單，程式宣告了整數變數a，而變數b的型態我們想由a去推斷，可以像下面這樣撰寫:

```c
int a;
decltype(a) b;
decltype(Test()) c;
decltype(Test() + 1) d;
```

這樣的型態判別動作跟區域型別推斷一樣是由Compile完成的，在編譯器中可以直接看到宣告的型態，運行階段不會產生額外的性能耗費。

![image_thumb_3.png](/images/posts/34737/image_thumb_3.png)

decltype關鍵字還能更進一步的與auto一起使用，簡化 template 函式的開發，撰寫上會像下面這樣的形式：

```c
auto function_name( parameters ) −> decltype( expression ) { function_body; }
```

這樣撰寫的好處是方法的回傳值是由運算式去決定的，以下面的例子來看方法的回傳值是x + y後回傳的型態。

![image_thumb_2.png](/images/posts/34737/image_thumb_2.png)

在開發上若是能善用這樣的功能，搭配template下去開發，能為開發人員減少不少的工作量。
