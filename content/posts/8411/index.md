---
title: "[Library][VB.NET].NET簡易測試用表單類別"
date: "2009-05-15 08:58:32"
description: "[Library][VB.NET].NET簡易測試用表單類別"
tags: [VB.NET,Library]
---

## Introduction

在撰寫程式時，我們時常會需要撰寫一些測試程式、或是需要顯示一些資料。多半這時我們會設計一些測試用的表單介面來使用。這些介面多半是很簡單的介面，設計上也大同小異，所以我們可以把這些表單介面整理起來方便以後重覆使用。

本篇介紹簡易測試用表單類別的寫法。這些表單具備任意組合使用的能力。

## 測試用表單類別

測試用表單類別的Code如下：

```
#Region "Imports"
Imports System.Windows.Forms
Imports System.Drawing
#End Region

'|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'Author: Larry Nung
'Date: 2009/5/13
'File:
'Memo:
'|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
''' <summary>
'''
''' </summary>
''' <remarks></remarks>
Friend Class TestForm

#Region "Public Shared Method"

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/14
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="dataSource"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowGridDlg(ByVal dataSource As DataTable) As DialogResult
        Return ShowGridDlg(String.Empty, dataSource)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/14
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="dataSource"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowGridDlg(ByVal title As String, ByVal dataSource As DataTable) As DialogResult
        Dim grid As New DataGridView
        Dim btnOk As New Button

        With grid
            .DataSource = dataSource
            .Dock = DockStyle.Fill
        End With

        With btnOk
            .Text = "OK"
            .Dock = DockStyle.Bottom
            .DialogResult = Windows.Forms.DialogResult.OK
        End With

        Return ShowForm(title, grid, btnOk)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/14
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="items"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowListDlg(ByVal items As ICollection) As DialogResult
        Return ShowListDlg(String.Empty, items)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/14
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="items"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowListDlg(ByVal title As String, ByVal items As ICollection) As DialogResult
        Dim lstbox As New ListBox

        With lstbox
            .BeginUpdate()
            .SelectionMode = SelectionMode.None
            For Each item In items
                .Items.Add(item)
            Next
            .Dock = DockStyle.Fill
            .EndUpdate()
        End With

        Return ShowForm(title, lstbox)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/13
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="obj"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowPropertySettingDlg(ByVal obj As Object) As DialogResult
        Return ShowPropertySettingDlg(obj.ToString, obj)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/13
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="obj"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowPropertySettingDlg(ByVal title As String, ByVal obj As Object) As DialogResult
        Dim prop As New PropertyGrid
        Dim btnOk As New Button

        With prop
            .SelectedObject = obj
            .Dock = DockStyle.Fill
        End With

        With btnOk
            .Text = "OK"
            .Dock = DockStyle.Bottom
            .DialogResult = Windows.Forms.DialogResult.OK
        End With

        Return ShowForm(title, prop, btnOk)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/13
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="items"></param>
    ''' <param name="selectedIdx"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowListSelectDlg(ByVal items As ICollection, ByRef selectedIdx As Integer) As DialogResult
        Return ShowListSelectDlg(String.Empty, items, selectedIdx)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/13
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="items"></param>
    ''' <param name="selectedIdx"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowListSelectDlg(ByVal title As String, ByVal items As ICollection, ByRef selectedIdx As Integer) As DialogResult
        Return ShowListSelectDlg(title, items, Nothing, selectedIdx)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/13
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="items"></param>
    ''' <param name="selectedItem"></param>
    ''' <param name="selectedIdx"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowListSelectDlg(ByVal items As ICollection, Optional ByRef selectedItem As Object = Nothing, Optional ByRef selectedIdx As Integer = -1) As DialogResult
        Return ShowListSelectDlg(String.Empty, items, selectedItem, selectedIdx)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/14
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="items"></param>
    ''' <param name="selectedItem"></param>
    ''' <param name="selectedIdx"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowListSelectDlg(ByVal title As String, ByVal items As ICollection, Optional ByRef selectedItem As Object = Nothing, Optional ByRef selectedIdx As Integer = -1) As DialogResult
        Dim lstbox As New ListBox
        Dim btnOk As New Button
        Dim btnCancel As New Button

        With lstbox
            .BeginUpdate()
            .SelectionMode = SelectionMode.One
            For Each item In items
                .Items.Add(item)
            Next
            .SelectedIndex = 0
            .Dock = DockStyle.Fill
            .EndUpdate()
        End With
        AddHandler lstbox.DoubleClick, Function(sender As Object, e As EventArgs) CallByName(btnOk, "PerformClick", CallType.Method, Nothing)

        With btnOk
            .Text = "OK"
            .Dock = DockStyle.Bottom
            .DialogResult = Windows.Forms.DialogResult.OK
        End With

        With btnCancel
            .Text = "Cancel"
            .Dock = DockStyle.Bottom
            .DialogResult = Windows.Forms.DialogResult.Cancel
        End With

        ShowListSelectDlg = ShowForm(title, lstbox, btnOk, btnCancel)

        With lstbox
            selectedItem = .SelectedItem
            selectedIdx = .SelectedIndex
        End With
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/14
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="file"></param>
    ''' <remarks></remarks>
    Public Shared Sub ShowChart(ByVal file As String)
        ShowChart(String.Empty, file)
    End Sub

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/14
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="file"></param>
    ''' <remarks></remarks>
    Public Shared Sub ShowChart(ByVal title As String, ByVal file As String)
        ShowChart(title, New Bitmap(file))
    End Sub

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/12
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="chart"></param>
    ''' <remarks></remarks>
    Public Shared Sub ShowChart(ByVal chart As Image)
        ShowChart(String.Empty, chart)
    End Sub

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/12
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="chart"></param>
    ''' <remarks></remarks>
    Public Shared Sub ShowChart(ByVal title As String, ByVal chart As Image)
        Dim p As New PictureBox
        Dim btnOk As New Button

        With p
            .Image = chart
            .Dock = DockStyle.Fill
            .SizeMode = PictureBoxSizeMode.Zoom
        End With

        With btnOk
            .Text = "OK"
            .Dock = DockStyle.Bottom
            .DialogResult = Windows.Forms.DialogResult.OK
        End With

        ShowForm(title, p, btnOk)
    End Sub

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/12
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="msg"></param>
    ''' <remarks></remarks>
    Public Shared Sub ShowMsg(ByVal msg As String)
        ShowMsg(String.Empty, msg)
    End Sub

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/12
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="msg"></param>
    ''' <remarks></remarks>
    Public Shared Sub ShowMsg(ByVal title As String, ByVal msg As String)
        Dim tbx As New TextBox
        Dim btnOk As New Button

        With tbx
            .Multiline = True
            .Dock = DockStyle.Fill
            .ReadOnly = True
            .BackColor = Color.White
            .Text = msg
        End With

        With btnOk
            .Text = "OK"
            .Dock = DockStyle.Bottom
            .DialogResult = Windows.Forms.DialogResult.OK
        End With

        ShowForm(title, tbx)
    End Sub

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/12
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="controls"></param>
    ''' <remarks></remarks>
    Public Shared Function ShowForm(ByVal ParamArray controls() As Control) As DialogResult
        Return ShowForm(String.Empty, controls)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/13
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="width"></param>
    ''' <param name="height"></param>
    ''' <param name="controls"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowForm(ByVal width As Integer, ByVal height As Integer, ByVal ParamArray controls() As Control) As DialogResult
        Return ShowForm(String.Empty, width, height, controls)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/12
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="controls"></param>
    ''' <remarks></remarks>
    Public Shared Function ShowForm(ByVal title As String, ByVal ParamArray controls() As Control) As DialogResult
        Return ShowForm(title, 300, 300, controls)
    End Function

    '***************************************************************************
    'Author: Larry Nung
    'Date: 2009/5/13
    'Purpose:
    'Memo:
    '***************************************************************************
    ''' <summary>
    '''
    ''' </summary>
    ''' <param name="title"></param>
    ''' <param name="width"></param>
    ''' <param name="height"></param>
    ''' <param name="controls"></param>
    ''' <returns></returns>
    ''' <remarks></remarks>
    Public Shared Function ShowForm(ByVal title As String, ByVal width As Integer, ByVal height As Integer, ByVal ParamArray controls() As Control) As DialogResult
        Dim f As New Form
        With f
            .SuspendLayout()
            .Width = width
            .Height = height
            .Text = title
            .Controls.AddRange(controls)
            .ResumeLayout()
            Return .ShowDialog()
        End With
    End Function

#End Region

End Class
```

