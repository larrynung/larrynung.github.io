---
title: SonarQube - Setup SonarQube windows service
date: 2016-09-28 22:34:14
tags: SonarQube
---

要設定 SonarQube Windows 服務，只要運行 InstallNTService.bat 檔即可。  

<!-- More -->

{% asset_img 1.png %}

<br/>


運行完，SonarQube 的 Service 就安裝設定完畢了。  

{% asset_img 2.png %}

<br/>


接著要將剛安裝的服務啟動，這邊看是要透過運行 StartNTService.bat 檔，或是透過 Services 視窗將服務啟動都可以。  

{% asset_img 3.png %}

<br/>


{% asset_img 4.png %}

<br/>


到這邊服務已經安裝並運行起來了，沒意外的話 SonarQube 已經可以正常使用了。  

<br/>


後續如果要停止或是移除 SonarQube 服務，這邊也都有對應的 bat 檔可供直接叫用。  
