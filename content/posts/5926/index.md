---
title: "[.NET Resource].NET Runtime Debug Tool - Crack.NET"
date: "2008-11-08 11:38:26"
description: "[.NET Resource].NET Runtime Debug Tool - Crack.NET"
tags: [.NET Resource]
---

## Abstract

- Introduction
- 系統需求
- Link

## Introduction

CrackNet釋出，不知對開發人員來說是好消息還是壞消息。該工具號稱可在Runtime階段做Debug的動作，記憶體中變數的值透過該工具可清楚的呈現。 因此在開發.NET程式時..把重要資料存放在記憶體中(像是Key,Password..)，可能再也不是個安全的做法了。這可能是繼反組譯問題後開發.NET軟體最大的挑戰。不過我只稍微試過，說不定並未像我說的這樣。也說不定混淆或像MaxToCode的核級加密技術能保護它，這就待有興趣的人自行測試了。

Crack.NET啟始畫面如下，用ComboBox下拉選取要察看的程式後，按下"Crack it"按鈕。即會進入Debug畫面。 
![clip_image002_thumb.jpg](/images/posts/5926/clip_image002_thumb.jpg)

Crack.NET Debug畫面如下，可以看到透過Crack.NET可以察看變數的值。

![annotatedmemoryexplorer_selectedobject_v11.png](/images/posts/5926/annotatedmemoryexplorer_selectedobject_v11.png)

如下圖Crack.NET也可以加些Script程式上去用來輔助Debug。

![clip_image006_thumb.jpg](/images/posts/5926/clip_image006_thumb.jpg)

## 系統需求

- .NET Framework version 3.5 with Service Pack 1
- Visual Studio 2008 with Service Pack 1 (if you want to compile the solution)

## Link

Documentation : <http://joshsmithonwpf.files.wordpress.com/2008/10/cracknet-article1.doc>

Link: <http://www.codeplex.com/cracknetproject>

Download (Binaries/code): <http://www.codeplex.com/cracknetproject/Release/ProjectReleases.aspx?ReleaseId=18629>
