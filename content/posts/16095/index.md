---
title: "[VB.NET]用反射取得XML序列化組件內的Serializer，加速Xml序列化使用效能"
date: "2010-06-23 08:32:03"
description: "[VB.NET]用反射取得XML序列化組件內的Serializer，加速Xml序列化使用效能"
tags: [VB.NET]
---

<p>記得之前有在使用XML序列化程式產生器工具加速XML序列化</a>這篇有做一些Xml序列化效能上的比較，使用Xml序列化組件內所產生的Serialzer來做序列化動作效能最佳。但是這樣的方法使用上十分的麻煩，必需先寫好自己的組件，建置後產生對應的Xml序列化組件，再回過頭來修改我們自己的程式，把Xml序列化組件加入參考，用Xml序列化組件內所產生的Serialzer取代本來的XmlSerializer。搞到最後想必像我一樣懶的都怯步了，乾脆在檔案系統中放置Xml序列化組件加點小速度就好。 但明知可以加速卻不加速，心理難免有所不快。因此興起了用反射取用XML序列化組件內的Serializer的念頭，這邊簡單記錄一下實作心得。</p>  <p> </p>  <p>我們必需要了解的是在序列化時，通常知道的資訊只有要序列化的物件個體，或是其類別型態。從類別型態我們必需往回推敲出該型態所在的組件位置，有了組件位置我們就可以斷定Xml序列化組件的位置，如此就能從該組件中取出可以加速的Serializer。</p>  <p><a href="http://files.dotblogs.com.tw/larrynung/1006/VB.NETXMLSerializerXml_1292F/image_2.png"><img style="border-bottom: 0px; border-left: 0px; display: inline; border-top: 0px; border-right: 0px" title="image" border="0" alt="image" src="\images\posts\16095\image_thumb.png" width="571" height="99" /> </p>  <p> </p>  <p>就像下面這段程式就可以取得XML序列化組件內的XmlSerializer，若找不到XML序列化組件內的XmlSerializer則會回傳本來的XmlSerializer：</p>  <pre class="VB.NET" name="code" rows="25" cols="70">    Private Function GetXmlSerializerUsedType(ByVal obj As Object) As XmlSerializer
        Dim objType As Type = obj.GetType
        Dim asmFile As String = objType.Assembly.Location
        Dim serializerAssemblyFile As String = asmFile.Substring(0, asmFile.LastIndexOf(".")) &amp; ".XmlSerializers.dll"
        If My.Computer.FileSystem.FileExists(serializerAssemblyFile) Then
            Dim serializerAssemblyObjType As Type = Assembly.LoadFile(serializerAssemblyFile).GetType(String.Format("Microsoft.Xml.Serialization.GeneratedAssembly.{0}Serializer", objType.Name))
            If serializerAssemblyObjType IsNot Nothing Then
                Return DirectCast(Activator.CreateInstance(serializerAssemblyObjType), XmlSerializer)
            End If
        End If
        Return New XmlSerializer(objType)
    End Function</pre>

<p> </p>

<p>有了這樣的概念，我們就可以寫出一個會依Xml序列化組件存在與否來做加速動作的XmlSerializer Cache機制，就像下面這樣：</p>

<pre class="VB.NET" name="code" rows="25" cols="70">#Region "Const"
    Const POOL_BUFFER_SIZE As Integer = 25
#End Region

#Region "Var"
    Private Shared _pool As Dictionary(Of Type, XmlSerializer)
#End Region

#Region "Private Shared Property"
    ''' &lt;summary&gt;
    ''' Gets the pool.
    ''' &lt;/summary&gt;
    ''' &lt;value&gt;The pool.&lt;/value&gt;
    ''' &lt;returns&gt;&lt;/returns&gt;
    ''' &lt;remarks&gt;&lt;/remarks&gt;
    Private Shared ReadOnly Property m_Pool() As Dictionary(Of Type, XmlSerializer)
        Get
            If _pool Is Nothing Then
                _pool = New Dictionary(Of Type, XmlSerializer)(POOL_BUFFER_SIZE)
            End If
            Return _pool
        End Get
    End Property
#End Region

#Region "Public Shared Method"
    Public Shared Function GetXmlSerializer(ByVal objType As Type) As System.Xml.Serialization.XmlSerializer
        SyncLock m_Pool
            If Not m_Pool.ContainsKey(objType) Then
                Dim asmFile As String = objType.Assembly.Location
                Dim serializerAssemblyFile As String = asmFile.Substring(0, asmFile.LastIndexOf(".")) &amp; ".XmlSerializers.dll"
                If My.Computer.FileSystem.FileExists(serializerAssemblyFile) Then
                    Dim serializerAssemblyObjType As Type = Assembly.LoadFile(serializerAssemblyFile).GetType(String.Format("Microsoft.Xml.Serialization.GeneratedAssembly.{0}Serializer", objType.Name))
                    m_Pool.Add(objType, If(serializerAssemblyObjType Is Nothing, New XmlSerializer(objType), DirectCast(Activator.CreateInstance(serializerAssemblyObjType), XmlSerializer)))
                Else
                    m_Pool.Add(objType, New XmlSerializer(objType))
                End If
            End If
        End SyncLock
        Return m_Pool(objType)
    End Function
#End Region</pre>

<p>以後要序列化時透過這道取得XmlSerializer就可以了，而之所有會做這樣的Cache機制，是因為網路上流傳有XmlSerializer會有Memory leak的問題，普遍看到的解決方式就是做這樣的機制。</p>
