---
title: SonarQube - Failed to create an empty directory
date: 2016-09-02 13:58:39
tags: SonarQube
---

SonarQube 運行 Pre-processing 時，可能會拋出 `Failed to create an empty directory` 這樣的錯誤訊息。  

<!-- More -->

<br/>


這錯誤是因為 SonarQube 運行時會需要建立一個 `.sonarqube` 的目錄，該目錄如果因位檔案佔住無法刪除就會發生這樣的錯誤。  

{% asset_img 1.png %}

<br/>


這問題發生時可以查看任務管理員，看看是否有殘留的 MSBuild 在背後運行，如果有將之刪除即可。  