---
title: "[Visual Studio]VB 11.0 New Feature - Namespace Global"
date: "2011-09-27 01:28:04"
description: "Namespace Global是VB 11.0的新功能，該功能可想成所有命名空間的根命名空間，能解決以往存在VB.NET許久的命名空間問題。舉個例子來說，假設以往我們在自己的命名空間內有一個System的子命名空間，專案中也匯入了.NET Framework中的System命名空間，"
tags: [VB.NET]
---

Namespace Global是VB 11.0的新功能，該功能可想成所有命名空間的根命名空間，能解決以往存在VB.NET許久的命名空間問題。舉個例子來說，假設以往我們在自己的命名空間內有一個System的子命名空間，專案中也匯入了.NET Framework中的System命名空間，當要在裡面使用.NET Framework內System命名空間下的類別時，會發現我們無法使用，在這種情況下使用的是自己System命名空間下的東西。

![image_thumb.png](/images/posts/37903/image_thumb.png)

這樣的問題現在可以透過Global關鍵字來解決。

![image_thumb_1.png](/images/posts/37903/image_thumb_1.png)

Global關鍵字也能用於Namespace Statement中，當想在程式中脫離專案主命名空間的限制時可以考慮使用。像是下面這個例子，筆者定義了Global.MyNamespace的命名空間，下面有一個MyClass1的類別，在專案主命名空間下是找不到的。

![image_thumb_5.png](/images/posts/37903/image_thumb_5.png)

因為是定義在根命名空間之下，可像下面這樣使用。

![image_thumb_4.png](/images/posts/37903/image_thumb_4.png)

同樣的概念也可以用來擴充現有的命名空間，像是下面這樣擴充系統的命名空間。

![image_thumb_6.png](/images/posts/37903/image_thumb_6.png)

## Link

* Namespaces in Visual Basic
