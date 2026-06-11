---
title: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: nullptr"
date: "2011-08-24 01:01:59"
description: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: nullptr"
tags: [Visual Studio,C++]
---

Visual studio 2010為C++的開發人員新增了nullptr這個C++0x的功能，用以表示空的指標位置，取代原先我們所使用的NULL，將空指標和整數0 的概念拆開，會有這樣的功能提出是因為以前用NULL來做空指標的處理時，由於NULL的定義為整數0，並非是真的空指標型態，所以在某些特定的狀況下使用會錯亂。

/* Define NULL pointer value */
#ifndef NULL
#ifdef __cplusplus
#define NULL 0
#else
#define NULL ((void *)0)
#endif
#endif

像是下面這個範例帶入NULL，我們預期運行到參數為int*型態的多載方法。

...
void Test(int* value)
{
cout

using namespace std;

void Test(int* value)
{
cout << "void Test(int* value)
";
}

void Test(int value)
{
cout << "void Test(int value)
";
}

int _tmain(int argc, _TCHAR* argv[])
{
Test(NULL);
Test((int*)NULL);
Test(nullptr);
return 0;
}

運行結果如下：

## Link


C++0x：static_assert 和 nullptr

C++0x features in VC2010 - nullptr

C++0x: nullptr

C++0x：static_assert 和 nullptr

C++0x - nullptr