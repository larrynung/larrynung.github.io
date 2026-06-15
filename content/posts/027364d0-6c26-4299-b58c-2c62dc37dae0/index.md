---
title: "[C#][JavaScript]WinForm與WebPage的JavaScript互通(二) - 動態加入並調用JavaScript"
slug: "[CSharp][JavaScript]WinForm與WebPage的JavaScript互通(二) - 動態加入並調用JavaScript"
date: "2013-11-06 12:00:00"
description: "[C#][JavaScript]WinForm與WebPage的JavaScript互通(二) - 動態加入並調用JavaScript"
tags: [CSharp]
---

筆者在[C#][JavaScript]WinForm與WebPage的JavaScript互通(一)這篇稍微介紹了一下基本的互通，實際在程式的運用上可能不是那樣簡單的互通就可以滿足我們的需求，有時候WinForm必須要動態將JavaScript插入網頁並調用，來做些更為進階的處理。

要動態將JavaScript插入網頁中，我們可以在WebBrowser.DocumentCompleted事件處發時去動些手腳。用WebBrowser.Document.GetElementsByTagName找到head的xml element tag，然後再用WebBrowser.Document.CreateElement建立要插入的xml element tag，將要插入的JavaScript塞到剛建立的element的text屬性，最後將建立的element附加到head的子節點就可以了。

```csharp
...
HtmlElement head = webBrowser1.Document.GetElementsByTagName("head")[0];
HtmlElement script = webBrowser1.Document.CreateElement("script");
IHTMLScriptElement element = (IHTMLScriptElement)script.DomElement;
element.text = "function GetVar(varName) { return eval('(' + varName + ')'); }";
head.AppendChild(script);
...
```

有了這樣的技術基礎我們就可以玩些有意思的東西，像是透過插入個JavaScript，我們可以取得網頁中所有的JavaScript變數值。

```csharp
[PermissionSet(SecurityAction.Demand, Name = "FullTrust")]
[ComVisible(true)]
public partial class Form1 : Form
{
    ...
    private void Form1_Load(object sender, EventArgs e)
    {
        webBrowser1.ObjectForScripting = this;
        webBrowser1.DocumentText = @"<head><script>
        var executeCount = 0;
        function ShowAlert(alertMessage) {
            ++executeCount;
            alert (alertMessage);
        }
        window.external.OnWebPageReady();</script></head>";
    }

    private void button1_Click(object sender, EventArgs e)
    {
        MessageBox.Show(webBrowser1.Document.InvokeScript("GetVar", new object[] { "executeCount" }).ToString());
    }

    public void OnWebPageReady()
    {
        HtmlElement head = webBrowser1.Document.GetElementsByTagName("head")[0];
        HtmlElement script = webBrowser1.Document.CreateElement("script");
        IHTMLScriptElement element = (IHTMLScriptElement)script.DomElement;
        element.text = "function GetVar(varName) { return eval('(' + varName + ')'); }";
        head.AppendChild(script);
    }
}
```

或是透過插入的JavaScript我們可以將JSON字串塞給JavaScript，透過JavaScript去Parse JSON資料。

```csharp
[PermissionSet(SecurityAction.Demand, Name = "FullTrust")]
[ComVisible(true)]
public partial class Form1 : Form
{
    ...
    private void Form1_Load(object sender, EventArgs e)
    {
        webBrowser1.ObjectForScripting = this;
        webBrowser1.DocumentText = @"<head><script>
        var executeCount = 0;
        function ShowAlert(alertMessage) {
            ++executeCount;
            alert (alertMessage);
        }
        window.external.OnWebPageReady();</script></head>";
    }

    public void OnWebPageReady()
    {
        webBrowser1.Document.InvokeScript("ShowAlert", new object[] { "WebPage Ready..." });

        HtmlElement head = webBrowser1.Document.GetElementsByTagName("head")[0];
        HtmlElement script = webBrowser1.Document.CreateElement("script");
        IHTMLScriptElement element = (IHTMLScriptElement)script.DomElement;
        element.text = "function GetJsonValue(json, member) { return eval('(' + json + '.' + member+ ')'); }";
        head.AppendChild(script);

        MessageBox.Show(webBrowser1.Document.InvokeScript("GetJsonValue", new object[] { "{'version': '1.0'}", "version" }).ToString());
    }
}
```

當然還有很多變化的可能性，就看個人怎樣運用了。這邊附上較為完整的範例：

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
using mshtml;

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
            webBrowser1.DocumentText = @"<head><script>
            var executeCount = 0;
            function ShowAlert(alertMessage) {
                ++executeCount;
                alert (alertMessage);
            }
            window.external.OnWebPageReady();</script></head>";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            webBrowser1.Document.InvokeScript("ShowAlert", new object[] { "alert message..." });
            MessageBox.Show(webBrowser1.Document.InvokeScript("GetVar", new object[] { "executeCount" }).ToString());
        }

        public void OnWebPageReady()
        {
            webBrowser1.Document.InvokeScript("ShowAlert", new object[] { "WebPage Ready..." });

            HtmlElement head = webBrowser1.Document.GetElementsByTagName("head")[0];
            HtmlElement script = webBrowser1.Document.CreateElement("script");
            IHTMLScriptElement element = (IHTMLScriptElement)script.DomElement;
            element.text = "function GetVar(varName) { return eval('(' + varName + ')'); }";
            head.AppendChild(script);

            script = webBrowser1.Document.CreateElement("script");
            element = (IHTMLScriptElement)script.DomElement;
            element.text = "function GetJsonValue(json, member) { return eval('(' + json + '.' + member+ ')'); }";
            head.AppendChild(script);

            MessageBox.Show(webBrowser1.Document.InvokeScript("GetJsonValue", new object[] { "{'version': '1.0'}", "version" }).ToString());
        }
    }
}
```

運行結果如下：

![image_thumb.png](/images/posts/027364d0-6c26-4299-b58c-2c62dc37dae0/image_thumb.png)

![image_thumb_1.png](/images/posts/027364d0-6c26-4299-b58c-2c62dc37dae0/image_thumb_1.png)

## Link

* How to inject Javascript in WebBrowser control?
