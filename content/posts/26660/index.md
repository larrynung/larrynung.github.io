---
title: "[IADP]C++ Intel AppUp Application Develop Process"
date: "2011-05-30 10:50:39"
description: "[IADP]C++ Intel AppUp Application Develop Process"
tags: [C++]
---

在C++中開發IADP AppUp的應用程式，其程式的撰寫方式跟.NET程式很類似，使用的類別類似、認證程式碼類似、工具的使用上類似，所要特別注意的地方就是在C++中必須要設定一些lib、目錄、並加入一些標頭檔，並記得釋放掉資源。開發時，開發人員必須先行安裝Intel AppUp SDK 1.1.1 for Windows C/C++，為了加速開發，這邊可以順便安裝上Intel AppUp™ SDK Microsoft Visual Studio* IDE Plug-in。

安裝完Intel AppUp™ SDK Microsoft Visual Studio* IDE Plug-in後，在Visual Studio建立Win32 Windows Application，或是在建立MFC Application時，可看到精靈畫面會增加一個Use Intel AppUp(TM) SDK library的選項。

勾選Use Intel AppUp(TM) SDK library這個選項後，建立出來的應用程式專案即會滿足Intel AppUp開發的所有必要條件，像是在專案屬性設定Project>Properties>Configuration Properties>Linker>Input>Additional Dependencies那邊

必須要加入下列lib檔：

Project>Properties>Configuration Properties>Linker>General>Additional Library Directories必須設定、並將撰寫與編譯時所需要的Header檔的加入專案、與加入認證程式碼等，這些繁雜的設定Plug-In都幫我們完成了，開發人員只要專心建立自己的應用程式即可。

這樣的功能在我們新建Intel AppUp應用程式特別好用。但是若想把現有的專案發佈到Intel AppUp Center呢?其實Plug-In也有這方面功能的支援。

透過在程式碼編輯區中按下滑鼠右建，點選右鍵快顯選單中的[Add Header for Intel AppUp(TM) software]選單選項，Plug-In會幫我們自動帶入Include程式碼，會Include開發所需的adpcppf.h檔。

再將滑鼠游標移至應用程式一開始建立的地方，按下滑鼠右鍵，點選右鍵快顯選單中的[Add Authorization Code for Intel AppUp(TM) software]選單選項，為應用程式加入Intel AppUp認證的功能。

此外，Intel AppUp C++應用程式開發所需要的必要條件都會在此時被加入，開發人員不需要手動再去處理。像是Project>Properties>Configuration Properties>Linker>Input>Additional Dependencies的設定。

Project>Properties>Configuration Properties>Linker>General>Additional Library Directories的設定。

與所需要的Header檔。

最後在開發上還有個跟.NET程式不一樣但卻很重要的小步驟，那就是必須要記得在程式結束時，在程式碼編輯區按下滑鼠右建，點選右鍵快顯選單中的[Add Cleanup Code for Intel AppUp(TM) software]選單選項，加入刪除資源的程式碼，以避免資源洩漏。