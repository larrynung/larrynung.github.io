---
title: "[C#][VB.NET]取得專案內所有表單名稱"
slug: "[CSharp][VB.NET]取得專案內所有表單名稱"
date: "2009-02-28 11:04:33"
description: "[C#][VB.NET]取得專案內所有表單名稱"
tags: [VB.NET,CSharp]
---

前陣子在藍色小鋪衝浪時看到網友的詢問，問題的需求很奇妙，是想要能取得專案內所有的表單名稱。雖然直覺上就覺得.NET Framework內不會有對應的函式可以直接使用，為求保險仍是去試了一下，結果跟想的一樣，找不到能直接使用的函式。最後只好回到用.NET反射機制(Reflection)去達到該需求。

程式流程為：

1. 利用.NET反射機制取得目前組件
2. 找尋組件內所有類別型態
3. 判斷並列出繼承Form的類別

簡單的範例Code如下：

VB.NET

```
Imports System.Reflection

Public Class Form1

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim a As Assembly = Assembly.GetExecutingAssembly       '取得目前組件
        For Each t As Type In a.GetTypes                        '找尋組件內所有類別型態
            If t.IsSubclassOf(GetType(Form)) Then                 '如果類別是繼承自Form的話
                TextBox1.AppendText(t.ToString & vbNewLine)     '列出該類別資訊
            End If
        Next
    End Sub
End Class
```

C#

```
using System;
```

```
using System.Collections.Generic;
```

```
using System.ComponentModel;
```

```
using System.Data;
```

```
using System.Drawing;
```

```
using System.Linq;
```

```
using System.Text;
```

```
using System.Windows.Forms;
```

```
using System.Reflection;
```

```

```

```
namespace WindowsFormsApplication1
```

```
{
```

```
public partial class Form1 : Form
```

```
{
```

```
public Form1()
```

```
{
```

```
InitializeComponent();
```

```
}
```

```

```

```
private void button1_Click(object sender, EventArgs e)
```

```
{
```

```
Assembly a = Assembly.GetExecutingAssembly();       //取得目前組件
```

```

```

```
foreach (Type t in a.GetTypes())                    //找尋組件內所有類別型態
```

```
{
```

```
if (t.IsSubclassOf(typeof(Form)))           //如果父類別是繼承自Form的話
```

```
{
```

```
textBox1.AppendText(t.ToString() + "\r\n"); //列出該類別資訊
```

```
}
```

```
}
```

```

```

```
}
```

```
}
```

```
}
```

```

```

其主要概念就是利用.NET反射機制，找出目前檔案內所有繼承自Form類別的子類別而已。

特別提醒一下，.NET反射機制有著效能不好的問題，使用上能避免使用.NET反射機制就盡然避免使用。

```

```

## 參考連結

* 藍色小鋪 - 如何取的專案內所有表單名稱
