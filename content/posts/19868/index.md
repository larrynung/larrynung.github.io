---
title: "Linq To Excel"
date: "2010-12-02 08:20:00"
description: "Linq To Excel"
tags: [Linq, CSharp]
---

Linq to Excel為一Open Source函式庫，該函式庫能讓我們使用Linq去對Excel與CSV做查詢的動作。

使用前需先將LinqToExcel.dll與Remotion.Data.Linq.dll這兩個組件檔給加入參考，並加入LinqToExcel命名空間就可以開始使用Linq to Excel了。

開始使用前需了解到ExcelQueryFactory為Linq to Excel的主要類別，我們主要都是對該類別下去做操作，因此我們必需要了解其內部的成員，這邊將其成員整理列表如下：

屬性

Name

Description

FileName

檔案名稱

StrictMapping

是否限制AddMapping所有設定的對應都要正確

方法

Name

Description

Worksheet

取得工作表中的資料

WorksheetNoHeader

取得工作表中不含標題的資料

WorksheetRange

取得工作表中特定範圍的資料

WorksheetRangeNoHeader

取得工作表中不含標題的特定範圍資料

AddMapping

設定Excel欄位與物件屬性的對應

AddTransformation

設定Excel欄位塞給物件屬性所要做的轉換動作

GetWorksheetNames

取得所有工作表名稱

GetColumnNames

取得所有欄位名稱

建立ExcelQueryFactory物件時我們有兩種選擇，一種是直接將Excel檔案位置帶入建構子建構。

var excel = new ExcelQueryFactory("Data.xls");

一種是使用預設建構子建立後，再透過FileName屬性設定Excel檔案位置。

var excel = new ExcelQueryFactory();
excel.File;

建立ExcelQueryFactory物件後，可以使用GetWorksheetNames方法可以取得所有工作表名稱 。

void ShowWorkSheetNames(string excelFile)
{
var excel = new ExcelQueryFactory(excelFile);
var workSheetNames = excel.GetWorksheetNames();
foreach (var item in workSheetNames)
{
System.Console.WriteLine(item.ToString());
}
}

GetColumnNames方法可取得指定工作表中所有欄位的名稱。

void ShowColumnNames(string excelFile,string sheetName)
{
var excel = new ExcelQueryFactory(excelFile);
var columnNames = excel.GetColumnNames(sheetName);
foreach (var item in columnNames)
{
System.Console.WriteLine(item.ToString());
}
}

這邊個人是發現在不同版本的Excel下，這道方法會取得的值會不有所不同，取得的值在某些條件下都會怪怪的，要特別留意一下。像是我在2003的Excel打入下列資料：

使用GetColumnNames方法取得的值會像下面這樣，只要Column打的是數值，取出來都會走樣。

同樣的資料在Excel 2007下，跑起來就正常許多，但在空行的部份仍是跟我預期的不同。

Worksheet、WorksheetNoHeader、WorksheetRange、WorksheetRangeNoHeader等方法可取得工作表內的資料，我們可藉這些方法取得回傳值後對這些工作表內的資料做Linq查詢。

．．．
var excel = new ExcelQueryFactory(excelFile);

//自己可自行加要過濾的條件，這邊只是示範
var linq = from item in excel.Worksheet(sheetName)
select item;
．．．

這些WorkSheet開頭方法多半會具有不含參數的多載版本，可用以取得"Sheet1"工作表內的資料，這邊需注意該方法取得的是"Sheet1"工作表內的資料，而非第一個工作表內的資料，工作表改名後使用該多載版本方法就會取不到。

．．．
var excel = new ExcelQueryFactory(excelFile);

//這邊會取使用Sheet1的工作表內容去做查詢動作
var linq = from item in excel.Worksheet()
select item;
．．．

或是具有帶入工作表索引或工作表名稱的多載版本，用以取得指定索引或名稱的工作表內的資料。有的還會含有泛型的多載版本，可帶入資料對應的物件類型，取得Excel資料時Linq To Excel會自動幫我們將資料塞成指定的類別。

