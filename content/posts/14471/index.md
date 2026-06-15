---
title: "[Extension Method]使用擴充方法來做物件的深層複製"
date: "2010-04-08 06:32:17"
description: "[Extension Method]使用擴充方法來做物件的深層複製"
tags: [VB.NET]
---

紀錄一下用序列化來做深層複製的擴充方法

```vb
Imports System.Runtime.CompilerServices
Imports System.Runtime.Serialization.Formatters.Binary

Public Module ObjectExtension

#Region "Const"
    Const BUFFER_SIZE As Integer = 512
#End Region

#Region "Public Method"

    <Extension()> _
      Public Function Clone(Of T)(ByVal obj As T, Optional ByVal serializeType As SerializationFormat = SerializationFormat.Binary) As T
        Select Case serializeType
            Case SerializationFormat.Binary
                Dim br As New BinaryFormatter()
                Using ms As New MemoryStream(BUFFER_SIZE)
                    br.Serialize(ms, obj)
                    ms.Seek(0, SeekOrigin.Begin)
                    Return DirectCast(br.Deserialize(ms), T)
                End Using
            Case SerializationFormat.Xml
                Dim x As New XmlSerializer(obj.GetType)
                Using ms As New MemoryStream(BUFFER_SIZE)
                    x.Serialize(ms, obj)
                    ms.Seek(0, SeekOrigin.Begin)
                    Return DirectCast(x.Deserialize(ms), T)
                End Using
        End Select
    End Function

#End Region

End Module
```

使用上直接呼叫Clone即可

```vb
Dim person As New Person()
Dim clonePerson as Person =  person.Clone()
```
