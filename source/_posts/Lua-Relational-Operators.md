---
title: Lua - Relational Operators
date: 2017-08-02 22:34:53
tags: [Lua]
---

Lua 的 Relational operators 有 ==、~=、<、>、<=、>=，這些運算符可用來處理兩者間的關係，其運算結果都為布林值，不是 true 就是 false。

<!-- More -->

| Operator | Description | 
|:-------------:|:-------------:|
| == | 用來判斷前者與後者是否相等 |
| ~= | 用來判斷前者與後者是否不相等 |
| < | 用來判斷前者是否小於後者 |
| > | 用來判斷前者是否大於後者 |
| <= | 用來判斷前者是否小於等於後者 |
| >= | 用來判斷前者是否大於等於後者 |

<br/>


使用起來就像下面這樣：  

```Lua
print(1 == 2)
print(1 ~= 2)
print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)
``` 

<br/>


{% asset_img 1.png %}

<br/>


Link
----
* [Lua 5.1 Reference Manual](http://www.lua.org/manual/5.1/manual.html#2.5.2)
