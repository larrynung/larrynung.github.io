---
layout: post
title: "Vagrant - Shell Provisioning"
date: 2015-10-26 00:13:00
comments: true
tags: [Vagrant]
keywords: "Vagrant, Provisioning"
description: "Vagrant - Shell Provisioning"
---

要讓 Vagrant 在第一次啟動時透過 Shell Script 去做些設定，我們可以透過 Vagrant 的 Shell Provisioning。  

<!-- More -->

<br/>


若想在 Vagrantfile 內直接設定，可以使用 Inline 的方式撰寫。像是下面這樣設定 config.vm.provision 為 `shell`，並在 `inline` 參數這邊直接將 Script 帶在後面。  

{% codeblock lang:rb %}
Vagrant.configure("2") do |config| 
    ... 
    config.vm.provision "shell", inline: "echo Hello, World" 
    ... 
end
```

<br/>


也可以先抽成方法後指給 inline 參數。  

{% codeblock lang:rb %}
$script = <<SCRIPT 
    echo I am provisioning... 
    date > /etc/vagrant_provisioned_at 
SCRIPT 

Vagrant.configure("2") do |config| 
    ... 
    config.vm.provision "shell", inline: $script 
    ... 
end
```

<br/>


若想將 Script 獨立於 Vagrantfile 外，這邊也可以透過 `path` 參數指定 Script 檔。  

{% codeblock lang:rb %}
Vagrant.configure("2") do |config| 
    ... 
    config.vm.provision "shell", path: "script.sh" 
    ... 
end
```

<br/>


如果 Script 需要額外的參數傳遞，可透過 `args` 參數。

{% codeblock lang:rb %}
Vagrant.configure("2") do |config| 
    ... 
    config.vm.provision "shell" do |s| 
        s.inline = "echo $1" 
        s.args = "'hello, world!'" 
    end 
    ... 
end
```

<br/>


Link
----
* [Shell Scripts - Provisioning - Vagrant Documentation](https://docs.vagrantup.com/v2/provisioning/shell.html)
