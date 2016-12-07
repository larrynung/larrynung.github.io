---
title: Web Deploy - Web Deploy Providers
date: 2016-12-07 23:19:42
tags: [Web Deploy]
---

Web Deploy Provider 主要是用來決定來源端或是目的端的資料要怎麼處理。  

<!-- More -->

{% asset_img 1.png %}
	
<br/>


可以用的 Providers 有：  

- Web Deploy appHostConfig Provider
- Web Deploy appHostSchema Provider
- Web Deploy appPoolConfig Provider
- Web Deploy appPoolEnable32Bit Provider
- Web Deploy appPoolNetFx Provider
- Web Deploy appPoolPipeline Provider
- Web Deploy archiveDir Provider
- Web Deploy auto Provider
- Web Deploy cert Provider
- Web Deploy comObject32 Provider
- Web Deploy comObject64 Provider
- Web Deploy contentPath Provider
- Web Deploy createApp Provider
- Web Deploy dbFullSql Provider
- Web Deploy dbMySql Provider
- Web Deploy dbSqlite Provider
- Web Deploy dirPath Provider
- Web Deploy fcgiExtConfig Provider
- Web Deploy filePath Provider
- Web Deploy gacAssembly Provider
- Web Deploy gacInstall Provider
- Web Deploy iisApp Provider
- Web Deploy machineConfig32 Provider
- Web Deploy machineConfig64 Provider
- Web Deploy manifest Provider
- Web Deploy metaKey Provider
- Web Deploy package Provider
- Web Deploy recycleApp Provider
- Web Deploy regKey Provider
- Web Deploy regValue Provider
- Web Deploy rootWebConfig32 Provider
- Web Deploy rootWebConfig64 Provider
- Web Deploy runCommand Provider
- Web Deploy setAcl Provider
- Web Deploy urlScanConfig Provider
- Web Deploy webApp Provider
- Web Deploy webServer Provider
- Web Deploy webServer60 Provider

<br/>


比較常用的有 appHostConfig、appPoolConfig、contentPath、createApp、dbFullSql、manifest、package、recycleApp、runCommand 這幾個 Provider。appHostConfig Provider 主要用來做站台的處理、appPoolConfig 做 Application Pool 的處理、contentPath 做站台內容的處理、createApp 做網站應用程式建立的處理、dbFullSql 做 MsSQL 的處理、manifest 做自定義內容的處理、package 做 package 的處理、recycleApp 做 Application Pool 回收的處理、runCommand 做命令執行的處理。  
