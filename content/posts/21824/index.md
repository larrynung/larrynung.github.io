---
title: "[C#]Everything SDK"
slug: "[CSharp]Everything SDK"
date: "2011-03-14 12:51:09"
description: "[C#]Everything SDK"
tags: [CSharp]
---
用過Everything也好一陣子了，一直以來都對他的快速搜尋有相當深刻的印象，但也只限於當作搜尋的工具之用，看了保哥介紹好用工具：Everything search engine (檔名搜尋工具)的這篇，發現原來該套軟體也有SDK可以使用，可藉由他的強大搜尋功能用來開發自己的工具，花點時間試著玩了一下，順手記錄一下。

SDK可在Download Everything這邊下載，內含C與C#的範例程式、DLL檔、以及C開發要用的標頭檔之類的檔案。Everything提供的是IPC類型的API，API的使用可參閱SDK - Wiki。這邊需注意到由於是IPC類型的API，故在使用時需確保Everything程式有被開啟。另外就是要確認SDK內的dll\Everything.dll是否有跟自己開發的程式放在一起。

為方便使用，這邊我又將API包了一層，除了一些控制搜尋的屬性外，最主要的就是Search方法，可提供搜尋我們所感興趣的資料：

```

using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Text;

namespace Everything
{
/// <summary>
///  /// </summary>
public class EverythingAPI
{
#region Const
const string EVERYTHING_DLL_;
#endregion

#region DllImport
[DllImport(EVERYTHING_DLL_NAME)]
private static extern int Everything_SetSearch(string lpSearchString);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern void Everything_SetMatchPath(bool bEnable);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern void Everything_SetMatchCase(bool bEnable);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern void Everything_SetMatchWholeWord(bool bEnable);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern void Everything_SetRegex(bool bEnable);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern void Everything_SetMax(int dwMax);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern void Everything_SetOffset(int dwOffset);

[DllImport(EVERYTHING_DLL_NAME)]
private static extern bool Everything_GetMatchPath();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern bool Everything_GetMatchCase();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern bool Everything_GetMatchWholeWord();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern bool Everything_GetRegex();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern UInt32 Everything_GetMax();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern UInt32 Everything_GetOffset();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern string Everything_GetSearch();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern StateCode Everything_GetLastError();

[DllImport(EVERYTHING_DLL_NAME)]
private static extern bool Everything_Query();

[DllImport(EVERYTHING_DLL_NAME)]
private static extern void Everything_SortResultsByPath();

[DllImport(EVERYTHING_DLL_NAME)]
private static extern int Everything_GetNumFileResults();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern int Everything_GetNumFolderResults();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern int Everything_GetNumResults();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern int Everything_GetTotFileResults();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern int Everything_GetTotFolderResults();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern int Everything_GetTotResults();
[DllImport(EVERYTHING_DLL_NAME)]
private static extern bool Everything_IsVolumeResult(int nIndex);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern bool Everything_IsFolderResult(int nIndex);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern bool Everything_IsFileResult(int nIndex);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern void Everything_GetResultFullPathName(int nIndex, StringBuilder lpString, int nMaxCount);
[DllImport(EVERYTHING_DLL_NAME)]
private static extern void Everything_Reset();
#endregion

#region Enum
enum StateCode
{
OK,
MemoryError,
IPCError,
RegisterClassExError,
CreateWindowError,
CreateThreadError,
InvalidIndexError,
InvalidCallError
}
#endregion

#region Property

/// <summary>
/// Gets or sets a value indicating whether [match path].
/// </summary>
/// <value><c>true</c> if [match path]; otherwise, <c>false</c>.</value>
public Boolean MatchPath  {
get
{
return Everything_GetMatchPath();
}
set
{
Everything_SetMatchPath(value);
}
}

/// <summary>
/// Gets or sets a value indicating whether [match case].
/// </summary>
/// <value><c>true</c> if [match case]; otherwise, <c>false</c>.</value>
public Boolean MatchCase  {
get
{
return Everything_GetMatchCase();
}
set
{
Everything_SetMatchCase(value);
}
}

/// <summary>
/// Gets or sets a value indicating whether [match whole word].
/// </summary>
/// <value><c>true</c> if [match whole word]; otherwise, <c>false</c>.</value>
public Boolean MatchWholeWord  {
get
{
return Everything_GetMatchWholeWord();
}
set
{
Everything_SetMatchWholeWord(value);
}
}

/// <summary>
/// Gets or sets a value indicating whether [enable regex].
/// </summary>
/// <value><c>true</c> if [enable regex]; otherwise, <c>false</c>.</value>
public Boolean EnableRegex  {
get
{
return Everything_GetRegex();
}
set
{
Everything_SetRegex(value);
}
}
#endregion

#region Public Method
/// <summary>
/// Resets this instance.
/// </summary>
public void Reset()
{
Everything_Reset();
}

/// <summary>
/// Searches the specified key word.
/// </summary>
/// <param>The key word.</param>
/// <returns></returns>
public IEnumerable<string> Search(string keyWord)
{
return Search(keyWord, 0, int.MaxValue);
}

/// <summary>
/// Searches the specified key word.
/// </summary>
/// <param>The key word.</param>
/// <param>The offset.</param>
/// <param>The max count.</param>
/// <returns></returns>
public IEnumerable<string> Search(string keyWord,int offset,int maxCount)
{
if (string.IsNullOrEmpty(keyWord))
throw new ArgumentNullException("keyWord");

if (offset < 0)
throw new ArgumentOutOfRangeException("offset");

if (maxCount < 0)
throw new ArgumentOutOfRangeException("maxCount");

Everything_SetSearch(keyWord);
Everything_SetOffset(offset);
Everything_SetMax(maxCount);
if (!Everything_Query())
{
switch (Everything_GetLastError())
{
case StateCode.CreateThreadError:
throw new CreateThreadException();
case StateCode.CreateWindowError:
throw new CreateWindowException();
case StateCode.InvalidCallError:
throw new InvalidCallException();
case StateCode.InvalidIndexError:
throw new InvalidIndexException();
case StateCode.IPCError:
throw new IPCErrorException();
case StateCode.MemoryError:
throw new MemoryErrorException();
case StateCode.RegisterClassExError:
throw new RegisterClassExException();
}
yield break;
}

const int buffer
StringBuilder buffer = new StringBuilder(bufferSize);
for (int idx = 0; idx < Everything_GetNumResults(); ++idx)
{
Everything_GetResultFullPathName(idx, buffer, bufferSize);
yield return buffer.ToString();
}
}
#endregion
}

/// <summary>
///  /// </summary>
public class MemoryErrorException:ApplicationException  {
}

/// <summary>
///  /// </summary>
public class IPCErrorException : ApplicationException
{
}

/// <summary>
///  /// </summary>
public class RegisterClassExException : ApplicationException
{
}

/// <summary>
///  /// </summary>
public class CreateWindowException : ApplicationException
{
}

/// <summary>
///  /// </summary>
public class CreateThreadException : ApplicationException
{
}

/// <summary>
///  /// </summary>
public class InvalidIndexException : ApplicationException
{
}

/// <summary>
///  /// </summary>
public class InvalidCallException : ApplicationException
{
}

}
```

使用上會像這個樣子：

```

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Linq;
using Everything;

namespace WindowsApplication1
{
public partial class Form1 : Form
{
public Form1()
{
InitializeComponent();
}

private void button1_Click(object sender, EventArgs e)
{
EverythingAPI everyThingAPI = new EverythingAPI();
var results = everyThingAPI.Search(textBox1.Text);

Text = textBox1.Text + " - " + results.Count() + " Results";

listBox1.Items.Clear();
foreach (var item in results)
{
listBox1.Items.Add(item);
}
}
}
}
```

運行結果如下：

![image_thumb.png](/images/posts/21824/image_thumb.png)

##
Download

Everything_SDK_Demo.rar

##
Link

-
SDK - Wiki
-
Download Everything
-
介紹好用工具：Everything search engine (檔名搜尋工具)