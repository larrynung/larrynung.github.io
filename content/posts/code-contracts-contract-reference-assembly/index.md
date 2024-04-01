---
title: "Code Contracts - Contract Reference Assembly"
date: "2014-03-23 13:26:00"
description: "Code Contracts - Contract Reference Assembly"
tags: [Code Contracts]
---


在使用 Code Contracts 時，程式會加上很多驗證的程式，可能是前置條件、可能是後置條件、也有可能是些不變性的驗證，因此很多人對於程式效能上都有相當的疑慮。 

<!-- More -->

<br/>

但其實 Code Contracts 在使用上有很大的彈性，因為它底層是透過 CCRewrite 去將驗證的程式插入至正確的位置，所以它可以在專案屬性那邊將驗證檢查給直接抽掉。因此在 Release 時就可以只保留前置條件做參數的驗證，甚至是整個抽掉，這部分就比以往利用 if-throw 來驗證要來的有彈性，也不會有多餘的效能耗費。  

<br/>

雖然無效能耗費，但如果是開發 DLL ，那抽掉 Code Contracts 後 Release，使用該 DLL 的程式就無法享有 Code Contracts 所帶來的好處，這不是我們所樂見的。故 Code Contracts 提供了 Contract Reference Assembly 功能，在抽掉 Code Contracts 的同時，可將 Code Contracts 抽至另外ㄧ個獨立的組件，連同對應的設定提示也可一併帶到組件的 XML 中，別的組件在引用時就仍可享有 Code Contracts 所帶來的好處。 

{% img /images/posts/ContractReferenceAssembly/1.png %}

<br/>

這個功能在 .Net Framework 中就有被廣泛使用。可以看到 .Net Framework 這邊就有提供許多的 Contract Reference Assembly 。 

{% img /images/posts/ContractReferenceAssembly/2.png %}

<br/>

反組譯可以看到裡面只有存放 Code Contracts 的部分。 

{% img /images/posts/ContractReferenceAssembly/3.png %}

<br/>

使用對應的方法，也能看到 Code Contracts 功能是正常運作的。  

{% img /images/posts/ContractReferenceAssembly/4.png %}

<br/>

介紹到這邊，我們可以得知使用 Code Contracts 技術並不會對程式效能有什麼不好的影響，就連 .Net Framework 本身也廣泛的使用。也因為 .Net Framework 本身的使用，這邊筆者更強烈建議開發人員應當安裝 Code Contracts 套件，在 Debug 的組態設定那邊開啟靜態分析與前置條件分析功能，儘管您尚未在自己的程式裡套 Code Contracts。
