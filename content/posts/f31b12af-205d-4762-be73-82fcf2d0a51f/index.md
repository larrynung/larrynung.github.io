---
title: "Bitbuck~Free source code hosting"
date: "2013-11-06 12:00:00"
description: "Bitbuck是一類似GitHub的source code hosting服務，跟GitHub最大的不同是Bitbuck可以建立無限制的私有專案，而在GitHub中是免費使用者只能建立公有專案，要建置私有專案就必須要付費。"
---

Bitbuck是一類似[GitHub](https://github.com/)的source code hosting服務，跟[GitHub](https://github.com/)最大的不同是[Bitbuck](https://bitbucket.org/)可以建立無限制的私有專案，而在[GitHub](https://github.com/)中是免費使用者只能建立公有專案，要建置私有專案就必須要付費。[Bitbuck](https://bitbucket.org/)隨然允許建立私有專案，但也是有限制的，每個專案的成員數必需要小於五位，但對於一般個人使用來說應該是相當的夠用。另外就是網路上有人說速度上會比[GitHub稍微慢了一些，但這邊以筆者來說是感覺不太出來，最起碼筆者還能接受。](https://github.com/)

Bitbuck使用前需先在首頁Sign up。

![image_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image_thumb.png)

可以建立Bitbuck的帳號，或是直接以Facebook這些社群服務去連接。

![image3_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image3_thumb.png)

註冊登入後會進到Dashboard，可在這邊建立 Repository或是從現有的Repository匯入，因為筆者有用CodePlex，所以這邊從現有的Repository匯入下去示範 。

![image6_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image6_thumb.png)

因為筆者的CodePlex都是用git的，而Bitbuck的CodePlex source類型只支援Subversion或是Mercurial，在這source type並不支援git。

![image9_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image9_thumb.png)

所以這邊不要選CodePlex source，而是要選git source，並輸入CodePlex專案的git位置，Bitbuck會自動從CodePlex帶入下面的資訊，我們只要特別注意資料是正確帶入、調整一下Description(匯入時格式可能會跑掉)、以及決定這個Repository是要公開還是要私人存取，都設定完後按下下方的Import repository進行匯入的動作。

![image12_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image12_thumb.png)

進行匯入時，匯入的進度會在界面上清楚的呈現。

![image15_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image15_thumb.png)

匯入完後，專案的頁面就建立完成了。頁面說明、程式碼、分支、Commit紀錄，以及tag...等都正確的匯入。

![image18_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image18_thumb.png)

![image21_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image21_thumb.png)

![image24_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image24_thumb.png)

![image2_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image2_thumb.png)

![image5%5B1%5D_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image5%5B1%5D_thumb.png)

![image8%5B1%5D_thumb.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image8%5B1%5D_thumb.png)

這邊我們實際將Repository從Bitbuck clone下來看看，在[Bitbuck專案首頁我們可以看到右側有這個專案的git位置，有HTTPS或是SSH兩種可供選擇。](https://bitbucket.org/)

![image_thumb_1.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image_thumb_1.png)

筆者使用HTTPS下去示範，開啟Git Shell後呼叫命令"git clone [Repository Url]"。

![image_thumb_2.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image_thumb_2.png)

就可以將指定的Repository整個抓下來。

![image_thumb_3.png](/images/posts/f31b12af-205d-4762-be73-82fcf2d0a51f/image_thumb_3.png)

抓下來後，剩下的就是一般的git操作了，相信有玩過git的都不成問題，而且也非Bitbuck的範疇，故這邊就不多做說明。

## Link

* Free source code hosting for Git and Mercurial by Bitbucket
* 使用BitBucket來管理你的程式碼
* bitbucket和github的簡單比較
* Bitbucket 開始支援 Git Repository
