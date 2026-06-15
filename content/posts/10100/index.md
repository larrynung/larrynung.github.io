---
title: "[VB.NET].NET多語系程式(四) - 已開啟表單的語系切換"
date: "2009-08-17 09:05:45"
description: "[VB.NET].NET多語系程式(四) - 已開啟表單的語系切換"
tags: [VB.NET]
---
記得在.NET多語系程式(一)中，有提到若要切換已開啟的表單時，我們可以參考Designer.vb檔，透過ComponentResourceManager配合遞迴來作切換的動作。這邊讓我們來看一下實作方式：

'''
''' Changes the UI language.
'''
''' The form.
'''
Public Shared Sub ChangeUILanguage(ByVal form As Form)
'-------------------------------
'Author: Larry Nung Date:2008/12/11
'Memo: 參數檢查
'-------------------------------
If form Is Nothing Then
Throw New ArgumentNullException("form")
End If
'-------------------------------
'Author: Larry Nung Date:2008/12/11
'Memo: 區域變數宣告
'-------------------------------
Dim rm As ComponentResourceManager = Nothing
'-------------------------------
'Author: Larry Nung Date:2008/2/11
'Memo: 切換介面顯示的語言
'-------------------------------
Try
rm = New ComponentResourceManager(form.GetType)

For Each ctl As Control In form.Controls
ApplyControlResource(ctl, rm)
Next
Finally
rm = Nothing
End Try
End Sub

'''
''' 套用資源設定到控制項(含選單與工具列)
'''
''' The control.
''' The ComponentResourceManager.
'''
Private Shared Sub ApplyControlResource(ByRef control As Control, ByRef rm As ComponentResourceManager)
'-------------------------------
'Author: Larry Nung Date:2008/12/11
'Memo: 參數檢查
'-------------------------------
If control Is Nothing Then
Throw New ArgumentNullException("control")
End If
If rm Is Nothing Then
Throw New ArgumentNullException("rm")
End If

'-------------------------------
'Author: Larry Nung Date:2008/12/11
'Memo:
'-------------------------------
rm.ApplyResources(control, control.Name)
If TypeOf control Is MenuStrip Then
Dim menuStrip As MenuStrip = CType(control, MenuStrip)
For Each menuItem As ToolStripItem In menuStrip.Items
ApplyToolStripResource(menuItem, rm)
Next
ElseIf TypeOf control Is ToolStrip Then
Dim toolStrip As ToolStrip = CType(control, ToolStrip)
For Each toolStriptItem As ToolStripItem In toolStrip.Items
ApplyToolStripResource(toolStriptItem, rm)
Next
ElseIf control.Controls.Count > 0 Then
For Each ctrl As Control In control.Controls
ApplyControlResource(ctrl, rm)
Next
End If
End Sub

'''
''' 套用資源設定到選單或工具列
'''
''' The tool strip item.
''' The ComponentResourceManager.
'''
Private Shared Sub ApplyToolStripResource(ByRef toolStripItem As ToolStripItem, ByRef rm As ComponentResourceManager)
'-------------------------------
'Author: Larry Nung Date:2008/12/11
'Memo: 參數檢查
'-------------------------------
If toolStripItem Is Nothing Then
Throw New ArgumentNullException("toolStripItem")
End If
If rm Is Nothing Then
Throw New ArgumentNullException("rm")
End If

'-------------------------------
'Author: Larry Nung Date:2008/12/11
'Memo:
'-------------------------------
rm.ApplyResources(toolStripItem, toolStripItem.Name)
If TypeOf toolStripItem Is ToolStripMenuItem Then
Dim toolStripMenuItem As ToolStripMenuItem = CType(toolStripItem, ToolStripMenuItem)
For Each Item As ToolStripItem In toolStripMenuItem.DropDownItems
ApplyToolStripResource(Item, rm)
Next
End If
End Sub

使用時，我們先用Threading.Thread.CurrentThread.CurrentUICulture切換當前語系，再呼叫ChangeUILanguage並把要切換語系的表單參考傳入即可，像是：

System.Threading.Thread.CurrentThread.CurrentUICulture = New Globalization.CultureInfo("en")
ChangeUILanguage(Me)

執行後已開啟的視窗介面就會被切換語系了

另外還有一種切換方式是在小歐大那邊貼的連結看到的，程式較為簡單，主要是透過呼叫InitializeComponent來達成，使用上會像下面這樣：

System.Threading.Thread.CurrentThread.CurrentUICulture = New Globalization.CultureInfo("en")
For idx As Integer = Controls.Count - 1 To 0 Step -1
Controls(idx).Dispose()
Next
InitializeComponent()

雖然簡單很多，但使用上需特別注意記憶體的使用與效率。因為InitializeComponent副程式內部會建立過多物件、設定過多不需重設的屬性，且使用中的物件可能會無法被GC回收。另外還會造成畫面閃爍與介面變回初始狀態等問題。

這邊我也做了點小實驗，讓我們看看ComponentResourceManager配合遞迴來切換語系的測試程式：

System.Threading.Thread.CurrentThread.CurrentUICulture = New Globalization.CultureInfo("en")
Dim sw As Stopwatch = Stopwatch.StartNew
For i As Integer = 1 To 10000
ChangeUILanguage(Me)
Next
MsgBox(sw.ElapsedMilliseconds.ToString & "ms")

測試後所花的時間為19943ms

記憶體佔用量為19,944k

InitializeComponent切換語系的測試程式如下：

System.Threading.Thread.CurrentThread.CurrentUICulture = New Globalization.CultureInfo("en")
Dim sw As Stopwatch = Stopwatch.StartNew
For i As Integer = 1 To 10000
For idx As Integer = Controls.Count - 1 To 0 Step -1
Controls(idx).Dispose()
Next
InitializeComponent()
Next
MsgBox(sw.ElapsedMilliseconds.ToString & "ms")

測試後所花的時間為35416ms

記憶體佔用量為20,100k

記憶體佔用量差異不大，有可能會有誤差值。請自行測試判斷。