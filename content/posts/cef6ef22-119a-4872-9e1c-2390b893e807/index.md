---
title: "Formatting XAML Code"
date: "2013-11-06 12:00:00"
tags: [XAML]
description: "最近在寫WPF應用程式，開發時常常會將元件、Template、Setter、Resource之類的複製來複製去，一不小心整個XAML程式就會變得很髒亂。程式看起來就像下面這張圖一樣，整個就是不對齊，就算怎樣在XAML編輯界面上按熱鍵Ctrl + K, F，就是硬不對齊，"
---

最近在寫WPF應用程式，開發時常常會將元件、Template、Setter、Resource之類的複製來複製去，一不小心整個XAML程式就會變得很髒亂。程式看起來就像下面這張圖一樣，整個就是不對齊，就算怎樣在XAML編輯界面上按熱鍵Ctrl + K, F，就是硬不對齊，唯一對齊的就只有Element前的"<"。

![image_thumb.png](/images/posts/cef6ef22-119a-4872-9e1c-2390b893e807/image_thumb.png)

查了一下發現這問題可以透過內建的設定改善，點選[Tools/Options]開啟Options對話框，左側切至[Text Editor/XAML/Formatting/Spacing]，將右側的Attribute Spacing設定調成Position each attribute on a separate line。

![image_thumb_1.png](/images/posts/cef6ef22-119a-4872-9e1c-2390b893e807/image_thumb_1.png)

再次在XAML編輯界面上按下熱鍵Ctrl + K, F，程式就會變成像下面這樣，自動會將屬性換行並對齊，整個程式因此整齊了許多。

![image_thumb_2.png](/images/posts/cef6ef22-119a-4872-9e1c-2390b893e807/image_thumb_2.png)
