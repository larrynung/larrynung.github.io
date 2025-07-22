---
title: "[C#][VB.NET]自定義例外對話框"
slug: "[CSharp][VB.NET]自定義例外對話框"
date: "2013-11-06 12:00:00"
description: "[C#][VB.NET]自定義例外對話框"
tags: [CSharp]
---

之前在『例外處理使用時機』這篇有提到我目前很少會寫例外處理。除了在那篇提到的原因之外，還有個因素就是我會弄個自定義的例外處理視窗，讓使用者在例外發生時，可以匯出例外訊息並提供給開發人員。有了匯出的例外訊息，我們就可以很快的把未處理完的例外(指給程式員看的例外)給修正。  
要做到自定義的例外對話框，我們需要利用Application.ThreadException事件。
  
先讓我們看一下MSDN的說明：

從MSDN的說明可以很清楚的看到，當執行緒發生例外，且該例外未被處理，則該事件即會觸發。

接著就讓我們來看看如何才能利用該事件做出自定義的例外對話框。首先，我們需要設計自定義的例外對話框。

接著撰寫繫上事件用的副程式。
  
VB.NET

C#

最後寫上事件觸發時要執行的事件處理函式。

VB.NET

C#

到此一個簡單的自定義例外對話框就完成了。使用上，我們只需呼叫剛寫的繫上事件用副程式即可。

VB.NET

C#

完整程式碼：

VB.NET

C#

執行畫面如下：

## Conclusion

透過Application.ThreadException事件，我們可以很容易達到該篇的效果。但需注意這樣的作法只對繫上的執行緒有效，非繫上的執行緒若發生例外，將無法截取到。在實際應用上，也可依自己需求加入記錄到事件記錄簿等功能，甚至可以使用.NET預設的例外視窗來顯示，只是多加了一些自己的處理，讓使用者感覺不出差異。

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        AddHandler Application.ThreadException, AddressOf Application_ThreadException
        ...
    End Sub

    Private Sub Application_ThreadException(ByVal sender As Object, ByVal e As ThreadExceptionEventArgs)
        ... 
        Dim exceptionDlg As New ThreadExceptionDialog(e.Exception)
        exceptionDlg.ShowDialog()
    End Sub

另外，若有興趣的也可以改繫上AppDomain.UnhandledException試看看。

## Download

ExceptionDlg.zip