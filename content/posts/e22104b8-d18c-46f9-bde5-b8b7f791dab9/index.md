---
title: "Google App Engine 1.8.2 New Feature - Push-to-Deploy"
date: "2013-11-06 12:00:00"
description: "Google App Engine 1.8.2 New Feature - Push-to-Deploy"
---

Google App Engine 1.8.2開始支援Git，允許透過Git Push的方式來做佈署的動作。這邊簡單的紀錄一下。

首先進到Application的Dashboard，在頁面的左側找到Application Settings的連結後用滑鼠點擊。

![image_thumb.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb.png)

在右側這邊找到Source Push-to-Deploy的設定區，點擊[Enable Push-to-Deploy...]按鈕。

![image_thumb_1.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_1.png)

點擊後Source Push-to-Deploy設定區會變成像下面這樣：

![image_thumb_2.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_2.png)

可以看到裡面會有個get your auth token連結，可以用來取得我們佈署所需要的認證碼。另外裡面還有一串網址，表示對應的repository位置，後面在用Git Push佈署時才知道是要Push到哪邊。

接者用滑鼠點擊get your auth token連結。

![image_thumb_3.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_3.png)

點擊後會要求授權，這邊直接按下[接受]按鈕繼續。

![image_thumb_4.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_4.png)

授權接受後會給予一串認證碼，將這認證碼選取複製。

![image_thumb_5.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_5.png)

開啟檔案總管將之切至%USERPROFILE%下，建立一個名為_netrc的檔案，檔案的內容需要遵循下面格式：

```xml
machine code.google.com login <email-address> password <auth-token>
```

其中<email-address>就是您的gmail帳號，<auth-token>就是上面我們所複製的認證碼。所以檔案內容會像下面這樣：

![image_thumb_8.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_8.png)

再來我們必須要設定HOME環境變數，可以在命令提示字元中呼叫命令"setx HOME %USERPROFILE%"。

![image_thumb_6.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_6.png)

或是直接在環境變數對話框中設定也可以。

![image_thumb_9.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_9.png)

都準備完成後我們可以實際的用Git佈署看看，呼叫命令"git remote add appengine `<repo-url>`" (這邊的`<repo-url>`指的就是上面我們按下[Enable Push-to-Deploy...]按鈕後所顯示出來的repo URL)將遠端的repository加入。

![image_thumb_12.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_12.png)

再呼叫命令"git push appengine master"就可以將程式佈署上去...

![image_thumb_11.png](/images/posts/e22104b8-d18c-46f9-bde5-b8b7f791dab9/image_thumb_11.png)

## Link

* Google App Engine 1.8.2 released
* Using Git and Push-to-Deploy
