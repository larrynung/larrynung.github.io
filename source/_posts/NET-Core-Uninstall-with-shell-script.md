---
title: .NET Core - Uninstall with shell script
date: 2019-12-13 07:54:12
tags: [.NET Core]
---

若非使用 HomeBrew 安裝 .NET Core，沒辦法使用 HomeBrew 命令直接反安裝，需就官方解除安裝的步驟進行反安裝。

<!-- More -->

</br>


不過官方反安裝步驟繁瑣，需自行去多個目錄清除資料，非常不便。所以這邊直接使用 dotnet/cli 提供的腳本來進行反安裝。

</br>


先下載腳本。  

    wget https://raw.githubusercontent.com/dotnet/cli/master/scripts/obtain/uninstall/dotnet-uninstall-pkgs.sh

{% asset_img 1.png %}

</br>


運行下載下來的腳本。  

    sudo sh dotnet-uninstall-pkgs.sh

{% asset_img 2.png %}

</br>


.NET Core 就會被反安裝了。  

    dotnet --version && dotnet --list-sdks && dotnet --list-runtimes

{% asset_img 3.png %}
