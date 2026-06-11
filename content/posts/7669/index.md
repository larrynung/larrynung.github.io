---
title: "[.NET Concept][C#][VB.NET].NET兩個表單間的資料互通"
date: "2009-03-24 12:44:08"
description: "[.NET Concept][C#][VB.NET].NET兩個表單間的資料互通"
tags: [CSharp,VB.NET,.NET Concept]
---

常會看到有人詢問兩個表單間的資料要如何互通，重覆詢問率之高讓該問題約可列入初學者必問的前幾大問題了，光在程式設計俱樂部大概這類問題我大概就已回答過4~5次了。最近又在批踢踢討論版中看到有人詢問，索性想說乾脆就整理一篇以後直接貼連結好了。

基本上要讓兩個表單間的資料達到互通大概有下列兩種方法：

### 方法一 使用Public欄位、屬性、或方法互通表單資料


如上圖所示，假設今天我們有兩個表單Form1跟Form2，且Form2由Form1所叫起，在這樣的條件之下，若Form1想要取得Form2上面的資料，相信應該對大家來說都不是問題，直接在Form1上使用Form2的Public欄位、屬性、或方法就可以了。如下程式所示，透過這些Public的成員，我們很容易的可以把Form1的資料送給Form2，也很容易的可以由Form1把Form2上的資料取回。

舉個例子來說，假如Form2內的資料存取範圍為Public或是Friend(控制項的話則如下圖把Modifiers屬性值設為Public或是Friend)。

則我們可以在Form1中透過Form2的物件參考直接去控制Form2的控制項或是內部的資料。

VB.NET

C#

很簡單吧？不過這並不是很好的寫法，因為此種寫法違反了物件導向的封裝原則。較好的寫法是利用屬性去封裝，首先我們需要把Form2的資料存取範圍設為Private(控制項的話則如下圖把Modifiers屬性值設為Private)，讓類別外無法直接做存取的動作。

接著，我們可以撰寫如下的Code，利用屬性封裝Form2的控制項甚至是內部的資料。

VB.NET

C#

用屬性封裝好後我們就可以在Form1中透過Form2的物件參考，藉由Form2的Public屬性控制Form2的控制項或內部的資料。

VB.NET

C#

介紹完Form1如何取得Form2上面的資料後，反過來要是Form2想要主動取得或設定Form1的資料呢？其實也很簡單，如下程式所示，只要把上面的概念活用，在Form2被Form1叫起後透過建構子或Public屬性把Form1的物件參考傳到Form2內，Form2就可以用Form1傳進來的物件參考對Form1內的Public成員做想要的動作。

VB.NET

Public Class Form1  
...
      'Form1透過Form2的Public成員把自身的物件參考傳入Form2
      Form2.MainForm = Me
...
End Class

Public Class Form2
...
      Public MainForm As Form1
...
      'Form2透過Form1傳進的物件參考控制Form1
      MainForm.Value = Me.NumericUpDown1.Value
...
End Class

C#

值得注意的是，上述方法我是為了示範較簡單的方式才會把Form1的物件參考傳入Form2，實際使用上，能避免這樣寫還是建議盡量避免，因為這樣會讓Form1跟Form2的耦合性提高，較好的方法是直接Binding。

或是在Form2內定義一些對應的事件，Form1在這些事件觸發時再利用Form2的物件做對應的處理。

程式大概如下：

P.S.這邊初學者很容易犯的問題就是會在Form2內再宣告出一個Form1，並對宣告出的Form1做資料互傳，最後的結果當然是資料互傳後結果不如預期。這是因為沒認清物件參考的原因，每宣告一個物件實體作業系統都會分配一塊記憶體空間，因此需認清本來的Form1表單與Form2內新宣告的Form1是不同的物件參考這個事實。

### 方法二 透過靜態變數互通表單資料


透過靜態變數也是可以互通表單資料的方法，使用起來很簡單，只要宣告個靜態變數，接著把該靜態變數指向物件參考，則程式內就可透過該靜態變數做資料的互通，但是該方法較不建議採用。

附帶一提，微軟的Beginner Developer Learning Center有此議題的教學影片，有興趣的可點選下方連結自行參閱：

##### Tier 3: Exchange Data Between Two Forms in a Windows Forms Application


## Download


CommunicationBetweenTwoForm.zip