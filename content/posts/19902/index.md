---
title: "Linq To Excel Provider"
date: "2010-12-04 11:49:31"
description: "Linq To Excel Provider跟Linq To Excel開放源始碼函式庫一樣都是用來對Excel做查詢用途，不同的是Linq To Excel Provider使用方式跟Linq To SQL有些接近，2.5版以後更具備更新、插入、與刪除等功能，"
tags: [CSharp,Linq]
---

Linq To Excel Provider跟Linq To Excel開放源始碼函式庫一樣都是用來對Excel做查詢用途，不同的是Linq To Excel Provider使用方式跟Linq To SQL有些接近，2.5版以後更具備更新、插入、與刪除等功能，這是Linq To Excel開放源始碼函式庫目前尚無法做到的一塊，也因如此Linq To Excel Provider在使用上就變得比Linq To Excel開放源始碼函式庫來得複雜許多，也多了些限制存在。

Linq To Excel Provider在官網有公開下載Source Code，使用前需先至官網下載，並將其加入專案，再把LinqToExcel命名空間加入使用。下載下來的Source Code雖然只有一個檔案，但裡面卻內含有使用範例，像是Person類別與啟始函式Main，在使用時我們可開啟Source Code先將裡面的範例拿掉。

Linq To Excel Provider使用上必需了解的類別有ExcelProvider與ExcelSheet<T>，其重要的類別成員列表如下：

ExcelProvider Property

<table border="1" cellpadding="2" cellspacing="0" width="400">
<tbody>
<tr>
<td valign="top" width="134">
				Name</td>
<td valign="top" width="264">
				Description</td>
</tr>
<tr>
<td valign="top" width="134">
				Filepath</td>
<td valign="top" width="264">
				Excel檔案位置</td>
</tr>
</tbody>
</table>

ExcelProvider Method

<table border="1" cellpadding="2" cellspacing="0" width="400">
<tbody>
<tr>
<td valign="top" width="133">
				Name</td>
<td valign="top" width="265">
				Description</td>
</tr>
<tr>
<td valign="top" width="133">
				Create</td>
<td valign="top" width="265">
				建立ExcelProvider物件實體</td>
</tr>
<tr>
<td valign="top" width="133">
				GetSheet&lt;T&gt;</td>
<td valign="top" width="265">
				取得工作表</td>
</tr>
<tr>
<td valign="top" width="133">
				SubmitChanges</td>
<td valign="top" width="265">
				接受工作表內容變更</td>
</tr>
</tbody>
</table>

ExcelSheet<T> Method

<table border="1" cellpadding="2" cellspacing="0" width="400">
<tbody>
<tr>
<td valign="top" width="133">
				Name</td>
<td valign="top" width="265">
				Description</td>
</tr>
<tr>
<td valign="top" width="133">
				DeleteOnSubmit</td>
<td valign="top" width="265">
				將此資料表中的實體置於 pending delete 狀態，待ExcelProvider .SubmitChanges呼叫後刪除。</td>
</tr>
<tr>
<td valign="top" width="133">
				InsertOnSubmit</td>
<td valign="top" width="265">
				將此資料表中的實體置於 pending insert狀態，待ExcelProvider .SubmitChanges呼叫後插入。</td>
</tr>
</tbody>
</table>

Linq To Excel Provider跟Linq To SQL一樣，皆需產生對應到資料的類別，這邊我們當然無法像Linq To SQL一樣透過Visual Studio去產生這樣的類別，而是要藉助作者提供的LINQ to Excel Code Generator網頁去產生。

![image_thumb_2.png](/images/posts/19902/image_thumb_2.png)

在LINQ to Excel Code Generator網頁中我們可依序設定要產生的語言、類別名稱、對應到的工作表名稱、及各欄位的名稱與型態。

![image_thumb_1.png](/images/posts/19902/image_thumb_1.png)

填完後按下下方的Generate按鈕，下方會生成你需要的類別程式碼。

```csharp
	//*********************************************************************************
//
//
//
//  Person.cs
//
//*********************************************************************************

using System.Linq;
using System.ComponentModel;

[ExcelSheet(Name="Sheet1")]
public class Person: INotifyPropertyChanged
{

	private double _id;
	private string _firstname;
	private string _lastname;
	private DateTime _birthdate;

	public event PropertyChangedEventHandler PropertyChanged;

	protected virtual void SendPropertyChanged(string propertyName)
	{
		PropertyChangedEventHandler handler = PropertyChanged;
		if (handler != null) {
			handler(this, new PropertyChangedEventArgs(propertyName));
		}
	}

	[ExcelColumn(Name="ID", Storage="_id")]
	public double ID
	{
		get { return _id;}
		set {
			_id = value;
			SendPropertyChanged("ID");
		}
	}

	[ExcelColumn(Name="FirstName", Storage="_firstname")]
	public string FirstName
	{
		get { return _firstname;}
		set {
			_firstname = value;
			SendPropertyChanged("FirstName");
		}
	}

	[ExcelColumn(Name="LastName", Storage="_lastname")]
	public string LastName
	{
		get { return _lastname;}
		set {
			_lastname = value;
			SendPropertyChanged("LastName");
		}
	}

	[ExcelColumn(Name="BirthDate", Storage="_birthdate")]
	public DateTime BirthDate
	{
		get { return _birthdate;}
		set {
			_birthdate = value;
			SendPropertyChanged("BirthDate");
		}
	}
}
```

