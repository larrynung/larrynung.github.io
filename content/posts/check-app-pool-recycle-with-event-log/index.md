---
title: "Check app pool recycle with event log"
date: "2014-12-27 23:25:00"
description: "Check app pool recycle with event log"
---


IIS Website 預設 29 小時回進行一次回收，所有 Session 連帶會被斷線。  

<!-- More -->

<br/>

若要偵測是否是因為該機制導致使用者斷線，我們可以從 Event Log 下去觀察，只要查閱 Windows Logs\System 內是否有 Source 為 WAS 且 Level 為 Information 的 Event 就可以了。 

{% img /images/posts/CheckAppPoolRecycle/1.png %}
