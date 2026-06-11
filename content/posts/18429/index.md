---
title: "[VB.NET]Attribute與反射的搭配使用"
date: "2010-10-18 08:59:31"
description: "[VB.NET]Attribute與反射的搭配使用"
tags: [VB.NET]
---

有時在撰寫程式為了增加彈性或是便利性，我們可考慮使用Attribute來為類別、方法、欄位、與屬性附加一些資訊。這樣的設計方式在.NET中已經存在許久，這類應用也越來越普及，相信大家就算沒有用過也有看過，像是製作控制項時會用到的Browsable、Description、Category...，做序列化時會用到的XmlIgnore、XmlElement...，許多地方都會用到這樣的小技巧。

在Attribute的建立上，簡單的說只是一個繼承Attribute的類別，裡面存放著所要附加的資料，並透過AttributeUsage屬性設定該Attribute所能使用的範圍。像是：

Class NewPropertyOrFieldAttribute
Inherits Attribute

Property Data as Object

End Class

這邊以利用Attribute將資訊附加在列舉成員欄位為例，假設我們有要做類似於Office這樣的軟體需求，為求方便使用，可能會希望開出一個建構子或是成員方法，裡面可帶入列舉，依帶入的列舉值開啟對應的應用程式。這時就可以透過Attribute為列舉的成員欄位附加對應要開啟的類別資訊，像是下面這樣：

NotInheritable Class RelativedTypeAttribute
Inherits Attribute

Property RelativedType As Type

Sub New(ByVal relativedType As Type)
Me.RelativedType = relativedType
End Sub

End Class

Enum ApplicationType
_
Word

_
Excel

_
Access

_
PowerPoint

_
Visio
End Enum

再透過反射取得列舉成員欄位對應的類別資訊，將其類別動態建立叫起使用就可以了。

Sub Main()
StartApplication(ApplicationType.Word)
End Sub

Sub StartApplication(ByVal apType As ApplicationType)
Dim type As Type = apType.GetType()
Dim field = type.GetField(apType.ToString)
Dim att = field.GetCustomAttributes(GetType(RelativedTypeAttribute), False).Cast(Of RelativedTypeAttribute)().FirstOrDefault()
Activator.CreateInstance(att.RelativedType).Start()
End Sub

又或是我們有需求透過列舉取得對應的描述字串，我們可以使用Attribute為列舉的成員欄位附加對應的資源編號，像是下面這樣：

NotInheritable Class ResouceIDAttribute
Inherits Attribute

Property ResourceID As String

Sub New(ByVal resourceID As String)
Me.Resource
End Sub

End Class

Enum InterfaceType
_
RS232

_
RS485

_
GPIB

_
I2C
End Enum

如此可透過反射去取得附加的資源ID，進一步取得資源檔所設定的字串。

Sub Main()
Dim instrumentInterface As InterfaceType
Dim type As Type = instrumentInterface.GetType()
Dim field = type.GetField(instrumentInterface.ToString)
Dim resource False).Cast(Of ResouceIDAttribute)().FirstOrDefault.ResourceID
Console.WriteLine(My.Resources.ResourceManager.GetString(resourceID))
End Sub

當然還可以用在很多地方，這邊只是舉幾個例子稍作紀錄。