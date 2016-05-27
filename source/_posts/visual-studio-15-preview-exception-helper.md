---
layout: post
title: "Visual Studio 15 Preview - Exception Helper"
date: 2016-04-25 22:57:00
comments: true
categories: [Visual Studio]
keywords: "Visual Studio"
description: "Visual Studio 15 Preview - Exception Helper"
---

Visual Studio 15 Preview 以前，託管的程式會透過 Exception Assistant 提供錯誤資訊。  

<!-- More -->

{% img /images/posts/VS15PreviewExceptionHelper/1.png %}

<br/>


非託管的程式或是將 Exception Assistant 關閉的話，則是透過
 Exception Dialog 提供錯誤資訊。  

{% img /images/posts/VS15PreviewExceptionHelper/2.png %}

<br/>


在 Visual Studio 15 Preview 以後，開發人員可以選擇使用 Exception Helper 來提供除錯資訊，只要開啟選項對話框，切換到偵錯頁面，啟用 Exception Helper。  

{% img /images/posts/VS15PreviewExceptionHelper/3.png %}

<br/>


當例外發生時，錯誤資訊就會改用 Exception Helper，可以看到新的 Exception Helper 訊息精簡許多。  

{% img /images/posts/VS15PreviewExceptionHelper/4.png %}

<br/>


新的 Exception Helper 不會像以往一樣直接蓋在程式碼上面，而且可釘選，查閱程式錯誤時不再那麼綁手綁腳。  

{% img /images/posts/VS15PreviewExceptionHelper/5.png %}

<br/>


如果有 Inner exception，也可以很直接就看到 Inner exception 的訊息，不用特別追進 Detail 查閱。  

{% img /images/posts/VS15PreviewExceptionHelper/6.png %}

<br/>


當然若有需要也是可以查閱到 Detail 的部分。  

{% img /images/posts/VS15PreviewExceptionHelper/7.png %}

<br/>

Link
----
* [Using the New Exception Helper in Visual Studio “15” Preview | Microsoft Application Lifecycle Management](https://blogs.msdn.microsoft.com/visualstudioalm/2016/03/31/using-the-new-exception-helper-in-visual-studio-15-preview/)
