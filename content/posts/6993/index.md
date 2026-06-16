---
title: "[WF]Sequential Workflow Example - Hello World"
slug: "wf-sequential-workflow-example-hello-world"
aliases: ["/posts/6993/"]
date: "2009-02-01 01:28:03"
description: "Abstract Introduction Hello Word Demo Conclusion Download Introduction 本篇藉由示範簡單的Hello Word程式，帶領大家一窺WF神秘的面紗。"
tags: [WF]
---

## Abstract

* Introduction
* Hello Word Demo
* Conclusion
* Download

## Introduction

本篇藉由示範簡單的Hello Word程式，帶領大家一窺WF神秘的面紗。

## Hello Word Demo

Step1.新增WF專案

![image_thumb.png](/images/posts/6993/image_thumb.png)

WF專案建立好後會看到如下畫面，我們可以清楚看到WF的程式編寫方式已明顯的與一般專案程式不同。程式編寫的方式已變成以流程為導向的編寫方式，藉由托拉控制項的元件編排程式的流程與邏輯，並在流程與邏輯元件內加入對應處理的程式碼，就可以完成WF程式的編寫。

![image_thumb_1.png](/images/posts/6993/image_thumb_1.png)

Step2.編寫程式邏輯與流程。這邊因為我們的範例程式只須秀出一串"Hello World"，因此我們只須把Code這個元件加到程式流程。

![image_thumb_2.png](/images/posts/6993/image_thumb_2.png)

元件放入後會看到如下畫面，由此圖是不是可以很清楚的看出程式的流程呢？(圖上的驚嘆號是提醒程式設計師未加入對應處理的程式碼)

![image_thumb_3.png](/images/posts/6993/image_thumb_3.png)

Step3.為程式的流程與邏輯加入對應的處理程式。在這邊我們只需在剛拉的元件上用滑鼠連點兩下，即會出現對應的程式碼區塊。在該區塊我們只要加上程式碼去顯示"Hello Word"即可。(VB與C#在這邊程式碼只差在分號，因此不貼Code了)

![image_thumb_4.png](/images/posts/6993/image_thumb_4.png)

Step4.執行。執行後我們可以看到如下的執行畫面，一個簡單的WF Hello Word範例就完成了。

![image_thumb_5.png](/images/posts/6993/image_thumb_5.png)

## Conclusion

Hello Word範例一直是程式入門的經典範例，藉由簡單的Hello Word程式的寫作，可以讓我們更快的進入並了解程式的特性與原理。而對於WF程式而言，這小範例可點出WF程式的編寫與一般程式的差異之處，有感覺的甚至可以了解WF程式可應用之處，甚至可以感受到WF程式在執行上效率好像會比一般程式來得慢。

## Download

WF_HelloWord.zip
