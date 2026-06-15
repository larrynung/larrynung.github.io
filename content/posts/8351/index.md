---
title: "[WPF]Grid"
date: "2009-05-08 12:31:26"
description: "[WPF]Grid"
tags: [WPF]
---

## Introduction

Grid容器提供像表格一樣可分割列與行的功能 。類似HTML中的Tabel。

## 命名空間

System.Windows.Controls

## XMLNS

http://schemas.microsoft.com/winfx/xaml/presentation

## Assemble

PresentationFramework (在 PresentationFramework.dll)

## 功能

定義由資料行和資料列組成的彈性方格區域。

## 範例

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition/>
            <RowDefinition/>
            <RowDefinition/>
        </Grid.RowDefinitions>
        <Grid.ColumnDefinitions >
            <ColumnDefinition/>
            <ColumnDefinition/>
            <ColumnDefinition/>
        </Grid.ColumnDefinitions>
        <Button FontSize="50" Grid.Row="0" Grid.Column="0">O</Button>
        <Button FontSize="50" Grid.Row="0" Grid.Column="1">X</Button>
        <Button FontSize="50" Grid.Row="0" Grid.Column="2">O</Button>
        <Button FontSize="50" Grid.Row="1" Grid.Column="0">O</Button>
        <Button FontSize="50" Grid.Row="1" Grid.Column="1">X</Button>
        <Button FontSize="50" Grid.Row="1" Grid.Column="2">X</Button>
        <Button FontSize="50" Grid.Row="2" Grid.Column="0">X</Button>
        <Button FontSize="50" Grid.Row="2" Grid.Column="1">O</Button>
        <Button FontSize="50" Grid.Row="2" Grid.Column="2">O</Button>
    </Grid>
</Window>
```

執行結果

![image_thumb.png](/images/posts/8351/image_thumb.png)
