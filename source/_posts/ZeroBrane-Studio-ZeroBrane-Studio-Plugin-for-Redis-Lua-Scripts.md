---
title: ZeroBrane Studio - ZeroBrane Studio Plugin for Redis Lua Scripts
date: 2017-04-19 00:16:51
tags: [ZeroBrane Studio]
---

要讓 ZeroBrane Studio 支援 Redis，先要取得 [redis.lua](https://github.com/pkulchenko/ZeroBranePackage/blob/master/redis.lua)。  

<!-- More -->

{% asset_img 1.png %}

<br/>


將其內容存檔。  

{% asset_img 2.png %}

<br/>


儲存到 ZeroBrane Studio 的 packages 目錄下。  

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


啟動 ZeroBrane Studio，選取 [Project|Lua Interpreter|Redis] 主選單選項，將 Lua Interpreter 切為 Redis。  

{% asset_img 5.png %}

<br/>


切完後 ZeroBrane Studio 就可以支援 Redis 的 Lua Script，像是除錯、Intellisense...等。

<br/>


第一次運行會詢問 Redis 的位置，將 Redis 位置填入設定後即可。  

<br/>


如果需要帶參數運行，也可以選取 [Project|Command Line Parameters...] 主選單選項。  

{% asset_img 6.png %}

<br/>


帶上 Redis 運行 Lua Script 所需要的 KEYS 與 ARGS。  

{% asset_img 7.png %}

<br/>


設定完後運行，指定的參數即會被帶入。  

{% asset_img 8.png %}

<br/>


Link
----
* [ZeroBrane Studio Plugin for Redis Lua Scripts](https://redislabs.com/blog/zerobrane-studio-plugin-for-redis-lua-scripts/)
