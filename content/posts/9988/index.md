---
title: "[VB.NET]VB 10.0 Auto-Implemented Properties"
date: "2009-08-11 08:59:53"
description: "[VB.NET]VB 10.0 Auto-Implemented Properties"
tags: [VB.NET]
---

## Introduction

Auto-Implemented Properties是VB.NET 10.0的特色之一。讓我們在撰寫屬性時只需短短一行即可，其細部的私有欄位與Get、Set區塊都將由編譯器在編譯時幫我們自動產生。可簡化屬性的撰寫，加速程式撰寫速度。

## Support
VB 10.0 or latter

## Auto-Implemented Properties

在以往我們要建立一個屬性時，我們通常會建立個私有欄位用來儲存屬性的值。並會利用Property關鍵字設定屬性區塊，在Get、Set區塊撰寫取值與設值的程式碼。就像是下面這樣：

    Private _name As String

    Property Name As String
        Get
            Return _name
        End Get
        Set(ByVal value As String)
            _name = value
        End Set
    End Property

透過VB.NET 10.0的Auto-Implemented Properties功能，我們可以將屬性的撰寫給簡化。像是上面的例子可簡化為像下面這樣：

Property Name As String

短短的一行就可以取代本來冗長的程式，是不是很方便呢？除此之外，Auto-Implemented Properties也可以利用變數初始器來設定屬性的預設值。就像：

Property Name As String = "Larry"

若是使用較為複雜的型別也可以

Property SupplierList() As New List(Of Supplier)
Property OrderList() As New List(Of Order) With {.Capacity = 100}

也可以用在介面屬性的實作上

Property Name() As String Implements ICustomer.Name

## 注意事項
1.不支援ReadOnly關鍵字
若在Auto-Implemented Properties前面加上ReadOnly關鍵字

ReadOnly Property Name() As String

則編譯器會顯示錯誤

2.不支援WriteOnly關鍵字
若在Auto-Implemented Properties前面加上WriteOnly關鍵字

WriteOnly Property Name() As String

則編譯器會顯示錯誤

3.不支援帶參數的屬性
若在Auto-Implemented Properties設定參數

Property Items(ByVal idx As Integer) As String

則編譯器會顯示錯誤

4.不支援索引器
由於無法支援帶參數的屬性，自然無法支援索引器。