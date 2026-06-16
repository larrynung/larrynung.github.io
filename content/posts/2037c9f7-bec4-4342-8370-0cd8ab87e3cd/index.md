---
title: "[Software][.NET Resource]Quickly Generate Multilingual Resource Files with XHEO RESX Translator"
slug: "software-dotnet-resource-quickly-generate-multilingual-resource-files-with-xheo-resx-translator"
aliases: ["/posts/2037c9f7-bec4-4342-8370-0cd8ab87e3cd/"]
date: "2013-11-06 12:00:00"
tags: [.NET Resource, Software]
description: "之前筆者介紹過Zeta Resource Editor這個資源檔編輯工具，它能夠透過翻譯產生特定語系的資源檔，但是新的版本它的翻譯服務改成雲端的服務，變得必須要有雲端服務的應用程式ID，整個翻譯功能就變得不好用了，甚至要付費給雲端服務。"
---

之前筆者介紹過Zeta Resource Editor這個資源檔編輯工具，它能夠透過翻譯產生特定語系的資源檔，但是新的版本它的翻譯服務改成雲端的服務，變得必須要有雲端服務的應用程式ID，整個翻譯功能就變得不好用了，甚至要付費給雲端服務。經過一番搜尋，筆者又發現了XHEO RESX Translator這套工具，可以達到類似的效果，這篇將其稍微做個整理。

XHEO RESX Translator是一套能透過Bing服務快速翻譯各國語系資源檔的工具，自RESX Automatic Translator下載後開啟，可看到像下面這樣的程式介面。

![image_thumb.png](/images/posts/2037c9f7-bec4-4342-8370-0cd8ab87e3cd/image_thumb.png)

使用前必須要有Bing的App ID，若不知道怎麼申請的可參閱筆者[[C#]使用Microsoft Translator Soap API實作翻譯功能](http://www.dotblogs.com.tw/larrynung/archive/2012/01/15/65819.aspx)這篇。帶入完Bing App ID後按下Next按鈕，我們可以指定要翻譯的資源檔，並指定該資源檔是什麼語系的資源檔，以及我們要由它產生出哪個語系的資源檔，這邊筆者是示範從英文的資源檔產生出繁體中文的資源檔，設定完後一樣按下Next按鈕。

![image_thumb_1.png](/images/posts/2037c9f7-bec4-4342-8370-0cd8ab87e3cd/image_thumb_1.png)

理想狀態下Resx Translator會開始進行翻譯的動作。

![image_thumb_2.png](/images/posts/2037c9f7-bec4-4342-8370-0cd8ab87e3cd/image_thumb_2.png)

Resx Translator翻譯完成會帶出下面畫面，詢問要將翻譯完成的資源檔儲存於何處，這邊可以直接套用預設的設定，直接按下Save按鈕繼續，翻譯完成的資源檔就會儲存於指定的位置。

![image_thumb_3.png](/images/posts/2037c9f7-bec4-4342-8370-0cd8ab87e3cd/image_thumb_3.png)

這邊筆者用前面介紹的Zeta Resource Editor來比較要翻譯的資源檔與翻譯完成的資源檔，直接比對來看，基本上大致翻譯還算不錯，但還是要稍微做些修正才能使用。

![image_thumb_4.png](/images/posts/2037c9f7-bec4-4342-8370-0cd8ab87e3cd/image_thumb_4.png)

## Link

* [RESX Automatic Translator](http://xheo.com/knowledge-base/deploylx/resx-automatic-translator)
* [How-to: Customize or Translate Form Text](http://xheo.com/knowledge-base/deploylx/licensing/how-to-customize-or-translate-form-text)
* [How to Create a Custom Translation](http://xheo.com/docs/dlxl/5/html/developers%20guide/advanced%20licensing/how%20to%20create%20a%20custom%20translation.html)
