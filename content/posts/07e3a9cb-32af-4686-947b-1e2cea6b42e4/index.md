---
title: "Specify  Nugetrsquo;s packages folder location"
date: "2013-11-06 12:00:00"
description: "Specify  Nuget’s packages folder location"
tags: [NuGet]
---

有使用過NuGet安裝套件的就會知道，使用NuGet安裝套件時，預設會將套件下載下來存放在packages目錄內。

在某些時候這樣的存放方式會讓人覺得很困擾，像是筆者目前的習慣是將方案的目錄結構調整成下面這個樣子。 

程式碼會放置於Source目錄內，建置出來的組件會放置於Bin目錄內，參考的組件存放在Lib目錄下。在這樣的架構之下，NuGet下載下來的套件就不是存放我們所期望的地方。

此時可以為其設置設定檔調整NuGet套件存放的位置。設定檔檔名為NuGet.config，跟方案檔放置在相同的目錄下。 

設定檔的內容在NuGet 2.1以前，我們需要使用像是下面這樣的格式，最外層為settings節點，settings節點內放置repositoryPath節點，repositoryPath節點中可指定NuGet套件期望存放的位置。

在NuGet 2.1以後，又額外多支援了類似.NET Config的格式可供選用。

設定檔設置完成實際下載NuGet套件看看，沒意外的話下載下來的套件就會改成我們在設定檔中所設定的存放位置。像是這邊筆者下載的SharpZip就確實的進到了Lib目錄內。

## Link
     .net - Is it possible to change the location of packages for NuGet    NuGet 2.1 Release Notes