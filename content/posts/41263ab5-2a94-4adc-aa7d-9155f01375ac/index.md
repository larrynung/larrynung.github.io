---
title: "[Visual Studio]透過Visual Studio 2012的選擇性貼上將XML與JSON直接轉成對應的類別"
date: "2013-11-06 12:00:00"
description: "[Visual Studio]透過Visual Studio 2012的選擇性貼上將XML與JSON直接轉成對應的類別"
---

在開發專案時若碰到要串接服務或是他人的API，常常避免不了都要面對XML或是JSON這兩種Data Format。以.NET的開發者來說XML這邊可以直接用Linq to XML或是XPath處理掉，JSON也可以透過JSON.NET避開產生對應的類別後去解序列化。但是難免總是會有些狀況我們不得不面對這樣的問題，這時若是是JSON的Format很多開發者可能就會使用json2csharp去輔助產生對應的類別。

不過其實我們可以不需要額外的網站輔助，也不需要勞心勞力的手動去建立。因為在Visual Studio 2012中新增了選擇性貼上的功能，能將剪貼簿中的XML內容直接貼成對應的類別。

像是以土豆為例，我們呼叫API：

http://api.tudou.com/v3/gw?method=album.channel.get&appKey=myKey&format=xml&channel=z&pageNo=1&pageSize=10

取得的XML會長的像下面這樣：

![image_thumb.png](/images/posts/41263ab5-2a94-4adc-aa7d-9155f01375ac/image_thumb.png)

這時我們就可以在Visual Studio 2012中新增個類別檔案去存放對應的類別。

![image_thumb_1.png](/images/posts/41263ab5-2a94-4adc-aa7d-9155f01375ac/image_thumb_1.png)

按下[Edit/Paste Special]選單內的[Paste XML As Classes]選單選項。

![image_thumb_2.png](/images/posts/41263ab5-2a94-4adc-aa7d-9155f01375ac/image_thumb_2.png)

剪貼簿內的XML內容就會被貼成對應的類別，像是下圖這樣：

![image_thumb_3.png](/images/posts/41263ab5-2a94-4adc-aa7d-9155f01375ac/image_thumb_3.png)

如果API吐回的格式是JSON格式的話就比較麻煩一點，因為Visual Studio 2012尚未將這塊內建，不過你可以加裝ASP.NET and Web Tools。

![image_thumb_4.png](/images/posts/41263ab5-2a94-4adc-aa7d-9155f01375ac/image_thumb_4.png)

加裝ASP.NET and Web Tools後，我們再次看一下[Edit/Paste Special]下的選單選項，可以看到除了本來的[Paste XML As Classes]選單選項外，又多了一個[Paste JSON As Classes]的選單選項。

![image_thumb_11.png](/images/posts/41263ab5-2a94-4adc-aa7d-9155f01375ac/image_thumb_11.png)

這邊一樣用土豆為例，呼叫跟上面相同的API，但是將資料格式改為JSON。

http://api.tudou.com/v3/gw?method=album.channel.get&appKey=myKey&format=json&channel=z&pageNo=1&pageSize=10

按下[Edit/Paste Special]選單內的[Paste JSON As Classes]選單選項，可以看到如預期的Visual Studio 2012幫我們產生了對應的類別。

![image_thumb_12.png](/images/posts/41263ab5-2a94-4adc-aa7d-9155f01375ac/image_thumb_12.png)

這樣貼心的小功能是不是很方便呢？我們不在需要類似json2csharp這樣的網站輔助開發，串接API時也只要取得API的回傳值後用產生的類別解序列化，資料就可以直接透過物件下去存取。

這邊最後一提，Web Essentials 2012也有類似的功能能輔助我們將JSON的資料轉成對應的類別，有興趣的可參閱Will保哥的影片介紹：

![video25923ff2a9df.jpg](/images/posts/41263ab5-2a94-4adc-aa7d-9155f01375ac/video25923ff2a9df.jpg)

## Link

* 活用 VS2012 擴充套件 - 將 JSON 轉換成 .NET 類別 (Web Essentials 2012)
* ASP.NET and Web Tools 2012.2
* TIP: “Paste XML as Classes” in Visual Studio 2012
* Generating Data Type Classes from XML
* VS 11 : Paste XML as Classes!
* Visual Studio 2012 – Paste XML as Classes
* ‘Paste JSON As Classes’ in ASP.NET and Web Tools 2012.2 RC
