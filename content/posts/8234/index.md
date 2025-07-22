---
title: "[VB.NET].NET多語系程式(三)"
date: "2009-04-29 12:05:15"
description: "[VB.NET].NET多語系程式(三)"
tags: [VB.NET]
---

## Abstract
Introduction學習目標操作步驟簡易實作範例

## Introduction

本篇將介紹.NET多語系程式的寫法 ，下面會利用XML文件來達到多語系的功能。

## 學習目標
.NET多語程式撰寫 用XML文件實現多語功能XML序列化與解序列化

## 操作步驟
Step1.建立內含多語訊息的XML文件
XML文件格式可能如下，內含CultureInfo代碼與對應的訊息字串。

Step2.切換語系時，從XML文件中抓取對應的顯示字串

## 簡易實作範例

基本上這邊只是提示多語程式功能可透過XML文件實現，實現步驟大概如上面所述。然而XML文件的格式與存取的方法與寫法則就看個人怎樣編寫。這邊提供個簡易的範例：
MultiLanguage類別
MultiLanguage類別的Code如下

建立各語系字串
 
切換語系
 
儲存XML
 
讀取XML