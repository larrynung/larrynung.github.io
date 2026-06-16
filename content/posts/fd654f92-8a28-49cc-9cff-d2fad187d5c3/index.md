---
title: "[Web] 使用json2csharp產生對應Json的C#類別"
date: "2013-11-06 12:00:00"
description: "筆者在之前介紹過[.NET Resource]JSON C# Class Generator，一樣能產生對應的C#類別，但是產出的類別有透過Json.NET做了些包裝處理，雖然使用便利，但卻讓它少了點使用上的彈性，若是不想要將Json.NET加入專案，或是想要進階控制一些屬性是否可以為空之類的，"
---

筆者在之前介紹過[.NET Resource]JSON C# Class Generator，一樣能產生對應的C#類別，但是產出的類別有透過Json.NET做了些包裝處理，雖然使用便利，但卻讓它少了點使用上的彈性，若是不想要將Json.NET加入專案，或是想要進階控制一些屬性是否可以為空之類的，就比較不方便。

有這樣的問題時我們可以json2sharp這個網站就能幫我們產生對應Json的C#類別，產出的類別不會有過度的包裝，也不會跟組件綁死，要用內建的序列化解序列化的方式都可以。

使用時只要將Json網址或是Json字串帶入，並按下下方的Generate按鈕。

![image_thumb_1.png](/images/posts/fd654f92-8a28-49cc-9cff-d2fad187d5c3/image_thumb_1.png)

像是下面這樣：

![image_thumb_2.png](/images/posts/fd654f92-8a28-49cc-9cff-d2fad187d5c3/image_thumb_2.png)

網頁就會在下方幫我們產生出對應的C#類別：

![image_thumb_3.png](/images/posts/fd654f92-8a28-49cc-9cff-d2fad187d5c3/image_thumb_3.png)

## Link

* [json2csharp](http://json2csharp.com/)
