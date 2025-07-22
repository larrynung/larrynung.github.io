---
title: "RVM (Ruby Version Manager)"
date: "2013-11-06 12:00:00"
description: "RVM (Ruby Version Manager)"
tags: [Ruby]
---

RVM (Ruby Version Manager)是Ruby的版控系統，開發人員可透過RVM輕易的安裝不同版本的Ruby至系統上，也可以去切換當前所要使用的Ruby版本。因為Ruby的改版很快，架構變動的幅度又很大，以往開發人員會需要想辦法生出不同的環境來做測試。RVM的出現解決了這樣的問題，當開發上有可能要使用不同版本的Ruby，RVM是一個不錯的選擇。 

  RVM的安裝很簡單，只要呼叫命令"curl -L https://get.rvm.io | bash -s stable --rails --autolibs=enabled"，我們就可以透過curl將https://get.rvm.io這邊所存放的Shell Script下載下來運行安裝 (有興趣的可自行連到https://get.rvm.io這邊查閱安裝用的Shell Script)。      

安裝完後，我們就可以實際呼叫RVM所提供的命令做些動作。

像是rvm list known命令可查閱RVM目前有提供哪些Ruby版本可供安裝使用。 

rvm install [version] ( e.x.rvm install 1.8.6 )命令可透過RVM安裝指定的Ruby版本至本機。 

rvm list命令可查閱本機已透過RVM安裝了哪些Ruby版本。 

rvm use [version] (e.x. rvm use 2.0.0)命令可透過RVM設定當前要使用哪一版的Ruby版本 (版本切換後，可呼叫命令ruby -v確認當前的Ruby版本)。 
  
rvm [version] --default (e.x. rvm 2.0.0 --default) 命令可透過RVM設定預設啟用的Ruby版本。 

rvm system命令可使用系統本來安裝的Ruby版本。 

rvm remove [version] (e.x. rvm remove 1.8.6)命令可移除已經安裝在本地的Ruby版本。

最後這邊提一下，在RVM下每個Ruby環境的Gem都是分別管理的，而在同一個Ruby環境下也可以建立不同的Gemset，在這邊不對此多做著墨。

## Link
     RVM and Gemsets    Cut Rubies with ease!    Installing RVM    Rails進階開發環境    RVM - Ruby enVironment (Version) Manager    查看RVM 實用指南    RVM CLI Usage