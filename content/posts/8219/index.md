---
title: "[Control]MarqueeLabel 1.0"
date: "2009-04-28 12:40:48"
description: "Introduction MarqueeLabel要是沒記錯，應該是去年無聊時寫的控制項 。該控制項的功能就如同它的名稱一樣就只是跑馬燈的效果而已。 加入控制項 Step1.工具箱=>滑鼠右鍵=>選擇項目 Step2.選取控制項檔案 完成後就會在工具箱內看到MarqueeLabel控制項 類別成員…"
tags: [Control]
---

## Introduction

MarqueeLabel要是沒記錯，應該是去年無聊時寫的控制項 。該控制項的功能就如同它的名稱一樣就只是跑馬燈的效果而已。

## 加入控制項

**Step1.工具箱=>滑鼠右鍵=>選擇項目**

![image_thumb.png](/images/posts/8219/image_thumb.png)

**Step2.選取控制項檔案**

![image_thumb_3.png](/images/posts/8219/image_thumb_3.png)

![image_thumb_1.png](/images/posts/8219/image_thumb_1.png)

![image_thumb_2.png](/images/posts/8219/image_thumb_2.png)

完成後就會在工具箱內看到MarqueeLabel控制項

![image_thumb_4.png](/images/posts/8219/image_thumb_4.png)

## 類別成員

欲使用MarqueeLabel控制項，首先須了解下面成員 ：

**屬性**

<table border="0" cellpadding="2" cellspacing="0" width="400">
<tbody>
<tr>
<td valign="top" width="200">
				名稱</td>
<td valign="top" width="200">
				說明</td>
</tr>
<tr>
<td valign="top" width="200">
				EnableMarquee</td>
<td valign="top" width="200">
				是否啟動跑馬燈</td>
</tr>
<tr>
<td valign="top" width="200">
				GradientTextStartColor</td>
<td valign="top" width="200">
				漸層起始顏色</td>
</tr>
<tr>
<td valign="top" width="200">
				GradientTextEndColor</td>
<td valign="top" width="200">
				漸層結束顏色</td>
</tr>
<tr>
<td valign="top" width="200">
				TickInterval</td>
<td valign="top" width="200">
				跑馬燈觸發毫秒</td>
</tr>
</tbody>
</table>

**方法**

<table border="0" cellpadding="2" cellspacing="0" width="400">
<tbody>
<tr>
<td valign="top" width="200">
				名稱</td>
<td valign="top" width="200">
				說明</td>
</tr>
<tr>
<td valign="top" width="200">
				StartMarquee</td>
<td valign="top" width="200">
				起動跑馬燈</td>
</tr>
<tr>
<td valign="top" width="200">
				StopMarquee</td>
<td valign="top" width="200">
				停止跑馬燈</td>
</tr>
<tr>
<td valign="top" width="200">
				PauseMarquee</td>
<td valign="top" width="200">
				暫停跑馬燈</td>
</tr>
</tbody>
</table>

## 簡易範例

**Step1.放入MarqueeLabel控制項**

![image_thumb_5.png](/images/posts/8219/image_thumb_5.png)

**Step2.設定漸層色與欲顯示的字串**

若要調整漸層色可透過設定GradientTextStartColor與GradientTextEndColor屬性，而要設定欲顯示的字串可修改Text屬性值。

![image_thumb_6.png](/images/posts/8219/image_thumb_6.png)

**Step3.啟動跑馬燈**

欲啟動跑馬燈可透過設定EnableMarquee屬性或是StartMarquee方法。

![image_thumb_7.png](/images/posts/8219/image_thumb_7.png) ![image_thumb_8.png](/images/posts/8219/image_thumb_8.png)

![image_thumb_9.png](/images/posts/8219/image_thumb_9.png) ![image_thumb_10.png](/images/posts/8219/image_thumb_10.png)

## Download

MarqueeLabel 1.0.zip
