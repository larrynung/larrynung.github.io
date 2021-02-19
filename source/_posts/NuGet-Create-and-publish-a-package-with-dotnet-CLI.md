---
title: NuGet - Create and publish a package with dotnet CLI
date: 2021-02-18 08:17:51
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

{% asset_img 1.png %}

<br>


然後可用 dotnet pack 命令將套件打包。  

    dotnet pack

{% asset_img 2.png %}

<br>


或是在專案檔內加設定 GeneratePackageOnBuild，讓專案在建置時自動產生。  

```xml
<GeneratePackageOnBuild>true</GeneratePackageOnBuild>
```

{% asset_img 3.png %}

<br>


{% asset_img 4.png %}

<br>


然後確定 NuGet 帳號已註冊且取得 API key。  

{% asset_img 5.png %}

<br>


{% asset_img 6.png %}

<br>


{% asset_img 7.png %}

<br>


再調用 dotnet nuget push，帶入 NuGet 套件檔的位置及 NuGet API key。  

    dotnet nuget push $package -k $key -s https://api.nuget.org/v3/index.json

{% asset_img 8.png %}

<br>


NuGet 套件即會被上傳至 NuGet server 上。  

{% asset_img 9.png %}

<br>


{% asset_img 10.png %}

<br>


Link
====
* [使用 dotnet CLI 建立及發佈 NuGet 套件 | Microsoft Docs](https://docs.microsoft.com/zh-tw/nuget/quickstart/create-and-publish-a-package-using-the-dotnet-cli)
