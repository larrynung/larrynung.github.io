---
layout: post
title: "WPF - DoEvents in WPF"
date: 2014-02-05 10:35:00
comments: true
categories: [WPF]
keywords: "WPF, DoEvents"
description: "WPF - DoEvents in WPF"
---

在做大量的運算處理時，不能避免的有時候會需要做 UI 更新的動作，以給予使用者一些反饋。理想上來說，這時我們應該將處理動作切離主執行緒，在另外一個執行緒去處理，需要反饋時再將更新動作帶回主執行緒。但難免有時會偷懶將處理動作直接放在主執行緒上運行，並利用 DoEvents 去釋放資源，讓 UI 得以更新。  

<!-- More -->

以這樣的情景來說，WinForm 中可直接叫用現成的 DoEvents ，但在 WPF 中則無現成的方法可供叫用，所以我們必須借用 WinForm 的 DoEvents 方法。  

只要將 `System.Windows.Forms.dll` 組件加入參考，接著將命名空間 `System.Windows.Forms` 加入，再呼叫 `Application.DoEvents()` 方法即可。  

{% codeblock lang:c# %}
using System.Windows.Forms;

...

Application.DoEvents();

...
{% endcodeblock %}

<br/>

或者是自行撰寫像下面這樣的程式來處理也可以。  

{% codeblock lang:c# %}
void DoEvents(){
DispatcherFrame f = new DispatcherFrame();
Dispatcher.CurrentDispatcher.BeginInvoke(DispatcherPriority.Background, 
(SendOrPostCallback)delegate(object arg) {
    DispatcherFrame fr =  arg as DispatcherFrame;
    fr.Continue=True;
}, f);
Dispatcher.PushFrame(frame);
}
{% endcodeblock %}

Link
----
* [DispatcherFrame Class (System.Windows.Threading)](http://msdn.microsoft.com/en-us/library/system.windows.threading.dispatcherframe.aspx)
* [程湘之間: WPF的UI更新方式](http://charlesbc.blogspot.tw/2011/06/wpfui.html)
* [Application.Doevents in WPF](http://www.dotblogs.com.tw/bauann/archive/2010/06/12/15841.aspx)
