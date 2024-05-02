---
title: "BusyBox - cp command"
date: "2019-03-25 20:30:37"
tags: [BusyBox]
---


cp 命令可用來做檔案的複製。  

<!-- More -->

<br/>


直接調用命令可查閱使用說明。  

    cp

![1.jpg](1.jpg)

<br/>


要將單檔複製到指定位置，可直接在命令後帶入來源檔案位置與目的檔案位置調用。  

    cp [SourceFile] [TargetFile]

![2.jpg](2.jpg)

<br/>


允許使用多組來源檔案，目的位置也可以使用目錄。  

    cp [SourceFile]... [TargetFolder]

![3.jpg](3.jpg)

<br/>


可使用萬用字元過濾篩選來源檔案。  

    cp [SourceFileFilter] [TargetFolder]

![4.jpg](4.jpg)

<br/>


來源位置也可以指定目錄，的來源目錄複製到目的目錄。  

    cp [SourceFolder] [TargetFolder]

![5.jpg](5.jpg)
