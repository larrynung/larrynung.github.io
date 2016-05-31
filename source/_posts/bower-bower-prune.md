---
layout: post
title: "Bower - Bower prune"
date: 2016-01-20 05:34:00
comments: true
tags: [Bower]
keywords: "Bower"
description: "Bower - Bower prune"
---

Bower prune 可用來移除未被使用的 bower 套件。  

<!-- More -->

<br/>


如果有 Bower 套件未被 bower.json 檔參照到，當呼叫 bower prune 時就會被移除。

<br/>


像是這邊本地已安裝了 Bootstrap 與 JQuery 套件，但這套件並未在 bower.json 有被參照，因此當呼叫了 bower prune 時就會被移除。  

{% img /images/posts/BowerPrune/1.png %}
