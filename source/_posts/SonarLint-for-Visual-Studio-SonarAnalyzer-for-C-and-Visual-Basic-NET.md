---
title: 'SonarLint for Visual Studio - SonarAnalyzer for C# and Visual Basic .NET'
date: 2016-09-30 23:36:00
tags:
---

SonarLint for Visual Studio 能讓 Visual Studio 與 SonarQube 整合，將 SonarQube 的 Rule 透過 Analyzer 的方式整進 Visual Studio，讓 Visual Studio 能用 SonarQube 的 Rule 下去對程式進行分析。  

<!-- More -->

<br/>


套件直接透過 Extension Manager 安裝即可。  

<br/>  


安裝完開啟 Team Explorer 連接 SonarQube。  

{% asset_img 1.png %}

<br/>


{% asset_img 2.png %}

<br/>


{% asset_img 3.png %}

<br/>


連結上 SonarQube 後將專案與 SonarQube 上的 Project Bind 在一起。  

{% asset_img 4.png %}

<br/>


{% asset_img 5.png %}

<br/>


{% asset_img 6.png %}

<br/>


Bind 完後 Solution Folder 會放置 Rule 的設定。  

{% asset_img 7.png %}

<br/>


專案也會被加入 Analyzer。  

{% asset_img 8.png %}

<br/>


運行分析時也會套用 SonarQube 的 Rule。  

{% asset_img 9.png %}

<br/>
