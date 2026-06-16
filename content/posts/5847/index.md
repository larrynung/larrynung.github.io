---
title: "[C#][VB.NET]Working with .NET Shortcuts"
slug: "csharp-vbnet-working-with-dotnet-shortcuts"
aliases: ["/posts/csharpvb.net.net捷徑shortcut控制/"]
date: "2008-11-02 01:53:03"
description: "Abstract Component ShortCut Type Control Method Text Edit Control Method Windows Script Host Method Control Method Shell.Application Control Method…"
tags: [CSharp,VB.NET]
---

## Abstract

* Component
* ShortCut Type
* Control Method
* Text Edit Control Method
* Windows Script Host Method Control Method
* Shell.Application Control Method
* Reference
* Download

## Component

一般來說，ShortCut主要是由下面幾個元素所構成：

1. Target
2. Working directory
3. HotKey
4. Running style
5. Description
6. Icon

![image_thumb_3.png](/images/posts/5847/image_thumb_3.png)

## ShortCut Type

1. **Url ShortCut**-Like browser 's shortcut,which extention file name is "url".
2. **Application ShortCut**-Normal application shortcut,which extention file name is "lnk".

## Control Method

1. **Text Edit**-Use to control the shortcut like browser use for.
2. **Windows Script Host (WSH)**
3. **Shell.Application**
4. **API**

## Text Edit Control Method

依照下圖格式範本建立副檔名為"url"的文字檔即可，這類型的捷徑控制只是一般的文字檔處理。

![image_thumb_1.png](/images/posts/5847/image_thumb_1.png)

若是要造Application類型的捷徑，則如下圖把"URL=http://..." 改成"URL=file:///..."即可。

![image_thumb_2.png](/images/posts/5847/image_thumb_2.png)

範例程式可參考 [C# - Creating URL shortcut to desktop 。當然你也可以不使用該範例的方法，而改透過Win32 Api去用存取Ini檔的方式來控制此種捷徑格式。](http://www.sorrowman.org/c-sharp-programmer/url-link-to-desktop.html)

## Windows Script Host Method Control Method

對於VB.NET的開發員來說。欲使用WSH，首先要利用CreateObject("WScript.Shell")建造WshShell物件。

```vb
Dim objWS As Object = CreateObject("WScript.Shell")
```

接著使用WshShell物件的CreateShortCut回傳的物件及其方法、屬性去控制捷徑。以建造捷徑為例，只要用CreateShortCut取得物件後，把要設定的值設定給對應的屬性後，呼叫該物件的Save方法即可。

```vb
With objWS.CreateShortCut(Environment.GetFolderPath(Environment.SpecialFolder.Desktop) & "\" & Replace(strEXE, ".EXE", ".LNK", 1, , 1))
    .TargetPath = objWS.ExpandEnvironmentStrings(strFolder & "\" & strEXE)
    .WorkingDirectory = strFolder
    .Description = strDesc
    .WindowStyle = 4
    .IconLocation = objWS.ExpandEnvironmentStrings(strFolder & "\" & strEXE & ",0")
    .Save()
End With
```

值得一提的是，雖然該WshShell物件的方法名稱為CreateShortCut。但是並不表示它只能用來建立捷徑，它也能用來讀取捷徑的設定。讀取時先用CreateShortCut取得物件後，直接從該物件對應的屬性去取出設定即可。

```vb
With objWS.CreateShortCut(lnkFile)
    Return .TargetPath
End With
```

P.S.C#的開發員請參考 [C#]用2种方法创建快捷方式.(Visual Studio .Net 2005)

## Shell.Application Control Method

欲使用此方法控制捷徑，如下圖所示，首先要加入Com參考"Microsoft Shell Controls And Automation"。

![image_thumb.png](/images/posts/5847/image_thumb.png)

加入參考後匯入Shell32命名空間，建立Shell物件實體，並利用Shell物件實體方法帶入檔案路徑與檔名去取得ShellLinkObject物件。

VB.NET

```vb
Dim s As New Shell
Return s.NameSpace(My.Computer.FileSystem.GetParentPath(file)).ParseName(My.Computer.FileSystem.GetName(file)).GetLink
```

C#

```csharp
Shell s = new Shell();
return (ShellLinkObject)s.NameSpace(Path.GetDirectoryName(lnkFile)).ParseName(Path.GetFileName(lnkFile)).GetLink;
```

再透過ShellLinkObject物件的屬性與方法即可對捷徑進行控制。

VB.NET

```vb
Function GetLnkArguments(ByVal shortCutFile As String) As String
    Return GetLnkObj(shortCutFile).Arguments
End Function

Function GetLnkWorkingDirectory(ByVal shortCutFile As String) As String
    Return GetLnkObj(shortCutFile).WorkingDirectory
End Function

Function GetLnkPath(ByVal shortCutFile As String) As String
    Return GetLnkObj(shortCutFile).Path
End Function
```

C#

```csharp
private String GetLnkArguments(string shortCutFile)
{
    return GetLnkObj(shortCutFile).Arguments;
}

private String GetLnkWorkingDirectory(string shortCutFile)
{
    return GetLnkObj(shortCutFile).WorkingDirectory;
}

private String GetLnkPath(string shortCutFile)
{
    return GetLnkObj(shortCutFile).Path;
}
```

這邊須注意的是，使用此方法建立捷徑時，若捷徑檔不存在於指定位置，則須先建立個空的捷徑檔案，才可取得ShellLinkObject物件。

VB.NET

```vb
If Not My.Computer.FileSystem.FileExists(shortCutFile) Then
    File.Create(shortCutFile).Close()
End If
```

C#

```csharp
if (!My.Computer.FileSystem.FileExists(shortCutFile))
{
    File.Create(shortCutFile).Close();
}
```

取得ShellLinkObject物件後，捷徑的建立與寫入也就只是設定對應的屬性值後呼叫Save方法。

VB.NET

```vb
lnkObj = GetLnkObj(shortCutFile)
With lnkObj
    .Arguments = arguments
    .Description = description
    .Path = path
    .WorkingDirectory = workingDirectory
    .ShowCommand = showCommand
    .Save()
End With
```

C#

```csharp
lnkObj = GetLnkObj(shortCutFile);
lnkObj.Arguments = arguments;
lnkObj.Description = description;
lnkObj.Path = path;
lnkObj.WorkingDirectory = workingDirectory;
lnkObj.ShowCommand = (int)showCommand;
lnkObj.Save(null);
```

## Reference

1. C# - Creating URL shortcut to desktop
2. [微軟技術社群討論區-請問如何建立桌面捷徑和網頁捷徑?](http://forums.microsoft.com/MSDN-CHT/ShowPost.aspx?PostID=713548&SiteID=14)
3. [強力鎯頭 の VB 部落-如何寫程式建立桌面捷徑 ( Shortcut )](http://blog.blueshop.com.tw/HammerChou/archive/2006/06/18/29111.aspx)
4. [Code Project-Creating Shell Links (Shortcuts) in .NET Programs Using WSH](http://www.codeproject.com/KB/dotnet/shelllink.aspx)
5. [[C#]用2种方法创建快捷方式.(Visual Studio .Net 2005)](http://www.chinadforce.com/viewthread.php?tid=941624&highlight=)

## Download

[ShortCut.rar](http://Files.Dotblogs.com.tw/larrynung/0901/200912612193547.rar)
