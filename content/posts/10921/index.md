---
title: "[C#]使用DebuggerDisplayAttribute自訂除錯監看訊息"
slug: "[CSharp]使用DebuggerDisplayAttribute自訂除錯監看訊息"
date: "2009-10-06 09:01:20"
description: "[C#]使用DebuggerDisplayAttribute自訂除錯監看訊息"
tags: [CSharp]
---

## Introduction
  
DebuggerDisplayAttribute可為自己開發的類別，及其所包含的欄位與屬性，加上自訂的除錯監看訊息。

## NameSpace
  
System.Diagnostics

## Assembly
  
mscorlib (in mscorlib.dll)

## DebuggerDisplayAttribute
  
一般我們在除錯的時候，都會使用Visual Studio IDE所內建的監看視窗來查看變數。但一個類別內含多個成員，往往我們要查看的、常用的就是那幾個。卻要展開才能查看，十分不便。

  未展開時      

  展開時      

  而透過DebuggerDisplayAttribute，我們可以自訂除錯監看訊息，可把自己常看的變數資訊直接顯示。使用上很簡單，只要在類別上方或是屬性、類別的上方設定DebuggerDisplay即可。像是：      
      [System.Diagnostics.DebuggerDisplay("Name = {Name}, Year = {Year}")]
    class Person

其監看結果如下： 

需特別注意，DebuggerDisplayAttribute參數在設定上，要帶入成員數值的地方需用"{}"包住。 

## Example

    class Program
    {
        static void Main(string[] args)
        {
            Person larry = new Person("Larry",28);
        }
    }

    [System.Diagnostics.DebuggerDisplay("Name = {Name}, Year = {Year}")]
    class Person
    {
        [System.Diagnostics.DebuggerDisplay("Name = {Name}")]
        string Name { get; set; }
        int Year { get; set; }

        public Person(string name, int year)
        {
            this.Name = name;
            this.Year = year;
        }
    }

監看結果