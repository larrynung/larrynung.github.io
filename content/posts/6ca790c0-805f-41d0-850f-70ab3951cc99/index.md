---
title: "[.NET Resource][Visual Studio]讓開發效能大幅提升的Visual Studio Extension - AutoCode"
date: "2013-11-06 12:00:00"
description: "[.NET Resource][Visual Studio]讓開發效能大幅提升的Visual Studio Extension - AutoCode"
---

AutoCode是一套能讓開發人員開發效能大幅提升的Visual Studio Extension，它內建有100個以上的命令，能夠簡單快速的幫我們產生程式碼，就像官方網站給的動畫範例一樣，熟悉這套Extension後開發就是那麼的方便快速。

![autocodedemo.gif](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/autocodedemo.gif)

AutoCode目前可以抓到的最新版本為AutoCode 4，已經能支援到Visual Studio 2011 beta了。

![image3_thumb.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image3_thumb.png)

這個Extension有標準版與專業版兩種版本，標準版是免費的，功能會比專業版少一點，但是相信已經相當夠用了。像是專業版裡面最吸引人的就是它提供了能自己撰寫並修改命令的功能，進階的玩家可以自行整理自己的命令庫，讓開發速度更為提升，但這樣的功能其實標準版也可以做到，只是沒有提供輔助的工具，必須要自行撰寫放到特定的目錄。

![image_thumb.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb.png)

AutoCode安裝後在使用時最重要的就是Ctrl + Enter的熱鍵，在沒有選取的狀態下按下該熱鍵，AutoCode會顯現一個對話框讓使用者輸入命令，下方會有命令的提示、說明、與使用方式。

![image_thumb_3.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_3.png)

另外熟悉命令後我們也可以直接在IDE編輯區中先輸入命令，然後再按下熱鍵。

![image_thumb_4.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_4.png)

完成後在編輯區中就會幫我們產生對應的程式碼，以上面的例子來說，我想要產生一個Person類別裡面有名字、暱稱、年齡這些屬性，我就可以用"string Mame string NickName int Age Person Class"這樣的命令下去產生，產生出來的程式碼就會像下面這樣：

![image_thumb_5.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_5.png)

產生了Person這個類別後，若是我們發現少加入了一些成員屬性，我們可以按下熱鍵驅動AutoCode，鍵入"<PropertyType> <PropertyName> p"，然後按下Enter。

![image_thumb_12.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_12.png)

AutoCode就會幫我們自動產生對應的程式。

![image_thumb_13.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_13.png)

接著如果我們想要針對某些程式碼去做群組，我們可以將程式碼選取起來，按下熱鍵驅動AutoCode，然後鍵入"<群組名稱> r"後按下Enter。

![image_thumb_6.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_6.png)

選取的程式碼就會以指定的名稱群組起來。

![image_thumb_7.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_7.png)

若只有一個Method想要群組，也可以不選取，直接在該Method中按熱鍵驅動AutoCode，鍵入r後按下Enter。

![image_thumb_8.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_8.png)

該Method就會被群組起來，並預設帶入Method Name為群組名稱。

![image_thumb_9.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_9.png)

除了產生程式碼外，AutoCode也可以幫我們做些其它的動作，像是我們產生了群組後想要立即將群組折疊，我們可以按熱鍵驅動後輸入rd，然後按下Enter。

![image_thumb_10.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_10.png)

群組就會被我們摺疊起來。

![image_thumb_11.png](/images/posts/6ca790c0-805f-41d0-850f-70ab3951cc99/image_thumb_11.png)

這邊只是簡單的介紹，AutoCode的強大很難一次說清，100+命令也不能一一帶過，有興趣的自己抓下來玩玩吧。

## Link

* [devProjects.net](http://www.devprojects.net/)
* [.net AutoCode v4.0](http://visualstudiogallery.msdn.microsoft.com/48eeb43f-cb46-4680-b7df-11e73cf894ca)
* [Visual Studio自動生成代碼插件AutoCode的使用](http://junnan.org/blog/71)
* [AutoCode (Visual Studio 插件)](http://izbl.blog.163.com/blog/static/182865333201212005850853/)
* [人生苦短，我用autocode](http://shui.us/blog/2011/05/19/%E4%BA%BA%E7%94%9F%E8%8B%A6%E7%9F%AD%EF%BC%8C%E6%88%91%E7%94%A8autocode/)
