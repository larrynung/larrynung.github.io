---
title: "dotnet-dump - Installation"
date: "2019-11-25 08:05:40"
tags: [dotnet-dump]
---


要安裝 dotnet-dump 可使用 dotnet tool install --global 將 dotnet-dump 安裝到全域。  

<!-- More -->

    dotnet tool install --global dotnet-dump

![1.png](1.png)

</br>


安裝完設定路徑。  

    export PATH="$PATH:/root/.dotnet/tools"

![2.png](2.png)

</br>


查驗版本確認安裝無誤即可。  

    dotnet-dump --version

![3.png](3.png)
