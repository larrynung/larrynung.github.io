---
title: "'SonarLint for Visual Studio - SonarAnalyzer for C# and Visual Basic .NET'"
date: "2016-09-30 23:36:00"
---

SonarLint for Visual Studio 能讓 Visual Studio 與 SonarQube 整合，將 SonarQube 的 Rule 透過 Analyzer 的方式整進 Visual Studio，讓 Visual Studio 能用 SonarQube 的 Rule 下去對程式進行分析。

套件直接透過 Extension Manager 安裝即可。

安裝完開啟 Team Explorer 連接 SonarQube。

![1.png](1.png)

![2.png](2.png)

![3.png](3.png)

連結上 SonarQube 後將專案與 SonarQube 上的 Project Bind 在一起。

![4.png](4.png)

![5.png](5.png)

![6.png](6.png)

Bind 完後 Solution Folder 會放置 Rule 的設定。

![7.png](7.png)

專案也會被加入 Analyzer。

![8.png](8.png)

運行分析時也會套用 SonarQube 的 Rule。

![9.png](9.png)