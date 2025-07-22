---
title: "[Design Pattern]Observer模式"
date: "2009-04-23 08:57:02"
description: "[Design Pattern]Observer模式"
tags: [Design Pattern]
---

## 字面意思
  
observer [əbˈzə:və]
  
n.觀察者，觀察員

## 意圖
     定義物件間的一種一對多的依賴關係，當物件狀態改變，所有依賴的物件都會收到通知並自動變更。    

## 口訣
  
通知狀態變更

## 問題
  
當某事件發生，需要向其它對象發出通知。

## 實現方法
     Observer向Subject註冊     Subject通知Observer事件發生