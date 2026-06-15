---
title: "[WPF]StackPanel"
date: "2009-05-07 12:42:17"
description: "[WPF]StackPanel"
tags: [WPF]
---

## Introduction

StackPanel容器可讓容器內的控制項呈現水平或垂直排列。

## 命名空間

System.Windows.Controls

## XMLNS

http://schemas.microsoft.com/winfx/xaml/presentation

## Assemble

PresentationFramework (在 PresentationFramework.dll)

## 功能

將子項目排列在可為水平或垂直方向的單一行中。

## 範例一

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <StackPanel Orientation="Horizontal" >
        <Button Background="Wheat" >按鈕一</Button>
        <Button Background="Yellow" >按鈕二</Button>
        <Button Background="#00AA00">按鈕三</Button>
    </StackPanel>
</Window>
```

執行結果

![image_thumb.png](/images/posts/8325/image_thumb.png)

## 範例二

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <StackPanel Orientation="Vertical"  >
        <Button Background="Wheat" >按鈕一</Button>
        <Button Background="Yellow" >按鈕二</Button>
        <Button Background="#00AA00">按鈕三</Button>
    </StackPanel>
</Window>
```

執行結果

![image_thumb_1.png](/images/posts/8325/image_thumb_1.png)

## 範例三

```
<Page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" WindowTitle="StackPanel Sample">
    <StackPanel>
        <Border Background="SkyBlue" BorderBrush="Black" BorderThickness="1">
            <TextBlock Foreground="Black" FontSize="12">Stacked Item #1</TextBlock>
        </Border>
        <Border Width="400" Background="CadetBlue" BorderBrush="Black" BorderThickness="1">
            <TextBlock Foreground="Black" FontSize="14">Stacked Item #2</TextBlock>
        </Border>
        <Border Background="LightGoldenRodYellow" BorderBrush="Black" BorderThickness="1">
            <TextBlock Foreground="Black" FontSize="16">Stacked Item #3</TextBlock>
        </Border>
        <Border Width="200" Background="PaleGreen" BorderBrush="Black" BorderThickness="1">
            <TextBlock Foreground="Black" FontSize="18">Stacked Item #4</TextBlock>
        </Border>
        <Border Background="White" BorderBrush="Black" BorderThickness="1">
            <TextBlock Foreground="Black" FontSize="20">Stacked Item #5</TextBlock>
        </Border>
    </StackPanel>
</Page>
```

執行結果

![image_thumb_2.png](/images/posts/8325/image_thumb_2.png)
