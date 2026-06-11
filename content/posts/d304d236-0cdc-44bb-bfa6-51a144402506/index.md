---
title: "Use Windows Error Reporting(WER) to collect user-mode dumps"
date: "2013-11-06 12:00:00"
description: "Use Windows Error Reporting(WER) to collect user-mode dumps"
tags: [CSharp]
---

在Windows Server 2008、Windows Vista with Service Pack 1 (SP1)以後，Windows Error Reporting(WER)具備了自動擷取並儲存user-mode dumps的能力。

相關的設定在"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps"這機碼位置，機碼的設定可參閱Collecting User-Mode Dumps這邊。

簡單的說有DumpFolder、DumpCount、DumpType、CustomDumpFlags這幾個設定，對應到的是Dump出來的檔案要存放的位置、最多Dump幾個檔案、Dump的型態(Mini Dump還是FullDump)、以及客製用的Flag。

這些設定都有其慣用的預設值，多半我們只需要設定需要修改的部分，其餘的直接讓它套用預設值即可。若要針對特定應用程式下去設定，將設定改設在"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps\[ApplicationAssembly]"就可以了。

這邊實際的示範一下，以下面這個簡易的程式為例：

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication46
{
class Program
{
static void Main(string[] args)
{
var x = 1;
var y = x - 1;
var result = x / y;
}
}
}

程式運行起來會因為除以0而掛掉。

這時開啟檔案總管，將當前目錄切至"%LOCALAPPDATA%\CrashDumps"(預設的dump存放在這個位置，可參閱上方MSDN的圖片)，可以看到Windows Error Reporting幫我們抓的dump就放在裡面。

滑鼠連點候用Visual Studio開啟，會看到像下面這樣的Minidump File Summary，這時點擊右側的Debug with Mixed連結。

Visual Studio若找的到對應的程式與PDB的話，就會將其帶出方便開發人員找到問題的所在。

如果要對特定應用程式做設定，像是將dump位置改掉，以這邊的例子來說，可在"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps"下新增ConsoleApplication46.exe的機碼。

然後新增一個可擴充字串值。

取名為DumpFolder，將其值設定為%localappdata%，讓dump出來的檔字直接放在Local App Data下。(注意到在win7以後的電腦，dump存放的位置要特別留意，不然可能會被UAC給擋住)

再次運行程式，程式掛掉後我們應該要可以在Local App Data下看到dump出來的檔案。

## Link


Collecting User-Mode Dumps

How to debug silent crashes in .Net