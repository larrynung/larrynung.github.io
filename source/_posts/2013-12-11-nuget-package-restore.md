---
layout: post
title: "NuGet - Package restore"
date: 2013-12-11 22:04:00
comments: true
categories: [Nuget]
keywords: "NuGet"
description: "NuGet - Package restore"
---

使用 NuGet 安裝套件，使用到的 Nuget 套件資訊會被記載在 packages.config 檔案內，所以這些 Nuget 套件是可以被重新安裝復原的。因此一般在上版控時，會習慣性將這些套件排除 Commit ，待從版控 Pull 下來時再行 Nuget 套件的復原。  

<!--More-->

<br/>


要做 Nuget 套件的復原，以前我們會在 Visual Studio 的方案上按下滑鼠右鍵，在彈出的滑鼠右鍵快顯選單中，按下 `Enable NuGet Package Restore` 這個滑鼠右鍵選單選項。點選下去，會針對專案檔做些修改，並產生一個名為 .nuget 的方案目錄，裡面會有 Nuget.config、Nuget.target、以及 Nuget.exe 這幾個檔案，此時再次建置就會將遺失的 Nuget 套件復原。  

{% img /images/posts/RestoreNugetPackage/1.png %}

<br/>


這邊這個動作產生的 Nuget.config 內容會像下面這樣
    <configuration>
      <solution>
        <add key="disableSourceControlIntegration" value="true" />
      </solution>
    </configuration>

<br/>


該設定會告知一些版控系統（如 TFS）要對 Nuget 套件進行忽略的動作。   

<br/>


不過這是舊的設定方式，若使用新版，不用做任何動作，系統就會自動處理還原的動作。    
<br/>

預設在 Options 視窗這邊會將 `Allow NuGet to download missing packages` 以及 `Automatically check for missing packages during build in Visual Studio` 這兩個選項勾起，建置時會自動將遺失的 Nuget 套件復原。

{% img /images/posts/RestoreNugetPackage/2.png %}

<br/>


除了建置時去做 Nuget 的復原外，我們也可以開啟 Visual Studio 的 Manage NuGet Packages 視窗，開啟後若有遺失的 Nuget 套件這邊會偵測到，按下 Restore 按鈕就可以立即進行復原的動作。  

{% img /images/posts/RestoreNugetPackage/3.png %}
 
<br/>


Nuget 套件的還原也支援命令列的觸發方式，在 Build Server 這邊，我們很常會需要藉此去還原套件讓建置動作正常的運行。  

在 Nuget 2.7 以前，我們需要用 Nuget install 的命令，像是下面這樣：

    Nuget install package.config -o packages

<br/>


Nuget install命令後接 package.config 的位置，接著帶入參數 -o ，並指定 Nuget 套件存放的位置。  

在 Nuget 2.7 以後，可以改用 Nuget restore 命令，像是下面這樣：

    Nuget restore

<br/>


或是

    Nuget restore XXX.sln

<br/>


Link
----
* [Using NuGet without committing packages to source control](http://docs.nuget.org/docs/workflows/using-nuget-without-committing-packages)
* [Package Restore - NuGet Docs](http://docs.nuget.org/docs/reference/package-restore)
* [NuGet 1.6 提供的新功能：啟用 NuGet 套件自動回復](http://blog.miniasp.com/post/2012/03/12/Using-NuGet-Without-Checking-In-Packages-Package-Restore.aspx)
* [The right way to restore NuGet packages - David Ebbo](http://blog.davidebbo.com/2014/01/the-right-way-to-restore-nuget-packages.html)
