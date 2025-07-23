---
title: "使用C#呼叫VB.NET的CallByName函式"
date: "2010-11-19 12:17:23"
description: "使用C#呼叫VB.NET的CallByName函式"
tags: [CSharp]
---

在VB.NET中有時會有要帶入方法名稱去執行對應方法，或是依屬性名稱去取得、設定其屬性值的需求，若不想使用麻煩的反射去處理，我們可以簡單的使用CallByName函式去達到這樣的需求。

若是在C#中想要使用VB.NET中的CallByName函式，我們可以將Microsoft.VisualBasic.dll加入參考。

![](/images/posts/19554/)

並在程式碼上方加入Microsoft.VisualBasic與Microsoft.VisualBasic.CompilerServices這兩個命名空間
```
using Microsoft.VisualBasic;
using Microsoft.VisualBasic.CompilerServices;
```
就可以透過Versioned類別的CallByName方法使用VB.NET的CallByName函式，就像下面這樣：
```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.VisualBasic;
using Microsoft.VisualBasic.CompilerServices;
using System.Data;

namespace ConsoleApplication1
{
class Program
{
static void Main(string[] args)
{
DataTable dt = new DataTable();
...
foreach (DataRow dr in dt.Rows)
{
foreach (DataColumn dc in dt.Columns)
{
Versioned.CallByName(obj, dc.ColumnName, CallType.Set, dr(dc.ColumnName));
}
}
}
}
}
```