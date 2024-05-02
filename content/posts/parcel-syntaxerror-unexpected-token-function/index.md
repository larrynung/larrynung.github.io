---
title: "'Parcel - SyntaxError: Unexpected token function'"
date: "2017-12-24 23:49:23"
tags: [Parcel]
---


使用 Parcel 時若發生 SyntaxError: Unexpected token function 錯誤。  

<!-- More -->


![1.png](1.png)

<br/>


這是因為 Parcel 用到了 Node.js 8.x 的語法，確認 Node.js 是否已更新到指定版本，更新完後即可正常運行。  

![2.png](2.png)

<br/>


Link
----
* [🐛 about SyntaxError: Unexpected token function · Issue #244 · parcel-bundler/parcel · GitHub](https://github.com/parcel-bundler/parcel/issues/244)
* [parcel 錯誤：SyntaxError: Unexpected token function - JJC 前端進階- SegmentFault](https://segmentfault.com/a/1190000012392912)
