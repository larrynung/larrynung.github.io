---
title: "FX.Configuration - A lightweight/simple/flexible/extensible library to read configurations using strongly typed classes"
date: "2016-05-21 23:03:00"
description: "FX.Configuration - A lightweight/simple/flexible/extensible library to read configurations using strongly typed classes"
tags: [FX.Configuration]
---


FX.Configuration 是一號稱輕量，簡單，具彈性，可擴充的 Configuration 讀取套件，可以將 Configuration 讀取到對應的強型別類別中，便於後續 Configuration 設定值得取用。支援 Application/JSON/Mixed Configuration。    

<!-- More -->

<br/>


使用上可分為幾個步驟。  

{% img /images/posts/FxConfiguration/1.png %}

<br/>


首先需先透過 NuGet 套件管理視窗安裝套件。  

{% img /images/posts/FxConfiguration/2.png %}

<br/>


或是透過 `Package Manager Console` 輸入下列命令安裝套件。  

    Install-Package FX.Configuration

{% img /images/posts/FxConfiguration/3.png %}

<br/>


套件安裝完成後，接著要準備 Configuration 設定檔案，視需求決定是要用 Application/JSON/Mixed 哪種 Configuration，並訂定 Configuration 的結構以及要有哪些設定值。  

<br/>


再來要建立 Configuration 對應的類別供後續讀取使用，不同型態的 Configuration 類別需繼承不同的基底類別。   

<br/>


最後建立 Configuration 對應的類別實體，存取該實體的成員屬性即可取得 Configuration 的設定值。  

<br/>


進一步的使用可參閱筆者其它文章，像是讀取[Application configuration](http://larrynung.github.io/2016/05/17/fx-dot-configuration-read-application-configuration/)，讀取[JSON configuration](http://larrynung.github.io/2016/05/21/fx-dot-configuration-read-json-configuration/)，以及讀取[mixed configuration](http://larrynung.github.io/2016/05/21/fx-dot-configuration-read-mixed-configuration/)。  

<br/>


Link
----
* [NuGet Gallery | FX.Configuration 0.4.1](https://www.nuget.org/packages/FX.Configuration/)
* [friendlyx / fx.configuration — Bitbucket](https://bitbucket.org/friendlyx/fx.configuration)
* [FX.Configuration - Read application configuration - Level Up](http://larrynung.github.io/2016/05/17/fx-dot-configuration-read-application-configuration/)
* [FX.Configuration - Read JSON configuration - Level Up](http://larrynung.github.io/2016/05/21/fx-dot-configuration-read-json-configuration/)
* [FX.Configuration - Read mixed configuration - Level Up](http://larrynung.github.io/2016/05/21/fx-dot-configuration-read-mixed-configuration/)
