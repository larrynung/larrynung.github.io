---
title: Consul - KV Data
date: 2018-12-17 23:15:19
tags: [Consul]
---


Consul 支援簡易的 Key-Value Store 功能。  

<!-- More -->

<br/>


可用 consul kv put 將資料存入 Key-Value Store。  

    consul kv put <Key> <Value>

{% asset_img 1.png %}

<br/>


用 consul kv get 將資料取出。  

    consul kv get <Key>

{% asset_img 2.png %}

<br/>


可加帶 -detailed 參數取出更為詳細的資料，像是 Flags、ModifyIndex...等。  

    consul kv get -detailed <Key>

{% asset_img 3.png %}

<br/>


如果要設置資料的 Flags，可在放入資料時加帶 -flags 參數指定 Flags。  

    consul kv put -flags=<Flags> <Key> <Value>  

{% asset_img 4.png %}

<br/>


{% asset_img 5.png %}

<br/>


若要列出所有存放的資料，可用 consul kv get 加帶 -recurse 參數。  

    consul kv get -recurse

{% asset_img 6.png %}

<br/>


要刪除存放的特定資料，可使用 consul kv delete 帶入要刪除的 Key。  

    consul kv delete <Key>

{% asset_img 7.png %}

<br/>


{% asset_img 8.png %}

<br/>


要刪除存放的所有資料，可使用 consul kv delete 加帶 -recurse 參數。  

    consul kv delete -recurse

{% asset_img 9.png %}

<br/>


{% asset_img 10.png %}

<br/>


儲存資料的更新跟存放是一樣的，只要用 consul kv put 帶入相同的 Key 與新的存放值即可。  

<br/>


Consul 也支援 CAS 方式的更新，先確認資料的 ModifyIndex。  

{% asset_img 11.png %}

<br/>


用 consul kv put 更新資料時，帶入 -cas 參數指定使用 Check-And-Set 的方式，帶入 -modify-index 參數指定 ModifyIndex，這樣舊只有 ModifyIndex 對得起來的命令會被成功運行。  

    consul kv put -cas -modify-index=<ModifyIndex> <Key> <Value>

{% asset_img 12.png %}

<br/>


Link
----
* [KV Data | Consul - HashiCorp Learn](https://learn.hashicorp.com/consul/getting-started/kv)
