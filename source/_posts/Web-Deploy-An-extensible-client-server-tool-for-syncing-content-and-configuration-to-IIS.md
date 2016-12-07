---
title: >-
  Web Deploy - An extensible client-server tool for syncing content and
  configuration to IIS
date: 2016-12-06 23:43:08
tags: [Web Deploy]
---

Web Deploy 是一 client-server 架構的工具程式，能用來同步 IIS 內容與設定，簡化網頁應用程式或是網站的佈署。  

<!-- More -->

{% asset_img 1.png %}

<br/>


具有以下幾個特點：  

- 與 IIS Manager、Visual Studio 無縫整合，能建立 package 並佈署到本地或是遠端機器
- 整合 WebMatrix
- 與 Web Platform Installer 無縫整合
- 網頁應用程式打包
-- 能夠打包網頁應用程式或是整個站台，包含關聯的資料庫
-- 能夠打包 ACLs、COM、GAC 與註冊檔設定
-- 支援 live 伺服器與壓縮後的 package 當成來源或是目的端
- 網頁應用程式佈署
-- 支援非 Admin 權限的網頁應用程式佈署
-- 支援參數化佈署，能在佈署時替換檔案中的字串
-- 整合 IIS Web Management Service 做非 Admin 的佈署
- 網站伺服器同步
-- 能夠同步整個網頁伺服器、網頁站台、或是網頁應用程式
-- 只同步變動的資料
-- 能夠在同步時偵測遺失的 dependencies
-- 同步時自動收集 IIS 設定、SSL certificates、與 ASP.NET 設定
- 變動前自動備份站台
-- 管理員可以設定啟用自動備份
-- 使用者可以直接還原站台
- 支援 CommandLine、PowerShell Cmdlets、與 API

<br/>


Web Deploy 在運作上如下圖所示：  

{% asset_img 2.png %}

<br/>


可以看到來源端與目的端都有許多的 Provider，這些 Provider 能針對 Dump、Sync、Delete 等操作有著各自不同的處理方式。這些 Provider 彼此可以搭配使用，達到更多不同的效果。  

<br/>


另外要注意到的是，來源端與目的端電腦之間有兩條可供連線的路，一條是透過 Remote Agent Service，一條是透過 Web Management Service。透過 Remote Agent Service 這條路需使用 Admin 的帳號，若是非 Admin 帳號就要走 Web Management Service 這條路。這兩條路在使用上必須要有所了解，安裝設定或是發生問題時才能知道要怎麼處理。    
