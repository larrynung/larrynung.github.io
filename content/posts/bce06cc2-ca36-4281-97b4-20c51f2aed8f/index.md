---
title: "How to use goagent GAE proxy"
date: "2013-11-06 12:00:00"
description: "goagent是一基於GAE的proxy服務，當網路被封鎖時我們可透過goagent繞道突破。 使用前請先至GoAgent - Google Code下載goagent的主程式。 下載完解壓縮會看到像下面這樣的內容。 goagent是基於GAE的解決方案，所以使用時需做些設定與佈署。"
---

goagent是一基於GAE的proxy服務，當網路被封鎖時我們可透過goagent繞道突破。

使用前請先至GoAgent - Google Code下載goagent的主程式。

![image_thumb.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb.png)

下載完解壓縮會看到像下面這樣的內容。

![image_thumb_1.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_1.png)

goagent是基於GAE的解決方案，所以使用時需做些設定與佈署。所以我們要先切至server目錄 (裡面存放的就是很一般的GAE Application)，找到並開啟app.yaml。

![image_thumb_4.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_4.png)

修改app.yaml的內容，將application設為我們的GAE Application ID，存檔後離開。

![image_thumb_5.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_5.png)

然後用滑鼠雙點擊呼叫uploader.bat。

![image_thumb_6.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_6.png)

雙點擊完會出現像下面這樣的畫面，會詢問帳號密碼，輸入完帳號密碼後會開始進行佈署的動作。

![image_thumb_7.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_7.png)

![image_thumb_9.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_9.png)

佈署完成切換至local目錄，找到並開啟proxy.ini。

![image_thumb_2.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_2.png)

修改gae區塊中的appid值，一樣將其值設為我們的GAE Application ID，存檔後離開。

![image_thumb_3.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_3.png)

接著用管理者權限開啟local目錄下的goagent.exe。

![image_thumb_10.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_10.png)

goagent會開始常駐...

![image_thumb_11.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_11.png)

同時帶出像下面這樣的主控台畫面，上面會顯示一些資訊，像是proxy的位置為127.0.0.1:8087。

![image_thumb_12.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_12.png)

goagent的Proxy啟動完畢，我們要開始調整網路的Proxy設定 。開啟網際網路選項對話框，切換至連線頁面，按下[LAN設定]按鈕。

![image_thumb_13.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_13.png)

在區域網路(LAN)設定對話框中設定Proxy位置為127.0.0.1，連接埠設為8087。

![image_thumb_14.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_14.png)

網路的Proxy設定完後，開啟瀏覽器看一下IP資訊，可以看到這邊筆者的網路位置已經被導到美國去了，代表我們已經成功地透過goagent繞道瀏覽網頁。

![image_thumb_15.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_15.png)

最後一提，透過goagent繞道瀏覽，瀏覽的細部資訊我們都可以透過goagent啟動時彈出的主控台畫面查看。

![image_thumb_16.png](/images/posts/bce06cc2-ca36-4281-97b4-20c51f2aed8f/image_thumb_16.png)

## Link

* [GoAgent - Google Code](https://code.google.com/p/goagent/)
* [GoAgent教學——穩定、快速、免費、跨平台的的翻牆方式](http://fyu45.pixnet.net/blog/post/91348886-goagent%E6%95%99%E5%AD%B8%E2%80%94%E2%80%94%E7%A9%A9%E5%AE%9A%E3%80%81%E5%BF%AB%E9%80%9F%E3%80%81%E5%85%8D%E8%B2%BB%E3%80%81%E8%B7%A8%E5%B9%B3%E5%8F%B0%E7%9A%84)
* [中國大陸翻牆教學 GoAgent+GAE，可連 YouTube、Facebook…等](http://www.soft4fun.net/software/internet/%E7%BF%BB%E7%89%86%E8%A8%AD%E5%AE%9A%E6%95%99%E5%AD%B8-goagent.htm)\
* [GoAgent - 维基百科，自由的百科全书 - 维基百科- Wikipedia](http://zh.wikipedia.org/zh-tw/GoAgent)
