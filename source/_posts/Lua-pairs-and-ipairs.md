---
title: Lua - pairs and ipairs
date: 2017-08-08 22:33:05
tags: [Lua]
---

Lua 內的 ipairs 可用來遍巡處理陣列，如果遍巡到非陣列元素，或是空值的話，遍巡動作即會中止。  

<!-- More -->

<br/>


所以像下面這樣的程式就不會將所有元素印出。  

```Lua
local data = {}
data[1] = "Value1"
data[2] = "Value2"
data[4] = "Value4"
data.Key1 = "Value4"
for x, y in ipairs(data) do
  print("( " .. x .. ", " .. y .." )")
end
```

{% asset_img 1.png %}

<br/>


若是使用 pairs，則可遍巡所有元素。   

```Lua
local data = {}
data[1] = "Value1"
data[2] = "Value2"
data[4] = "Value4"
data.Key1 = "Value4"
for x, y in pairs(data) do
  print("( " .. x .. ", " .. y .." )")
end
```


{% asset_img 2.png %}

<br/>

