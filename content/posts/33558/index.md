---
title: "[C++][Visual Studio]Modify Inherited Properties with the Property Manager"
slug: "cpp-visual-studio-modify-inherited-properties-with-the-property-manager"
aliases: ["/posts/33558/"]
date: "2011-08-19 01:14:40"
description: "在Visual Studio 2010以前透過Tools\\Options...開啟Options對話框，在Projects and Solutions\\VC++ Directories下面可以設定VC++會用到的目錄，在Visual Studio 2010這個選項已經不能在本來的地方設定了。"
tags: [Visual Studio,C++]
---

在Visual Studio 2010以前透過Tools\Options...開啟Options對話框，在Projects and Solutions\VC++ Directories下面可以設定VC++會用到的目錄，在Visual Studio 2010這個選項已經不能在本來的地方設定了。

![image_thumb.png](/images/posts/33558/image_thumb.png)

設定被改至Project\Properties對話框中的Configuration Properties\VC++ Directories頁面內。

![image_thumb_1.png](/images/posts/33558/image_thumb_1.png)

透過該頁面我們一樣可以設定目錄的位置，但有的時候安裝了一些額外的組件，會寫入一些目錄位置，可能造成衝突使得專案編譯不過。像是在這邊同事的電腦就碰到這樣的問題，光開啟一個新的C++專案就無法編譯過。但是有時候這些目錄位置是繼承下來的，也就是顯示在下半部不可編輯的區塊呢。

![image_thumb_3.png](/images/posts/33558/image_thumb_3.png)

碰到這樣的狀況時，我們可以使用Property Manager去調整繼承的屬性，透過View\Other Windows\Property Manager將Property Manager視窗開啟。

![image_thumb_2.png](/images/posts/33558/image_thumb_2.png)

接著在Property Manager視窗中找到Microsoft.Cpp.Win32.user後，按下滑鼠右鍵，在滑鼠右鍵快顯選單中點選Properties項目。

![image_thumb_5.png](/images/posts/33558/image_thumb_5.png)

一樣切換至Configuration Properties\VC++ Directories頁面，這時候去編輯就是編輯繼承的屬性了。以這邊這個例子來說，我想要將C:\QT\Include的目錄位置給拿掉，就可以在這邊將其直接刪除。

![image_thumb_6.png](/images/posts/33558/image_thumb_6.png)

刪除後回到專案屬性那邊去看，下方不可編輯的繼承區就不會有我們修掉的目錄了。

![image_thumb_7.png](/images/posts/33558/image_thumb_7.png)

## Link

* ##### Inherited Properties and Property Sheets
* ##### 屬性管理員
