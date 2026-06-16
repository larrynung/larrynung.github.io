---
title: "Visual Studio 2010 New Feature - 建議模式(Consume First Mode)"
date: "2011-01-17 08:12:22"
description: "在以往我們使用Visual Studio，當輸入部份關鍵字Intellisense就會自動幫忙找到可能要輸入的Intellisence提示項目，並將最符合的Intellisence提示項目選取，此時若我們按下Tab或是Space，Visual Studio會自動幫我們用選取的字串帶入編輯區。"
tags: [CSharp,Visual Studio]
---

在以往我們使用Visual Studio，當輸入部份關鍵字Intellisense就會自動幫忙找到可能要輸入的Intellisence提示項目，並將最符合的Intellisence提示項目選取，此時若我們按下Tab或是Space，Visual Studio會自動幫我們用選取的字串帶入編輯區。

![image6_thumb.png](/images/posts/20863/image6_thumb.png)

這樣貼心的功能在大多數時候是十分的方便，但若團隊是採用TDD下去開發時，這樣的貼心功能就會變得有點綁手綁腳。以下面這張圖片為例，若在專案中已有MyClassBase類別，且MyClassBase類別中已有RunTest成員方法，此時在想在單元測試中先為名為Run的新方法撰寫單元測試的話，就會被IDE自動帶出RunTest，還需手動下去刪除修改。

![image_thumb.png](/images/posts/20863/image_thumb.png)

但若是有按下Ctrl+Alt+Space切換至建議模式(Consume First Mode)的話，可看到Intellisence上面會多出一個輸入方框，此時若不手動下去按上下鍵或是用滑鼠左鍵選取Intellisence提示的項目，IDE也不會自動幫我們選取Intellisence提示的項目，而會先以消耗使用者輸入的為主。

![image_thumb_1.png](/images/posts/20863/image_thumb_1.png)

因此我們可以一邊撰寫完單元測試，一邊利用Visual Studio的另一個新功能Generate From Usage為該類別加入對應的方法。

![image_thumb_2.png](/images/posts/20863/image_thumb_2.png)

待所有的單元測試整個完成後在回到類別中完成程式碼。

![image_thumb_3.png](/images/posts/20863/image_thumb_3.png)

## Link

* [VS2010 Online]解析Historical debug in Visual Studio 2010 - IntelliTrace
* Intellisense for TDD in Visual Studio 2010
