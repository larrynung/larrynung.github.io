---
title: "[C#][VB.NET]XML序列化私有欄位"
slug: "[CSharp][VB.NET]XML序列化私有欄位"
date: "2008-11-29 10:17:07"
description: "[C#][VB.NET]XML序列化私有欄位"
tags: [VB.NET,CSharp]
---

<p>
	      假設今天有個Person的類別如下。除了名字、年齡、性別外，內含_friends清單用以提供IsFriend與AddFriend函式所須用到的朋友清單資料。</p>
<p>
	VB.NET</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e6005972-a1a9-4f20-93da-a8dac69a39c7" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="vb" name="code">
	Public Class Person

#Region "Enum"
    Enum SexType
        Boy
        Girl
    End Enum
#End Region


#Region "Var"
    Private _name As String
    Private _year As Integer
    Private _sex As SexType
    Private _friendNames As New List(Of String)
#End Region


#Region "Property"
    Public Property Name() As String
        Get
            If String.IsNullOrEmpty(_name) Then
                Return String.Empty
            End If
            Return _name
        End Get
        Set(ByVal value As String)
            _name = value
        End Set
    End Property

    Public Property Year() As Integer
        Get
            Return _year
        End Get
        Set(ByVal value As Integer)
            _year = value
        End Set
    End Property

    Public Property Sex() As SexType
        Get
            Return _sex
        End Get
        Set(ByVal value As SexType)
            _sex = value
        End Set
    End Property
#End Region


#Region "Public Method"
    Public Sub AddFriend(ByVal people As Person)
        _friendNames.Add(people.Name)
    End Sub

    Public Function IsFriend(ByVal people As Person) As Boolean
        For Each friendName As String In _friendNames
            If friendName = people.Name Then
                Return True
            End If
        Next
        Return False
    End Function
#End Region


End Class
</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	C#</p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:beb2d7ce-b328-48ad-a2ee-9deb910f22c4" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
	public class Person
    {

        #region Enum
        public enum SexType
        {
            Boy,
            Girl
        }
        #endregion

        #region Var
        private string _name;
        private int _year;
        private SexType _sex;
        private List&lt;String&gt; _friendNames = new List&lt;String&gt;();
        #endregion


        #region Property
        public string Name
        {
            get
            {
                if (string.IsNullOrEmpty(_name))
                {
                    return string.Empty;
                }
                return _name;
            }
            set { _name = value; }
        }

        public int Year
        {
            get { return _year; }
            set { _year = value; }
        }

        public SexType Sex
        {
            get { return _sex; }
            set { _sex = value; }
        }
        #endregion


        #region Public Method
        public void AddFriend(Person people)
        {
            _friendNames.Add(people.Name);
        }

        public bool IsFriend(Person people)
        {
            foreach (String friendName in _friendNames)
            {
                if (friendName == people.Name)
                {
                    return true;
                }
            }
            return false;
        }
        #endregion


    }</pre>
</div>
<p>
	 </p>
<p>
	      在.NET程式裡，若將該類別直接做XML序列化，則其類別的_friends這個私有的欄位資料將不會被序列化保存 (因為.NET XML序列化無法序列化私有欄位資料)。此時我們可以用自定義XML的方式來去解決此問題。透過自定義XML序列化，我們可以自己定義XML序列化的格式。也可以把本來不會序列化的私有欄位一併序列化。</p>
<p>
	      但是，若只是很單純的去實作自定義XML序列化。做出來的類別將無法與.NET本身的XML序列化做整合。舉個例子來說，假設今天Person這個類別實作了自定義XML序列化。而程式中又有個PersonCollection這個類別內含Person這個類別成員。則此時，若PersonCollection這個類別沒有實作自定義XML序列化，而想直接用來序列化的話。該程式在序列化時將會發生錯誤。也就是說，當A這個類別做了自定義XML序列化，而B這個類別的成員內含A這個類別時，則B通常也將需要自定義XML序列化。</p>
