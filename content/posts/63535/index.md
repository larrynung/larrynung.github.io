---
title: "[C++]使用Visual Leak Detector for Visual C++ 2008/2010輔助偵測程式中記憶體洩漏的問題"
date: "2011-12-27 12:52:07"
description: "[C++]使用Visual Leak Detector for Visual C++ 2008/2010輔助偵測程式中記憶體洩漏的問題"
tags: [C++]
---

Visual Leak Detector for Visual C++ 2008/2010是一免費的開放源碼工具，能輔助開發人員偵測C++程式中記憶體洩漏的問題，使用上也算十分簡單，至Visual Leak Detector for Visual C++ 2008/2010下載主程式後。

安裝後會在Program Files(x86)下找到安裝的程式，裡面比較重要的就是bin、lib跟include幾個目錄，bin目錄存放dll組件，lib存放靜態函式庫，include則是存放著標頭擋。

這邊以靜態函式庫為例，先開啟專案的屬性，在Additional Dependencies這邊設定lib檔的位置。

Additional Include Directories這邊設定include目錄位置。

都設定好後在程式中加入vld.h檔的引用，建置後執行程式，當關閉時偵測的結果就會顯現在輸出視窗中。

#include "vld.h"

這邊筆者示範個簡潔的範例，程式碼如下：

// Test_VisualLeakDetector.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "vld.h"

int _tmain(int argc, _TCHAR* argv[])
{
char* buffer = new char[512];
return 0;
}

運行後關閉，在輸出視窗就會顯現像下面這樣的偵測結果，不僅僅每個偵測到的Leak都會有當下的呼叫堆疊與記憶體資訊，也會列出簡單的統計資訊，像是總共發現的leak數、最大記憶體用量、與總共花費的記憶體。若要修正偵測到的Memory leak，可點擊感興趣的call stack，程式碼會自動跳至對應的位置。

## Link


Visual Leak Detector for Visual C++ 2008/2010