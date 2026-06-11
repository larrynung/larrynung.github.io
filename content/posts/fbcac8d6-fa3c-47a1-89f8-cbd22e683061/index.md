---
title: "MetaWeblog Backupper V1.0 alpha"
date: "2013-11-06 12:00:00"
description: "MetaWeblog Backupper V1.0 alpha"
---

筆者最近抽空寫了一支簡單的備份程式，可以將網誌資料備份下來，因為預期是要能支援所有MetaWeblog API的Blog，所以姑且就稱這隻小程式為MetaWeblog Backupper。

目前這隻小程式還在開發階段，因為先讓prototype出來，所以程式目前還是寫的很髒，預期想做的功能也沒完全達成，效能也尚未最佳化處理，但初步的功能已經Work了，能正常的備份網站內容與圖片，所以這邊就先行釋出一版alpha版(這樣筆者才能改去玩些別的東西XD)，有需要的自行取用。

使用方式很簡單，選取要備份到的目錄位置後按下下方的Backup按鈕。

如果未做登入，程式會跳出對話框詢問登入所需要的ID與Password。

輸入完成程式就會開始進行備份的動作，因為這版還是alpha，而且MetaWeblog API有些設計上的缺陷，所以這邊請耐心等待。

備份完成程式會跳出對話框告知。

此時我們可以看到網誌的資訊都被備份到指定的目錄。

若有需要查閱備份的網誌內容可以直接開啟裡面產生的網頁...

## Download


MetaWeblogBackupper.zip