<p>
	     要解決該問題，照著下面程式碼片段的格式去實作自定義XML序列化即可。</p>
<p>
	VB.NET</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:1190d147-6616-4415-9301-22fafbbe04cc" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="vb" name="code">
	#Region "Implement IXmlSerializable"
    Public Function GetSchema() As System.Xml.Schema.XmlSchema Implements System.Xml.Serialization.IXmlSerializable.GetSchema
        Return Nothing
    End Function

    Public Sub ReadXml(ByVal reader As System.Xml.XmlReader) Implements System.Xml.Serialization.IXmlSerializable.ReadXml
        Dim startElementName As String = reader.Name
        Dim currentElementName As String

        Me._friendNames.Clear()
        Do
            currentElementName = reader.Name
            If currentElementName = startElementName AndAlso (reader.MoveToContent = Xml.XmlNodeType.EndElement OrElse reader.IsEmptyElement) Then
                reader.Read()
                Exit Do
            End If

            Select Case currentElementName
                Case "Name"
                    Me.Name = reader.ReadElementString()

                Case "Sex"
                    Me.Sex = CType(reader.ReadElementString(), SexType)

                Case "Year"
                    Me.Year = CInt(reader.ReadElementString())

                Case "Friend"
                    Me._friendNames.Add(reader.GetAttribute("Name"))
                    reader.Read()
                Case Else
                    reader.Read()

            End Select

        Loop
    End Sub

    Public Sub WriteXml(ByVal writer As System.Xml.XmlWriter) Implements System.Xml.Serialization.IXmlSerializable.WriteXml
        writer.WriteElementString("Name", Name)
        writer.WriteElementString("Sex", CInt(Sex).ToString)
        writer.WriteElementString("Year", Year.ToString)
        For Each friendName As String In _friendNames
            writer.WriteStartElement("Friend")
            writer.WriteAttributeString("Name", friendName)
            writer.WriteEndElement()
        Next
    End Sub
#End Region</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	C#</p>
<p>
	 </p>
<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:c15452b7-06ba-4e05-88d5-39d9792fdbbf" style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">
	<pre class="c#" name="code">
	#region Implement IXmlSerializable 

        public System.Xml.Schema.XmlSchema GetSchema()
        {
            throw new NotImplementedException();
        }

        public void ReadXml(System.Xml.XmlReader reader)
        {
            string startElementName = reader.Name;
            string currentElementName;

            this._friendNames.Clear();
            do
            {
                currentElementName = reader.Name;
                if (currentElementName == startElementName &amp;&amp; (reader.MoveToContent() == System.Xml.XmlNodeType.EndElement || reader.IsEmptyElement))
                {
                    reader.Read();
                    break; 
                }

                switch (currentElementName)
                {
                    case "Name":
                        this.Name = reader.ReadElementString();
                        break;

                    case "Sex":                        
                        this.Sex = (SexType)int.Parse (reader.ReadElementString());
                        break;

                    case "Year":
                        this.Year = int.Parse(reader.ReadElementString());
                        break;

                    case "Friend":
                        this._friendNames.Add(reader.GetAttribute("Name"));
                        reader.Read();
                        break;
                    default:
                        reader.Read();
                        break;

                }
            }while (true);
        }

        public void WriteXml(System.Xml.XmlWriter writer)
        {
            writer.WriteElementString("Name", Name);
            writer.WriteElementString("Sex", ((int)Sex).ToString());
            writer.WriteElementString("Year", Year.ToString());
            foreach (string friendName in _friendNames)
            {
                writer.WriteStartElement("Friend");
                writer.WriteAttributeString("Name", friendName);
                writer.WriteEndElement();
            }
        }

        #endregion</pre>
</div>
<p>
	 </p>
<p>
	 </p>
<p>
	      其主要重點概念如下圖所示：</p>
<p>
	<img alt="image" border="0" height="269" src="\images\posts\6127\image_thumb.png" style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" width="644" /></p>
