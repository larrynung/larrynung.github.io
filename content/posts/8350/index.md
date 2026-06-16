---
title: "[WPF]DockPanel"
date: "2009-05-08 12:30:45"
description: "Introduction DockPanel容器主要為容器內部的控制項提供停靠的機制。 命名空間 System.Windows.Controls XMLNS http://schemas.microsoft.com/winfx/xaml/presentation Assemble…"
tags: [WPF]
---

## Introduction

DockPanel容器主要為容器內部的控制項提供停靠的機制。

## 命名空間

System.Windows.Controls

## XMLNS

http://schemas.microsoft.com/winfx/xaml/presentation

## Assemble

PresentationFramework (在 PresentationFramework.dll)

## 功能

定義一個區域，讓子項目可以依彼此相對的水平或垂直位置來排列。

## 範例

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <DockPanel Height="263" Name="DockPanel1" Width="276">
        <Menu DockPanel.Dock="Top" >
            <MenuItem Header="File">
                <MenuItem Header="Open"></MenuItem>
            </MenuItem>
        </Menu>

        <ToolBarPanel DockPanel.Dock="Top">
            <Button HorizontalAlignment="Left" >Tool</Button>
        </ToolBarPanel>

        <StackPanel Width="150" Background="Yellow"   DockPanel.Dock="Left">
            <TextBlock Background="Gray">Tool1</TextBlock>
            <TextBlock Background="Aqua">Tool2</TextBlock>
        </StackPanel>

        <StackPanel Width="150" DockPanel.Dock="Left">
        </StackPanel>

    </DockPanel>
</Window>
```

執行結果

![image_thumb.png](/images/posts/8350/image_thumb.png)
