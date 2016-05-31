---
layout: post
title: "EyeDisposable - IL instrumenter to help detect IDisposable leaks in .NET programs"
date: 2013-12-26 22:34:00
comments: true
tags: 
keywords: EyeDisposable, Leak
description: "EyeDisposable - IL instrumenter to help detect IDisposable leaks in .NET programs"
---

EyeDisposable 是ㄧ用來檢測程式是否有正確 Dispose 資源的命令列工具。  

<!--More-->

程式可至 [kizzx2/EyeDisposable · GitHub](https://github.com/kizzx2/EyeDisposable) 這邊下載。因為有用到 Sub Module ，所以用 Git Clone 下來後需要更新 SubModule 。

    git clone git://github.com/kizzx2/EyeDisposable.git
    cd EyeDisposable
    git submodule update


更新好後建置即可...  

若是不會使用 SubModule ，或是網路限制導致無法連 Git ，這邊也可以手動將方案開啟，然後移除 Mono.Cecil 專案，改用 NuGet 將 Mono.Cecil 組件加入參考。  

{% img /images/posts/EyeDisposable/1.png %}  


程式主檔建立完成後，使用時我們只要將組件位置帶入即可。  

    EyeDisposable [AssemblyName]


組件帶入後，EyeDisposable會開始進行分析，並強制插入偵測 Leak 用的程式。分析的結果會顯示於主控台，可從中看到程式的方法中建立了多少可釋放的物件，而又釋放了多少次。

{% img /images/posts/EyeDisposable/2.png %}  


這邊可依此線索下去查找沒被釋放的資源。像是以筆者的例子來說，他就找到在 Main 那邊建立出一個物件，但是卻沒做過釋放的動作，所以查驗一下程式碼，就可以看到這邊筆者建立了 RNGCryptoServiceProvider 物件卻未釋放。  

{% img /images/posts/EyeDisposable/3.png %}  


若是依此線索找不出來，也可以將程式點擊開啟，然後對程式做些操作後關閉。因為剛剛 EyeDisposable 已經將一些偵測用的程式注入，所以關閉時程式所在的目錄會多個 `.DisposeLeaks.log` 為檔案結尾的文字檔，開啟後若有偵測到 Leak ，該文字檔會有對應的資訊。

{% img /images/posts/EyeDisposable/4.png %}  


最後一提，依筆者實測，注入的過程有時會造成程式毀損無法開啟，有點像是 Entry Point 沒處理好導致，感覺上命令列的程式比較適用。不過雖然注入可能造成程式毀損無法開啟，但也只是無法讓程式運行準確的抓出 Leak ，且在注入的同時 EyeDisposable 也有提供一些線索讓我們去找尋 Leak ，整體來說還是不失為一個不錯的參考工具。  

Link
----
* [kizzx2/EyeDisposable · GitHub](https://github.com/kizzx2/EyeDisposable)