所產生的類別程式碼，說穿了只是為類別與屬性加些Attribute去修飾，讓Linq To Excel Provider能知道該類別的資料要從哪個工作表的哪個欄位去截取，並實作INotifyPropertyChanged介面讓Linq To Excel Provider能偵測到資料的改變。不過使用上我們不需要了解那麼多，LINQ to Excel Code Generator網頁工具已經處理掉了這塊，我們只要將產生的類別程式碼放入專案後，就可以開始使用Linq To Excel Provider了。

使用時我們可透過ExcelProvider.Create方法，帶入指定的Excel檔案位置，以產生ExcelProvider的物件實體。

```csharp
ExcelProvider provider = ExcelProvider.Create(@"Data.xls");
```

透過ExcelProvider.GetSheet<T>取得資料去做Linq查詢。

```csharp
ExcelProvider provider = ExcelProvider.Create(@"Data.xls");
            var linq = from item in provider.GetSheet<Person>()
                       select item;
```

透過ExcelSheet<T>.DeleteOnSubmit、ExcelSheet<T>.InsertOnSubmit或是直接修改GetSheet<>後取出的資料，再搭配ExcelProvider .SubmitChanges去做插入、刪除與修改動作。

```csharp
Person p = new Person();
p.Id = 10.0;
p.FirstName = "Alex";
p.LastName = "Zander";
p.BirthDate = new DateTime(1980, 4, 4);
ExcelProvider provider = ExcelProvider.Create(@"Data.xls");
provider.GetSheet<Person>().InsertOnSubmit(p);
provider.SubmitChanges();
```

Linq To Excel Provider算是滿好的Excel查詢與編輯的解決方案，但使用上具有一些限制，像是一定要先有對應Excel資料的類別，與無法用來產生資料，若Excel一開始是空的，在使用Linq To Excel Provider時，它會因為無法找到Column而掛掉，若一開始有欄位卻無資料，在取資料時可能會在塞值那邊掛掉。另外一提，追了一下Linq To Excel Provider的程式，感覺在效能上的處理並沒有最佳化，有些資料在使用時是重覆一直去取的，沒有套用一些快取的機制，像是它裡面的ExcelMapReader.GetColumnList，這邊在使用時若有這方面的問題可自行調整一下。

## 完整範例

Program.cs

```csharp
using System;
using System.Linq;
using LinqToExcel;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {

            ExcelProvider provider = ExcelProvider.Create(@"Data.xls");
            var linq = from item in provider.GetSheet<Person>()
                       select item;

            Console.WriteLine("現有資料...");
            foreach (Person item in linq)
            {
                Console.WriteLine(item.ToString ());
            }

            Console.WriteLine();
            Console.WriteLine("插入資料...");
            Person p = new Person();
            p.Id = 10.0;
            p.FirstName = "Alex";
            p.LastName = "Zander";
            p.BirthDate = new DateTime(1980, 4, 4);
            provider.GetSheet<Person>().InsertOnSubmit(p);
            provider.SubmitChanges();
            Console.WriteLine(p.ToString());

            Console.WriteLine();
            Console.WriteLine("插入後資料...");
            foreach (Person item in linq)
            {
                Console.WriteLine(item.ToString());
            }
        }
    }

    [ExcelSheet(Name = "Sheet1")]
    public class Person : System.ComponentModel.INotifyPropertyChanged
    {
        private double id;
        private string fName;
        private string lName;
        private DateTime bDate;

        public event System.ComponentModel.PropertyChangedEventHandler PropertyChanged;

        protected virtual void SendPropertyChanged(string propertyName)
        {
            System.ComponentModel.PropertyChangedEventHandler handler = PropertyChanged;
            if (handler != null)
            {
                handler(this, new System.ComponentModel.PropertyChangedEventArgs(propertyName));
            }
        }

        public Person()
        {
            id = 0;
        }
        [ExcelColumn(Name = "ID", Storage = "id")]
        public double Id
        {
            get { return id; }
            set { id = value; }
        }

        [ExcelColumn(Name = "FirstName", Storage = "fName")]
        public string FirstName
        {
            get { return this.fName; }
            set
            {
                fName = value;
                SendPropertyChanged("FirstName");
            }
        }

        [ExcelColumn(Name = "LastName", Storage = "lName")]
        public string LastName
        {
            get { return this.lName; }
            set
            {
                lName = value;
                SendPropertyChanged("LastName");
            }
        }

        [ExcelColumn(Name = "BirthDate", Storage = "bDate")]
        public DateTime BirthDate
        {
            get { return this.bDate; }
            set
            {
                bDate = value;
                SendPropertyChanged("BirthDate");
            }
        }

        public String ToString()
        {
            return string.Join(",", new string[] { id.ToString(), FirstName, LastName, BirthDate.ToShortDateString() });
        }
    }
}
```

運行後結果如下：

![image_thumb.png](/images/posts/19902/image_thumb.png)

## Download

LinqToExcelProvider.zip

## Link

* LINQ to Excel Provider 2.0
* LINQ to Excel Provider 2.5
* LINQ to Excel Code Generator
