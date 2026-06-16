---
title: "[C#][JavaScript]Interop Between WinForm and Web Page JavaScript (Part 1)"
slug: "csharp-javascript-interop-between-winform-and-web-page-javascript-part-1"
aliases: ["/posts/csharpjavascriptwinform與webpage的javascript互通一/"]
date: "2013-11-06 12:00:00"
description: "有時候我們在開發時會將網頁嵌入WinForm程式之中，把網頁跟WinForm程式做個整合，最常見的就是登入或註冊時將動作導給網頁來做。也有某些程式是把整個WebPage給嵌入，WinForm只是做一個殼，程式的畫面與邏輯完全都是用WebPage的，最多針對一些細節下去調整或做些輔助功能，"
tags: [CSharp]
---

有時候我們在開發時會將網頁嵌入WinForm程式之中，把網頁跟WinForm程式做個整合，最常見的就是登入或註冊時將動作導給網頁來做。也有某些程式是把整個WebPage給嵌入，WinForm只是做一個殼，程式的畫面與邏輯完全都是用WebPage的，最多針對一些細節下去調整或做些輔助功能，這樣程式就能很快的導入各個平台使用。這樣的開發方式以後會越來越常碰到，因為網頁的功能越來越強大，尤其是HTML5技術成熟後更是如此。

要以上面的方式下去開發，我們必需對WinForm程式與WebPage之間的交互處理很熟悉才行。

若整個程式核心仍在WinForm，只有部份整合WebPage，可能是在做Social network的OAUTH認證，像這類的處理通常不需太緊密的交互，WinForm程式只需要去監控當前頁面的網址去做些對應的處理，WinForm需要的WebPage資料通常會透過網址的參數或是另外的Restful API取得。

若是整個核心跟界面幾乎都在WebPage的話，WinForm與WebPage就必需要較為緊密的交互，像是WinForm有時必需主動觸發WebPage做事，或是WebPage主動觸發WinForm做事。

以WinForm主動觸發WebPage做事來說，WebBrowser內的Document具有現成的方法名為InvokeScript，就可以很簡單的觸發WebPage內的JavaScript，像是:

```csharp
webBrowser1.Document.InvokeScript("scriptFuncName");
```

實際的使用情境上會像下面這樣：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            webBrowser1.DocumentText = @"<script>function ShowAlert(alertMessage) {alert (alertMessage);}</script>";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            webBrowser1.Document.InvokeScript("ShowAlert", new object[] { "alert message..." });
        }
    }
}
```

![image_thumb.png](/images/posts/5891ab4d-be09-42ea-b8bf-47b400c462a1/image_thumb.png)

若是要以WebPage主動觸發WinForm做事就比較麻煩些。大概需要四個主要的步驟：

1.Set PermissionSet and ComVisibleAttribute attribute
2.Add C# function call by web
3.Set WebBrowser.ObjectForScripting
4.JS use window.external to call C# function

第一步必須在WebBrowser所在表單類別加上PremissionSet與ComVisible屬性。

```csharp
[PermissionSet(SecurityAction.Demand, Name = "FullTrust")]
[ComVisible(true)]
public partial class Form1 : Form
{
	...
}
```

第二步必須在WebBrowser所在表單類別中準備個Public Function，給WebPage調用用。

```csharp
[PermissionSet(SecurityAction.Demand, Name = "FullTrust")]
[ComVisible(true)]
public partial class Form1 : Form
{
    ...
    public void OnWebPageReady()
    {
        webBrowser1.Document.InvokeScript("ShowAlert", new object[] { "WebPage Ready..." });
    }
    ...
}
```

第三步設定WebBrowser的ObjectForScripting屬性，以這邊的例子來說是設定WebBrowser所在表單類別。

```csharp
[PermissionSet(SecurityAction.Demand, Name = "FullTrust")]
[ComVisible(true)]
public partial class Form1 : Form
{
    ...
    private void Form1_Load(object sender, EventArgs e)
    {
        webBrowser1.ObjectForScripting = this;
    }
    ...
}
```

第四步是WebPage中的JavaScript必須透過window.external去叫用WinForm中的方法。

```csharp
[PermissionSet(SecurityAction.Demand, Name = "FullTrust")]
[ComVisible(true)]
public partial class Form1 : Form
{
    ...
    private void Form1_Load(object sender, EventArgs e)
    {
        webBrowser1.ObjectForScripting = this;
        webBrowser1.DocumentText = @"<script>function ShowAlert(alertMessage) {alert (alertMessage);}
        window.external.OnWebPageReady();</script>";
    }
    ...
}
```

完整的實作範例如下：

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Security.Permissions;

namespace WindowsFormsApplication3
{
    [PermissionSet(SecurityAction.Demand, Name = "FullTrust")]
    [ComVisible(true)]
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            webBrowser1.ObjectForScripting = this;
            webBrowser1.DocumentText = @"<script>function ShowAlert(alertMessage) {alert (alertMessage);}
            window.external.OnWebPageReady();</script>";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            webBrowser1.Document.InvokeScript("ShowAlert", new object[] { "alert message..." });
        }

        public void OnWebPageReady()
        {
            webBrowser1.Document.InvokeScript("ShowAlert", new object[] { "WebPage Ready..." });
        }
    }
}
```

運行結果如下：

![image_thumb_1.png](/images/posts/5891ab4d-be09-42ea-b8bf-47b400c462a1/image_thumb_1.png)

## Link

* HtmlDocument.InvokeScript 方法 (String)
* HtmlDocument.InvokeScript 方法 (String, Object())
* Calling JavaScript in a WebBrowser control from C#
* Using WebBrowser.Document.InvokeScript() to mess around with foreign JavaScript
* VB.NET/C# and JavaScript communication
* Calling JavaScript
* [C#]讓Webbrowser中的js直接呼叫Winform的function
* WebBrowser.ObjectForScripting Property
* WinForm透過WebBrowser與JavaScript溝通
* JavaScript extensions: window.external
* Calling JavaScript in a WebBrowser control from C#
* C# - vertical bandobject with WebBrowser control in it -> Calling C# from JavaScript
* C# winform與Javascript的相互調用
