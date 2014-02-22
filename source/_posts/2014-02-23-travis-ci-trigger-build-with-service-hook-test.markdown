---
layout: post
title: "Travis CI - Trigger build with service hook test"
date: 2014-02-23 00:19
comments: true
categories: [Travis, CI]
keywords: "Travis CI"
description: "Travis CI - Trigger build with service hook test"
---

一般來說， Travis CI 在使用時會主動在程式碼 Push 到 Server 時自動做建置的動作，但難以避免的，有的時候我們還是會需要在特定時機點手動觸發建置。這時如果為此特意 Commit ，整個版控紀錄會變得很亂，所以要透過 GitHub 的 Test Service Hook 功能去觸發 Travis CI 建置。   

<!-- More -->

使用前要先進入 Repository 的 Service Hooks 頁面。  

這邊可直接由 GitHub repository's setting 進入， 或是由 Travis CI 進入。  

{% img /images/posts/TravisCIServiceHookTest/1.png %}

<br/>

進入後會看到像這樣的畫面：

{% img /images/posts/TravisCIServiceHookTest/2.png %}

<br/> 

往下捲動找到 Travis CI 後點擊。

{% img /images/posts/TravisCIServiceHookTest/3.png %}

<br/>

接著點選 Test Hook 按鈕觸發 Travis CI 建置就可以了。    

{% img /images/posts/TravisCIServiceHookTest/4.png %}

<br/>

{% img /images/posts/TravisCIServiceHookTest/5.png %}

