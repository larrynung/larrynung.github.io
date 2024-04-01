---
title: "SonarQube - Analyzing with SonarQube scanner for MSBuild from the command line"
date: "2016-06-09 21:34:12"
tags: [SonarQube]
---


要使用 SonarQube scanner for MSBuild 在命令列下進行程式碼的掃描，需先確保 .NET Framework 有到 4.5.2 以上的版本，以及 jre 有到 7u75 以上的版本。  

<!-- More -->

<br/>


接著下載 [SonarQube scanner for MSBuild](https://github.com/SonarSource-VisualStudio/sonar-msbuild-runner/releases/download/2.0/MSBuild.SonarQube.Runner-2.0.zip) 後將其解壓縮。  


![1.png](1.png)

<br/>


再來要開啟 `SonarQube.Analysis.xml` 設定 SonarQube 的位置以及認證的資訊。  

![2.png](2.png)

<br/>


設定完後運行 `MSBuild.SonarQube.Runner.exe begin` 開始分析。  

    MSBuild.SonarQube.Runner.exe begin /k:"sonarqube_project_key" /n:"sonarqube_project_name" /v:"sonarqube_project_version"

![3.png](3.png)

<br/>


接著用 MSBuild 建置要分析的專案。  

![4.png](4.png)

<br/>


最後運行 `MSBuild.SonarQube.Runner.exe end` 停止分析。  

    MSBuild.SonarQube.Runner.exe end

![5.png](5.png)

<br/>


分析完的結果就會送到 SonarQube 上。  

![6.png](6.png)

<br/>


![7.png](7.png)

<br/>


![8.png](8.png)

<br/>


![9.png](9.png)

<br/>


![10.png](10.png)

<br/>


![11.png](11.png)

<br/> 


Link
