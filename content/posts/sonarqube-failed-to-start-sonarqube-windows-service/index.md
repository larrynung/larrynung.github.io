---
title: "SonarQube - Failed to start SonarQube windows service"
date: "2016-09-28 23:47:21"
tags: [SonarQube]
---


在啟動 SonarQube windows service 食，有可能會看到像下面這樣的畫面：  

<!-- More -->

![1.png](1.png)

<br/>


如果是透過 Services 視窗啟動的畫，會看到像下面這樣的畫面：  

![2.png](2.png)

<br/>


這時可以檢查任務管理員是否有殘留的 java.exe 與 conhost.exe，有的話將之刪除，再次啟動應該就可以了。  

![3.png](3.png)

<br/>
