---
title: "LINQ to CSV library"
date: "2010-12-08 01:01:18"
description: "LINQ to CSV library"
tags: [CSharp,Linq]
---
Matt Perdeck開發的LINQ to CSV library提供強大的CSV檔存取功能，可讓我們很輕鬆的取出CSV檔內容，搭配使用Linq去做查詢的動作，也具備有CSV檔文件產出與例外處理的功能，使用上十分的彈性好用。

其具備以下特點：

依循 CSV 檔格式

可指定分隔符號

支援延遲讀取

支援存取檔案中的日期與數字格式

可自動辨識各種不同的日期與數字格式

可彈性的控制日期與數字的輸出格式

支援不同的字集編碼 ( Encoding )

完善的錯誤處理機制

使用前我們需至LINQ to CSV library下載程式專案，將其建置後取出LINQtoCSV.dll組件。

在使用上LINQ to CSV library也算是很容易上手的一個函式庫，因為我們不需要了解太多類別，主要要了解的有CsvContext、CsvFileDescription、與CsvColumnAttribute這三個，外加一些做例外處理用的例外類別(LINQ to CSV library這邊就有很詳細的類別與成員的介紹，故例外類別不在此多做著墨)。

CsvContext為主要我們要操控的類別，內有Read與Write方法兩種方法，皆具有許多的多載，用以讀取CSV檔的檔案內容，與寫入檔案內容至CSV檔案之中。

Write(IEnumerable values, string fileName)
Write(IEnumerable values, string fileName, CsvFileDescription fileDescription)
Write(IEnumerable values, TextWriter stream)
Write(IEnumerable values, TextWriter stream, CsvFileDescription fileDescription)

Read(string fileName)
Read(string fileName, CsvFileDescription fileDescription)
Read(StreamReader stream)
Read(StreamReader stream, CsvFileDescription fileDescription)

CsvFileDescription為存取CSV檔所需要的一些細項描述，像是SeparatorChar屬性用以設定CSV檔資料的分隔符號、FirstLineHasColumnNames屬性用以指示資料的第一行是否含有欄位名稱、FileCultureName屬性用以指示CSV檔寫入與讀取時所要採用的文化語系...等等。

CsvColumnAttribute則是用以設定屬性與CSV檔欄位的對應方式，像是Name屬性可設定對應的欄位名稱、CanBeNull指示欄位資料是否可為空值、FieldIndex指示欄位的索引、OutputFormat指示輸出的格式...等等。

在做寫入CSV檔時，主要是先建立要寫入的資料內容，這邊的資料內容為具有CsvColumnAttribute修飾屬性的類別集合。像是下面這樣：

public class Person
{
[CsvColumn (,FieldIndex =0)]
public String FirstName { get; set; }

[CsvColumn(, FieldIndex = 1)]
public String LastName { get; set; }

[CsvColumn(, FieldIndex = 2)]
public String Sex { get; set; }

[CsvColumn(, FieldIndex = 3)]
public String Birthday { get; set; }

public String Memo { get; set; }

public override string ToString()
{
return string.Join(",", new string[] { FirstName, LastName, Sex, Birthday, Memo });
}
}

建立完後，透過CsvContext.Write，帶入資料內容與檔名就可將指定的內容寫入至CSV檔中

const string FILE_;

CsvContext cc = new CsvContext();
Person[] persons = new Person[]
{
new Person() { First, Last, Sex = "Boy", Birthday = "1980/04/19" }
};

cc.Write(persons, FILE_NAME);

讀檔的話則是透過CsvContext.Read，帶入檔名與泛型類別，檔案的內容就會讀出轉成指定的泛型類別集合。

const string FILE_;
CsvContext cc = new CsvContext();
Var data = cc.Read(FILE_NAME);

##
完整範例

Person.cs

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using LINQtoCSV;

namespace ConsoleApplication1
{
public class Person
{
[CsvColumn (,FieldIndex =0)]
public String FirstName { get; set; }

[CsvColumn(, FieldIndex = 1)]
public String LastName { get; set; }

[CsvColumn(, FieldIndex = 2)]
public String Sex { get; set; }

[CsvColumn(, FieldIndex = 3)]
public String Birthday { get; set; }

public String Memo { get; set; }

public override string ToString()
{
return string.Join(",", new string[] { FirstName, LastName, Sex, Birthday, Memo });
}
}
}

Program.cs

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using LINQtoCSV;

namespace ConsoleApplication1
{
class Program
{
static void Main(string[] args)
{
const string FILE_;

CsvContext cc = new CsvContext();
Person[] persons = new Person[]
{
new Person() { First, Last, Sex = "Boy", Birthday = "1980/04/19" }
};

cc.Write(persons, FILE_NAME);

Console.WriteLine("CSV File Content...");
Console.WriteLine(System.IO.File.ReadAllText(FILE_NAME));

Console.WriteLine("Read From CSV...");
Console.WriteLine(cc.Read(FILE_NAME).FirstOrDefault().ToString());

Console.WriteLine(new string('=', 50));
CsvFileDescription cfd = new CsvFileDescription()
{
SeparatorChar = ' ',
FirstLineHasColumnNames = true,
EnforceCsvColumnAttribute =true
};

cc.Write(persons, FILE_NAME,cfd);

Console.WriteLine("CSV File Content...");
Console.WriteLine(System.IO.File.ReadAllText(FILE_NAME));

cfd = new CsvFileDescription()
{
SeparatorChar = ' ',
FirstLineHasColumnNames = false ,
EnforceCsvColumnAttribute = true
};
Console.WriteLine("Read From CSV...");
Console.WriteLine(cc.Read(FILE_NAME, cfd).FirstOrDefault().ToString());

Console.WriteLine(new string('=', 50));
cfd = new CsvFileDescription()
{
FirstLineHasColumnNames = false,
EnforceCsvColumnAttribute = true
};

cc.Write(persons, FILE_NAME, cfd);

Console.WriteLine("CSV File Content...");
Console.WriteLine(System.IO.File.ReadAllText(FILE_NAME));

cfd = new CsvFileDescription()
{
SeparatorChar = ' ',
FirstLineHasColumnNames = false,
EnforceCsvColumnAttribute = true
};
Console.WriteLine("Read From CSV...");
Console.WriteLine(cc.Read(FILE_NAME, cfd).FirstOrDefault().ToString());
}
}
}

運行結果如下：

##
Download

LinqToCSVDemo.zip

##
Link

LINQ to CSV library

好用的 LINQ to CSV library