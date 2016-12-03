---
title: Web Deploy - Publish with MsBuild
date: 2016-12-03 17:59:16
tags: [Web Deploy]
---

要使用 MsBuild 建置專案並佈署，可以在 MsBuild 建置時帶上 DeployOnBuild 參數告知 MsBuild 在建置完要做佈署，並帶上 PublishProfile 參數指定要使用的 Publish Profile。  

<!-- More -->

    msbuild <ProjectFile|SolutionFile> /p:Configuration=<Configuration>;Platform="<Platform>";DeployOnBuild=true;PublishProfile=<PublishProfile>

<br/>


若有需要可加帶 UserName 參數指定帳號，加帶 Password 參數指定密碼。  

    msbuild <ProjectFile|SolutionFile> /p:Configuration=<Configuration>;Platform="<Platform>";DeployOnBuild=true;PublishProfile=<PublishProfile>;UserName=<UserName>;Password=<Password>

<br/>


或是加帶 AllowUntrastedCertificate參數。  

    msbuild <ProjectFile|SolutionFile> /p:Configuration=<Configuration>;Platform="<Platform>";DeployOnBuild=true;PublishProfile=<PublishProfile>;UserName=<UserName>;Password=<Password>;AllowUntrustedCertificate=True


{% asset_img 1.png %}

<br/>


或是加帶 EnableMSDeployAppOffline 參數使用 AppOffline rule 做佈署，讓 Web deploy 在做發佈的同時幫你放上 App_Offline 頁面。  

    msbuild <ProjectFile|SolutionFile> /p:Configuration=<Configuration>;Platform="<Platform>";DeployOnBuild=true;PublishProfile=<PublishProfile>;UserName=<UserName>;Password=<Password>;AllowUntrustedCertificate=True; EnableMSDeployAppOffline=true


{% asset_img 2.png %}

<br/>
