---
title: "[VB.NET]利用反射載入並運行資源檔中的組件"
date: "2010-06-02 11:39:32"
description: "[VB.NET]利用反射載入並運行資源檔中的組件"
tags: [VB.NET]
---要載入並運行資源檔中的組件，最簡單的方法就是開個新的專案，把要真正要執行的組件加入資源檔中。

再用Assembly.Load載入組件後，呼叫EntryPoint.Invoke去執行組件即可。

Imports System.IO
Imports System.Reflection

Module MainModule

_
Public Sub main(ByVal args() As String)
Assembly.Load(My.Resources.ColorPicker).EntryPoint.Invoke(Nothing, New Object() {args})
End Sub
End Module

同樣的概念，其實放在資源檔中的組件可以先經過壓縮處理，再放入資源檔中。載入時只要先經過解壓縮的動作，把要執行的組件從壓縮中解出，就可以執行了。

Imports System.IO
Imports System.Reflection
Imports ICSharpCode.SharpZipLib.Zip

Module MainModule

_
Public Sub main(ByVal args() As String)
Using compressedMS As New MemoryStream(My.Resources.ColorPicker)
Dim zf As New ZipFile(compressedMS)
Dim ze As ZipEntry = zf.GetEntry("ColorPicker.exe")
Dim zs As Stream = zf.GetInputStream(ze)
Dim buffer(ze.Size - 1) As Byte
zs.Read(buffer, 0, buffer.Length - 1)
Assembly.Load(buffer).EntryPoint.Invoke(Nothing, New Object() {args})
End Using
End Sub
End Module

那若是放在資源檔中的組件需要參考多個組件呢?這邊借用小朱大的PLURK小圈圈管理工具來作實驗，我們可以把所有需要的組件壓縮成一個壓縮檔後，同樣也把它放入資源檔中。

利用CurrentDomain.AssemblyResolve事件，從壓縮中取出欲執行的組件會參考到的組件，把Assembly.Load載入的組件回傳就可以了。

Imports System.IO
Imports System.Reflection
Imports ICSharpCode.SharpZipLib.Zip

Module MainModule

Private Function GetAssembly(ByVal assemblyName As String) As Assembly
Using compressedMS As New MemoryStream(My.Resources.CliqueManager)
Dim zf As New ZipFile(compressedMS)
Dim ze As ZipEntry = zf.GetEntry(assemblyName)
Dim zs As Stream = zf.GetInputStream(ze)
Dim buffer(ze.Size - 1) As Byte
zs.Read(buffer, 0, buffer.Length - 1)
Return Assembly.Load(buffer)
End Using
End Function

_
Public Sub main(ByVal args() As String)
Dim currentDomain As AppDomain = AppDomain.CurrentDomain
AddHandler currentDomain.AssemblyResolve, AddressOf currentDomain_AssemblyResolve

GetAssembly("CliqueManager.exe").EntryPoint.Invoke(Nothing, Nothing)
End Sub

Private Function currentDomain_AssemblyResolve(ByVal sender As Object, ByVal e As ResolveEventArgs) As Assembly
Return GetAssembly(e.Name.Substring(0, e.Name.IndexOf(","c)) & ".dll")
End Function
End Module

以此例子來看，處理下來最後檔案總容量會變為執行檔195KB與壓縮組件196KB，共391KB，檔案大小會變得比較小，佈署的組件數量也會比較少。

## Download

ExecuteAssemblyFromResource.zip