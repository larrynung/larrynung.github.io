---
title: Web Deploy - Generate Web Deploy package with MsBuild
date: 2016-12-05 00:15:52
tags: [Web Deploy]
---

要使用 MsBuild 建置 Web Deploy package，可以在 MsBuild 建置時用 /t:package 告知要產生 Web Deploy package，並帶上 PackageLocation 參數指定產出的 Package 放置位置。  

<!-- More -->

    msbuild <ProjectFile|SolutionFile> 
            /p:Configuration=<Configuration>;
               Platform="<Platform>";
               PackageLocation="<PackageLocation>" 
            /t:package

{% asset_img 1.png %}

<br/>


建置完成就可以在指定的位置看到產出的 Web Deploy package。  

{% asset_img 2.png %}

<br/>
