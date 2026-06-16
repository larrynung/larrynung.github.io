---
title: "[VB.NET]Update Changed DataGridView Data with MyDataBase"
slug: "vbnet-update-changed-datagridview-data-with-mydatabase"
aliases: ["/posts/8783/"]
date: "2009-06-11 12:39:37"
description: "Introduction 這陣子碰到許多網友再問如何用Update更新資料到資料庫。為回答網友的提問，用MyDataBase偷懶的寫了一個範例程式。主要功能是把DataGridView上更動的資料寫回資料庫。在此隨手記錄一下。 欲看Update的寫法可參考MyDataBase原始碼。"
tags: [VB.NET]
---

## Introduction

這陣子碰到許多網友再問如何用Update更新資料到資料庫。為回答網友的提問，用MyDataBase偷懶的寫了一個範例程式。主要功能是把DataGridView上更動的資料寫回資料庫。在此隨手記錄一下。

欲看Update的寫法可參考MyDataBase原始碼。需注意的是，MyDataBase內部所用的Command是用自動產生的，在效能上會較直接指定Command來得差，參考看看就好。

## 範例

![image_thumb.png](/images/posts/8783/image_thumb.png)

VB.NET

```
Public Class Form1

    Dim dbA As New UseDB.AccessDB("A.mdb")
    Dim dbB As New UseDB.AccessDB("B.mdb")

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        LoadADB()
        LoadBDB()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        WriteToDB(dbA)
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        LoadADB()
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        WriteToDB(dbB)
    End Sub

    Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
        LoadBDB()
    End Sub

    Private Sub LoadADB()
        Me.DataGridView1.DataSource = dbA.GetDataTable("Select * from test")
    End Sub

    Private Sub LoadBDB()
        Me.DataGridView2.DataSource = dbB.GetDataTable("Select * from test")
    End Sub

    Private Sub WriteToDB(ByVal db As UseDB.AccessDB)
        Dim table As DataTable = DirectCast(Me.DataGridView1.DataSource, DataTable)
        Dim changeTable As DataTable = table.GetChanges
        If changeTable Is Nothing Then
            MsgBox("Without Change")
            Return
        End If
        db.WriteDataFromDataTable(changeTable, "Test")
        table.AcceptChanges()
        If db Is dbA Then
            LoadADB()
        Else
            LoadBDB()
        End If
    End Sub
End Class
```
