---
layout: post
title: "Vagrant - Creating a new box from an existing VM"
date: 2015-10-17 18:06:00
comments: true
categories: [Vagrant]
keywords: "Vagrant"
description: "Vagrant - Creating a new box from an existing VM"
---

要將已經存在的 VM 匯出成 Vagrant Box，我們可以透過 Vagrant package 命令的 `--base` 參數。  

<!-- More -->

<br/>


參數使用方式官方的說明如下： 
 
    --base NAME - Instead of packaging a VirtualBox machine that Vagrant manages, this will package a VirtualBox machine that VirtualBox manages. NAME should be the name or UUID of the machine from the VirtualBox GUI.

<br/>


簡單的說就是以直接在 `--base` 參數後帶入欲匯出的虛擬機的名稱即可。以匯出筆者電腦的 Win7 VM 為例，就是帶入 Win7，這邊另帶 `--output` 參數指定匯出後的 box 檔。  

{% img /images/posts/CreateVagrantBoxFromExistingVM/1.png %}

<br/>


輸入完我們就會看到指定的 box 產出。  

<br/>


我們可以將 box 加入。  

{% img /images/posts/CreateVagrantBoxFromExistingVM/2.png %}

<br/>


後續直接透過 box 建立對應的環境。   

{% img /images/posts/CreateVagrantBoxFromExistingVM/3.png %}

<br/>


Link
----
* [vagrant box - Command-Line Interface - Vagrant Documentation](https://docs.vagrantup.com/v2/cli/box.html)
* [Creating a new Vagrant base box from an existing VM | Abhishek Tiwari](http://abhishek-tiwari.com/hacking/creating-a-new-vagrant-base-box-from-an-existing-vm)
