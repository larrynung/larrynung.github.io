---
title: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: auto"
date: "2011-08-23 12:39:30"
description: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: auto"
tags: [C++,Visual Studio]
---
Visual studio 2010為C++的開發人員新增了auto這個C++0x的功能，讓變數宣告時的型態能由編譯器自動判別，自動依照初始值的型態去決定變數的型態，使得複雜的類型宣告能有更簡單的宣告方式。雖然變數的型態是由初始值判斷，但是是編譯時期所作的處理，在編譯到MSIL時就會用正確的型態去替換，故不會影響程式運行的效能，也是型別安全的編程方式。這也就是C#與VB.Net領域在.Net 3.0所提供的區域型別推斷功能。

使用的語法如下:

auto declarator initializer;

使用auto關鍵字宣告變數，宣告的同時需指定初始值，如此編譯器才能從初始值推斷出變數的型別。因此auto不能用來宣告陣列、做為函式的回傳值、方法或 樣板的參數。

最後來看個範例加深印象：

// test auto.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include
#include
#include

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
auto x = 1, *y = &x, **z = &y; // Resolves to int.
auto a(2.01), *b (&a); // Resolves to double.
auto c = 'a', *d(&c); // Resolves to char.
auto m = 1, &n = m; // Resolves to int.

map> mapObj;
map>::iterator i1 = mapObj.begin();
auto i2 = mapObj.begin();

auto lambda = []()->int
{
return 0;
};
return 0;
}

##
Link

VS2010 中的 C++ 0x 新特性：Lambdas、auto 和 static_assert

C++0x: auto 和 decltype

C++ 語法再加強：C++0x

auto Keyword (Type Deduction)