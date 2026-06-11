---
title: "Google App Engine 1.8.2 New Feature - Push-to-Deploy"
date: "2013-11-06 12:00:00"
description: "Google App Engine 1.8.2 New Feature - Push-to-Deploy"
---

Google App Engine 1.8.2開始支援Git，允許透過Git Push的方式來做佈署的動作。這邊簡單的紀錄一下。

首先進到Application的Dashboard，在頁面的左側找到Application Settings的連結後用滑鼠點擊。

在右側這邊找到Source Push-to-Deploy的設定區，點擊[Enable Push-to-Deploy...]按鈕。

點擊後Source Push-to-Deploy設定區會變成像下面這樣：

可以看到裡面會有個get your auth token連結，可以用來取得我們佈署所需要的認證碼。另外裡面還有一串網址，表示對應的repository位置，後面在用Git Push佈署時才知道是要Push到哪邊。

接者用滑鼠點擊get your auth token連結。

點擊後會要求授權，這邊直接按下[接受]按鈕繼續。

授權接受後會給予一串認證碼，將這認證碼選取複製。

開啟檔案總管將之切至%USERPROFILE%下，建立一個名為_netrc的檔案，檔案的內容需要遵循下面格式：

machine code.google.com login password

其中就是您的gmail帳號，就是上面我們所複製的認證碼。所以檔案內容會像下面這樣：

再來我們必須要設定HOME環境變數，可以在命令提示字元中呼叫命令"setx HOME %USERPROFILE%"。

或是直接在環境變數對話框中設定也可以。

都準備完成後我們可以實際的用Git佈署看看，呼叫命令"git remote add appengine " (這邊的指的就是上面我們按下[Enable Push-to-Deploy...]按鈕後所顯示出來的repo URL)將遠端的repository加入。

再呼叫命令"git push appengine master"就可以將程式佈署上去...

## Link


Google App Engine 1.8.2 released

Using Git and Push-to-Deploy