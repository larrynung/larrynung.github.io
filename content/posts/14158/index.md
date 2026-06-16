---
title: "[VB.NET]用FindExecutable API取得開啟文件用的執行檔位置"
date: "2010-03-22 04:53:06"
description: "FindExecutable API可用來取得開啟文件用的執行檔位置，像是Doc檔就用Word開啟、Pdf檔就用Adobe開啟，這道API就是可以找到開啟文件用的執行檔位置。"
tags: [VB.NET]
---

FindExecutable  API可用來取得開啟文件用的執行檔位置，像是Doc檔就用Word開啟、Pdf檔就用Adobe開啟，這道API就是可以找到開啟文件用的執行檔位置。

該API的函式原型如下：

```
HINSTANCE FindExecutable(
  __in      LPCTSTR lpFile,
  __in_opt  LPCTSTR lpDirectory,
  __out     LPTSTR lpResult
);
```

在VB.NET可像下面這樣宣告該API

```vb
    <Runtime.InteropServices.DllImport("shell32.DLL", EntryPoint:="FindExecutable")> _
Private Shared Function FindExecutable(ByVal lpFile As String, ByVal lpDirectory As String, ByVal lpResult As StringBuilder) As Integer
    End Function
```

傳入文件路徑、 預設目錄、與存放開啟用執行檔位置的變數即可。值得注意的是，該API的回傳值若大於32，則表示該API執行無誤。若回傳的值小於32，則有可能是檔案找不到、文件類型未設定預設開啟的執行檔、或是記憶體不足等。

<table border="1" cellpadding="2" cellspacing="0" width="400"><tbody>
<tr>
<td valign="top" width="200">SE_ERR_FNF (2)</td>
<td valign="top" width="200">指定的檔案不存在</td>
</tr>
<tr>
<td valign="top" width="200">SE_ERR_NOASSOC (31)</td>
<td valign="top" width="200">沒有對應用來開啟的執行檔</td>
</tr>
<tr>
<td valign="top" width="200">SE_ERR_OOM (8)</td>
<td valign="top" width="200">Windows XP only. 系統記憶體資源不足</td>
</tr>
</tbody></table>

為方便使用該API，可整理成下面類別

```vb
Imports System.Runtime.InteropServices
Imports System.Text
Imports System.IO

Public Class NoAssociatedFileTypeException
    Inherits ApplicationException

End Class

Public Class Win32API
    Const SE_ERR_FNF As Integer = 2
    Const SE_ERR_OOM As Integer = 8
    Const SE_ERR_NOASSOC As Integer = 31

    <Runtime.InteropServices.DllImport("shell32.DLL", EntryPoint:="FindExecutable")> _
Private Shared Function FindExecutable(ByVal lpFile As String, ByVal lpDirectory As String, ByVal lpResult As StringBuilder) As Integer
    End Function

    Public Shared Function GetAssociatedExeFile(ByVal file As String, Optional ByVal throwException As Boolean = True) As String
        Dim sb As New StringBuilder(512)
        Dim result As Integer = FindExecutable(file, Nothing, sb)
        If result > 32 Then
            Return sb.ToString
        Else
            If Not throwException Then
                Return String.Empty
            End If
            Select Case result
                Case SE_ERR_FNF
                    Throw New FileNotFoundException
                Case SE_ERR_NOASSOC
                    Throw New NoAssociatedFileTypeException
                Case SE_ERR_OOM
                    Throw New OutOfMemoryException
            End Select
            Throw New Exception
        End If
    End Function
End Class
```

或整理成擴充FileInfo類別的方法

```vb
Imports System.Runtime.CompilerServices
Imports System.Runtime.InteropServices
Imports System.Text
Imports System.IO

Public Class NoAssociatedFileTypeException
    Inherits ApplicationException

End Class

Module FileInfoExtension
    Const SE_ERR_FNF As Integer = 2
    Const SE_ERR_OOM As Integer = 8
    Const SE_ERR_NOASSOC As Integer = 31

    <Runtime.InteropServices.DllImport("shell32.DLL", EntryPoint:="FindExecutable")> _
Private Function FindExecutable(ByVal lpFile As String, ByVal lpDirectory As String, ByVal lpResult As StringBuilder) As Integer
    End Function

    <Extension()> _
    Public Function GetAssociatedExeFile(ByVal fileInfo As FileInfo, Optional ByVal throwException As Boolean = True) As String
        Dim sb As New StringBuilder(512)
        Dim result As Integer = FindExecutable(fileInfo.FullName, Nothing, sb)
        If result > 32 Then
            Return sb.ToString
        Else
            If Not throwException Then
                Return String.Empty
            End If
            Select Case result
                Case SE_ERR_FNF
                    Throw New FileNotFoundException
                Case SE_ERR_NOASSOC
                    Throw New NoAssociatedFileTypeException
                Case SE_ERR_OOM
                    Throw New OutOfMemoryException
            End Select
            Throw New Exception
        End If
    End Function
End Module
```

使用上就會像下面這樣：

```vb
Dim associatedExeFile As String = My.Computer.FileSystem.GetFileInfo("C:\Test.Doc").GetAssociatedExeFile
```

## Link

* FindExecutable Function
* myFindExecutable 函數
* FindExecutable (shell32)
