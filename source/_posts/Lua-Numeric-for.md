---
title: Lua - Numeric for
date: 2017-08-06 23:20:34
tags: [Lua]
---

Lua numeric for 的語法如下，for 後面設定迴圈內要使用的變數，變數後面用等號帶上數值的起點、終點、遞增/減值  設定值間用逗號隔開，然後用 do...end 設定迴圈的區塊，在迴圈的區塊內帶入要運行的動作即可。    

<!-- More -->

```Lua
    for var=from,to[,step] do
      something
    end
```

<br/>


像是要簡單的跑迴圈五次，然後印出 1 到 5 的數值，就可以像下面這樣撰寫：  

```Lua
for i=1,5 do
  print(i)
end
```

{% asset_img 1.png %}

<br/>


若是要跑迴圈印出 1、3、5，可像下面這樣調整遞增條件：  

```Lua
for i=1,5,2 do
  print(i)
end
```

{% asset_img 2.png %}

<br/>


Link
----
* [Programming in Lua : 4.3.4](https://www.lua.org/pil/4.3.4.html)
