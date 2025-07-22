---
title: "error LNK1123_ failure during conversion to COFF_ file invalid or corrupt"
date: "2013-11-06 12:00:00"
description: "error LNK1123_ failure during conversion to COFF_ file invalid or corrupt"
---

今天在弄CI Server卡了很久，因為有個C++的專案在CI Server上建置會有error LNK1123: failure during conversion to COFF: file invalid or corrupt的錯誤。同樣的程式在筆者跟同事的環境是可以建置的，但在CI Server那台就是建置不過，而且很奇怪的是之前的其他專案的建置是會過的，理論上環境應該是OK的。

用錯誤訊息查閱了一下網路，發現有個說法是本來電腦上有Visual Studio 2010，再將Visual Studio 2012安裝上去就會發生這樣的狀況。原因是因為這樣做會導致C:\Program Files (x86)\Microsoft Visual Studio 10.0\VCin