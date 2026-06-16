---
title: "Set an Incorrect #GUID Heap Size on a .NET Assembly to Thwart Decompilation"
slug: "set-an-incorrect-guid-heap-size-on-a-dotnet-assembly-to-thwart-decompilation"
aliases: ["/posts/4b3a1259-615b-46c9-82c5-3446c72b1b23/"]
date: "2013-11-06 12:00:00"
tags: [CSharp, .NET]
description: ".NET組件的安全性一直是開發人員所關注的問題，若是花錢購買現成的方案可以保護的比較周全些，發生問題也可以要求保護方案的供應商提供更安全的防護。但是多半的情況下是沒有這類的工具的，尤其是自己私下開發的程式更是如此。"
---

.NET組件的安全性一直是開發人員所關注的問題，若是花錢購買現成的方案可以保護的比較周全些，發生問題也可以要求保護方案的供應商提供更安全的防護。但是多半的情況下是沒有這類的工具的，尤其是自己私下開發的程式更是如此。通常在這樣的情況下我們會尋求一些替代的方案，像是免費的混淆工具、或是修改程式為組件附加些具有防護作用的attribute...等等。這篇要介紹的也是一種簡易的替代性方案，透過為程式添加錯誤的metadata來達到保護的效果。之所以會具備保護的效果，是因為特定的metadata錯誤會使得某些反編譯軟體失效，但是程式卻可以正常的運行。

這邊我們需要透過CFF Explorer這套工具做metadata的修改，可到NTCore下載。

下載後開啟我們所要加以保護的.NET組件，左邊的樹狀結構切到MetaData Streams的節點，此時我們可以看到右邊有#GUID的metadata，這就是我們所要動手腳的地方。根據定義"The Guid heap is an array of GUIDs, each 16 bytes wide. Its first element is numbered 1, its second 2, and so on"，所以#GUID heap的大小會是16的倍數。像下圖中我們剛開起來所看到的#GUID Size是00000010，就完全符合#GUID heap的定義。

![image_thumb_2.png](/images/posts/4b3a1259-615b-46c9-82c5-3446c72b1b23/image_thumb_2.png)

這邊我們可以利用這個特性將#GUID heap的size改為非16的倍數，改完後存檔。

![image_thumb_1.png](/images/posts/4b3a1259-615b-46c9-82c5-3446c72b1b23/image_thumb_1.png)

透過Reflector去嘗試對其反組譯，就會看到Reflector無法正常解析，顯示了錯誤訊息。某種程度來說這個組件已經被我們加入了很簡易的保護在裡面了。

![image_thumb.png](/images/posts/4b3a1259-615b-46c9-82c5-3446c72b1b23/image_thumb.png)

最後一提，這種保護方式並不是對每個反組譯工具都有效，也很容易被破解。雖然很多保護的工具也都會內含這類保護機制，但若單獨使用這種保護就顯得十分的陽春，應避免太過於依賴這種保護方式。

## Link

* NTCore
* Anatomy of a .NET Assembly – CLR metadata 1
* Metadata探秘
* MS.Net CLR擴展PE結構分析(1)
* The .NET File Format
* Overview of Metadata Physical Layout in PE Files