## 測試用表單畫面

**秀圖界面**

![image_thumb.png](/images/posts/8411/image_thumb.png)

**訊息界面**

![image_thumb_1.png](/images/posts/8411/image_thumb_1.png)

**清單界面**

![image_thumb_2.png](/images/posts/8411/image_thumb_2.png)

**選取界面**

![image_thumb_3.png](/images/posts/8411/image_thumb_3.png)

**屬性界面**

![image_thumb_4.png](/images/posts/8411/image_thumb_4.png)

**表格界面**

![image_thumb_5.png](/images/posts/8411/image_thumb_5.png)

## 使用範例

![image_thumb_6.png](/images/posts/8411/image_thumb_6.png)

使用範例如下：

```
Public Class Form1

    Private Sub btnShowPhoto_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnShowPhoto.Click
        Dim openDlg As New OpenFileDialog
        openDlg.Filter = "Photo file|*.bmp;*.jpg"
        If openDlg.ShowDialog = Windows.Forms.DialogResult.OK Then
            TestForm.ShowChart("Photo", openDlg.FileName)
        End If
    End Sub

    Private Sub btnShowFile_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnShowFile.Click
        Dim openDlg As New OpenFileDialog
        openDlg.Filter = "Text file|*.txt"
        If openDlg.ShowDialog = Windows.Forms.DialogResult.OK Then
            TestForm.ShowMsg("Text", My.Computer.FileSystem.ReadAllText(openDlg.FileName))
        End If
    End Sub

    Private Sub btnShowFileContent_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnShowFileContent.Click
        Dim selectedItem As Object = Nothing
        Dim folderDlg As New FolderBrowserDialog
        If folderDlg.ShowDialog = Windows.Forms.DialogResult.OK Then
            If TestForm.ShowListSelectDlg("Select File", My.Computer.FileSystem.GetFiles(folderDlg.SelectedPath, FileIO.SearchOption.SearchTopLevelOnly, "*.txt"), selectedItem) = Windows.Forms.DialogResult.OK Then
                TestForm.ShowMsg(My.Computer.FileSystem.ReadAllText(selectedItem.ToString))
            End If
        End If
    End Sub

    Private Sub btnSetProperty_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSetProperty.Click
        TestForm.ShowPropertySettingDlg(Me)
    End Sub

    Private Sub btnShowFileList_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnShowFileList.Click
        Dim folderDlg As New FolderBrowserDialog
        If folderDlg.ShowDialog = Windows.Forms.DialogResult.OK Then
            TestForm.ShowListDlg(My.Computer.FileSystem.GetFiles(folderDlg.SelectedPath))
        End If
    End Sub

    Private Sub btnShowGrid_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnShowGrid.Click
        Dim dt As New DataTable
        dt.Columns.Add()
        TestForm.ShowGridDlg(dt)
    End Sub
End Class
```
