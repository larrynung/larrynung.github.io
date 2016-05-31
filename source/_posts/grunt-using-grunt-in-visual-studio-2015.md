---
layout: post
title: "Grunt - Using Grunt in Visual Studio 2015"
date: 2016-01-28 01:25:00
comments: true
tags: [Grunt]
keywords: "Grunt"
description: "Grunt - Using Grunt in Visual Studio 2015"
---

Visual Studio 2015 開始支援 Grunt，使用時需先為專案加入 NPM Configuration File。  

<!-- More -->

{% img /images/posts/GruntInVS2015/1.png %}

<br/>


還有 Grunt Configuration File。  

{% img /images/posts/GruntInVS2015/2.png %}

<br/>


接著在 package.json 中加入要使用的 Grunt plugin。  

{% img /images/posts/GruntInVS2015/3.png %}

<br/>


{% img /images/posts/GruntInVS2015/4.png %}

<br/>


設定完按下編譯或是滑鼠右鍵快顯選單中的 Restore Packages 選單選項，即可透過 NPM 下載 Grunt plugin。  

{% img /images/posts/GruntInVS2015/5.png %}

<br/>


我們可以透過 Visual Studio 的狀態列觀察到套件下載的狀態。  

{% img /images/posts/GruntInVS2015/6.png %}

<br/>


{% img /images/posts/GruntInVS2015/7.png %}

<br/>


若有需要也可以透過 Output 視窗查看細部處理資訊。  

{% img /images/posts/GruntInVS2015/8.png %}

<br/>


下載完畢，設定完 gruntfile.js，我們就可以在 Task Runner Explorer 點選對應的 Task 進行運行。  

{% img /images/posts/GruntInVS2015/9.png %}
