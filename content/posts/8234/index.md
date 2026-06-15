---
title: "[VB.NET].NET多語系程式(三)"
date: "2009-04-29 12:05:15"
description: "[VB.NET].NET多語系程式(三)"
tags: [VB.NET]
---

## ![image_thumb_2.png](/images/posts/8234/image_thumb_2.png)

## Abstract

* Introduction
* 學習目標
* 操作步驟
* 簡易實作範例

## Introduction

本篇將介紹.NET多語系程式的寫法 ，下面會利用XML文件來達到多語系的功能。

## 學習目標

* .NET多語程式撰寫
* 用XML文件實現多語功能
* XML序列化與解序列化

## 操作步驟

**Step1.建立內含多語訊息的XML文件**

XML文件格式可能如下，內含CultureInfo代碼與對應的訊息字串。

![image_thumb.png](/images/posts/8234/image_thumb.png)

**Step2.切換語系時，從XML文件中抓取對應的顯示字串**

![image_thumb_1.png](/images/posts/8234/image_thumb_1.png)

![image_thumb_3.png](/images/posts/8234/image_thumb_3.png)

![image_thumb_4.png](/images/posts/8234/image_thumb_4.png)

## 簡易實作範例

基本上這邊只是提示多語程式功能可透過XML文件實現，實現步驟大概如上面所述。然而XML文件的格式與存取的方法與寫法則就看個人怎樣編寫。這邊提供個簡易的範例：

**MultiLanguage類別**

MultiLanguage類別的Code如下

```
Imports System.Globalization
Imports System.Threading
Imports System.Xml.Serialization

Public Class MultiLanguage
    Implements IXmlSerializable

#Region "Var"
    Private _pool As New Hashtable
#End Region

#Region "Public Shared Method"
    Public Shared Function GetFromXml(ByVal file As String) As MultiLanguage
        Dim m As MultiLanguage
        Dim x As New Xml.Serialization.XmlSerializer(GetType(MultiLanguage))
        Dim fs As New IO.FileStream(file, IO.FileMode.Open)
        m = CType(x.Deserialize(fs), MultiLanguage)
        fs.Dispose()
        Return m
    End Function
#End Region

#Region "Public Method"
    Public Sub AddString(ByVal key As String, ByVal msg As String, ByVal culture As String)
        If Not _pool.ContainsKey(key) Then
            _pool.Add(key, New Hashtable)
        End If
        CType(_pool(key), Hashtable).Add(culture, msg)
    End Sub

    Public Sub AddString(ByVal key As String, ByVal msg As String)
        AddString(key, msg, Thread.CurrentThread.CurrentCulture.Name)
    End Sub

    Public Function GetString(ByVal key As String, ByVal culture As String) As String
        If Not _pool.ContainsKey(key) Then
            Return String.Empty
        End If
        Dim msgPool As Hashtable = CType(_pool(key), Hashtable)
        If Not msgPool.ContainsKey(culture) Then
            Return String.Empty
        End If
        Return msgPool(culture).ToString
    End Function

    Public Function GetString(ByVal key As String) As String
        Return GetString(key, Thread.CurrentThread.CurrentCulture.Name)
    End Function

    Public Sub SaveXml(ByVal file As String)
        Dim x As New Xml.Serialization.XmlSerializer(GetType(MultiLanguage))
        Dim fs As New IO.FileStream(file, IO.FileMode.Create)
        x.Serialize(fs, Me)
        fs.Dispose()
    End Sub
#End Region

#Region "Implements IXmlSerializable"
    Public Function GetSchema() As System.Xml.Schema.XmlSchema Implements System.Xml.Serialization.IXmlSerializable.GetSchema
        Return Nothing
    End Function

    Public Sub ReadXml(ByVal reader As System.Xml.XmlReader) Implements System.Xml.Serialization.IXmlSerializable.ReadXml
        Dim startElementName As String = reader.Name
        Dim currentElementName As String

        Do
            currentElementName = reader.Name
            If currentElementName = startElementName AndAlso (reader.MoveToContent = Xml.XmlNodeType.EndElement OrElse reader.IsEmptyElement) Then
                reader.Read()
                Exit Do
            End If

            Select Case currentElementName
                Case "Item"
                    Dim key As String = reader.GetAttribute("Key")
                    Dim cultureKey As String = reader.GetAttribute("Culture")
                    Dim value As String = reader.ReadString()
                    reader.ReadEndElement()
                    AddString(key, value, cultureKey)

                Case Else
                    reader.Read()
            End Select

        Loop

    End Sub

    Public Sub WriteXml(ByVal writer As System.Xml.XmlWriter) Implements System.Xml.Serialization.IXmlSerializable.WriteXml
        Dim msgPool As Hashtable
        For Each key As String In _pool.Keys
            msgPool = CType(_pool(key), Hashtable)
            For Each cultureKey As String In msgPool.Keys
                writer.WriteStartElement("Item")
                writer.WriteAttributeString("Key", key)
                writer.WriteAttributeString("Culture", cultureKey)
                writer.WriteString(msgPool(cultureKey).ToString)
                writer.WriteEndElement()
            Next
        Next
    End Sub
#End Region

End Class
```

**建立各語系字串**

m.AddString("title", "Title", "en") m.AddString("title", "標題", "zh-CHT") m.AddString("title", "标题", "zh-CHS")

**切換語系**

```
Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
     Me.Text = m.GetString("title", "en")
 End Sub

 Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
     Me.Text = m.GetString("title", "zh-CHT")
 End Sub

 Private Sub Button5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button5.Click
     Me.Text = m.GetString("title", "zh-CHS")
 End Sub
```

**儲存XML**

```
m.SaveXml("c:\test.xml")
```

**讀取XML**

```
Dim m As MultiLanguage = MultiLanguage.GetFromXml("c:\test.xml")
```

![image_thumb_6.png](/images/posts/8234/image_thumb_6.png)
