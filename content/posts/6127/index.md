---
title: "[C#][VB.NET]XML序列化私有欄位"
slug: "[CSharp][VB.NET]XML序列化私有欄位"
date: "2008-11-29 10:17:07"
description: "[C#][VB.NET]XML序列化私有欄位"
tags: [VB.NET,CSharp]
---假設今天有個Person的類別如下。除了名字、年齡、性別外，內含_friends清單用以提供IsFriend與AddFriend函式所須用到的朋友清單資料。

VB.NET

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
_
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
If friend Then
Return True
End If
Next
Return False
End Function
#End Region

End Class

C#

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
private List _friendNames = new List();
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
set { _ }
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
if (friend people.Name)
{
return true;
}
}
return false;
}
#endregion

}

      在.NET程式裡，若將該類別直接做XML序列化，則其類別的_friends這個私有的欄位資料將不會被序列化保存 (因為.NET XML序列化無法序列化私有欄位資料)。此時我們可以用自定義XML的方式來去解決此問題。透過自定義XML序列化，我們可以自己定義XML序列化的格式。也可以把本來不會序列化的私有欄位一併序列化。

      但是，若只是很單純的去實作自定義XML序列化。做出來的類別將無法與.NET本身的XML序列化做整合。舉個例子來說，假設今天Person這個類別實作了自定義XML序列化。而程式中又有個PersonCollection這個類別內含Person這個類別成員。則此時，若PersonCollection這個類別沒有實作自定義XML序列化，而想直接用來序列化的話。該程式在序列化時將會發生錯誤。也就是說，當A這個類別做了自定義XML序列化，而B這個類別的成員內含A這個類別時，則B通常也將需要自定義XML序列化。

     要解決該問題，照著下面程式碼片段的格式去實作自定義XML序列化即可。

VB.NET

#Region "Implement IXmlSerializable"
Public Function GetSchema() As System.Xml.Schema.XmlSchema Implements System.Xml.Serialization.IXmlSerializable.GetSchema
Return Nothing
End Function

Public Sub ReadXml(ByVal reader As System.Xml.XmlReader) Implements System.Xml.Serialization.IXmlSerializable.ReadXml
Dim startElementName As String = reader.Name
Dim currentElementName As String

Me._friendNames.Clear()
Do
currentElement
If currentElement AndAlso (reader.MoveToContent = Xml.XmlNodeType.EndElement OrElse reader.IsEmptyElement) Then
reader.Read()
Exit Do
End If

Select Case currentElementName
Case "Name"
Me.

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
#End Region

C#

#region Implement IXmlSerializable

public System.Xml.Schema.XmlSchema GetSchema()
{
throw new NotImplementedException();
}

public void ReadXml(System.Xml.XmlReader reader)
{
string startElement
string currentElementName;

this._friendNames.Clear();
do
{
currentElement
if (currentElement startElementName && (reader.MoveToContent() == System.Xml.XmlNodeType.EndElement || reader.IsEmptyElement))
{
reader.Read();
break;
}

switch (currentElementName)
{
case "Name":
this.
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

#endregion

      其主要重點概念如下圖所示：