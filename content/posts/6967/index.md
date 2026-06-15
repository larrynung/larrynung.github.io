---
title: "[Visual Studio]Speed Up Visual Studio"
date: "2009-01-29 10:23:05"
description: "[Visual Studio]Speed Up Visual Studio"
tags: [Visual Studio]
---

![image_thumb_14.png](/images/posts/6967/image_thumb_14.png)

## Abstract

* Introduction
* Speed Up Visual Studio
  * 關閉動畫
  * 關閉巡覽列
  * 關閉追蹤修訂
  * 關閉追蹤現有項目
  * 關閉AutoToolboxPopulate
  * 關閉啟始頁
  * 關閉歡迎畫面
  * 關閉所有不必要的panels/tabs
* Conclusion
* Reference

## Introduction

本篇整理了八點Visual Studio IDE效能相關設定。藉由這些環境設定的修改，讓Visual Studio的開啟速度大為提升，增進程式開發效率。

## Speed Up Visual Studio

* 關閉動畫

工具=>選項=>環境=>取消勾選動畫環境工具

![image_thumb_3.png](/images/posts/6967/image_thumb_3.png)

* 關閉巡覽列

當使用了ReSharper等輔助軟體，或是本身沒有使用巡覽列的習慣，可以關閉Visual Studio的巡覽列功能。(下圖為巡覽列功能示意圖)

![image_thumb_6.png](/images/posts/6967/image_thumb_6.png)

若要關閉Visual Studio的巡覽列功能，我們可以依下圖所示，工具=>選項=>文字編輯器=>[語言]=>一般=>取消勾選巡覽列。

![image_thumb_4.png](/images/posts/6967/image_thumb_4.png)

* 關閉追蹤修訂

工具=>選項=>文字編輯器=>一般=>取消勾選追蹤修訂

![image_thumb_8.png](/images/posts/6967/image_thumb_8.png)

* 關閉追蹤現有項目

工具=>選項=>專案和方案=>取消勾選在方案總管中追蹤現用項目
![image_thumb_9.png](/images/posts/6967/image_thumb_9.png)

* 關閉AutoToolboxPopulate

工具=>選項=>WindowsForm設計工具=>AutoToolboxPopulate設為False

![image_thumb_10.png](/images/posts/6967/image_thumb_10.png)

p.s.若時常會有寫控制項的需求，不建議關閉AutoToolboxPopulate。因為這樣寫的控制項不會在建置後自動跑到工具箱，使用上會較為不便。

* 關閉啟始頁

工具=>選項=>環境=>啟動=>把"顯示啟始頁"改設為"顯示空白環境"

![image_thumb_11.png](/images/posts/6967/image_thumb_11.png)

* 關閉歡迎畫面

Step1.滑鼠右鍵開啟 Visual Studio 2005 捷徑內容

Step2.在目標路徑後面增加"`/nosplash`"參數

![image_thumb_12.png](/images/posts/6967/image_thumb_12.png)

* 關閉所有不必要的panels/tabs

防止Visual Studio IDE在讀取時做不必要的載入

## Conclusion

本文介紹了八點關於Visual Studio效能方面的設定 ，這些設定雖對於Visual Studio IDE在速度上面有相當的助益。但在實際使用上仍須視自己的習慣與需求而定。舉例來說，個人因習慣的關係，在使用上就不會關閉AutoToolboxPopulate與關閉巡覽列功能。

## Reference

1. [Optimize the launch of the Visual Studio 2005](http://dotnettipoftheday.org/tips/optimize_launch_of_vs2005.aspx)
2. [Speed up Visual Studio 2005](http://dotnettipoftheday.org/tips/speedup_visual_studio.aspx)
