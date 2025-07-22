---
title: "[C#]如何取出最近在Windows上所使用的文件檔案"
slug: "[CSharp]如何取出最近在Windows上所使用的文件檔案"
date: "2013-11-06 12:00:00"
description: "[C#]如何取出最近在Windows上所使用的文件檔案"
tags: [CSharp]
---最近在評估一個功能，希望能用Windows最近使用的文件檔案做些對應的處理，這邊不想用監控整個檔案系統的方式，也不想要像防毒軟體一樣Hook，因此想到在Windows中有Recent Items這樣的東西，假設我能取得這邊的資訊，應該也就夠我做些處理了。

稍微花點時間研究了一下，發現Recent Items的資料主要是由"%appdata%\Microsoft\Windows\Recent"這邊來的。

我們可以由上圖看到裡面的檔案都是以捷徑的方式存在，也就是說當我在用Windows存取某些檔案，Windows會自動幫我建立對應的捷徑並丟到這個位置。因此若是遍巡這個目錄位置內的每個捷徑檔案，並將捷徑檔案所指到的原始檔位置讀出，就可以知道在Windows上最近所使用的文件檔案了。

以程式的撰寫來看，我們可以透過Environment.GetFolderPath(Environment.SpecialFolder.Recent)去取得Recent Items資料存放的目錄。
var recentFolder = Environment.GetFolderPath(Environment.SpecialFolder.Recent);

取得Recent Items資料存放的目錄後，遍巡所有檔案並參閱[C#][VB.NET].NET捷徑(ShortCut)控制，將所有捷徑檔案指到的原始檔案位置讀出就可以了。這邊筆者稍微將需要的動作整理成一個輔助類別。

public class RecentlyFileHelper
{
public static string GetShortcutTargetFile(string shortcutFilename)
{
var type = Type.GetTypeFromProgID("WScript.Shell");
object instance = Activator.CreateInstance(type);
var result = type.InvokeMember("CreateShortCut", BindingFlags.InvokeMethod, null, instance, new object[] { shortcutFilename });
var targetFile = result.GetType().InvokeMember("TargetPath", BindingFlags.GetProperty, null, result, null) as string;

return targetFile;
}

public static IEnumerable GetRecentlyFiles()
{
var recentFolder = Environment.GetFolderPath(Environment.SpecialFolder.Recent);
return from file in Directory.EnumerateFiles(recentFolder)
where Path.GetExtension(file) == ".lnk"
select GetShortcutTargetFile(file);
}
}

使用起來就像這個樣子：

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
public partial class Form1 : Form
{
public Form1()
{
InitializeComponent();
}

private void Form1_Load(object sender, EventArgs e)
{
listBox1.Items.Clear();

foreach (var file in RecentlyFileHelper.GetRecentlyFiles())
{
listBox1.Items.Add(file);
}

var recentFolder = Environment.GetFolderPath(Environment.SpecialFolder.Recent);
fileSystemWatcher1.Path = recentFolder;
fileSystemWatcher1.Created += new System.IO.FileSystemEventHandler(fileSystemWatcher1_Created);
}

void fileSystemWatcher1_Created(object sender, System.IO.FileSystemEventArgs e)
{
listBox1.Items.Add(RecentlyFileHelper.GetShortcutTargetFile(e.FullPath));
}

}
}

運行後可以看到我們能準確的抓到Windows上最近所使用的文件檔案了。

最後補充一下，若想要偵測的僅僅是用Office所存取的文件，不想要偵測那麼大範圍的話，我們可以改用"%appdata%\Microsoft\Office\Recent"位置去做一樣的處理動作，它們的存放方式是一樣的。

## Link

View the list of recently opened files in Windows width C#

how to get a list of recent documents in windows 7?

Get Recent documents folder in .NET