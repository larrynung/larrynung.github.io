---
title: "[Wix]Wix製作安裝包時為特定檔案指定使用NGen產生Native Image"
date: "2013-11-06 12:00:00"
description: "[Wix]Wix製作安裝包時為特定檔案指定使用NGen產生Native Image"
---
使用Wix製作安裝包時，若想要指定某些特定檔案，為其產生Native Image的話，可以將安裝專案加入WixNetFxExtension.dll組件參考。

並在wxs file內的Wix element加上netfx命名空間(xmlns:netfx="http://schemas.microsoft.com/wix/NetFxExtension")。

然後找到想要產生Native Image的檔案設定，在File element中間穿插，像是下面這樣：

這樣設定完後所產生的安裝包在安裝時就會為指定的檔案產生Native Image。若是不放心，這邊我們可以透過Process Explorer來驗證一下，如果Process運行時所加載的組件位置是C:\Windows\Assembly\NativateImagex...的話，就代表我們在安裝專案中所做的設定正確無誤，所以運行時會改呼叫Native Image，而不會在運行時才Compile。

##
Link

How To: NGen Managed Assemblies During Installation

NGen: Creating Setup Projects

How to NGEN files in an MSI-based setup package using WiX

NGen support in WiX