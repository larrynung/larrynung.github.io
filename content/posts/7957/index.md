---
title: "[WCF]認識WCF"
date: "2009-04-10 12:37:51"
description: "[WCF]認識WCF"
tags: [WCF]
---

## ![image_thumb.png](/images/posts/7957/image_thumb.png)

## 需求

* .NET Framework 3.0以上

## 特點

* 單一的分散式服務架構
* 合約(Contract)驅動
* 以組態作業為基礎

## 通訊技術

* WS-* protocols
* Message Queuing (MSMQ)
* .NET Remoting
* Socket-based Communication
* POX
* Basic,ASMX Web services

## 優點

* 使用統一的程式設計技巧提供多種分散式通訊服務。
* 建立/使用WCF服務時，可不用考慮WCF服務的Host環境。

## 支援的四種型式合約(Contract)

* ServiceContract-定義用戶端可呼叫的服務
* DataContract-定義用戶端與伺服器端的資料交換格式
* MessageContract-定義SOAP訊息的格式
* FaultContract-宣告服務功能執行失敗會引發的例外

![image_thumb_1.png](/images/posts/7957/image_thumb_1.png)
