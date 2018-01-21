---
title: "Windows Server - Switch from Server Core to Windows GUI"
date: 2018-01-21 23:50:33
tags:
---

Windows Server 有 Server Core 與 GUI 兩種模式，有時後玩一玩 Windows 會不知怎麼的從 GUI 模式變到 Server Core 模式，這時進到 Windows 就會看到空空的一遍，只有一個命令提示字元在上面。  

<!-- More -->

{% asset_img 1.png %}
 
<br/>


要恢復到本來熟悉的 GUI 畫面，我們可以用 PowerShell 或是 MS-DOS 將 Windows Server 切回到 GUI 模式。  

<br/>


這邊直接使用 MS-DOS 命令切回 GUI 模式。  

    Dism /online /enable-feature /featurename:Server-Gui-Mgmt /featurename:Server-Gui-Shell /featurename:ServerCore-FullServer /all

{% asset_img 2.png %}
 
<br/>


跑完後重新啟動即會恢復到熟悉的 GUI 畫面。  

{% asset_img 3.png %}
 
<br/>


Link
=====
* [Windows 2012 R2 Remote Desktop Is A Black Screen With Command Prompt Only](https://ravingroo.com/1720/windows-server-2012-r2-boots-to-black-screen-command-prompt-gui-core/)
* [如何在 Windows Server 2012 的 Server Core 與 GUI 介面做切換 | 小歐ou | 菜鳥自救會 - 點部落](https://dotblogs.com.tw/chou/archive/2012/09/05/74618.aspx)
