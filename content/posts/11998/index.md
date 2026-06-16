---
title: "[VB.NET]Detect Design-Time & Run-Time"
date: "2009-11-16 01:22:12"
description: "Introduction 在撰寫控制項時，我們常會需要依照不同的階段作不同的處理。像是在設計階段顯示與運行階段不同的畫面、關閉些在設計階段會造成錯誤的處理等等。這邊將對偵測目前所處階段的語法作些整理。"
tags: [VB.NET]
---

## Introduction

在撰寫控制項時，我們常會需要依照不同的階段作不同的處理。像是在設計階段顯示與運行階段不同的畫面、關閉些在設計階段會造成錯誤的處理等等。這邊將對偵測目前所處階段的語法作些整理。

## Detect Design-Time & Run-Time

若要在程式中分辨設計階段(Design-Time)與運行階段(Run-Time)，我們大致上有以下幾種方法。

### WinForm

**1.判斷Component.DesignMode**

```vb
Dim isDesignTime As Boolean = Component.DesignMode
```

**2.判斷Site.DesignMode**

```vb
Dim isDesignTime As Boolean = Me.Site IsNot Nothing AndAlso Me.Site.DesignMode
```

**3.判斷當前處理序是否為Visual Studio**

```vb
Dim isDesignTime As Boolean = Process.GetCurrentProcess().ProcessName.Equals("devenv", StringComparison.OrdinalIgnoreCase)
```

**4.判斷LicenseUsageMode.UsageMode是否為LicenseUsageMode.Designtime**

```vb
Dim isDesignTime As Boolean = System.ComponentModel.LicenseManager.UsageMode = System.ComponentModel.LicenseUsageMode.Designtime
```

**5.判斷GetService(GetType(System.ComponentModel.Design.IDesignerHost))不為空**

```vb
Dim isDesignTime As Boolean = GetService(GetType(System.ComponentModel.Design.IDesignerHost)) IsNot Nothing
```

### ASP.NET

請參閱Detecting Designmode in ASP.Net

### WPF

請參閱Detecting design time mode in WPF and Silverlight

## Link

* How Do I Detect Design-Time Vs Run-Time in a .NET Control?
* Identifying the Run-Time and the Design Mode
* Design Time Detection
* Detect if Code is Running from the IDE
* Detecting Design-time in C#
* #### Windows Forms designer and DesignMode property issues
* MSDN - Component.DesignMode Property
* MSDN - IDesignerHost 介面
* #### Detecting Designmode in ASP.Net
* #### Detecting design time mode in WPF and Silverlight
