---
title: Web Deploy - Web Deploy Command Line
date: 2016-12-16 00:00:50
tags: [Web Deploy]
---

Web Deploy 支援命令列操作，在 Web Deploy 安裝完後，Web Deploy command line 程式會被放置於 `%ProgramFile%\IIS\Microsoft Web Deploy V3\` 下。  

<!-- More -->

<br/>


其 Syntax 如下：  

    msdeploy.exe 
	-verb:<verbName>              
	-source:<provider>[=<pathToProviderObject>                       
		[,<providerSetting>=<providerSettingValue>]]              
	[-dest:<provider>[=<pathToProviderObject>                       
		[,<providerSetting>=<providerSettingValue>]]              
	]              
	[-<MSDeployOperationSetting> ...]

<br/>


-verb 參數後面接的是 verb 的名稱，指定 Web Deploy 來源物件或是目的物件要處理的動作。可以是 dump、sync、delete、getDependencies、getSystemInfo。  

<br/>


-source 參數後面接的是 provider，指定來源端的資料物件。    

<br/>


-dest 參數後面接的是 provider，指定目的端的資料物件。  

<br/>


Provider 後面可以接 provider setting 針對 provider 做些設定，可以用的 provider setting 有：  

- authType
- computerName
- encryptPassword
- getCredentials
- ignoreErrors
- includeAcls
- password
- storeCredentials
- tempAgent
- userName
- wmsvc

<br/>


比較常用的為 userName、password、computerName，當要指定遠端 provider 時會用需要設定。  

<br/>


命令列最後帶的參數為 operation setting，可針對整個操做作些設定，可以使用的設定有：  

- allowUntrusted
- appHostConfigDir
- declareParam
- declareParamFile
- disableLink
- disableRule
- disableSkipDirective
- enableLink
- enableRule
- enableSkipDirective
- postSync
- preSync
- removeParam
- replace
- retryAttempts
- retryInterval
- setParam
- setParamFile
- showSecure
- skip
- unicode
- useCheckSum
- verbose
- webServerDir
- whatif
- xml
- xpath

<br/>


其中比較常用的大概就是 disableRule、enableRule、postSync、preSync、retryAttempts、retryInterval、setParam、setParamFile、useCheckSum、whatif 這幾個參數。  
