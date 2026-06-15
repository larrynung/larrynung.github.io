---
title: "[C#]Decode Unicode Character"
date: "2013-11-06 12:00:00"
description: "[C#]Decode Unicode Character"
tags: [CSharp]
---

最近偷閒玩些自己的東西，碰到要解析的資料有像是\u0026這樣的Unicode Character，必須要將之解碼才會變成我們想要的資料。這時候就卡在怎樣做解碼的動作，本來在研究的程式牠是直接將\u0026用"&"取代，這真是髒到我用不下手，所以順手下去研究了一下，找到How to decode “\u0026” in a URL?這篇還不錯的範例。簡單的來說，解碼的動作就是要先取得Unicode Character的後四碼，然後將其從16進位轉換為10進位，再將其數值轉回字元就可以了。像是下面這樣：

```csharp
private string GetValueFromUnicodeCharacter(string unicodeCharacter)
{
var match = Regex.Match(unicodeCharacter, @"\\u(?```` \d{4})");
if (!match.Success)
return string.Empty;
var code = match.Groups["code"].Value;
int value = Convert.ToInt32(code, 16);
return ((char)value).ToString();
}
``` ````

也可以用Regex.Replace將裡面所有的Unicode Character都替換。

```csharp
private string DecodeUnicodeCharacter(string unicodeCharacter)
{
MatchEvaluator matchAction = (match) =>
{
var code = match.Groups["code"].Value;
int value = Convert.ToInt32(code, 16);
return ((char)value).ToString();
};
return Regex.Replace(unicodeCharacter, @"\\u(?```` \d{4})", matchAction);
}
``` ````

為什麼會這樣轉換也可以參閱ASCII表，搭配上面的程式與說明應該不難理解為什麼可以這樣處理。

![image_thumb_1.png](/images/posts/c619b8a0-8469-4141-9d3a-25ae65c9f17a/image_thumb_1.png)

最後附上簡易的程式範例：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Text.RegularExpressions;
namespace WindowsFormsApplication35
{
public partial class Form1 : Form
{
public Form1()
{
InitializeComponent();
}
private string GetValueFromUnicodeCharacter(string unicodeCharacter)
{
var match = Regex.Match(unicodeCharacter, @"\\u(?```` \d{4})");
if (!match.Success)
return string.Empty;
var code = match.Groups["code"].Value;
int value = Convert.ToInt32(code, 16);
return ((char)value).ToString();
}
private void textBox1_TextChanged(object sender, EventArgs e)
{
label1.Text = GetValueFromUnicodeCharacter(textBox1.Text);
}
}
}
``` ````

運行畫面如下：

![image_thumb.png](/images/posts/c619b8a0-8469-4141-9d3a-25ae65c9f17a/image_thumb.png)

## Link

- How to decode “\u0026” in a URL?
- Unicode Character Value Table - Other Punctuations
