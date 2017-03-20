---
title: Jenkins - Quality Gates Plugin
date: 2017-03-20 12:42:46
tags: [SonarQube, Jenkins]
---

Jenkins 安裝 SonarQube Plugin 後，雖然能用 Jenkins 分析程式並將分析結果送至 SonarQube，但是不論分析的結果是否有通過 SonarQube Quality Gate， Jenkins 的 job 都是會過。  

<!-- More -->

<br/>


若要讓 Jenkins job 依照 SonarQube Quality Gate 通過與否去決定建置的成功狀態，可以為 Jenkins 安裝 Quality Gate Plugin。  

{% asset_img 1.png %}

<br/>


{% asset_img 2.png %}

<br/>
  
  
{% asset_img 3.png %}

<br/>


安裝完後進入 Jenkins 的 `設定系統` 頁面。

{% asset_img 4.png %}

<br/>


在 Quality Gates 這邊按下 `ADD SONAR INSTANCE`。  

{% asset_img 5.png %}

<br/>


設定 SonarQube 的名稱與位置。  

{% asset_img 6.png %}

<br/>


接著到 Job 組態這邊設定建置後動作，使用 Quality Gates 套件，帶入 Project Key。  

{% asset_img 7.png %}

<br/>


這樣 Job 在運行時最後就會開始運行 Quality Gates 套件。  

{% asset_img 8.png %}

<br/>


Job 的建置狀態就會依 Quality Gates 通過與否去決定。  

{% asset_img 9.png %}

<br/>
