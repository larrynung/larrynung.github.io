---
title: "Vagrant - VBox Snapshot"
date: "2015-10-19 23:45:00"
description: "Vagrant - VBox Snapshot"
tags: [Vagrant]
---


要透過 Vagrant 去操作 Snapshot，我們可以借助 Vagrant 的 vagrant-vbox-snapshot 套件。  

<!-- More -->

<br/>


用 vagrant plugin install 帶入套件名稱 vagrant-vbox-snapshot 進行套件的安裝。  

    vagrant plugin install vagrant-vbox-snapshot

<br/>


這邊若有需要可能會連帶要求安裝套件 vagrant-winnfsd。  

    vagrant plugin install vagrant-winnfsd


{% img /images/posts/VagrantSnapshot/1.png %}

<br/>


套件安裝完畢後，我們就可以視需要調用命令進行 Snapshot 的操作。  

<br/>


套件的使用方式如下：  

    Usage
        vagrant snapshot <command> [<args>]
    
    Sub Commands
        back
            vagrant snapshot back [vm-name]
        delete
            vagrant snapshot delete [vm-name] <SNAPSHOT_NAME>
        go
            vagrant snapshot go [vm-name] <SNAPSHOT_NAME>
        list
            vagrant snapshot list
        take
            vagrant snapshot take [vm-name] <SNAPSHOT_NAME>


使用上會像這樣：  

    Vagrant snapshot take “init”
    Vagrant snapshot list
    Vagrant snapshot go “init”
    Vagrant snapshot delete “init”

  
像是 vagrant snapshot take 後面接 Snapshot 的名稱下去調用即可進行 Snapshot 的建立。vagrant snapshot list 可查驗有哪些 Snapshot 可用。  

{% img /images/posts/VagrantSnapshot/2.png %}

<br/>


要刪除特定的 Snapshot，可用 vagrant snapshot delete 後面接 Snapshot 名稱下去調用。  

{% img /images/posts/VagrantSnapshot/3.png %}

<br/>


要還原到特定的 Snapshot，可用 vagrant snapshot go 接 Snapshot 名稱下去調用。  

{% img /images/posts/VagrantSnapshot/4.png %}

<br/>


Link
----
* [dergachev/vagrant-vbox-snapshot](https://github.com/dergachev/vagrant-vbox-snapshot/)
* [Vagrant VBox Snapshot | Sitting in Oblivion](https://sittinginoblivion.com/wiki/vagrant-vbox-snapshot)
* [Snapshotting Vagrant](http://priyaaank.tumblr.com/post/50707609769/snapshotting-vagrant)
