---
title: "[.NET Concept]使用BeginXXX/EndXXX與SuspendLayout/ResumeLayout時，考慮加上Try/Finally"
date: "2010-07-18 12:48:29"
description: "[.NET Concept]使用BeginXXX/EndXXX與SuspendLayout/ResumeLayout時，考慮加上Try/Finally"
tags: [.NET Concept]
---

相信大家都知道當在更新介面時，有的控制項會提供BeginUpdate/EndUpdate，甚至是BeginEdit/EndEdit、BeginInit/EndInit、SuspendLayout/ResumeLayout等暫停更新的方法，可用以加速介面的更新動作。像是ComboBox控制像就有這類方法：
          ComboBox1.BeginUpdate()
        For i As Integer = 1 To 10000
            ComboBox1.Items.Add(i.ToString)
        Next
        ComboBox1.EndUpdate()

但若是未使用Try/Finally包住，當程式在呼叫EndUpdate前被莫名的原因中斷，像是例外發生。

        ComboBox1.BeginUpdate()
        ...
        Throw New Exception
        ...
        ComboBox1.EndUpdate()

此時微軟預設的例外對話框會跳出，若使用者不願跳出系統因而按下繼續按鈕。

或是您自行處理了一些事件把預設的例外框給取消掉。

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        AddHandler Application.ThreadException, AddressOf Application_ThreadException
        ...
        ComboBox1.BeginUpdate()
        ...
        Throw New Exception
        ...
        ComboBox1.EndUpdate()
    End Sub

    Private Sub Application_ThreadException(ByVal sender As Object, ByVal e As EventArgs)
        ...
    End Sub

整個介面在更新上就會出問題。

要避免這樣的問題，必須養成適時為這些程式加上Try/Finally的好習慣，如此當中斷發生時就能確保介面仍能正常更新。

        Try
            ComboBox1.BeginUpdate()
            ...
            Throw New Exception
            ...
        Finally
            ComboBox1.EndUpdate()
        End Try