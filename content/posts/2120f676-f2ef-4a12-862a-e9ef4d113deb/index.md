---
title: "DropBox開發系列 - App Key與App Secret的申請"
date: "2013-11-06 12:00:00"
description: "DropBox開發系列 - App Key與App Secret的申請"
---

要開發可以存取DropBox的應用程式，跟一般的SNS開發一樣，必須在Dropbox for Developers網站上建立應用程式並取得開發所需的App Key跟App Secret，再將取得的App Key跟App Secret帶到程式中，就可以對DropBox進行我們想要做的操作。  
 
  申請的步驟很簡單，首先連到Dropbox for Developers網站，網站左側可以看到My apps的連結，點擊後右側可以看到Create an App按鈕，點擊下去開始進行應用程式的創建。     

創建應用程式時會需要輸入應用程式的名稱、描述、與層級，應用程式名稱與描述應該都沒什麼問題，填入你想要創建的應用程式叫什麼並對他做些描述就可以了。至於層級的部份DropBox提供了App folder與Full Dropbox兩種選擇，App folder是只能存取app的目錄，而Full DropBox是能存取整個DropBox，這邊如沒特殊需求的話，建議是選取App folder，畢竟要求的權限比較少會比較安全一些。都輸入完後按下Create按鈕完成應用程式的創建。

應用程式創建完成後會進入應用程式的細部設定頁面，這邊可以設定像是應用程式名稱、應用程式的目錄、及一些其它的資訊，最重要的是這頁會顯示該應用程式的App Key與App Secret，這兩個就是我們在後續開發程式會用到的兩把Key。

## Link
     Dropbox for Developers