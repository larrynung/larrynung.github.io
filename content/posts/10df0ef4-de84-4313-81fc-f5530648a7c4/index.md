---
title: "[Visual Studio]Introduce Visual Studio Achievements"
date: "2013-11-06 12:00:00"
description: "Visual Studio Achievements是Visual Studio的成就系統外掛，能外掛在Visual Studio上，有點類似於一般遊戲的成就系統，當達到特定的目標會頒給勳章以資獎勵，可以讓寫程式變得像是玩遊戲一般輕鬆，"
---

Visual Studio Achievements是Visual Studio的成就系統外掛，能外掛在Visual Studio上，有點類似於一般遊戲的成就系統，當達到特定的目標會頒給勳章以資獎勵，可以讓寫程式變得像是玩遊戲一般輕鬆，也能逐步帶領使用者熟悉整個Visual Studio的使用與較好的Coding方式。

目前具有六大類不同的勳章，每類勳章都有不同的意義，像是Don't Try This At Home這類的勳章就是代表不是很好的寫作習慣，可以自己設定找些勳章當自己的里程碑，像是UML God勳章等，都是不錯的目標。

![image_thumb_1.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image_thumb_1.png)

Visual Studio Achievement目前只支援Visual Studio 2010，可直接透過Extension Manager安裝。

![image_thumb.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image_thumb.png)

安裝完後系統會提示您重開Visual Studio，重開後會跳出提示視窗請求登入Channel9，整個Visual Studio Achievements的運作必須透過Channel9的帳號，可直接點選Sing In連結進行登入。

![image3_thumb.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image3_thumb.png)

點選完Sing In連結，頁面會帶到Sing in to Channel 9，這邊筆者有點搞不懂得是，這邊找不到任何的註冊選項，所以筆者透過右上角的Sing In連結下去登入。

![image9_thumb.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image9_thumb.png)

此時Sing In畫面會變得像下面這樣，這畫面就比較熟悉了，一般Windows Live的服務都是透過這個畫面將服務與Windows Live ID綁再一起，這邊用自己的Windows Live ID與密碼登入就可以了。

![image6_thumb.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image6_thumb.png)

接著會被導到下面這個頁面建立Channel9的Profile，注意右上角，此時也已完成了登入的動作。

![image12_thumb.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image12_thumb.png)

完成後，我們可以透過Tools→Achievements將安裝好的Visual Studio Achievements叫起。

![image15_thumb.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image15_thumb.png)

點選左邊的按鈕啟用。

![image18_thumb.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image18_thumb.png)

你會在Visual Studio右下角中看到下圖的畫面，兩個勳章到手，後續完成任務得到勳章就會像這樣顯示。

![image21_thumb.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image21_thumb.png)

若再照上面的步驟，透過Tools→Achievements將安裝好的Visual Studio Achievements叫起，會發現Visual Studio Achievements畫面已經變成了勳章的列表，可以透過這個畫面查閱所有的勳章、得到的勳章、與尚未取得的勳章。

![image26_thumb.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image26_thumb.png)

類似的資訊也可以透過網址查閱 ，把自己的UserName帶入下列網只去瀏覽就可以了。

```xml
http://channel9.msdn.com/niners/[UserName]/achievements/visualstudio
```

![image_thumb_11.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image_thumb_11.png)

這邊可直接點選勳章圖示，Visual Studio會帶出對應勳章的詳細資料，像是說明、完成時間、與分數。

![image_thumb_12.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image_thumb_12.png)

右上方還有分享按鈕可以直接透過FB或是tweet與朋友分享，美中不足的是不能自動分享。

![image_thumb_13.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image_thumb_13.png)

若要查閱依分數下去排名是多少可以至Visual Studio Achievements Leaderboard這邊查閱。

![image_thumb_10.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image_thumb_10.png)

Visual Studio Achievement也提供Widget讓使用者能輕易的將自己的成就資訊分享於網站，在網站原始碼中加入下面的Script，並替換自己的UserName。

```xml
<script src="\images\posts\10df0ef4-de84-4313-81fc-f5530648a7c4\VSachievements.min.js?user=[UserName]" id="ch9VSachievements"></script>
```

網站即會出現像下面這樣的Widget。

![image_thumb_15.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image_thumb_15.png)

![image_thumb_14.png](/images/posts/10df0ef4-de84-4313-81fc-f5530648a7c4/image_thumb_14.png)

## Link

* Visual Studio Achievements
* Visual Studio Achievements
* Visual Studio Achievements Leaderboard
* Announcing Visual Studio Achievements Beta
* Visual Studio Achievements Widget
