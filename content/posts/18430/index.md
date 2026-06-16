---
title: "[VB.NET]Get CustomAttributes Using an Extension Method"
slug: "vbnet-get-customattributes-using-an-extension-method"
aliases: ["/posts/18430/"]
date: "2010-10-18 09:02:31"
description: "整理一下自己用來取得CustomAttributes的擴充方法。 EnumExtension TypeExtension ObjectExtension 使用範例"
tags: [VB.NET]
---

整理一下自己用來取得CustomAttributes的擴充方法。

## EnumExtension

```vb
Imports System.Runtime.CompilerServices

Module EnumExtension

    <Extension()> _
    Function GetCustomAttributes(Of T)(ByVal e As [Enum]) As IEnumerable(Of T)
        Return e.GetType.GetField(e.ToString).GetCustomAttributes(GetType(T), False).Cast(Of T)()
    End Function

    <Extension()> _
    Function GetCustomAttribute(Of T)(ByVal e As [Enum]) As T
        Return GetCustomAttributes(Of T)(e).FirstOrDefault
    End Function

End Module
```

## TypeExtension

```vb
Imports System.Runtime.CompilerServices

Module TypeExtension

    <Extension()> _
    Function GetCustomAttributes(Of T)(ByVal type As Type) As IEnumerable(Of T)
        Return type.GetCustomAttributes(GetType(T), False).Cast(Of T)()
    End Function

    <Extension()> _
    Function GetCustomAttribute(Of T)(ByVal type As Type) As T
        Return DirectCast(GetCustomAttributes(Of T)(type).FirstOrDefault, T)
    End Function

    <Extension()> _
    Function GetCustomAttributes(Of T)(ByVal type As Type, ByVal memberName As String) As IEnumerable(Of T)
        Dim m = type.GetMember(memberName).FirstOrDefault
        If m Is Nothing Then
            Throw New MissingMemberException
        End If
        Return m.GetCustomAttributes(GetType(T), False)
    End Function

    <Extension()> _
    Function GetCustomAttribute(Of T)(ByVal type As Type, ByVal memberName As String) As T
        Return GetCustomAttributes(Of T)(type, memberName).FirstOrDefault
    End Function
End Module
```

## ObjectExtension

```vb
Imports System.Runtime.CompilerServices
Imports System.Reflection

Module ObjectExtension

    <Extension()> _
    Function GetCustomAttributes(Of T)(ByVal obj As Object) As IEnumerable(Of T)
        Return obj.GetType.GetCustomAttributes(GetType(T), False).Cast(Of T)()
    End Function

    <Extension()> _
    Function GetCustomAttribute(Of T)(ByVal obj As Object) As T
        Return GetCustomAttributes(Of T)(obj).FirstOrDefault
    End Function

    <Extension()> _
    Function GetCustomAttributes(Of T)(ByVal obj As Object, ByVal memberName As String) As IEnumerable(Of T)
        Dim m = obj.GetType.GetMember(memberName).FirstOrDefault
        If m Is Nothing Then
            Throw New MissingMemberException
        End If
        Return m.GetCustomAttributes(GetType(T), False)
    End Function

    <Extension()> _
    Function GetCustomAttribute(Of T)(ByVal obj As Object, ByVal memberName As String) As T
        Return GetCustomAttributes(Of T)(obj, memberName).FirstOrDefault
    End Function
End Module
```

## 使用範例

```vb
Module Module1

    Enum InterfaceType
        <Description("RS232 Interface")> _
        RS232

        <Description("RS485 Interface")> _
        RS485

        <Description("GPIB Interface")> _
        GPIB

        <Description("I2C Interface")> _
        I2C
    End Enum

    <Description("Test Class")> _
    Class TestClass

        <Description("Test Property")> _
        Property TestProperty As String

    End Class

    Sub Main()
        Dim c As New TestClass
        Console.WriteLine(InterfaceType.GPIB.GetCustomAttribute(Of DescriptionAttribute)().Description)
        Console.WriteLine(c.GetCustomAttribute(Of DescriptionAttribute).Description)
        Console.WriteLine(c.GetCustomAttribute(Of DescriptionAttribute)("TestProperty").Description)
    End Sub

End Module
```
