---
title: SonarQube - Remote access
date: 2016-09-01 12:27:30
tags: SonarQube
---

SonarQube 裝完後若未做任何修改，只能透過本地存取服務。  

<!-- More -->

<br/>

如果要開放遠端存取服務，可開啟 `conf\sonar.properties` 設定檔進行設定。像是將 sonar.web.host 設為 0.0.0.0，或是透過設定 sonar.web.port 改變 port 號。  

{% asset_img 1.png %}