．．．
var excel = new ExcelQueryFactory(excelFile);

var linq = from item in excel.Worksheet(sheetName)
where item.Sex==SexType.Boy
select item;
．．．

在使用泛型多載版本時，要是用以填值的類別其屬性跟Excel欄位名稱不符，我們可以透過AddMapping設定兩者間的對應關係。

．．．
var excel = new ExcelQueryFactory(excelFile);
excel.AddMapping(item => item.FirstName, "First Name");
excel.AddMapping(item => item.LastName, "Last Name");
．．．

若是設定完欄位與屬性的對應後，有些屬性的資料與欄位內的資料或是型態有所差異時，可加設AddTransformation去做兩者間的轉換。

．．．
var excel = new ExcelQueryFactory(excelFile);
excel.AddMapping(item => item.FirstName, "First Name");
excel.AddMapping(item => item.LastName, "Last Name");
excel.AddTransformation(item => item.Sex, item => (item == "Boy") ? SexType.Boy : SexType.Girl);
．．．

另外一提，Linq to Excel在使用上會自動去找尋第一個符合的資料，就算內容不是從Excel最左上的A1欄位開始，Linq to Excel都會幫我們自動找尋，多半我們可以不指定要抓取的範圍，除非工作表內的資料是分成好幾塊。

## 完整範例


若有需要範例程式可至larrynung / LinqToExcelDemo這邊下載。

Data.xls

SexType.cs

namespace ConsoleApplication1
{
enum SexType
{
Boy,
Girl
}
}

Blogger.cs

using System;

namespace ConsoleApplication1
{
class Blogger
{
public int ID { get; set; }
public String FirstName { get; set; }
public String LastName { get; set; }
public SexType Sex { get; set; }
public int Age { get; set; }
public String Blog { get; set; }

public override string ToString()
{
return string.Join(",", new string[] { ID.ToString(), FirstName, LastName, Sex.ToString(), Age.ToString(), Blog });
}
}
}

Program.cs

using LinqToExcel;

namespace ConsoleApplication1
{
class Program
{
static void Main(string[] args)
{
const string EXCEL_FILE = "Data.xls";
const string FIRST_SHEET = "BlogData1";
const string SECOND_SHEET = "BlogData2";

var excel = new ExcelQueryFactory(EXCEL_FILE);
System.Console.WriteLine("Excel File: {0}", excel.FileName);

System.Console.WriteLine();
System.Console.WriteLine("WorksheetNames...");
var workSheetNames = excel.GetWorksheetNames();
foreach (var item in workSheetNames)
{
System.Console.WriteLine(item.ToString());
}

System.Console.WriteLine();
System.Console.WriteLine("BlogData's Columns...");
var columnNames = excel.GetColumnNames(FIRST_SHEET);
foreach (var item in columnNames)
{
System.Console.WriteLine(item.ToString());
}

System.Console.WriteLine();
System.Console.WriteLine("BlogData1 With ExcelQueryFactory.Worksheet...");
excel.AddMapping(item => item.FirstName, "First Name");
excel.AddMapping(item => item.LastName, "Last Name");
excel.AddTransformation(item => item.Sex, item => (item == "Boy") ? SexType.Boy : SexType.Girl);

foreach (var item in excel.Worksheet(FIRST_SHEET))
{
System.Console.WriteLine(item.ToString());
}

System.Console.WriteLine();
System.Console.WriteLine("BlogData2 With ExcelQueryFactory.Worksheet...");

foreach (var item in excel.Worksheet(SECOND_SHEET))
{
System.Console.WriteLine(item.ToString());
}

System.Console.WriteLine();
System.Console.WriteLine("BlogData2 With ExcelQueryFactory.WorksheetRange...");

foreach (var item in excel.WorksheetRange("B2", "G3", SECOND_SHEET))
{
System.Console.WriteLine(item.ToString());
}

}
}
}

運行後結果如下：

## Link


讀取 Excel 你還在用 NPOI 嗎?快來試試 LinqToExcel

Linq to Excel