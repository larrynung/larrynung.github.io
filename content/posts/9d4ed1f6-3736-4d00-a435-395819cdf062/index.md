---
title: "Vagrant - Create and configure lightweight, reproducible, and portable development environments"
date: "2013-11-06 12:00:00"
description: "Vagrant - Create and configure lightweight, reproducible, and portable development environments"
---

做程式開發的應該都能體認環境的建立是很重要的，不論是開發環境、建置環境、還是測試環境，多半的開發人員在環境的建立這邊耗費了非常多的時間。可能是做些設定、裝些相依的套件、甚至是一些慣用的外掛。若是安裝較為繁複的話，總是難免會漏掉某些步驟，這時就會需要花費更多的時間反覆測試，將漏掉的設定抓出。 
       
Vagrant這項技術能有效的利用Virtual box解決這樣的問題。環境變得可攜且可複製，開發人員從此能像遊牧民族般逐電腦而居，新加入的開發人員也可因此省下建置環境的時間耗費，快速進入程式開發的階段。   

Vagrant上的所有操作都只需要shell就可以完成，不需要滑鼠的介入，所以操作更為快速，也容易做自動化的操作。且可以設定port的對應、啟動時的scrip...等等，再複雜的環境建置也不用怕。

  Vagrant的安裝也非常的簡單，先安裝好Virtual Box。若是Unix用戶，請參閱筆者RubyGems這篇，呼叫RubyGems的命令gem install vagrant下去安裝Vagrant。    
 
  若是Windows用戶，請至Vagrant Downloads下載安裝包，安裝後重啟電腦即可。     

安裝好後，Unix用戶請啟動Shell叫用命令，Windows用戶則是啟動PowerShell。

  首先呼叫命令vagrant box add [box name] [box path]，將指定的vagrant box下載下來並加入到vagrant box列表中。若是第一次接觸vagrant，可以至Vagrantbox.es這邊挑選想要的vagrant box，或是直接用Vagrant提供的Ubuntu Box(http://files.vagrantup.com/lucid32.box)。    

接著需要呼叫命令vagrant init去讓Vagrant做初始化的設定 ，這個命令會產生Vagrant box的設定檔Vagrantfile。

初始設定完成後實際呼叫命令vagrant up將機器啟動。 

啟動後可以叫用命令vagrant ssh，使用ssh連進vagrant。連進vagrant後我們可以在vagrant內建立需要的開發環境，像是為其安裝MongoDB之類的。

以MongoDB為例，我們需要去設定Vagrantfile將Port forward出來，只要依config.vm.forward_port [vagrant port], [local port]這樣的格式輸入，像是這邊筆者輸入的config.vm.forward_port 27017, 27018，就是將vagrant內部的27017 port對應到本地的27018 port，這樣直接連本機的27018 port就等同於連到vagrant內的27017 port。

設定完Vagrantfile，若是vagrant仍舊啟動中，我們可以呼叫vagrant reload將設定重新載入。(注意到這邊載入的訊息我們可以看到port forward的狀態，像是22=>222與2017=>2018，啟動時可以由這邊確認forward的狀態。)

載入後叫用命令mongo 127.0.0.1:27018實際的連線測試，沒意外的話應該可以正常運行，感覺就像是本機的服務一般。

當環境建立妥當，我們可以叫用vagrant package命令將開發環境打包成vagrant box，後續開發環境的建立可以直接拿該vagrant box去做vagrant box add。

開發環境的建立告一段落時，可以叫用vagrant suspend命令暫停vagrant，或是叫用vagrant halt命令將vagrant關閉。

若是系統中殘留有不用的vagrant box，可呼叫命令vagrant destory將對應的VM移掉，然後呼叫vagrant box remove [vagrant box name]將它從vagrant box list中移除。

## Link
     Vagrant Downloads    A brief introduction to Vagrant – 原來 VirtualBox 可以這樣玩     Vagrantbox.es     Vagrant 101: Simple Linux VMs     用 Vagrant 快速建立開發環境     使用Vagrant 搭建開發環境     Ubuntu 安裝和設定 Vagrant (上)