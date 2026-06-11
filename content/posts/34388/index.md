---
title: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: lambda"
date: "2011-08-26 12:58:26"
description: "[C++][Visual Studio]Visual studio 2010 C++0x new feature: lambda"
tags: [C++,Visual Studio]
---

Visual studio 2010為C++的開發人員新增了lambda這個C++0x的功能，為一沒有名稱的方法，也可將之稱為匿名方法。多使用於方法主題較短、方法較不常觸發或較不適合放為成員方法...等情境。

使用上類似下面這樣：

auto lambda = [](int val1, int val2)
{
return val1 + val2;
};

auto result = lambda(1,2);

這是一個很簡單的例子，設定一個lambda表示式允許接受兩個參數val1與val2，並將兩數相加後回傳。

若要指定lambda的回傳值型態，可透過在lambda後面加上"->"指定回傳的型態。

auto lambda = [](int val1, int val2) -> int
{
return val1 + val2;
};

auto result = lambda(1,2);

若是想直接使用lambda主體外的參數，可在中括號內加入"="，表示能將需要的lambda主體外的參數以傳值的方式傳入使用。

int val1 = 1;
int val2 = 2;
int result;

auto lambda = [=]() -> int
{
return val1 + val2;
};

result = lambda();

若想以傳址的方式傳入lambda主體使用，可使用"&"關鍵字，像是下面程式想在lambda主體內存取主體外的result變數，可在中括號內加入"&result"，指定result變數以傳址的方式傳入lambda主體。

int result;
auto lambda = [&result](int val1, int val2)
{
result = val1 + val2;
};

lambda(1,2);

要傳址的參數過多的話，我們也可以直接在中括號內加入"&"就好。

int result;
auto lambda = [&](int val1, int val2)
{
result = val1 + val2;
};

lambda(1,2);

若有的要傳址有的要傳值的話，可將兩者混用，像是下面這樣。

int val1 = 1;
int val2 = 2;
int result;

auto lambda = [=, &result]()
{
result = val1 + val2;
};

lambda();

## Link


Lambda Expressions in C++

Lambda Expression Syntax

Examples of Lambda Expressions