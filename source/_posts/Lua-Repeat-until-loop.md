---
title: Lua - Repeat until loop
date: 2017-08-10 23:07:24
tags: [Lua]
---

Lua 的 repeat until 寫法如下，repeat until 區塊內帶入要運行的動作，until 後帶上要跳脫迴圈的條件即可。  

<!-- More -->

```Lua
repeat
  ...
until condition
```

<br/>


像是要簡單的跑迴圈五次，然後印出 1 到 5 的數值，就可以像下面這樣撰寫：  

```Lua
local idx = 1
local count = 5
repeat
  print(idx)
  idx = idx + 1
until idx > count
```

<br/>


{% asset_img 1.png %}

<br/>


Link
----
* [Programming in Lua : 4.3.3](https://www.lua.org/pil/4.3.3.html)
