---
title: "SonarQube - Manual setup plugins"
date: "2017-03-16 23:49:23"
tags: [SonarQube]
---


SonarQube 有些套件未放置在 Update Center，無法透過 Update Center 進行安裝，必須自行手動安裝。  

<!-- More -->

<br/>


這邊以 PL/SQL Cop 的 SonarQube 套件為例做個示範，先將套件下載下來。  

![1.png](1.png)

<br/>


將下載的套件放置於 `extensions\plugins` 下(不用解壓縮)。  

![2.png](2.png)

<br/>


接著將 SonarQube 的服務重啟。  

![3.png](3.png)

<br/>


重啟後安裝的套件即會生效。因為多半的套件會有設定頁面，像是這邊示範的 PL/SQL Cop 套件就有，所以可以先從設定頁面這邊做個初步的確認。  

![4.png](4.png)

<br/>
