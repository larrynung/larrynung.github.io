---
title: "[C#]設定WebBrowser Control運行的User Agent版本"
slug: "[CSharp]設定WebBrowser Control運行的User Agent版本"
date: "2013-11-06 12:00:00"
description: "[C#]設定WebBrowser Control運行的User Agent版本"
tags: [CSharp]
---

今天再弄WebBrowser Control元件的測試，發現IE9無法運行我寫的WebSocket程式，因此稍微測試了一下HTML5的支援程度，發現用IE開起來可以跑出138的分數，但在WebBrowser Control中只能跑出41分。

經過Aaron大神的開示，發現這其實是因為直接用IE跟使用WebBrowser Control運行的是不同的User Agent。像是這邊筆者的IE跑的是IE9，但是WebBrowser Control跑的是IE7。

所以我們必須要將WebBrowser Control的User Agent設定調整一下，我們可以透過修改IE的Feature登錄資訊來達到這個效果，機碼位置如下：

32 bit:
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_BROWSER_EMULATION

64 bit:
HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_BROWSER_EMULATION

在這機碼下新增個跟應用程式同名的Dword Key，設定的值可參閱Internet Feature Controls (B..C)這篇文章，不同的值對應到不同版本的User Agent。

像是筆者要將名為WindowsFormApplication3.exe的應用程式指定用IE9的User Agent下去運作，就可以像下面這般設定。

除了手動修改外，我們也可以透過程式去做，像是下面這樣撰寫：

...
public Form1()
{
var appName = Process.GetCurrentProcess().MainModule.ModuleName;
Registry.SetValue(@"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_BROWSER_EMULATION", appName, 9999, RegistryValueKind.DWord);
InitializeComponent();	
}
...

設定完後運行，可以看到已經使用IE9的User Agent下去運行。

再次測試HTML5的支援程度，分數已從41分升為137分，跟直接用IE去開是差不多的。

## Link


Web Browser Control – Specifying the IE Version

Internet Feature Controls (B..C)

More IE8 Extensibility Improvements

C# 視窗程式：如何使用新版的瀏覽器控件？

C# Web Browser component is IE7 not IE8? How to change this?