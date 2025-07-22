---
title: "[.NET Concept].NET 跨平台?!"
date: "2009-01-23 10:45:22"
description: "[.NET Concept].NET 跨平台?!"
tags: [.NET Concept]
---

一直以來，.NET所謂的跨平台一直被人所垢病，甚至被嘲諷只能跨Windows作業系統。而我一直以為.NET所謂的跨平台，只要是Window作業系統，再外加個.NET Framework就可以跑.NET程式了，身為微軟產品的愛好者，自然對此不以為意。殊不知連在Windows下灌.NET Framework也有其限制。

一直到前陣子我才知道，原來不是Windows作業系統就一定可以灌上所要的.NET Framework版本。越新的Framework越不支援舊的作業系統。因此在產品開發上這點可能就要注意一下，若是目標客戶可能有舊型機台且灌的是舊型的作業系統的話，在開發上就要以舊版的Framework語法來開發。而在目標客戶沒有使用舊型作業系統的情況下，就可以考慮採用新的Framework語法來開發。

下表為目前.NET Framework的版本與作業系統支援對照表
.NET Framework版本支援作業系統1.1Windows 2000; Windows Server 2003 Service Pack 1 for Itanium-based Systems; Windows Server 2003 x64 editions; Windows Server 2008 Datacenter; Windows Server 2008 Enterprise; Windows Server 2008 for Itanium-based Systems; Windows Server 2008 Standard; Windows Vista Business; Windows Vista Enterprise; Windows Vista Home Basic; Windows Vista Home Premium; Windows Vista Starter; Windows Vista Ultimate; Windows XP; Windows XP Professional x64 Edition2.0Windows 2000 Service Pack 3; Windows 98; Windows 98 Second Edition; Windows ME; Windows Server 2003; Windows XP Service Pack 23.0Longhorn (Windows Code Name) ; Windows Server 2003 Service Pack 1; Windows Vista; Windows XP Service Pack 23.5Windows Server 2003; Windows Server 2008; Windows Vista; Windows XP
 
作業系統.NET Framework版本Windows 982.0Windows 20001.1, 2.0Windows ME2.0Windows XP1.1, 2.0, 3.0, 3.5Windows Server 20031.1, 2.0, 3.0, 3.5Windows Server 20081.1, 3.5Windows Vista3.0, 3.5

相關連結Microsoft® .NET Framework 1.1 版可轉散發套件Microsoft .NET Framework 2.0 版可轉散發套件 (x86)Microsoft .NET Framework 3.0 可轉散發套件Microsoft .NET Framework 3.5