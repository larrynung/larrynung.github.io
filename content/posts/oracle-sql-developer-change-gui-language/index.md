---
title: "Oracle SQL Developer - Change GUI language"
date: "2017-08-03 23:07:35"
tags: [Oracle SQL Developer]
---


要變更 Oracle SQL Develop 界面的語言，可先開啟 idein\ide.boot 檔。  

<!-- More -->

![1.png](1.png)

<br/>


查閱 oracle.translated.locates 設定中可支援的語言有哪些。  

![2.png](2.png)

<br/>


再來開啟 sqldeveloperin\sqldeveloper.conf 檔。  

![3.png](3.png)

<br/>


將 AddVMOption -Duser.language 設定值設為欲使用的語言，然後重啟 Oracle SQL Developer。  

![4.png](4.png)

<br/>


Oracle SQL Developer 就會變成指定的語言界面。  

![5.png](5.png)

<br/>
