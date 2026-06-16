---
title: "[C#]使用NBug函式庫為程式加上錯誤回報機制"
slug: "csharp-使用nbug函式庫為程式加上錯誤回報機制"
aliases: ["/posts/csharp使用nbug函式庫為程式加上錯誤回報機制/"]
date: "2013-11-06 12:00:00"
description: "NBug是一開放源碼的函式庫，可輕鬆快速的為應用程式加上錯誤回報機制的，當錯誤發生時NBug能幫我們自動產生開發人員所需的錯誤報告，內含詳細的錯誤內容資訊與MiniDump File，錯誤報告會以壓縮檔的方式儲存在指定位置，沒指定的話通常是存放在當前目錄下。"
tags: [CSharp]
---

![image46_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image46_thumb.png)

NBug是一開放源碼的函式庫，可輕鬆快速的為應用程式加上錯誤回報機制的，當錯誤發生時NBug能幫我們自動產生開發人員所需的錯誤報告，內含詳細的錯誤內容資訊與MiniDump File，錯誤報告會以壓縮檔的方式儲存在指定位置，沒指定的話通常是存放在當前目錄下。

![image4_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image4_thumb.png)

當下次啟動程式時，NBug會嘗試將錯誤報告回傳至指定的位置，這邊NBug提供了許多錯誤報告回傳的方法可供選擇，像是：

* E-mail addresses
* Redmine Issue Tracker (using REST api)
* Any web page or form (via HTTP POST request)
* FTP servers
* Trac Issue Tracker (using XML-PRC)
* GitHub Issues Tracker (using GitHub api with POST (HTTP))
* Google Code Issue Tracker (using Google Code api with XML w/ POST)
* Databases (using ADO.NET)
* Mantis/Bugzilla

也就是說當錯誤發生時，我們能透過EMail、Redmine、FTP、HTTP之類的方法取得錯誤報告，不需要再去用USB之類的方法去收集錯誤報告，NBug可以替我們在背後自動處理、傳送，甚至是直接就傳到Issue tracker系統上面。

NBug使用上十分簡單，可直接透過NuGet去將組件加入使用，但這邊筆者強烈建議還是要去官網下載NBug，因為官網下載的[NBug會含有設定Config檔的Tool，方便開發人員編寫NBug的Config檔。下載完後解壓縮，進到tools目錄可以看到裡面有NBug.Configurator.exe、與NBug.Example.WinForm.exe，這邊我們主要需要用到的是NBug.Configurator.exe，NBug.Example.WinForm.exe只是輔助測試用的，可透過NBug.Configurator.exe叫起。](http://nbug.codeplex.com/)

![image10_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image10_thumb.png)

NBug.Configurator.exe開啟後可看到下面設定畫面，一開起來很多設定會是灰階的，因為我們並還未指定Config檔，這邊看個人需求是要編輯已經存在的設定檔還是建立新的設定檔會有不同的操作。這邊筆者假設要建立個新的設定檔，所以用滑鼠點擊後方的Create按鈕。

![image13_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image13_thumb.png)

設定完設定檔名後按下Save儲存離開。

![image19_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image19_thumb.png)

完成後本來灰階的設定欄位就會被開啟，可以開始進行設定檔的設定動作。

![image22_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image22_thumb.png)

在設定檔的設定上，我們可以透過User Interface指定當錯誤發生時，NBug要給予使用者怎樣的錯誤回報提示頁面，UI Provider後方的Preview按鈕可以做簡易的預覽。

![image34_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image34_thumb.png)

![image37_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image37_thumb.png)

除了User Interface外，Reporting這邊的設定也很重要，可以指定當錯誤發生時MiniDump要到什麼程度，也能指定何時去做錯誤報告回傳的動作。

General頁面的設定設定完後，我們必需要切到Submit頁面，這邊可以指定當錯誤發生時我們要怎樣回報錯誤，是要用EMail、Redmine、FTP、還是HTTP。

![image40_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image40_thumb.png)

每種回報方式有不同的設定要設，這邊應該大家都沒什麼問題，就不一一介紹了。

![image43_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image43_thumb.png)

當所有設定都設定完後，可以點擊下方的Save & Run Test App，之前提到的NBug.Example.WinForm.exe就會被帶出，我們可以藉由這個UI來測試當錯誤發生時會有怎樣的情形，選取好Exception後按下Generate Exception就可以了。

![image25_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image25_thumb.png)

這邊若是設定檔的UI Mode是Full的話應該會看到像下面這樣的畫面，簡單的帶出了例外的資訊，下方還允許使用者加些簡短的操作描述，使用者也可自行決定是否傳送。

![image28_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image28_thumb.png)

![image31_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image31_thumb.png)

這邊需特別提醒一下，NBug為了讓開發人員能追蹤錯誤報告傳不出去的問題，當錯誤報告傳送不出去時會彈出NBug Internal Exception Viewer視窗，這在產品Release時最好在設定那邊勾選Release Mode將之關閉。

![image_thumb_1.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image_thumb_1.png)

上面大致的將整的NBug的功能簡介了一下，也將設定檔的設定稍稍的帶過了，實際套用到現有程式專案中應該大家都能掌握了，只要很簡單的透過NuGet將NBug加入。

![image_thumb.png](/images/posts/fc5031f6-5ff7-4db9-9a43-416af96c1f52/image_thumb.png)

並加入下列程式碼，將未處理的例外交由NBug去處理就可以了。

```csharp
AppDomain.CurrentDomain.UnhandledException += NBug.Handler.UnhandledException;
Application.ThreadException += NBug.Handler.ThreadException;
```

## Link

* NBug
* NBug – Automated Bug Reporting for .NET
* Getting Started
* Configuration
