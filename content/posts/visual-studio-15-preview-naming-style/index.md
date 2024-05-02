---
title: "Visual Studio 15 Preview - Naming style"
date: "2016-04-18 15:28:00"
description: "Visual Studio 15 Preview - Naming style"
tags: [Visual Studio]
---


Visual Studio 15 Preview 開始支援命名規則的檢查。  

<!-- More -->

<br/>


使用時可開啟選項視窗，切換到 [Text Editor | C# | Code Style | Naming] 頁面，點選右側頁面的 "+" 按鈕，加入新的命名規則。  

{% img /images/posts/VS15PreviewNamingStyle/1.png %}

<br/>


在彈出的命名規則對話框中，我們要先為這個命名規則取個名字，接著點選符號規格後的 "+" 按鈕，設定命名規則要套的範圍。  

{% img /images/posts/VS15PreviewNamingStyle/2.png %}

<br/>


符號規格對話框這邊，我們一樣要給符號規格命名，然後決定命名規則套用的範圍。像是這邊筆者想要對所有方法生效，在符號種類這邊就要選取 method，存取範圍則全部選取。  

{% img /images/posts/VS15PreviewNamingStyle/3.png %}

<br/>


符號規則訂定後，接著要訂定命名樣式，命名樣式這邊一樣要為它命名，然後設定他的前置詞，後置詞，分隔字元，大小寫。像是這邊筆者想要讓所有的方法都用 Pascal 命名，所以這邊將設定調為 `Pascal 大小寫名稱`。  

{% img /images/posts/VS15PreviewNamingStyle/4.png %}

<br/>


最後要設定的是命名規則的嚴重程度，這邊視個人需要下去調整即可，看覺得是 None，Info，Warning，Error 哪個層級都可。   

{% img /images/posts/VS15PreviewNamingStyle/5.png %}

<br/>


設定好後在撰寫程式時 Visual Studio 就會依照制定的命名規則下去檢查。  

{% img /images/posts/VS15PreviewNamingStyle/6.png %}

<br/>
