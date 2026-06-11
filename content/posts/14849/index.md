---
title: "[Extension Method][VB.NET]ErrorProvider.GerErrorMsgs & ErrorProvider.HasError"
date: "2010-04-26 11:37:16"
description: "[Extension Method][VB.NET]ErrorProvider.GerErrorMsgs & ErrorProvider.HasError"
tags: [VB.NET]
---

GetErrorMsgs擴充方法可找出介面上所有有用ErrorProvider顯示的錯誤訊息，HasError可以判斷介面上是否有任何用ErrorProvider顯示的錯誤訊息，程式碼如下：
```
Imports System.Runtime.CompilerServices
Imports System.Windows.Forms

Public Module ErrorProviderExtension

_
Public Function GetErrorMsgs(ByVal ep As ErrorProvider) As String()
If ep.ContainerControl Is Nothing Then
Return New String() {}
End If
Dim linq = From c In ep.ContainerControl.Controls Let msg = ep.GetError(c) Where msg.Length > 0 Select msg
Return linq.ToArray
End Function

_
Public Function HasError(ByVal ep As ErrorProvider) As Boolean
Return ep.GetErrorMsgs.Length > 0
End Function

End Module
```
可以用在設定表單關閉時，判斷是否有未填寫正確的資料。
```
Private Sub btnOK_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnOK.Click
Dim errorMsgs() As String = ErrorProvider1.GetErrorMsgs
If errorMsgs.Length > 0 Then
MsgBox(String.Join(vbCrLf, errorMsgs))
Return
End If
End Sub
```