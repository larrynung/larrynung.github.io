---
title: Redis - Generate Snowflake generator id with client info
date: 2019-10-07 07:36:15
tags: [Redis, Snowflake]
---

在做分散式系統時，有些情境下免不了要給節點維一的識別號，像是在用 Snowflake 分散式 Id 演算法時會需要給予 10 bit 長的 Generator id，用以避免 Id 碰撞。

<!-- More -->

</br>


識別號有的會直接取 IP 某段，或是 Process no，這樣並不能確保值的唯一。要確保維一只能依賴自行靠設定將設定值錯開，或是設計一個演算法配給。  

</br>


若是搭配 Redis 使用，最直覺的演算法可能就是在每個服務實體啟動時去 Redis 註冊一個唯一的識別值，服務實體與識別值的資訊都放置在 Redis 中，並設有過期時間。每個服務定時到 Redis 延長過期時間，如果資訊過期，則對應的識別碼要釋出給新服務用。  

</br>


上面的演算法很直覺，但有兩點較大的問題，一個是實作上很麻煩，一個是定時到 Redis 延長過期時間的做法對系統來說不是很好。好在 Redis 有維護每個連線的 Client 資訊，也都取的到，透過 Redis client 的資訊實作上會簡單許多，對系統來說處理也比較沒那麼吃重。  

</br>


舉個例子來說，假設我用 Redis 的 Hash 來實作，Key 假定為 generator，裡面的 field 用來放 Generator id，value 用來放 Redis client 的 Id。  

```
generator =>
{
    {$generator-id, $redis-client-id},
    ...
}
```

</br>


這樣在第一個服務上線時，Redis 內的資料是空的。  

```
generator =>
{
}
```

</br>


這時透過 Redis 命令 CLIENT LIST 取得所有連線的 Id，與 CLIENT ID 命令取得當前連線的 Id，就可以去更新並配給 Generator id。像是所有連線 Id 問回來只有一個連線，且連線 Id 跟當前連線 Id 一樣都是 0，就會將 Generator id 0 配給 Redis client 0。  

```
generator =>
{
    {0, 0}
}
```

</br>


當第二個服務上線，Redis 有兩個連線，當前連線 Id 為 1，則將 Generator id 1 配給 Redis client 1。

```
generator =>
{
    {0, 0},
    {1, 1}
}
```


當第三個服務上線時，假設第一個服務也斷線了，透過 Redis 命令 CLIENT LIST 取得所有連線的 Id 得到 1 跟 3。得知連線 0 已經下線，故將 Generator id 0 可配給 Redis client 3。


```
generator =>
{
    {0, 3},
    {1, 1}
}
```
