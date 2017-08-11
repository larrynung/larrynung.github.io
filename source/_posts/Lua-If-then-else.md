---
title: Lua - If then else
date: 2017-08-11 23:23:44
tags: [Lua]
---

Lua 的 if 寫法如下，if 後接進入的條件，then ... end 區塊內帶入要運行的動作即可。  

<!-- More -->

```Lua
if condition then
    ... 
end
```

<br/>


如果有多個分支條件，可以用 elseif 區塊帶上另外的分支條件，或是用 else 區塊指定所有分支條件條件都不滿足時要運行的動作。  

```Lua
if condition then 
    ... 
elseif condition then
    ...
else 
    ... 
end
```

<br/>


像是要寫個簡易的程式能讓使用者輸入來決定要運行的動作，就可以像下面這樣撰寫：    

```Lua
local input
repeat
  input = io.read()
  if input == "y" then 
    print("y")
  elseif input == "n" then
    print("n")
  else
    print("unknow")
  end
until input == "exit"
```

<br/>


{% asset_img 1.png %}

<br/>


Link
---
* [Programming in Lua : 4.3.1](https://www.lua.org/pil/4.3.1.html)
