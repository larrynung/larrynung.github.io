---
title: "Visual Studio 2010 UML 朔模功能初步概述"
date: "2010-10-01 12:29:42"
description: "Visual Studio 2010 UML 朔模功能初步概述"
tags: [UML,Visual Studio]
---

Visual Studio 2010針對UML的支援上做了一些改進，可支援的UML圖有下列六種：
     使用案例圖(Use Class Diagrams)    活動圖(Activity Diagrams)    順序圖(Sequence Diagrams)    元件圖(Component Diagrams)    類別圖(Class Diagrams)    套件圖(Package Diagrams)   

透過方案總管右鍵快顯選單中的加入新增項目，我們可以直接將這些UML圖加入至現有的專案中。

也可以新增個專門用來存放UML的Modeling Project專案，與其它程式碼分開存放，統一放置朔模用的UML圖形。

值得注意的是，這兩種使用方法有一些差異存在，像是加入UML圖形至現有專案，UML Model Explore視窗就無任何功用。

而若UML圖形加入的是Modeling Project，則UML Modeling Explore可正常運作。

若是畫好了UML的類別圖，透過VS2010的輔助也能幫您產生對應的程式碼框架。需注意的是，VS2010預設內建並無從UML類別圖產生程式碼的功能，使用前需另行安裝Visual Studio 2010 Feature Packs才可使用。

安裝完後我們就可以透過已經朔模好的類別圖進行產生對應的程式碼框架，可在類別圖中的空白區域或是特定的類別上，按下滑鼠右鍵，在彈出的右鍵快顯選單中，點選Generate Code快顯選單選項。

或是透過UML Model Expolrer視窗，選取根節點或是特定的類別後，按下滑鼠右鍵，在彈出的右鍵快顯選單中，點選Generate Code快顯選單選項。

按下Generate Code快顯選單選項後，VS2010會開始進行產生對應的程式碼框架動作。

完成後，會加入一個程式專案，用以存放透過類別圖產出的程式碼框架。值得注意的是，這邊所產出的程式碼框架會依照前面選取的不同而有所差異，若是前面是選取特定類別的話，程式碼框架就只會產生所選取的類別。反之，則類別圖中所有的類別都會產生對應的程式碼框架。

除此之外，VS2010在UML上與Team Foundation Server也做了相當程度的整合，能為UML上的畫的項目建立對應的Work Item，將朔模流程與開發流程合，增加開發的能見度。

## Link
     HOW TO：建立 UML 模型專案和圖表    Visual Studio 2010 Feature Packs    Visual Studio 2010: UML modeling projects    How to: Generate Code from UML Class Diagrams    How to: Generate Files from a UML Model