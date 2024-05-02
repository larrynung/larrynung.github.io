---
title: "[.Net Concept]適時採用事件動態繫結來替代用If判斷作功能的啟用"
date: "2010-07-18 10:59:19"
description: "[.Net Concept]適時採用事件動態繫結來替代用If判斷作功能的啟用"
tags: [.NET Concept]
---

<p>對於程式功能的啟用，我想多半一開始大家接觸到的寫法就是用個Flag去判斷功能是否啟用，如果啟用就做某些動作，這樣的程式多半會在主要的程式邏輯中加入If判斷，這樣的寫法雖然在Flag有設的狀態才會執行主要功能，但若Flag未設定，該If判斷多少也都會對其效能造成影響，而且會讓程式的邏輯與新功能的程式混在一起，變得不易理解。因此這邊記錄一下另一種寫法，純粹是個人的小小經驗，小小體會。</p>  <p> </p>  <p>這邊簡單的來看個例子：</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c8d147a5-b8ef-4aeb-8697-593605049150" class="wlWriterSmartContent"><pre name="code" class="vb">Class Executor

    Private _enableLogData As Boolean
    Public Property EnableLogData() As Boolean
        Get
            Return _enableLogData
        End Get
        Set(ByVal value As Boolean)
            _enableLogData = value
        End Set
    End Property

    Event Executing As EventHandler
    Event Executed As EventHandler

    Protected Sub OnExecuting(ByVal e As EventArgs)
        RaiseEvent Executing(Me, e)
    End Sub

    Protected Sub OnExecuted(ByVal e As EventArgs)
        RaiseEvent Executed(Me, e)
    End Sub

    Sub GoExecute()
        For i As Integer = 1 To 100000000
            OnExecuting(New EventArgs)
            '運行動作，這邊為了看出差異，故不做動作
            If EnableLogData Then
                    '紀錄動作，這邊為了看出差異，故不做動作
            End If
            OnExecuted(New EventArgs)
        Next
    End Sub
End Class</pre></div>

<p> </p>

<p>這樣的程式若用下面程式去做測試</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e374b373-07ac-470a-8291-eafc3a9be021" class="wlWriterSmartContent"><pre name="code" class="vb">    Sub Main()
        Dim executor As New Executor
        Dim sw As Stopwatch = Stopwatch.StartNew
        executor.GoExecute()
        Console.WriteLine(sw.ElapsedMilliseconds.ToString)

        executor.EnableLogData = True
        sw.Reset()
        sw.Start()
        executor.GoExecute()
        Console.WriteLine(sw.ElapsedMilliseconds.ToString)
    End Sub</pre></div>

<p> </p>

<p>輸出的結果如下</p>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\16631\image_thumb_5.png" width="321" height="143" /> </p>

<p> </p>

<p>以這個例子來看，若換個想法改用事件動態繫結的方式去做，當啟動功能時才把功能的動作繫上，當關閉功能時把功能的動作給卸下，功能的動作就可以跟主要的邏輯分開，少了不必要的If判斷，同一個事件也可以繫上不同功能的動作。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:fd0a374a-0178-41c1-b25a-c9b44c526632" class="wlWriterSmartContent"><pre name="code" class="vb">Class Executor

    Private _enableLogData As Boolean
    Public Property EnableLogData() As Boolean
        Get
            Return _enableLogData
        End Get
        Set(ByVal value As Boolean)
            If _enableLogData &lt;&gt; value Then
                OnEnableLogDataChanging(New EventArgs)
                _enableLogData = value
                OnEnableLogDataChanged(New EventArgs)
            End If
        End Set
    End Property

    Event EnableLogDataChanging As EventHandler
    Event EnableLogDataChanged As EventHandler
    Event Executing As EventHandler
    Event Executed As EventHandler

    Protected Sub OnEnableLogDataChanging(ByVal e As EventArgs)
        RaiseEvent EnableLogDataChanging(Me, e)
    End Sub

    Protected Sub OnEnableLogDataChanged(ByVal e As EventArgs)
        RaiseEvent EnableLogDataChanged(Me, e)
    End Sub

    Protected Sub OnExecuting(ByVal e As EventArgs)
        RaiseEvent Executing(Me, e)
    End Sub

    Protected Sub OnExecuted(ByVal e As EventArgs)
        RaiseEvent Executed(Me, e)
    End Sub

    Sub GoExecute()
        For i As Integer = 1 To 100000000
            OnExecuting(New EventArgs)
            '運行動作，這邊為了看出差異，故不做動作
            OnExecuted(New EventArgs)
        Next
    End Sub

    Private Sub LogData(ByVal sender As Object, ByVal e As System.EventArgs)
        '紀錄動作，這邊為了看出差異，故不做動作        
    End Sub

    Private Sub Executor_EnableLogDataChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.EnableLogDataChanged
        RemoveHandler Executed, AddressOf LogData
        If EnableLogData Then
            AddHandler Executed, AddressOf LogData
        End If
    End Sub
End Class</pre></div>

<p><img style="border-right-width: 0px; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px" border="0" alt="image" src="\images\posts\16631\image_thumb_4.png" width="249" height="127" /></p>
