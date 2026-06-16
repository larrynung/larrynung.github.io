---
title: "土豆視頻開發系列-開發前準備"
date: "2013-11-06 12:00:00"
tags: [土豆視頻]
description: "土豆網為了讓開發人員能夠開發相關的應用程式，開放了API給開發人員叫用，開發人員可從土豆視頻開發平台取得完整的開發資訊。土豆網API是採HTTP API的形式，取得的資料會以json或是xml兩種型態返回。"
---

土豆網為了讓開發人員能夠開發相關的應用程式，開放了API給開發人員叫用，開發人員可從土豆視頻開發平台取得完整的開發資訊。土豆網API是採HTTP API的形式，取得的資料會以json或是xml兩種型態返回。API在使用上又可分為需要認證的API與不需認證的API兩種，需要認證的API在使用上需帶入App Key與App Secret，而不需認證的API只需帶入App Key，因此我們在開發之前必須先取得開發所需的App Key與App Secret。

要取得開發所需的App Key與App Secret，我們必須擁有土豆網的帳號，以土豆網的帳號登入土豆視頻開發平台，接著在土豆視頻開發平台中創建應用程式，就可以取得開發所需的App Key與App Secret了。

![image_thumb_7.png](/images/posts/3aa8a1e9-7a6e-464c-8ccf-5e19a566fd59/image_thumb_7.png)

這邊詳細的示範一遍，透過土豆網右上角的註冊聯結我們可以進入土豆的註冊頁面，註冊時只需帶入電子郵件、密碼、與暱稱這幾個簡單的資料。

![image_thumb_1.png](/images/posts/3aa8a1e9-7a6e-464c-8ccf-5e19a566fd59/image_thumb_1.png)

註冊完後會有個啟用信件寄送到註冊時填入的EMail，啟用後回到土豆網視頻開發平台，透過右上角的登入聯結進入登入畫面，登入後切換到[我的應用]頁面，點選[創建應用]聯結進入應用程式建立頁面。

![image_thumb_2.png](/images/posts/3aa8a1e9-7a6e-464c-8ccf-5e19a566fd59/image_thumb_2.png)

填入應用程式的名稱、描述、網址、與Logo。

![image_thumb_3.png](/images/posts/3aa8a1e9-7a6e-464c-8ccf-5e19a566fd59/image_thumb_3.png)

建立完成後可由應用控制面板中看到剛剛所建立的應用程式。

![image_thumb_4.png](/images/posts/3aa8a1e9-7a6e-464c-8ccf-5e19a566fd59/image_thumb_4.png)

點選進去後可以在右側看到該應用程式的App Key與App Secret。

![image_thumb_5.png](/images/posts/3aa8a1e9-7a6e-464c-8ccf-5e19a566fd59/image_thumb_5.png)

到此開發前準備就已完成，不過有一點仍需特別注意，土豆網API的叫用有些限制，像是每分鐘限制只能呼叫幾次API等，我們可以切換到應用程式的統計概覽頁面去瀏覽相關的限制，也可以查看到目前API的叫用量。

![image_thumb_6.png](/images/posts/3aa8a1e9-7a6e-464c-8ccf-5e19a566fd59/image_thumb_6.png)

## Link

* [土豆視頻開發平台](http://api.tudou.com/apps/main.php)
* [新手指南](http://api.tudou.com/wiki/index.php/%E6%96%B0%E6%89%8B%E6%8C%87%E5%8D%97)
