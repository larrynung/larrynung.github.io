---
title: "JFrog - Install JFrog Artifactory open source on Windows"
date: "2017-09-08 13:36:48"
tags: [JFrog]
---


要在 Windows 安裝 JFrog Artifactory open source，可先到 JFrog Artifactory open source 的下載頁面。  

<!-- More -->

![1.png](1.png)

<br/>


![2.png](2.png)

<br/>


下載 Windows 用的壓縮檔。  

![3.png](3.png)

<br/>


解壓縮下載下來的壓縮檔。  

![4.png](4.png)

<br/>


![5.png](5.png)

<br/>


![6.png](6.png)

<br/>


切到 bin 目錄用 Administrator 運行 artifactory.bat。  

![7.png](7.png)

<br/>


即會運行 JFrog Artifactory 服務。  

![8.png](8.png)

<br/>


瀏覽器訪問 http://localhost:8081 即可看到 JFrog Artifactory 頁面。  

![9.png](9.png)

<br/>


如果要將 JFrog Artifactory 註冊成 Windows 服務，可用 Administrator 運行命令提示字元，在命令提示字元中運行 installService.bat 註冊 Windows 服務。

![10.png](10.png)

<br/>


![11.png](11.png)

<br/>


註冊好後可以看到增加的 Artifactory Windows 服務。  

![12.png](12.png)

<br/>


如果要將 JFrog Artifactory 的 Windows 服務移除，一樣用 Administrator 運行命令提示字元，在命令提示字元中運行 uninstallService.bat 取消註冊 Windows 服務。

![13.png](13.png)

<br/>


![14.png](14.png)

<br/>


Link
----
* [JFrog - Managing Binaries for Maven Repository, Docker, npm, Ruby and More](https://www.jfrog.com/)
