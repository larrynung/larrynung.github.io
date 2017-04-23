---
title: LuaRocks - The Lua package manager
date: 2017-04-23 21:29:25
tags: [Lua]
---

LuaRocks 是 Lua 的套件管理程式，可在官網找到下載頁面。  

<!-- More -->

{% asset_img 1.png %}

<br/>


{% asset_img 2.png %}

<br/>


{% asset_img 3.png %}

<br/>


點選下載所要使用的版本。  

{% asset_img 4.png %}

<br/>


安裝包下載下來後，解壓縮即可進行安裝，但是安裝前需先確定是否已裝有 Lua binary，如果 Lua binary 已經備妥，可以運行 'install.bat' 進行 LuaRocks 的安裝。  

{% asset_img 5.png %}

<br/>


{% asset_img 6.png %}

<br/>


因為 LuaRocks 需要 C compiler，MinGW 或是 Microsoft compiler 都可以，所以這邊筆者直接使用 Visual Studio 內建的命令列模式來操作。  

<br/>


設定 LuaRocks 的路徑。  

{% asset_img 7.png %}

<br/>


就可以用 LuaRocks install 安裝指定的 Lua 套件。  

    LuaRocks install <LuaPackage>

{% asset_img 8.png %}

<br/>


Link
----
* [LuaRocks - The Lua package manager](https://luarocks.org/)
