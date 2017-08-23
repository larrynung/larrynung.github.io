---
title: Redis - LREM command
date: 2017-08-23 21:46:22
tags: [Redis]
---

LREM 命令可以用來移除 Redis List 中指定的元素值。  

<!-- More -->

<br/>


其語法如下：  

    LREM key count value

<br/>


LREM 後面帶入 List 的 Key、要刪除的元素個數、要刪除的元素值，回傳值為被移除的元素數量。  

<br/>


其中 count 值如果為正則會從頭到尾找尋符合指定值的元素移除、如果為負則會從尾到頭移除符合指定值的元素、如果為 0 則會移除所有符合指定值的元素。  

<br/>


LREM 命令的時間複雜度為 O(N)，N 為 List 的長度。  

<br/>  


雖然時間複雜度為 O(N)，但是因為該命令會由指定的方向片巡，且當移除了足夠的元素數量後就會停止遍巡，因此在某些情境下命令使用恰當的話效率其實不會到 O(N) 那麼糟。  

<br/>


像是如果準備 1 - 10000 的 List，然後用 LREM 將資料從尾部移除 1 - 10000。  

```Lua
for i=1,10000 do
redis.call('lpush', 'Test123', i)
end

for i=1, 10000 do
  redis.call('lrem', 'Test123', -1, i)
end
```

<br/>


這樣運行起來會是 0.23 s。  

{% asset_img 1.png %}

<br/>


如果反過來用 LREM 將資料從頭部移除 1 - 10000。

```Lua
for i=1,10000 do
redis.call('lpush', 'Test123', i)
end

for i=1, 10000 do
  redis.call('lrem', 'Test123', 1, i)
end
```

<br/>


運行的時間就會放大到 4.65 s。  

{% asset_img 2.png %}

<br/>


Link
----
* [LREM – Redis](https://redis.io/commands/lrem)
