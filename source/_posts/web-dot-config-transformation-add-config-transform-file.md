---
layout: post
title: "Web.Config Transformation - Add Config Transform File"
date: 2014-07-07 23:01:00
comments: true
tags: [Web.Config Transformation]
keywords: "Web.Config, Transformation"
description: "Web.Config Transformation - Add Config Transform File"
---

當我們建立一個 Web 專案，Visual Studio 預設就會幫我們產生好 Debug 與 Release 這兩個轉換檔。但隨著專案的進行，專案中的 Build Configuration 可能會隨之增加。此時我們需要為新建的建置組態建立對應的 Config Transform 檔。 

<!-- More -->

<br/>

建立新的 Config Transform 檔很簡單，只要在方案總管中找到 Web.config 檔，在檔案上按下滑鼠右鍵。在彈出的滑鼠右鍵快顯選單中，選取 Add Config Transform 選單選項。Visual Studio 即會比對 Build Configuration 去產生缺少的 Config Transform 檔案。    

<br/>

{% img /images/posts/AddConfigTransform/1.png %}
