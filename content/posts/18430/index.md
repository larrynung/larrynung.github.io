---
title: "[VB.NET]用Extension Method取得CustomAttributes"
date: "2010-10-18 09:02:31"
description: "[VB.NET]用Extension Method取得CustomAttributes"
tags: [VB.NET]
---整理一下自己用來取得CustomAttributes的擴充方法。

## EnumExtension
Imports System.Runtime.CompilerServices

Module EnumExtension

_
Function GetCustomAttributes(Of T)(ByVal e As [Enum]) As IEnumerable(Of T)
Return e.GetType.GetField(e.ToString).GetCustomAttributes(GetType(T), False).Cast(Of T)()
End Function

_
Function GetCustomAttribute(Of T)(ByVal e As [Enum]) As T
Return GetCustomAttributes(Of T)(e).FirstOrDefault
End Function

End Module

## TypeExtension

Imports System.Runtime.CompilerServices

Module TypeExtension

_
Function GetCustomAttributes(Of T)(ByVal type As Type) As IEnumerable(Of T)
Return type.GetCustomAttributes(GetType(T), False).Cast(Of T)()
End Function

_
Function GetCustomAttribute(Of T)(ByVal type As Type) As T
Return DirectCast(GetCustomAttributes(Of T)(type).FirstOrDefault, T)
End Function

_
Function GetCustomAttributes(Of T)(ByVal type As Type, ByVal memberName As String) As IEnumerable(Of T)
Dim m = type.GetMember(memberName).FirstOrDefault
If m Is Nothing Then
Throw New MissingMemberException
End If
Return m.GetCustomAttributes(GetType(T), False)
End Function

_
Function GetCustomAttribute(Of T)(ByVal type As Type, ByVal memberName As String) As T
Return GetCustomAttributes(Of T)(type, memberName).FirstOrDefault
End Function
End Module

## ObjectExtension

Imports System.Runtime.CompilerServices
Imports System.Reflection

Module ObjectExtension

_
Function GetCustomAttributes(Of T)(ByVal obj As Object) As IEnumerable(Of T)
Return obj.GetType.GetCustomAttributes(GetType(T), False).Cast(Of T)()
End Function

_
Function GetCustomAttribute(Of T)(ByVal obj As Object) As T
Return GetCustomAttributes(Of T)(obj).FirstOrDefault
End Function

_
Function GetCustomAttributes(Of T)(ByVal obj As Object, ByVal memberName As String) As IEnumerable(Of T)
Dim m = obj.GetType.GetMember(memberName).FirstOrDefault
If m Is Nothing Then
Throw New MissingMemberException
End If
Return m.GetCustomAttributes(GetType(T), False)
End Function

_
Function GetCustomAttribute(Of T)(ByVal obj As Object, ByVal memberName As String) As T
Return GetCustomAttributes(Of T)(obj, memberName).FirstOrDefault
End Function
End Module

## 使用範例

Module Module1

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

_
Class TestClass

_
Property TestProperty As String

End Class

Sub Main()
Dim c As New TestClass
Console.WriteLine(InterfaceType.GPIB.GetCustomAttribute(Of DescriptionAttribute)().Description)
Console.WriteLine(c.GetCustomAttribute(Of DescriptionAttribute).Description)
Console.WriteLine(c.GetCustomAttribute(Of DescriptionAttribute)("TestProperty").Description)
End Sub

End Module