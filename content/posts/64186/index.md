---
title: "[C++]使用Global Flags偵測記憶體越界錯誤"
date: "2012-01-03 10:03:27"
description: "[C++]使用Global Flags偵測記憶體越界錯誤"
tags: [C++,Software]
---

筆者在[C++]使用Pageheap偵測記憶體越界錯誤這篇介紹了如何利用Pageheap去偵測記憶體的越界錯誤，這樣的功能也可以使用Debuging Tools內的Global Flags工具，可以達到相同的效果，且較易取得與使用。

Debuging Tools有需要可在Microsoft Windows SDK for Windows 7 and .NET Framework 4這邊下載。

安裝時要注意Common Utilities下的Debuging Tools for Windows必須勾選。

安裝完後，若需要使用可直接點擊Global Flags開啟GUI。

GUI視窗帶出後切換至Image File頁籤，在Image輸入框中鍵入要偵測的程式名稱。

輸入完偵測的程式名稱后按下Tab鍵，下方被Disable的Checkbox會變為Enable狀態，這時可以針對需要去做些勾選設定，以筆者個人來說視習慣將heap有關的都勾選起來，設定好後按下套用即可。

當程式啟用偵測後，越界問題能更容易被發現，就像是筆者在[C++]使用Pageheap偵測記憶體越界錯誤這篇所提到的一樣，下面的Code運行在Debug模式下能得到跟Release模式一樣的運行結果，運行後因為越界錯誤所以直接Crush。

#include "stdafx.h"
#include

int _tmain(int argc, _TCHAR* argv[])
{
int m_len = 5;
char *m_p = (char *)HeapAlloc (GetProcessHeap (), HEAP_ZERO_MEMORY, m_len);
m_p[m_len] = 0;
HeapFree (GetProcessHeap (),0, m_p);

return 0;
}

Google Flags程式除了可以用GUI的方式去設定，也可以透過命令列的方式去使用，使用時必須注意命令提示字元要給予管理者的權限。

命令提示字元開啟後，我們可以帶入-p、/enable、與要偵測的程式名稱：

gflags -p /enable [ExeFile]

要關閉偵測時，則是帶入-p、/disable、與要關閉偵測的程式名稱：

gflags -p /disable [ExeFile]

若要查詢有哪些程式開啟了偵測狀態，可以只帶入-p參數：

gflags -p

##
Link

Download and Install Debugging Tools for Windows

Microsoft Windows SDK for Windows 7 and .NET Framework 4

使用Gflags来检测heap问题

如何設定使用 Gflags.exe 工具 GlobalFlag 登錄值

Detecting Heap Corruption Using GFlags and Dumps

windows下堆异常调试神器--gflags

[C++]使用Pageheap偵測記憶體越界錯誤