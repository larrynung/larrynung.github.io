---
title: "A First Look at UML Modeling in Visual Studio 2010"
slug: "a-first-look-at-uml-modeling-in-visual-studio-2010"
aliases: ["/posts/18011/"]
date: "2010-10-01 12:29:42"
description: "Visual Studio 2010針對UML的支援上做了一些改進，可支援的UML圖有下列六種： 使用案例圖(Use Class Diagrams) 活動圖(Activity Diagrams) 順序圖(Sequence Diagrams) 元件圖(Component Diagrams)…"
tags: [UML,Visual Studio]
---

Visual Studio 2010針對UML的支援上做了一些改進，可支援的UML圖有下列六種：

1. 使用案例圖(Use Class Diagrams)
2. 活動圖(Activity Diagrams)
3. 順序圖(Sequence Diagrams)
4. 元件圖(Component Diagrams)
5. 類別圖(Class Diagrams)
6. 套件圖(Package Diagrams)

透過方案總管右鍵快顯選單中的加入新增項目，我們可以直接將這些UML圖加入至現有的專案中。

![image_thumb_3.png](/images/posts/18011/image_thumb_3.png)

![image_thumb_4.png](/images/posts/18011/image_thumb_4.png)

也可以新增個專門用來存放UML的Modeling Project專案，與其它程式碼分開存放，統一放置朔模用的UML圖形。

![image_thumb.png](/images/posts/18011/image_thumb.png)

![image13_thumb.png](/images/posts/18011/image13_thumb.png)

![image_thumb_1.png](/images/posts/18011/image_thumb_1.png)

值得注意的是，這兩種使用方法有一些差異存在，像是加入UML圖形至現有專案，UML Model Explore視窗就無任何功用。

![image_thumb_5.png](/images/posts/18011/image_thumb_5.png)

而若UML圖形加入的是Modeling Project，則UML Modeling Explore可正常運作。

![image_thumb_6.png](/images/posts/18011/image_thumb_6.png)

若是畫好了UML的類別圖，透過VS2010的輔助也能幫您產生對應的程式碼框架。需注意的是，VS2010預設內建並無從UML類別圖產生程式碼的功能，使用前需另行安裝Visual Studio 2010 Feature Packs才可使用。

![image23_thumb.png](/images/posts/18011/image23_thumb.png)

安裝完後我們就可以透過已經朔模好的類別圖進行產生對應的程式碼框架，可在類別圖中的空白區域或是特定的類別上，按下滑鼠右鍵，在彈出的右鍵快顯選單中，點選Generate Code快顯選單選項。

![image20_thumb.png](/images/posts/18011/image20_thumb.png)

或是透過UML Model Expolrer視窗，選取根節點或是特定的類別後，按下滑鼠右鍵，在彈出的右鍵快顯選單中，點選Generate Code快顯選單選項。

![image_thumb_2.png](/images/posts/18011/image_thumb_2.png)

按下Generate Code快顯選單選項後，VS2010會開始進行產生對應的程式碼框架動作。

![image_thumb_7.png](/images/posts/18011/image_thumb_7.png)

完成後，會加入一個程式專案，用以存放透過類別圖產出的程式碼框架。值得注意的是，這邊所產出的程式碼框架會依照前面選取的不同而有所差異，若是前面是選取特定類別的話，程式碼框架就只會產生所選取的類別。反之，則類別圖中所有的類別都會產生對應的程式碼框架。

![image_thumb_8.png](/images/posts/18011/image_thumb_8.png)

除此之外，VS2010在UML上與Team Foundation Server也做了相當程度的整合，能為UML上的畫的項目建立對應的Work Item，將朔模流程與開發流程合，增加開發的能見度。

## Link

* [HOW TO：建立 UML 模型專案和圖表](http://msdn.microsoft.com/zh-tw/library/dd409445.aspx)
* [Visual Studio 2010 Feature Packs](http://msdn.microsoft.com/zh-tw/vstudio/ff655021(en-us).aspx)
* [Visual Studio 2010: UML modeling projects](http://weblogs.asp.net/gunnarpeipman/archive/2009/11/04/visual-studio-2010-uml-modeling-projects.aspx)
* [How to: Generate Code from UML Class Diagrams](http://msdn.microsoft.com/en-us/library/ff657795.aspx)
* [How to: Generate Files from a UML Model](http://msdn.microsoft.com/en-us/library/ee329480.aspx)
