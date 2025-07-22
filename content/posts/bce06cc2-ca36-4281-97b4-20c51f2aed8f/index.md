---
title: "How to use goagent GAE proxy"
date: "2013-11-06 12:00:00"
description: "How to use goagent GAE proxy"
---

goagent是一基於GAE的proxy服務，當網路被封鎖時我們可透過goagent繞道突破。

  使用前請先至GoAgent - Google Code下載goagent的主程式。     

下載完解壓縮會看到像下面這樣的內容。

goagent是基於GAE的解決方案，所以使用時需做些設定與佈署。所以我們要先切至server目錄 (裡面存放的就是很一般的GAE Application)，找到並開啟app.yaml。

修改app.yaml的內容，將application設為我們的GAE Application ID，存檔後離開。

然後用滑鼠雙點擊呼叫uploader.bat。

雙點擊完會出現像下面這樣的畫面，會詢問帳號密碼，輸入完帳號密碼後會開始進行佈署的動作。

佈署完成切換至local目錄，找到並開啟proxy.ini。

修改gae區塊中的appid值，一樣將其值設為我們的GAE Application ID，存檔後離開。

接著用管理者權限開啟local目錄下的goagent.exe。

goagent會開始常駐...

同時帶出像下面這樣的主控台畫面，上面會顯示一些資訊，像是proxy的位置為127.0.0.1:8087。

goagent的Proxy啟動完畢，我們要開始調整網路的Proxy設定 。開啟網際網路選項對話框，切換至連線頁面，按下[LAN設定]按鈕。

在區域網路(LAN)設定對話框中設定Proxy位置為127.0.0.1，連接埠設為8087。

網路的Proxy設定完後，開啟瀏覽器看一下IP資訊，可以看到這邊筆者的網路位置已經被導到美國去了，代表我們已經成功地透過goagent繞道瀏覽網頁。

最後一提，透過goagent繞道瀏覽，瀏覽的細部資訊我們都可以透過goagent啟動時彈出的主控台畫面查看。

## Link
     GoAgent - Google Code    GoAgent教學——穩定、快速、免費、跨平台的的翻牆方式    中國大陸翻牆教學 GoAgent+GAE，可連 YouTube、Facebook…等\    GoAgent - 维基百科，自由的百科全书 - 维基百科- Wikipedia