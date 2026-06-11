---
title: "[C#]使用Windows API Code Pack存取媒體櫃內存放的資料"
slug: "[CSharp]使用Windows API Code Pack存取媒體櫃內存放的資料"
date: "2013-11-06 12:00:00"
description: "[C#]使用Windows API Code Pack存取媒體櫃內存放的資料"
tags: [CSharp]
---

要用程式存取媒體櫃內存放的資料，我們大概可以有兩種方法，一種是自行解析，一種則是使用包好的函式庫(像是Windows API Code Pack)去作控制。之所以能夠自行解析是因為媒體櫃的資訊是存放在附檔名為.library-ms的XML檔案中。

可以看到裡面有很多資訊存放在裡面，而我們最關心的目錄位置也在其中。

這邊不再對自行解析多作解釋，只要會了解格式與熟悉XML的操作應該都沒問題。而若是使用Windows API Code Pack來做，我們需要將Microsoft.WindowsAPICodePack.dll以及Microsoft.WindowsAPICodePack.Shell.dll這兩個組件加入參考。

加入參考後加入命名空間Microsoft.WindowsAPICodePack.Shell，就可以開始程式的撰寫。
  using Microsoft.WindowsAPICodePack.Shell;

使用Windows API Code Pack來操作媒體櫃主要要用到ShellLibrary這個類別，若要建立一個新的媒體櫃，很簡單的建立一個ShellLibrary物件就可以了，建立時要帶入新媒體櫃的名稱。

using (ShellLibrary library = new ShellLibrary(libraryName, true))
{
...
}

而若是要載入現有的媒體櫃，則可以呼叫ShellLibrary.Load，帶入要載入的媒體櫃名稱。

using (ShellLibrary shellLibrary =
    ShellLibrary.Load(libraryName, folderPath, isReadOnly))
{
...
}

不論是建立還是載入媒體櫃，我們都可以拿到ShellLibrary的物件實體，透過這個物件實體我們可以針對媒體櫃做增刪目錄等進階的操作。

...
shellLibrary.Remove(folderToRemove);
shellLibrary.Add(folderToAdd);
...

若是要遍巡找出媒體櫃內有哪些目錄及檔案，可以直接對取得的ShellLibrary物件實體去遍巡，這邊要注意的是，遍巡的元素可能是ShellFolder，也有可能是ShellFile，若有需要ShellFolder還必須再另行處理。

...
using (ShellLibrary library = ShellLibrary.Load("Pictures", false))
{
foreach (ShellFolder folder in library)
{
var folderPath = folder.ParsingName;
Console.WriteLine(folderPath);
}
}
...

## Link

  Windows 7 Libraries C# Quick Reference

  如何以程式設計方式操作 Windows 7 殼層文件庫