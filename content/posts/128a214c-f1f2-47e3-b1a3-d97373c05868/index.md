---
title: "Use Xaml Styler to style your xaml code"
date: "2013-11-06 12:00:00"
description: "Use Xaml Styler to style your xaml code"
---

筆者在Formatting XAML Code這篇介紹了一下要怎樣透過Visual Studio內建的功能讓XAML Code變得比較整齊好看，整理出來的結果已經相當的不錯了，但仍舊是有些美中不足的地方，因為內建的功能其實也只是讓XAML的Tag attribute換行對齊而已，雖然看起來是好看了許多，但並未將attribute做個排序整理。所以可能有的元素相同的Attribute在前面，而有的會放在後面，相同性質的Attribute也不會自動群聚在一起，因此在XAML Code的瀏覽上還是有些不方便。

這個問題我們可以透過Xaml Styler來解決，透過Extension and Updates搜尋Xaml Styler並安裝。

![image_thumb.png](/images/posts/128a214c-f1f2-47e3-b1a3-d97373c05868/image_thumb.png)

安裝好後開啟我們的XAML Code，從這張圖我們可以發現透過Visual Studio內建的整理功能，每個元素都可以換行對齊的很整齊，但是卻都維持本來的Attribute順序。Visual Studio沒幫我們排序甚至是分類整理，所以可以看到像是x:Class就在很中間的位置才去設定，x:Name的位置也很不好找，或是事件與屬性的穿插設定，整個XAML Code依舊不是很好閱讀。

![image_thumb_1.png](/images/posts/128a214c-f1f2-47e3-b1a3-d97373c05868/image_thumb_1.png)

這邊我們可以按下滑鼠右鍵，點選Beautity Xaml這個滑鼠右鍵選單選項，讓Xaml Styler幫我們把XAML Code做些整理(也可以透過Ctrl+S存檔觸發，或是按下熱鍵Ctrl+K, Ctrl+2觸發)。

![image_thumb_2.png](/images/posts/128a214c-f1f2-47e3-b1a3-d97373c05868/image_thumb_2.png)

Xaml Styler會依照下面順序幫我們排序整理：

* x:Class
* XML Namespaces
  * WPF built-in namespaces
  * User defined namespaces
* Key, Name or Title attributes
  * x:Key
  * x:Name
  * Title
* Grid or Canvas related attached layout attributes
* Numeric layout attributes
  * Width/MinWidth/MaxWidth
  * Height/MinHeight/MaxHeight
  * Margin
* Alignment related attributes
  * HorizontalAlignment/ContentHorizontalAlignment
  * VerticalAlignment/ContentVerticalAlignment
  * Panel.ZIndex
* Other attributes

所以上面的XAML Code整理完會變成像下圖這樣，是不是好閱讀許多呢？雖然依舊無法解決屬性事件穿插設定，但是已經某種程度將Attribute分類整理了。其它像是不必要的End Element或是雜亂的註解，Xaml Styler也能幫我們順便整理一下。

![image_thumb_3.png](/images/posts/128a214c-f1f2-47e3-b1a3-d97373c05868/image_thumb_3.png)

Xaml Styler在Options中也有提供設定頁面，若要細部微調，像是要將某些Attribute加進整理、是否要存檔自動就整理、是否要合併不必要的End Element...等，這些都可在這邊做些調整。

![image_thumb_6.png](/images/posts/128a214c-f1f2-47e3-b1a3-d97373c05868/image_thumb_6.png)

若有需要將設定保存，Xaml Styler也支援設定的匯出與匯入。

![image_thumb_4.png](/images/posts/128a214c-f1f2-47e3-b1a3-d97373c05868/image_thumb_4.png)

## Link

* Xaml Markup Styler Visual Studio 2012 Extension
* Xaml Styler
