---
title: "[C#][VB.NET]設定.NET透明表單"
date: "2008-11-10 12:49:27"
description: "[C#][VB.NET]設定.NET透明表單"
tags: [VB.NET, CSharp]
---

## Abstract

*   Introduction
*   Form.Opacity屬性設定不透明度
*   Form.TransparencyKey屬性設定透明的顏色
*   Form.Opacity VS Form.TransparencyKey
*   Conclusion

## Introduction

在.NET WinForm程式中，要設定透明表單有兩種方式。一種是用Form.Opacity屬性來設定表單的不透明度，一種則是用Form.TransparencyKey屬性來設定表單上視為透明的顏色。本篇將會對兩種方法做個簡單的介紹，並針對兩者做點小小的比較。

## Form.Opacity屬性設定不透明度

以Form.Opacity屬性為例，該屬性值所設定的是0~1之間的雙精度浮點數(Double)，用以表示表單的不透明度比例。如下圖所示，該值越小越透明、越大則越不透明。

<table border="0" cellpadding="2" cellspacing="0" width="400">

<tbody>

<tr>

<td valign="top" width="133">Form.Opacity = 0.3</td>

<td valign="top" width="133">Form.Opacity = 0.6</td>

<td valign="top" width="133">Form.Opacity = 1</td>

</tr>

<tr>

<td valign="top" width="133">![image](\images\posts\5931\image_thumb_8.png)</td>

<td valign="top" width="133">![image](\images\posts\5931\image_thumb_9.png)</td>

<td valign="top" width="133">![image](\images\posts\5931\image_thumb_10.png)</td>

</tr>

</tbody>

</table>

完整範例如下:

VB.NET

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2c97cd15-6618-4836-bdef-60b2d360966e" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<pre class="vb" name="code">	Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load
        With Me.TrackBar1
            .TickStyle = TickStyle.None
            .Maximum = 100
            .Minimum = 0
            .Value = 100
        End With
        Me.Text = String.Format("不透明度 - {0}%", TrackBar1.Value)
    End Sub

    Private Sub TrackBar1_ValueChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles TrackBar1.ValueChanged
        Me.Opacity = TrackBar1.Value / 100
        Me.Text = String.Format("不透明度 - {0}%", TrackBar1.Value)
    End Sub</pre>

</div>

C#

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:76fc05ab-a29a-4615-9649-b6053c0fcdf4" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<pre class="c#" name="code">	private void Form1_Load(object sender, EventArgs e)
        {
            this.trackBar1.TickStyle = TickStyle.None;
            this.trackBar1.Maximum = 100;
            this.trackBar1.Minimum = 0;
            this.trackBar1.Value = 100;
            this.Text = string.Format("不透明度 - {0}%", trackBar1.Value);
        }

        private void trackBar1_ValueChanged(object sender, EventArgs e)
        {
            this.Opacity = trackBar1.Value / 100;
            this.Text = string.Format("不透明度 - {0}%", trackBar1.Value);
        }</pre>

</div>

## Form.TransparencyKey屬性設定透明的顏色

要用Form.TransparencyKey屬性來設定表單透明度，只須把該屬性設為欲透明的顏色，則當表單上存在著被設為透明色的顏色區塊時，該顏色區塊就會被視為是透明的。用該方法設定的透明效果跟用Form.Opacity的方法是不同的。該方法的透明是完全的透明(透明度100%)，且若用滑鼠點選在表單中透明的區塊上，滑鼠的點選動作會穿透目前的表單點選到目前表單下方的視窗，而Form.Opacity的透明除非是設為完全透明，不然無法穿透目前的表單。

**P.S.**Form.Opacity = 0 雖然也可以完全穿透目前表單，但是表單上面的元件也會跟著透明。

## Form.Opacity VS Form.TransparencyKey

<table border="1" cellpadding="5" cellspacing="0" width="748">

<tbody>

<tr>

<td valign="top" width="303">**Form.Opacity**</td>

<td valign="top" width="301">**Form.TransparencyKey**</td>

</tr>

<tr>

<td valign="top" width="138">**優點**</td>

<td valign="top" width="303">

*   可調整透明度比例

</td>

<td valign="top" width="300">

*   點選表單透明區塊可穿透表單
*   可設定表單一部份為透明區塊，只會影響跟設定相同顏色的區塊

</td>

</tr>

<tr>

<td valign="top" width="138">**缺點**</td>

<td valign="top" width="303">

*   點選表單不完全透明區塊(Form.Opacity != 0)不可穿透表單
*   透明度會影響整個表單上的元件

</td>

<td valign="top" width="300">

*   不可調整透明度比例

</td>

</tr>

</tbody>

</table>

## Conclusion

本篇介紹了WinForm中改變表單透明度的兩種方法。雖然兩種方法都可以達到透明表單的效果，但在實際的應用上，我個人覺得用Form.TransparencyKey來設定表單透明度較為實用。雖此方法無法調整透明程度，但是其所具備的穿透透明區塊與可透明表單中部分區塊的特性，大幅增加了應用上的彈性。
