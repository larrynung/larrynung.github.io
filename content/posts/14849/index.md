---
title: "[Extension Method][VB.NET]ErrorProvider.GerErrorMsgs amp; ErrorProvider.HasError"
date: "2010-04-26 11:37:16"
description: "[Extension Method][VB.NET]ErrorProvider.GerErrorMsgs &amp; ErrorProvider.HasError"
tags: [VB.NET]
---

<p>GetErrorMsgs擴充方法可找出介面上所有有用ErrorProvider顯示的錯誤訊息，HasError可以判斷介面上是否有任何用ErrorProvider顯示的錯誤訊息，程式碼如下：</p>  <p />  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ad77281c-91f3-4d75-923b-e1b07ca12895" class="wlWriterEditableSmartContent"><pre name="code" class="vb">
Imports System.Runtime.CompilerServices 
Imports System.Windows.Forms 

Public Module ErrorProviderExtension 

    &lt;Extension()&gt; _ 
    Public Function GetErrorMsgs(ByVal ep As ErrorProvider) As String() 
        If ep.ContainerControl Is Nothing Then 
            Return New String() {} 
        End If 
        Dim linq = From c In ep.ContainerControl.Controls Let msg = ep.GetError(c) Where msg.Length &gt; 0 Select msg 
        Return linq.ToArray 
    End Function 

    &lt;Extension()&gt; _ 
    Public Function HasError(ByVal ep As ErrorProvider) As Boolean 
        Return ep.GetErrorMsgs.Length &gt; 0 
    End Function 

End Module
</pre></div>

<p />

<p> </p>

<p>可以用在設定表單關閉時，判斷是否有未填寫正確的資料。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:b0da6a7b-98bd-4cd5-8006-a74d20064796" class="wlWriterEditableSmartContent"><pre name="code" class="vb">    Private Sub btnOK_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnOK.Click
        Dim errorMsgs() As String = ErrorProvider1.GetErrorMsgs
        If errorMsgs.Length &gt; 0 Then
            MsgBox(String.Join(vbCrLf, errorMsgs))
            Return
        End If
    End Sub</pre></div>
