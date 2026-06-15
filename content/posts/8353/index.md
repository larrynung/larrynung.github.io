---
title: "[WPF]WrapPanel"
date: "2009-05-08 12:32:01"
description: "[WPF]WrapPanel"
tags: [WPF]
---

## Introduction

WrapPanel容器跟StackPanel一樣可由上而下或由左而右排列容器內的控制項。不同的是，當超過容器邊緣WrapPanel會自動換行或換列。

## 命名空間

System.Windows.Controls

## XMLNS

http://schemas.microsoft.com/winfx/xaml/presentation

## Assemble

PresentationFramework (在 PresentationFramework.dll)

## 功能

將子項目由左至右依序放置，在包含方塊的邊緣將內容換行。依據 Orientation 屬性的值，後續的排列方式會由上至下或由右至左依序進行。

## 範例一

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <WrapPanel Orientation="Horizontal" ItemHeight="50" ItemWidth="70">
        <Button>按鈕一</Button>
        <Button>按鈕二</Button>
        <Button>按鈕三</Button>
        <Button>按鈕四</Button>
        <Button>按鈕五</Button>
    </WrapPanel>
</Window>
```

執行結果

![image_thumb.png](/images/posts/8353/image_thumb.png)

## 範例二

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <WrapPanel Orientation="Vertical"  ItemHeight="50" ItemWidth="70">
        <Button>按鈕一</Button>
        <Button>按鈕二</Button>
        <Button>按鈕三</Button>
        <Button>按鈕四</Button>
        <Button>按鈕五</Button>
    </WrapPanel>
</Window>
```

執行結果

![image_thumb_1.png](/images/posts/8353/image_thumb_1.png)

## 範例三

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <WrapPanel Orientation="Vertical" FlowDirection="RightToLeft"  ItemHeight="50" ItemWidth="70">
        <Button>按鈕一</Button>
        <Button>按鈕二</Button>
        <Button>按鈕三</Button>
        <Button>按鈕四</Button>
        <Button>按鈕五</Button>
    </WrapPanel>
</Window>
```

執行結果

![image_thumb_2.png](/images/posts/8353/image_thumb_2.png)
