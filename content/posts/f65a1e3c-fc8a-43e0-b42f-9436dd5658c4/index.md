---
title: "[C++][Visual Studio]How to generate XML Documentation Files with visual studio C++"
date: "2013-11-06 12:00:00"
description: "[C++][Visual Studio]How to generate XML Documentation Files with visual studio C++"
---

這幾天又看到有人在論題上發問要如何在叫用所開發C++的函式庫時，能夠顯示自己在編寫所加註的註解。這問題也滿常重複問到的，稍稍的紀錄一下。

  其實在Visual Studio中要顯示註解，不論是什麼語言，都要在成員上加註特定的註解格式。格式上也都大同小異，寫起來就跟在C#或是VB.NET中沒什麼兩樣。   

但是為甚麼C++中常會有人碰到這樣的問題呢。有興趣的可以開啟個新專案試著建置看看就知道了，可以看到真的還是沒有產生。

  這是因為專案預設沒有啟動這樣的功能，所以雖然你有標註註解，但他就是不會產生對應的XML文件。若要啟動我們必須參閱/doc (Process Documentation Comments) (C/C++)。     

叫出Project Properties，依序點開 Cofiguration Properties => C/C++ => Output Files，將右側的Generate XML Documentation Files選項調為Yes(/doc)。

調完後再次編譯，就會在輸出目錄中看到產生出了對應的XML。

連帶XML檔跟著組件一起佈署，引用後叫用函式庫時就會帶出對應的註解。

## Link
     XML Documentation (Visual C++)    /doc (Process Documentation Comments) (C/C++)    Recommended Tags for Documentation Comments (Visual C++)    Delimiters for Visual C++ Documentation Tags