---
title: "SonarQube - Unsupported major.minor version 52.0"
date: "2016-09-01 13:59:21"
tags: [SonarQube]
---


SonarQube 如果出現 Unsupported major.minor version 52.0 這樣的錯誤。  

<!-- More -->

![1.png](1.png)

<br/>


代表 JRE 與 JDK 版本對不起來，可以安裝對應的版本，然後用 Java -version 與 Javac -version 確認看看。    

![2.png](2.png)

<br/>


確認版本是對的後再次運行 SonarQube，應該就可以了。
