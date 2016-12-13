---
title: Web Deploy - Web Deploy Rules
date: 2016-12-13 23:23:28
tags: [Web Deploy]
---

Web Deploy 提供許多不同的 Rule，像是：  

<!-- More -->

- AboFilter 
- AnonymousUser 
- ApplicationExistsRule 
- AppPoolIdentity 
- AppRootNormalize 
- BlockHarmfulDeleteOperations 
- BlockUnsupportedDeleteOperations 
- ClassicAppPoolProtectRule 
- CreateApplicationRule 
- CrossPlatformRule 
- DependencyCheckAppPoolExists 
- DependencyCheckFailOnError 
- DependencyCheckFailOnWarning 
- DependencyCheckInUse 
- DoNotDeleteRule 
- EnvironmentVariableNormalize 
- IgnoreFileLastWriteTime 
- IISConfigFrom64To32 
- MetakeyToIIS6 
- Parameterization 
- SchemaSection 
- SkipInvalidSource 
- SkipNewerFilesRule 
- SkipUNC 
- SyncGeneral 
- SyncXP 
- UrlScanSkipIncompat 
- WarnForEncryptedDataRule 
- XpIsapis 

<br/>


這些 Rule 能讓我們更改 sync operation 的行為。  

<br/>


這些 Rule 中以 DoNotDeleteRule 較常使用，能用來決定 sync 時是否刪除多餘的檔案。  

<br/>

Link
----
* [Web Deploy Rules](https://technet.microsoft.com/en-us/library/dd568992(v=ws.10).aspx)
