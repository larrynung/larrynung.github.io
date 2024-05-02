---
title: "Vagrant - SSH in windows"
date: "2014-10-02 23:55:00"
description: "Vagrant - SSH in windows"
tags: [Vagrant]
---


要在 Windows 下使用 SSH 連進 Vagrant 作些設定，我們有幾種方式可以使用。  

<!-- More -->

<br/>

一種是透過 SSH 連線軟體連進 Vagrant，像是 PuTTY。  

<br/>

輸入 IP 與 Port 進行連線。  

{% img /images/posts/VagrantSSHInWindow/1.png %}

<br/>


連進去後輸入 Vagrant Box 的帳密即可，如果不知道帳密的話，通常這邊的帳密會是 `vagrant`，可以試試看。  

{% img /images/posts/VagrantSSHInWindow/2.png %}

<br/>


另外一種方式則是直接透過命令提示字元叫用 Vagrant SSH 連進 Vagrant。使用前需先安裝 Git，並將 Bin 的路徑設上，都完成後即可直接叫用Vagrant SSH 連進 Vagrant。  

{% img /images/posts/VagrantSSHInWindow/3.png %}

<br/>


路徑的設定可以直接在系統的環境變數中設定，叫用上會比較方便。但若有需要也可以直接在命令提示字元中加入。  

    set PATH=%PATH%;C:\Program Files (x86)\Gitin


此外也可以直接叫用 SSH 連進去，比較麻煩一點就是了。  

{% img /images/posts/VagrantSSHInWindow/4.png %}
