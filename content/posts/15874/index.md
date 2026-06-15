---
title: "[Visual Studio]Visual Studio 2010啟用切換頁面預覽畫面"
date: "2010-06-14 12:56:04"
description: "[Visual Studio]Visual Studio 2010啟用切換頁面預覽畫面"
tags: [Visual Studio]
---

在Visual Studio 2010中，按下Ctrl+Tab切換頁面時，很多人可能會發現切換頁面中的預覽畫面不見了。

![image_thumb.png](/images/posts/15874/image_thumb.png)

要開啟預覽畫面，可在執行中輸入下面的指令：

```xml
reg ADD HKCU\Software\Microsoft\VisualStudio\10.0\General /v ShowThumbnailsOnNavigation /t REG_DWORD /d 1
```

![image_thumb_2.png](/images/posts/15874/image_thumb_2.png)

執行完後，再次按下Ctrl+Tab切換頁面，就會看到預覽畫面了。

![image_thumb_1.png](/images/posts/15874/image_thumb_1.png)

## Link

* 15 minute blog post: A Hidden Feature in Visual Studio 2010
