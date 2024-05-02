---
title: "NuGet - Create and publish a package with dotnet CLI"
date: "2021-02-18 08:17:51"
tags: [NuGet]
---


要建立 NuGet 套件，需先確認專案檔內有設計 NuGet 套件所需之資訊，像是套件識別碼、版本、作者、公司等。  

<!-- More -->

<br>


```xml
<PackageId>AppLogger</PackageId>
<Version>1.0.0</Version>
<Authors>your_name</Authors>
<Company>your_company</Company>
```

![1.png](1.png)

<br>


然後可用 dotnet pack 命令將套件打包。  

    dotnet pack

![2.png](2.png)

<br>


或是在專案檔內加設定 GeneratePackageOnBuild，讓專案在建置時自動產生。  

```xml
<GeneratePackageOnBuild>true</GeneratePackageOnBuild>
```

![3.png](3.png)

<br>


![4.png](4.png)

<br>


然後確定 NuGet 帳號已註冊且取得 API key。  

![5.png](5.png)

<br>


![6.png](6.png)

<br>


![7.png](7.png)

<br>


再調用 dotnet nuget push，帶入 NuGet 套件檔的位置及 NuGet API key。  

    dotnet nuget push $package -k $key -s https://api.nuget.org/v3/index.json

![8.png](8.png)

<br>


NuGet 套件即會被上傳至 NuGet server 上。  

![9.png](9.png)

<br>


![10.png](10.png)

<br>


Link
====
* [使用 dotnet CLI 建立及發佈 NuGet 套件 | Microsoft Docs](https://docs.microsoft.com/zh-tw/nuget/quickstart/create-and-publish-a-package-using-the-dotnet-cli)
