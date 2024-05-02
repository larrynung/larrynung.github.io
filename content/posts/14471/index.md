---
title: "[Extension Method]使用擴充方法來做物件的深層複製"
date: "2010-04-08 06:32:17"
description: "[Extension Method]使用擴充方法來做物件的深層複製"
tags: [VB.NET]
---

<p>紀錄一下用序列化來做深層複製的擴充方法</p>  <p>   </p><div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:17caeb0f-cab6-4674-b0d8-1884f1375eec" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Imports System.Runtime.CompilerServices
Imports System.Runtime.Serialization.Formatters.Binary

Public Module ObjectExtension

#Region "Const"
    Const BUFFER_SIZE As Integer = 512
#End Region

#Region "Public Method"

    &lt;Extension()&gt; _
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

End Module</pre></div>


<p> </p>

<p>使用上直接呼叫Clone即可 </p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:b0bf29f8-8890-44b1-8f6d-f7c9d100d42a" class="wlWriterEditableSmartContent"><pre name="code" class="vb">Dim person As New Person()
Dim clonePerson as Person =  person.Clone()</pre></div>
