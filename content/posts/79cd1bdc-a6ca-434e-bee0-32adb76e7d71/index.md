---
title: "RyuJIT_ The next-generation JIT compiler for .NET"
date: "2013-11-06 12:00:00"
description: "RyuJIT_ The next-generation JIT compiler for .NET"
tags: [JIT]
---

RyuJIT是微軟新一代的JIT Compiler。

	之所以要開發新的JIT Compiler，是因為舊的x64 JIT Compiler當初在開發之時， 以當時的時空背景來說，64bit的機器尚未普及，且多是用於伺服器上面，雲端應用也尚未盛行，所以伺服器上的網站或服務就是最主要的使用場景。這些服務通常預先就已開啟，且是長時間的運行，編譯及啟動速度不是那麼的重要，若真有需求也可以用Ngen去解，因此當初是以C++的Optimizing Compiler為基礎下去開發，以期望產生較為高效的程式碼。

	反觀現今，64 bit機器普及，雲端應用亦已盛行。相較於產生高效的程式碼，編譯及啟動速度變得更為重要了。因此新的RyuJIT改採用本來的x86 JIT Compiler為基礎下去開發。本來的x86 JIT Compiler在編譯以及啟動速度上的優化已經做的很好了，故採用x86 JIT Compiler為基礎，能讓x64 JIT Compiler有較佳的編譯及啟動速度 ，微軟這邊也不需要維護兩份不同的程式碼，能加快開發的速度。

	RyuJIT比舊的64bit JIT Compiler快上2倍，啟動時間也快上30%(因為JIT Compiler的處理只佔啟動時間的ㄧ部份，所以速度提升無法到達兩倍) 。這邊官方有提供一份效能分析表可供參考，以RFC822 e-mail RegEx來說，Compile benchmark以以前的JIT64要花60秒以及1.4 GB的記憶體空間，而RyuJIT只需要1.8秒以及199MB的記憶體空間。

	目前RyuJIT還在CTP版，只支援Windows 8.1 x64與Windows Server 2012 R2，後續開發告一段落後，將會取代現有的JIT Compiler，也會開始支援x86。若要搶先體驗，可至http://aka.ms/RyuJIT這邊下載安裝程式，並將之安裝。

	安裝完成後，若要針對特定程式使用RyuJIT，可設定環境變數COMPLUS_AltJit=*。

	若要針對所有程式都套用RyuJIT，可以在登錄檔HKLM\SOFTWARE\Microsoft\.NETFramework這邊設定名為AltJit且值為"*"的字串值。

	值得注意的是，RyuJIT目前在運行時，據官方的說法是會讓Visual Studio的Edit and continue功能失效，但依筆者實際測試是會讓除錯發生錯誤，這部份可能後續會做個調整。但無論如何，該特性暫時可用來做為是否啟用RyuJIT的一個判斷依據。

## 
	Link

		RyuJIT: The next-generation JIT compiler for .NET