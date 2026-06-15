---
title: "[HTML]HTML5 New Feature - x-webkit-speech"
date: "2013-11-06 12:00:00"
description: "[HTML]HTML5 New Feature - x-webkit-speech"
---

HTML5的Input tag新提供x-webkit-speech語法，目前只能在Chrome 11以後的瀏覽器上使用，能讓我們將語音輸入的功能很簡單的帶到我們的網站中。最簡易的運用方式是像下面這樣將x-webkit-speech加在input tag後方就可以了。

運行起來後我們可以在輸入框後方看到麥克風的圖示。

![image_thumb.png](/images/posts/4c7c9536-cf32-4c67-b33c-911f15226dff/image_thumb.png)

點選麥克風的圖示即可啟動語音輸入功能。

![image_thumb_1.png](/images/posts/4c7c9536-cf32-4c67-b33c-911f15226dff/image_thumb_1.png)

![image_thumb_2.png](/images/posts/4c7c9536-cf32-4c67-b33c-911f15226dff/image_thumb_2.png)

若有需要這邊我們可以再進一步透過lang指定語音輸入所要使用的語系，像是帶入lang= "zh-CN"的話，語音輸入所識別出來的文字就會變成簡體字。

![image_thumb_5.png](/images/posts/4c7c9536-cf32-4c67-b33c-911f15226dff/image_thumb_5.png)

此外我們也可以透過onwebkitspeechchange去為語音輸入時加些對應的動作。

![image_thumb_4.png](/images/posts/4c7c9536-cf32-4c67-b33c-911f15226dff/image_thumb_4.png)

x-webkit-speech使用上就是那麼簡單，但是最後這邊還是要再提一下，x-webkit-speech語法並不是所有瀏覽器都可以支援的，因此我們在使用上必須針對與法是否支援做些檢查，有需要的話檢查的動作可參閱下面的簡易範例。

![image_thumb_3.png](/images/posts/4c7c9536-cf32-4c67-b33c-911f15226dff/image_thumb_3.png)

若有在用點部落的，我們也可以用這個語法來加強點部落的搜尋功能，只要在網站管理頁面的Custom HTML/Script區域將textSearch的element啟用webkitSpeech功能就可以了。

![image_thumb_6.png](/images/posts/4c7c9536-cf32-4c67-b33c-911f15226dff/image_thumb_6.png)

是不是很簡單呢？

![image_thumb_7.png](/images/posts/4c7c9536-cf32-4c67-b33c-911f15226dff/image_thumb_7.png)

## Link

* x-webkit-speech 語音輸入功能
* Google語音識別||x-webkit-speech–HTML5實現聲音錄製功能的方法
* How to Use HTML5 Speech Input Fields
* x-webkit-speech input and textareas
* Collect Speech Input with HTML5 on Google Chrome
