---
title: "Try .NET - Installation"
date: "2019-09-23 08:50:28"
tags: [Try .NET]
---


要安裝 Try .NET，可透過 dotnet tool install 將 dotnet-try 安裝到全域。  

<!-- More -->

    dotnet tool install --global dotnet-try

![1.png](1.png)

</br>


安裝完就可以開始使用。  

    dotnet try -h

![2.png](2.png)

</br>


若無法運行，可查驗一下是否為路徑問題。  

    export PATH="$PATH:/root/.dotnet/tools"

![3.png](3.png)

</br>


若有需要可透過 dotnet tool update 更新 dotnet-try 套件。  

      dotnet tool update -g dotnet-try

![4.png](4.png)
