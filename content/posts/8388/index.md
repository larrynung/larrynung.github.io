---
title: "[WPF]TextBlock"
date: "2009-05-12 05:44:57"
description: "命名空間 System.Windows.Controls XMLNS http://schemas.microsoft.com/winfx/xaml/presentation Assemble PresentationFramework (在 PresentationFramework.dll)…"
tags: [WPF]
---

## 命名空間

System.Windows.Controls

## XMLNS

http://schemas.microsoft.com/winfx/xaml/presentation

## Assemble

PresentationFramework (在 PresentationFramework.dll)

## 功能

提供輕量控制項，以顯示少量的非固定格式內容。

## 範例

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <Grid>
        <TextBlock TextWrapping="Wrap" Height="262" VerticalAlignment="top">
            <Button>Button</Button>
            Normal
            <Bold>Bold</Bold>
            <Hyperlink>Hyperlink</Hyperlink>
            <Italic>Italic</Italic>
            <Underline>Underline</Underline>
        </TextBlock>
    </Grid>
</Window>
```

執行結果

![image_thumb.png](/images/posts/8388/image_thumb.png)
