---
layout: post
title: "DNVM - The .NET Version Manager"
date: 2015-11-05 23:22
comments: true
categories: 
keywords: "DNVM"
description: "DNVM - The .NET Version Manager"
---

DNVM 是一命令列工具，允許我們透過命令去管理 .NET CLR/CoreCLR SDK 與運行的環境(DNX)。   

<!-- More -->

<br/>


可透過命令提示字元進行安裝  

    @powershell -NoProfile -ExecutionPolicy unrestricted -Command "&{$Branch='dev';iex ((new-object net.webclient).DownloadString('https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.ps1'))}"

<br/>


或是透過 Powershell 安裝  

    &{$Branch='dev';$wc=New-Object System.Net.WebClient;$wc.Proxy=[System.Net.WebRequest]::DefaultWebProxy;$wc.Proxy.Credentials=[System.Net.CredentialCache]::DefaultNetworkCredentials;Invoke-Expression ($wc.DownloadString('https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.ps1'))}

<br/>


主要會用到的命令有 list、 upgrade、 install、 use、 alias。  	

<br/>


list 命令是用來列出本機有哪些 DNX 可供使用。  

    dnvm list

{% img /images/posts/DNVM/1.png %}

<br/>

可以看到 DNX 的 Version、 Runtime、 Architeure、 Location、 Alias，以及目前在用的是哪一個。  

<br/>


upgrade 命令可用以更新 DNX，會自動安裝最新版的 clr DNX，將之設為 default alias，並將指定使用最新版的 DNX。  

    dnvm upgrade

{% img /images/posts/DNVM/2.png %}

<br/>


跟加帶 `-r clr` 的效果是一樣的。  

    dnvm upgrade -r clr

{% img /images/posts/DNVM/3.png %}

<br/>



若要更新 CoreClr 的 DNX，可改加帶 `-r coreclr`。  

    dnvm upgrade -r coreclr

{% img /images/posts/DNVM/4.png %}

<br/>


install 命令可安裝指定版本的 DNX。

    dnvm install -r [runtime] [version]
    dnvm install -r [runtime] -arch [architeure] [version]

{% img /images/posts/DNVM/5.png %}

<br/>


use 命令可切換使用的 DNX。  

    dnvm use -r [runtime] [version]
    dnvm use -r [runtime] -arch [architeure] [version]

{% img /images/posts/DNVM/6.png %}

<br/>


Link
----
* [aspnet/dnvm](https://github.com/aspnet/dnvm)
* [Up and running with DNX/DNVM/DNU | Stuart Blackler's Tech Blog - sblackler.net](http://www.sblackler.net/2015/05/02/Up-And-Running-With-DNX-DNVM-DNU/)
* [DNVM, DNX, and DNU - Understanding the ASP.NET 5 Runtime Options - CodeProject](http://www.codeproject.com/Articles/1005145/DNVM-DNX-and-DNU-Understanding-the-ASP-NET-Runtime)
* [Installing .NET Core on Windows — .NET Core Documentation 0.0.1 documentation](http://dotnet.readthedocs.org/en/latest/getting-started/installing-core-windows.html)
