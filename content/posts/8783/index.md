---
title: "[VB.NET]用MyDataBase更新DataGridView上變動的資料"
date: "2009-06-11 12:39:37"
description: "[VB.NET]用MyDataBase更新DataGridView上變動的資料"
tags: [VB.NET]
---

## Introduction

這陣子碰到許多網友再問如何用Update更新資料到資料庫。為回答網友的提問，用MyDataBase偷懶的寫了一個範例程式。主要功能是把DataGridView上更動的資料寫回資料庫。在此隨手記錄一下。

欲看Update的寫法可參考MyDataBase原始碼。需注意的是，MyDataBase內部所用的Command是用自動產生的，在效能上會較直接指定Command來得差，參考看看就好。

## 範例

VB.NET