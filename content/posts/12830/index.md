---
title: "[VB.NET]Reading MFC CArchive"
slug: "vbnet-reading-mfc-carchive"
aliases: ["/posts/12830/"]
date: "2010-01-05 11:26:43"
description: "CArchive是MFC的序列化處理類別，除了一般的序列化存檔會用到外，在SendMessage傳送WN_COPYDATA訊息，連帶觸發OnCopyData，其傳遞的資料也是CArchive的格式。"
tags: [VB.NET]
---

CArchive是MFC的序列化處理類別，除了一般的序列化存檔會用到外，在SendMessage傳送WN_COPYDATA訊息，連帶觸發OnCopyData，其傳遞的資料也是CArchive的格式。

CArchive的檔案格式若要在.NET程式中讀取，我們可以直接使用.NET Framework中的BinaryReader。

也可以參考MFC CArchive的寫法自行實作讀取，有興趣的可直接透過VC6 Debug追進CArchive看程式的處理，或是直接看網路上的文章。

下面這個類別就是之前自己寫來讀取CArchive的。

```vb
Imports System.IO
Imports System.Text
Public Class CArchive

#Region "Config"
    Private ReadOnly BYTES_COUNT_IN_BOOL As Byte = 4  'VC6的BOOL佔 4 Bytes
    Private ReadOnly BYTES_COUNT_IN_INT As Byte = 4  'VC6的Int佔 4 Bytes
    Private ReadOnly BYTES_COUNT_IN_FLOAT As Byte = 4  'VC6的Float佔 4 Bytes
    Private ReadOnly BYTES_COUNT_IN_DOUBLE As Byte = 8  'VC6的Double佔 8 Bytes
    Private ReadOnly BUFFERSIZE As Integer = 512

#End Region

#Region "Private Var"

    Private m_baryBinaryData(BUFFERSIZE) As Byte
    Private m_fsFileStream As FileStream

    Private m_nDataLength As Integer
    Private m_strData As String
    Private m_nData As Integer
    Private m_sData As Single
    Private m_dData As Double
    Private m_bData As Boolean
#End Region

#Region "Constructer"

    Public Sub New(ByVal FilePath As String)
        m_fsFileStream = New FileStream(FilePath, FileMode.Open)
    End Sub

#End Region

#Region "Public Method"

    Public Function GetString() As String
        m_nDataLength = m_fsFileStream.ReadByte

        m_fsFileStream.Read(m_baryBinaryData, 0, m_nDataLength)

        m_strData = Encoding.Default.GetString(m_baryBinaryData, 0, m_nDataLength)

        Return m_strData

    End Function

    Public Function GetInt() As Integer

        m_fsFileStream.Read(m_baryBinaryData, 0, BYTES_COUNT_IN_INT)

        m_nData = BitConverter.ToInt32(m_baryBinaryData, 0)

        Return m_nData

    End Function

    Public Function GetDouble() As Double

        m_fsFileStream.Read(m_baryBinaryData, 0, BYTES_COUNT_IN_DOUBLE)

        m_dData = BitConverter.ToDouble(m_baryBinaryData, 0)

        Return m_dData

    End Function

    Public Function GetFloat() As Single

        m_fsFileStream.Read(m_baryBinaryData, 0, BYTES_COUNT_IN_FLOAT)

        m_sData = BitConverter.ToSingle(m_baryBinaryData, 0)

        Return m_sData

    End Function

    Public Function GetBoolean() As Boolean

        m_fsFileStream.Read(m_baryBinaryData, 0, BYTES_COUNT_IN_BOOL)

        m_bData = BitConverter.ToBoolean(m_baryBinaryData, 0)

        Return m_bData

    End Function

#End Region

End Class
```
