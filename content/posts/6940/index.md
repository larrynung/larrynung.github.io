---
title: "[Visual Studio]The Toolbar Solution Configuration for More Convenient Builds"
slug: "visual-studio-the-toolbar-solution-configuration-for-more-convenient-builds"
aliases: ["/posts/6940/"]
date: "2009-01-25 03:11:42"
description: "一般來說當要切換建置的類型是Debug或是Release的話，通常我們可通過下列四種方法。 專案=>屬性=>建置 (圖一) 方案總管上按右鍵=>屬性=>建置 (圖一) 連點兩下Properties=>建置 (圖一) 建置=>組態管理員 (圖二) 圖一 屬性頁面設定建置類型 圖二 組態管理員…"
tags: [Visual Studio]
---

一般來說當要切換建置的類型是Debug或是Release的話，通常我們可通過下列四種方法。

1. 專案=>屬性=>建置 (圖一)
2. 方案總管上按右鍵=>屬性=>建置 (圖一)
3. 連點兩下Properties=>建置 (圖一)
4. 建置=>組態管理員 (圖二)

![image_thumb_1.png](/images/posts/6940/image_thumb_1.png)

圖一 屬性頁面設定建置類型

![image_thumb_2.png](/images/posts/6940/image_thumb_2.png)

圖二 組態管理員

但不論是上面哪一種方法，個人覺得使用上都不會比能直接在工具列上選擇方案組態來得方便。不僅能清楚判別目前是Debug還是Release，在切換上也方便了許多。

![image_thumb_3.png](/images/posts/6940/image_thumb_3.png)

要把方案組態設到工具列主要步驟如下：

Step1. "工具=>自訂=>建置=>方案組態" 或 "工具列上按右鍵=>自訂=>建置=>方案組態"

![image_thumb_4.png](/images/posts/6940/image_thumb_4.png)

Step2.把右半部命令區的方案組態用滑鼠拖曳到工具列上想放的位置。

Step3.關閉自訂對話框

p.s.若是把方案組態放上去工具列後發現是灰階無法選取，或是當你在專案屬性的建置頁面看不到如圖一的畫面，又或著是在建置的選單下找不到方案組態時。我們需到 "工具=>選項=>專案與方案" 把 "顯示進階建置組態"給勾選。

![image_thumb_5.png](/images/posts/6940/image_thumb_5.png)
