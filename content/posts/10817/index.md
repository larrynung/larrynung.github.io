---
title: "[C#][VB.NET]使用SystemInformation.PowerStatus查看目前電源使用狀態"
slug: "[CSharp][VB.NET]使用SystemInformation.PowerStatus查看目前電源使用狀態"
date: "2009-09-29 08:22:26"
description: "Introduction 這篇簡單記錄一下，如何透過SystemInformation類別的PowerStatus屬性，來查看目前電源的使用狀態。 Namespace System.Windows.Forms Assembly System.Windows.Forms (in…"
tags: [CSharp]
---

## Introduction

這篇簡單記錄一下，如何透過SystemInformation類別的PowerStatus屬性，來查看目前電源的使用狀態。

## Namespace

System.Windows.Forms

## Assembly

System.Windows.Forms (in System.Windows.Forms.dll)

## Properties

以下為PowerStatus類別所擁有的屬性(摘自MSDN Library)

<table border="1" cellpadding="2" cellspacing="0" width="701"><tbody> <tr> <td valign="top" width="200">BatteryChargeStatus</td> <td valign="top" width="499">Gets the current battery charge status.</td> </tr> <tr> <td valign="top" width="200">BatteryFullLifetime</td> <td valign="top" width="499">Gets the reported full charge lifetime of the primary battery power source in seconds.</td> </tr> <tr> <td valign="top" width="200">BatteryLifePercent</td> <td valign="top" width="499">Gets the approximate percentage of full battery time remaining.</td> </tr> <tr> <td valign="top" width="200">BatteryLifeRemaining</td> <td valign="top" width="499">Gets the approximate number of seconds of battery time remaining.</td> </tr> <tr> <td valign="top" width="200">PowerLineStatus</td> <td valign="top" width="499">Gets the current system power status.</td> </tr> </tbody></table>

MSDN上已經說明的很清楚了，這邊就只簡單的說明一下：

<table border="1" cellpadding="2" cellspacing="0" width="701"><tbody> <tr> <td valign="top" width="200">BatteryChargeStatus</td> <td valign="top" width="499">表示目前充電狀態。          <br/>回傳值為BatteryChargeStatus型態的列舉值，其值可為High(高電量)、Low(低電量)、Critical(極低電量)、Charging(充電中)、NoSystemBattery(沒電池)、與Unknown(狀態不詳)。</td> </tr> <tr> <td valign="top" width="200">BatteryFullLifetime</td> <td valign="top" width="499">表示充滿電力可使用多久時間(-1為不詳)。</td> </tr> <tr> <td valign="top" width="200">BatteryLifePercent</td> <td valign="top" width="499">表示電力剩餘多少百分比(255為不詳)。</td> </tr> <tr> <td valign="top" width="200">BatteryLifeRemaining</td> <td valign="top" width="499">表示剩餘電力可使用多久時間(-1為不詳)。</td> </tr> <tr> <td valign="top" width="200">PowerLineStatus</td> <td valign="top" width="499">表示電源狀態。          <br/>回傳值為PowerLineStatus型態的列舉值，其值可為Online(充電狀態)、Offline(電池模式)、與Unknow(狀態不詳)。</td> </tr> </tbody></table>

## Example

C#

```csharp
namespace BatteryInfo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void UpdateInfo()
        {
            PowerStatus ps = SystemInformation.PowerStatus;
            this.tbxPowerStatus.Text = ps.PowerLineStatus.ToString();
            this.tbxBatteryChargeStatus.Text = ps.BatteryChargeStatus.ToString();
            this.tbxBatteryFullLifetime.Text = ps.BatteryFullLifetime.ToString();
            this.tbxBatteryLifePercent.Text = ps.BatteryLifePercent.ToString();
            this.tbxBatteryLifeRemaining.Text = ps.BatteryLifeRemaining.ToString();
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            UpdateInfo();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            UpdateInfo();
        }
    }
}
```

VB.NET

```vb
Public Class Form1
    Private Sub UpdateInfo()
        Dim ps As PowerStatus = SystemInformation.PowerStatus
        With Me
            .tbxPowerStatus.Text = ps.PowerLineStatus.ToString
            .tbxBatteryChargeStatus.Text = ps.BatteryChargeStatus.ToString
            .tbxBatteryFullLifetime.Text = ps.BatteryFullLifetime
            .tbxBatteryLifePercent.Text = ps.BatteryLifePercent
            .tbxBatteryLifeRemaining.Text = ps.BatteryLifeRemaining
        End With
    End Sub
    Private Sub timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles timer1.Tick
        UpdateInfo()
    End Sub
    Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        UpdateInfo()
    End Sub
End Class
```

執行畫面

![image_thumb.png](/images/posts/10817/image_thumb.png)

## Link

* PowerStatus 類別
* PowerLineStatus 列舉型別
* BatteryChargeStatus 列舉型別
