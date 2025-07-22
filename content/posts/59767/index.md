---
title: "[C++]使用Pageheap偵測記憶體越界錯誤"
date: "2011-11-28 01:14:47"
description: "[C++]使用Pageheap偵測記憶體越界錯誤"
tags: [C++]
---Pageheap工具能輔助C++開發人員偵測難以察覺的記憶體越界錯誤，工具程式可至這邊下載。

Pageheap可分為兩種偵測模式，一種是一般分頁堆積，一種是完整分頁堆積。不同的偵測模式有不同的效果，在如何在 Windows XP 和 Windows 2000 中使用 Pageheap.exe這篇中有很清楚的介紹，這邊截錄文章裡面的表格，可以很清楚的看到兩個模式的差異，這邊是自己的需要去選擇模式就可以了。

失敗

一般分頁堆積

完整分頁堆積

無效的堆積指標

立刻發現

立刻發現

無效的堆積區塊指標

立刻發現

立刻發現

非同步的存取

立刻發現

立刻發現

假設重新配置位址

直到確實釋放發現率 90%

立刻發現率 90%

重複釋放

立刻發現率 90%

立刻發現率 90%

重新使用釋放後區塊

直到確實釋放發現率 90%

立刻發現率 90%

存取區塊結束位址後區塊

釋放時發現

立刻發現

存取區塊起始位址後區塊

釋放時發現

立刻發現 (特殊旗標)

若要查閱Pageheap的指令可在命令提示字元下輸入：

Pageheap /?

就可看到詳細的命令與使用方式：

pageheap - Page heap utility, v 1.04
Copyright (C) Microsoft Corp. 1981-1999

pageheap Displays pageheap enabled programs
pageheap /enable PROGRAM Enables page heap for PROGRAM
pageheap /enable PROGRAM FLAGS Enables page heap for PROGRAM using
FLAGS (hex number) for heap flags.
pageheap /disable PROGRAM Disables page heap for PROGRAM
pageheap PROGRAM Displays current setting for PROGRAM

Example: pageheap /enable notepad
pageheap /disable pbrush

Note. Enabling page heap does not affect currently running
processes. If you need to use page heap for processes that are
already running and cannot be restarted (csrss.exe, winlogon.exe),
a reboot is needed after the page heap has been enabled for
that process.

FLAGS hex value (0x...) has the following structure:

B7-B0 Bit flags 1 - enable page heap

01 - enable page heap. If zero normal heap is used.
In 99% of the cases you will want this to be set.
02 - collect stack traces (default on checked builds)
04 - minimize memory impact
08 - minimize randomly(1)/based on size range(0)
10 - catch backward overruns

B15-B8 Percentage of available memory from total memory below
which allocations will be made from normal heap. Used
in conjuction with bit flag 04.

B31-B24 Probability for page heap allocation. Bit 4 and 8 must
be set.

B31-B24 Size range start
B23-B16 Size range end
Allocations in this size range will be made in page heap.
Bit 4 must be set and bit 8 must be reset.

Examples:

pageheap /enable PROGRAM 0x03

Enable stack trace collection on free builds where it is not
the default.

pageheap /enable PROGRAM 0x13

Put the not accessible page at the begining of the allocation
and enable stack traces.

pageheap /enable PROGRAM 0x3000300F

With 48% probability allocate in page heap. If memory gets
below 48% then all allocations are done in normal heap.

這邊實際來操演一次，先建立一個C++的Console專案，將專案命名為testPageHeap1。

在testPageHeap1.cpp內撰寫如下程式：

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

程式撰寫完後建置，執行後可以看程式並不會掛掉，但是這邊的程式卻已經存取到陣列外，是有問題的程式。此時可以使用Pageheap對此程式啟用越界錯誤的檢查。

在使用Pageheap時必須注意到須以系統管理員身分執行命令提示字元。

不然再使用Pageheap時會出現"Error: Cannot open image registry key for testpageheap1.exe"這樣的錯誤訊息。

以系統管理員身分執行命令提示字元後，我們將目錄切至要偵測的程式所在目錄，使用Pageheap /enable [檔名]啟用越界錯誤的偵測，接著輸入Pageheap確認是否啟用越界錯誤偵測成功。

啟用成功後再次執行我們的程式，可以發現越界錯誤發生了，這樣我們就可以立即的找到並修復這樣的問題。

當調試完成，我們可以執行Pageheap /disable [檔名]將越界錯誤偵測給關閉。

##
Link

如何在 Windows XP 和 Windows 2000 中使用 Pageheap.exe

堆调试工具——pageheap的使用和原理分析

使用PageHeap.EXE或GFlags.EXE檢查內存越界錯誤（轉載）