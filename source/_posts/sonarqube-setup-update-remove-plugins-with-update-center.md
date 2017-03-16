---
title: "SonarQube - Setup/update/remove plugins with Update Center"
date: 2017-03-16 13:35:50
tags: SonarQube
---

SonarQube 提供 Update Center 可以讓我們很容易的控管 SonarQube 外掛套件。要使用 Update Center，可點選 [Administrator | System | Update Center]。  

<!-- More -->

<br/>


{% asset_img 1.png %}

<br/>


Update Center 中的 Installed 頁面會列出所有已安裝的套件，Updates Only 頁面會列出所有可更新的套件，Available 頁面會列出所有可安裝的套件。

<br/>


套件列表後方的按鈕可供我們安裝、更新、或是移除套件。

{% asset_img 2.png %}

<br/>


按下後會將對應的動作 Queue 起來等待運行，當確定要運行時可按下上方的 Restart 按鈕。  

{% asset_img 3.png %}

<br/>


再次按下 Restart 按鈕確認。  

{% asset_img 4.png %}

<br/>


就會開始運行對應的動作並將服務重啟。  

{% asset_img 5.png %}

<br/>


重啟後對應的設定即會生效。  