---
title: "[.NET Resource]JSON C# Class Generator"
date: "2011-04-22 12:35:04"
description: "[.NET Resource]JSON C# Class Generator"
tags: [CSharp,.NET Resource]
---

JSON C# Class Generator為一C# JSON類別產生工具，能接受輸入JSON字串，產生其所對應的強型別類別。使用時需先至JSON C# Class Generator下載工具程式，解壓縮後雙擊開啟。左上方可設定命名空間、類別名稱、與輸出目錄等資訊。右上方可設定產生要屬性或欄位、可視層級、是否產生輔助類別、與是否轉為Pascal命名。程式下方則是用來輸入要轉換的JSON字串。

![image_thumb.png](/images/posts/23323/image_thumb.png)

資料填齊後，按下右下方的[Generate]按鈕，所有產生出來的類別即會存放在所指定的目錄。
![image_thumb_1.png](/images/posts/23323/image_thumb_1.png)

開發時將Newtonsoft.Json.dll加入參考，並將產出的類別放入專案中，即可直接透過產出的類別開發。透過JSON C# Class Generator所產生的類別會具備直接載入JSON字串的能力，不需在建立類別後自行塞入資料，也不需透過解序列化的方式取得資料，只需在建構的同時將JSON字串帶入即可。

...

```
const string url = @"http://api.tudou.com/v3/gw?method=album.channel.get&appKey=myKey&format=json&channel=m&pageNo=1&pageSize=10";
var tudouVideoAlbum = new TudouVideoAlbum(GetHTMLSourceCode(url));
```

...

這邊以Tudou視頻網站示範，可以看到透過所產生的類別來處理整個解析動作就不需要我們自行處理了，撰寫速度大幅提升，完整範例如下：

```
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Tudou;
using System.Net;
using System.IO;
```

```
namespace WindowsFormsApplication4
{
public partial class Form1 : Form
{
  public Form1()
  {
   InitializeComponent();
  }
```

```
  private string GetHTMLSourceCode(string url)
  {
   HttpWebRequest request = (WebRequest.Create(url)) as HttpWebRequest;
   HttpWebResponse response = request.GetResponse() as HttpWebResponse;
   using (StreamReader sr = new StreamReader(response.GetResponseStream()))
   {
    return sr.ReadToEnd();
   }
  }
```

```
  private void Form1_Load(object sender, EventArgs e)
  {
   const string url = @"http://api.tudou.com/v3/gw?method=album.channel.get&appKey=myKey&format=json&channel=m&pageNo=1&pageSize=10";
   var tudouVideoAlbum = new TudouVideoAlbum(GetHTMLSourceCode(url));
   foreach (var item in tudouVideoAlbum.MultiResult.Results)
   {
    listBox1.Items.Add(item.Name);
   }
  }
}
}
```

運行結果：

![image_thumb_2.png](/images/posts/23323/image_thumb_2.png)

## Download

JSONClassGeneratorDemo.rar

## Link

* JSON C# Class Generator
