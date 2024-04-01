---
title: "[C#]如何修正MDI父視窗受子視窗影響而無法正常關閉的問題"
date: "2013-11-06 12:00:00"
description: "[C#]如何修正MDI父視窗受子視窗影響而無法正常關閉的問題"
---

<p>昨天有讀者在筆者[VB.NET]MDI子視窗清單的實作</a>這篇反應用筆者的程式讓MDI的父視窗無法正常關閉，筆者覺得很不可思議，因為筆者的程式只有替換掉內建的MDI子視窗清單，並在點選時將對應的子視窗帶上來，不怎麼可能造成視窗無法關閉的情況，就算影響也應該只影響子視窗才是，因為筆者並未動到父視窗的部分。因此用Visual Studio內建的MDI樣板來做試驗。</p>  <p> </p>  <p>實際照著步驟測試，先點開兩個子視窗。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1301/CMDI_BBFB/image_2.png"><img style="border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px" border="0" alt="image" src="\images\posts