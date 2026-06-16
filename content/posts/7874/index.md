---
title: "[.NET Concept]Notes on Maximizing MDI Child Windows (Part 2)"
slug: "dotnet-concept-notes-on-maximizing-mdi-child-windows-part-2"
aliases: ["/posts/7874/"]
date: "2009-04-06 12:05:08"
description: "不知道大家有沒有碰過當把MDI子表單放大時，Menu選單會變得如下圖一樣怪怪的現象。 會發生如上圖這樣的現象，其實是因為Form.MainMenuStrip屬性沒設定所造成的。"
tags: [.NET Concept]
---

不知道大家有沒有碰過當把MDI子表單放大時，Menu選單會變得如下圖一樣怪怪的現象。

![image_thumb.png](/images/posts/7874/image_thumb.png)

會發生如上圖這樣的現象，其實是因為Form.MainMenuStrip屬性沒設定所造成的。

![image_thumb_2.png](/images/posts/7874/image_thumb_2.png)

[MSDN](http://msdn.microsoft.com/zh-tw/library/system.windows.forms.form.mainmenustrip(VS.80).aspx)上對該屬性的說明如下：

![image4_thumb.png](/images/posts/7874/image4_thumb.png)

可能很都人在開發時都不知道，也從沒設定過這個屬性，這多半是因為在Visual Studio中，當把選單元件放到表單時，Visual Studio會很聰明的幫我們把Form.MainMenuStrip這個屬性給設定上去的緣故。因此在一般的情況下我們是不需要額外做此設定的。

但是這並不代表這個問題就不會發生，也不代表我們不需要注意這點。因為只要當你不是第一次加入選單，Visual Studio就不會幫你設定該屬性了。

## 問題重現步驟

若有興趣重現該問題，可照下列操作步驟：

**Step1:在MDI主表單放入MenuStrip與ToolStrip**

此時若切到主表單的屬性視窗，可看到MainMenuStrip已被自動設定。執行後子表單的放大動作正常。

**Step2:把MenuStrip殺掉**

此時若切到主表單的屬性視窗，可看到MainMenuStrip已被清空。

**Step3:加入MenuStrip**

此時若切到主表單的屬性視窗，可看到MainMenuStrip仍保持清空狀態。執行後放大子表單就會看到該問題發生。
