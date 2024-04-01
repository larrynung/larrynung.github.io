---
title: "[C#][JavaScript]WinForm與WebPage的JavaScript互通(二) - 動態加入並調用JavaScript"
date: "2013-11-06 12:00:00"
description: "[C#][JavaScript]WinForm與WebPage的JavaScript互通(二) - 動態加入並調用JavaScript"
tags: [CSharp]
---

<p>筆者在[C#][JavaScript]WinForm與WebPage的JavaScript互通(一)這篇稍微介紹了一下基本的互通，實際在程式的運用上可能不是那樣簡單的互通就可以滿足我們的需求，有時候WinForm必須要動態將JavaScript插入網頁並調用，來做些更為進階的處理。</p>  <p> </p>  <p>要動態將JavaScript插入網頁中，我們可以在WebBrowser.DocumentCompleted事件處發時去動些手腳。用WebBrowser.Document.GetElementsByTagName找到head的xml element tag，然後再用WebBrowser.Document.CreateElement建立要插入的xml element tag，將要插入的JavaScript塞到剛建立的element的text屬性，最後將建立的element附加到head的子節點就可以了。</p>  <div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:ecacf107-cdfa-40b0-bc08-33c687cb51b2" class="wlWriterSmartContent"><pre name="code" class="c#">...        
HtmlElement head = webBrowser1.Document.GetElementsByTagName("head")[0];
HtmlElement script = webBrowser1.Document.CreateElement("script");
IHTMLScriptElement element = (IHTMLScriptElement)script.DomElement;
element.text = "function GetVar(varName) { return eval('(' + varName + ')'); }";
head.AppendChild(script);
...</pre></div>

<p> </p>

<p>有了這樣的技術基礎我們就可以玩些有意思的東西，像是透過插入個JavaScript，我們可以取得網頁中所有的JavaScript變數值。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:e4216fff-0c33-4491-8f90-c574dbe34192" class="wlWriterSmartContent"><pre name="code" class="c#">    [PermissionSet(SecurityAction.Demand, Name = "FullTrust")]
    [ComVisible(true)]
    public partial class Form1 : Form
    {
        ...
        private void Form1_Load(object sender, EventArgs e)
        {
            webBrowser1.ObjectForScripting = this;
            webBrowser1.DocumentText = @"&lt;head&gt;&lt;script&gt;
            var executeCount = 0;
            function ShowAlert(alertMessage) {
                ++executeCount;
                alert (alertMessage);
            }
            window.external.OnWebPageReady();&lt;/script&gt;&lt;/head&gt;"; 
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
    }</pre></div>

<p> </p>

<p>或是透過插入的JavaScript我們可以將JSON字串塞給JavaScript，透過JavaScript去Parse JSON資料。</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:2b29a2b9-0bff-46e7-96b9-384fbdc264fa" class="wlWriterSmartContent"><pre name="code" class="c#">    [PermissionSet(SecurityAction.Demand, Name = "FullTrust")]
    [ComVisible(true)]
    public partial class Form1 : Form
    {
        ...
        private void Form1_Load(object sender, EventArgs e)
        {
            webBrowser1.ObjectForScripting = this;
            webBrowser1.DocumentText = @"&lt;head&gt;&lt;script&gt;
            var executeCount = 0;
            function ShowAlert(alertMessage) {
                ++executeCount;
                alert (alertMessage);
            }
            window.external.OnWebPageReady();&lt;/script&gt;&lt;/head&gt;"; 
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
    }</pre></div>

<p> </p>

<p>當然還有很多變化的可能性，就看個人怎樣運用了。這邊附上較為完整的範例：</p>

<div style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:467eaf06-8f23-489a-ab34-b164cd68d4ec" class="wlWriterSmartContent"><pre name="code" class="c#">using System;
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
            webBrowser1.DocumentText = @"&lt;head&gt;&lt;script&gt;
            var executeCount = 0;
            function ShowAlert(alertMessage) {
                ++executeCount;
                alert (alertMessage);
            }
            window.external.OnWebPageReady();&lt;/script&gt;&lt;/head&gt;"; 
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
}</pre></div>

<p> </p>

<p>運行結果如下：</p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts�64d0-6c26-4299-b58c-2c62dc37dae0\image_thumb.png" width="304" height="304" /> </p>

<p><img style="border-bottom: 0px; border-left: 0px; border-top: 0px; border-right: 0px" border="0" alt="image" src="\images\posts�64d0-6c26-4299-b58c-2c62dc37dae0\image_thumb_1.png" width="304" height="304" /> </p>

<p> </p>

<h2>Link</h2>

<ul>
  <li>How to inject Javascript in WebBrowser control?</li>
</ul>
