---
title: "[WPF]Canvas"
date: "2009-05-08 12:31:46"
description: "[WPF]Canvas"
tags: [WPF]
---

## Introduction

Canvas容器可任意設置容器內部控制項的相對位置。

## 命名空間

System.Windows.Controls

## XMLNS

http://schemas.microsoft.com/winfx/xaml/presentation

## Assemble

PresentationFramework (在 PresentationFramework.dll)

## 功能

定義一個區域，您可以在其中使用與 Canvas 區域相對的座標，明確地放置子項目。

範例

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <Canvas>
        <TextBlock Canvas.Left="20" Canvas.Top="50">
            ● &lt;- 學校 (20,50)
        </TextBlock>
        <TextBlock Canvas.Left="150" Canvas.Top="200">
            ● &lt;- 火車站 (150,200)
        </TextBlock>
        <TextBlock  Canvas.Top="100">
            ● &lt;- 加油站 (0,100)
        </TextBlock>
    </Canvas>
</Window>
```

執行結果

![image_thumb.png](/images/posts/8352/image_thumb.png)
