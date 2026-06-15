---
title: "[Software]設定Chrome瀏覽器的暫存目錄到虛擬磁碟機"
date: "2010-06-08 09:31:59"
description: "[Software]設定Chrome瀏覽器的暫存目錄到虛擬磁碟機"
tags: [Software]
---

預設Google Chrome瀏覽器的暫存目錄位置為

C:\Documents and Settings\[你的帳號]\Local Settings\Application Data\Chromium\User Data

若想把暫存為置移至別的位置，例如虛擬磁碟機，則可透過--user-data-dir這個參數來設定，像是：

C:\Users\[User Name]\AppData\Local\Google\Chrome\Application\chrome.exe --user-data-dir=[新的存放位置]

![image_thumb.png](/images/posts/15733/image_thumb.png)

這樣設定後下次執行就會把資料暫存到所指定的位置，不過設定檔仍會存在本來的地方，因此我們還需複製設定檔至新的位置，像是：

XCopy C:\Documents and Settings\[User Name]\Local Settings\Application Data\Chromium\User Data\Default [新的暫存位置]\Default

這邊我們可以在[開始]→[執行]，鍵入gpedit.msc帶出本機群組編輯器。

![image_thumb_1.png](/images/posts/15733/image_thumb_1.png)

在[電腦設定]→[Windows設定][指令碼 - (啟動/關機)]上點選兩下，分別設定[啟動]與[關機]所要執行的命令。

![image_thumb_2.png](/images/posts/15733/image_thumb_2.png)

這邊我把命令都指到C:\Program Files裡面的批次檔

![image_thumb_3.png](/images/posts/15733/image_thumb_3.png)

![image_thumb_4.png](/images/posts/15733/image_thumb_4.png)

下面為執行的批次檔內容，Start.Bat主要的動作是把本來的設定檔給複製至新設定的位置

```xml
@echo off
xcopy /y "C:\Users\[User Name]\AppData\Local\Google\Chrome\User Data\Default" z:\TEMP\Default
```

Close.Bat則是把新位置的設定檔回存至本來的位置

```xml
@echo off
xcopy /y z:\TEMP\Default "C:\Users\[User Name]\AppData\Local\Google\Chrome\User Data\Default"
```

這樣設定後在切換休眠狀態時就能正常運作，但若電腦要關機的，可能還需要在啟動的地方執行才行。
