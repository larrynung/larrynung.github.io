---
title: Lua - Assignment
date: 2017-08-13 11:22:45
tags: [Lua]
---

Lua 的賦值語法如下：  

<!-- More -->

```Lua
variable1[, variable2 ...] = value1[, value2 ...]
```

<br/>


簡單說就是先寫要被賦值的變數，接著帶上賦值運算子 =，然後再帶入要賦予的值即可。像是下面這樣：

```Lua
local a = 1
local b = 2
print(a)
print(b)
```

<br/>


{% asset_img 1.png %}

<br/>


若要一次賦予多個變數，可用逗號隔開帶上數個要被賦值的變數與要賦予的值。  

```Lua
local a, b = 1, 2
print(a)
print(b)
```

<br/>


{% asset_img 2.png %}

<br/>


賦值語法也可以拿來做數值的交換。  

```Lua
variable1, variable2 = value2, value1
```

<br/>


像是下面這樣：  

```Lua
local a, b = 1, 2
a, b = b, a
print(a)
print(b)
```

<br/>


{% asset_img 3.png %}

<br/>


Link
----
* [Programming in Lua : 4.1](https://www.lua.org/pil/4.1.html)
